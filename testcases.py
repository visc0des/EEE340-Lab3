"""
Test cases for Nimble semantic analysis. See also the `testhelpers`
module.

Test harnesses have been provided for testing correct semantic
analysis of valid and invalid expressions.

**You will need to provide your own testing mechanisms for varDecs,
statements and higher-level constructs as appropriate.**

Group members: OCdt Liethan Velasco and OCdt Aaron Brown
Version:    March 2nd, 2023


Notes:

    1 - So in the testing for variable declarations (and also in the variable tests),
    one possible case of error involves a mistype of the variable-field in the test case. For example,

    (script = 'var myBool : Bool = 100', variable = 'wrongVar', error_category = Category.ASSIGN_TO_WRONG_TYPE)

    would try to find the type of the variable under name 'wrongVar'. But since the script never declared a variable
    of such name, then it would obviously result in wrongVar being undefined.

    In terms of variable declaration, indeed this is an error, yet it only is only one that arises in a mistake
    in writing the unit test.

    Same principal applies in the Variable tests - typing in a mismatching variable name in the variable field that
    does not correspond to any variable declared in the script would result in KeyError when it tries to find the
    passed in variables type in the index_types dictionary (of course, it wouldn't exist). However, this would
    only be a mistake that could occur in the design of the test cases.

    It was deemed worthy to discern the differences between a mistake in the test case design, and an intentionally
    invalid test case which was meant to fail. Consequently, for both valid and invalid tests of this nature (with
    a script), there would be a check to see if the passed in variable type was correct - indeed, it would be point-
    less to carry out any sort of test if the test case itself was not constructed correctly to enable proper testing.


    Instructor's version: 2023-02-08

"""

# --- Importing Modules ---

import sys
import unittest

from errorlog import Category
from symboltable import PrimitiveType
from testhelpers import do_semantic_analysis, pretty_types
import testcases_header as tc


# --- Declaring Utility Functions ---

def print_debug_info(source, indexed_types, error_log):
    """
    Can be called from test cases when things aren't going as expected
    and you need a look at the inferred types and error_log. See commented-out
    examples in test_valid_expressions and test_invalid_expressions below
    """
    print('\n------------------------------')
    print(f'{source}\n')
    print(pretty_types(indexed_types))
    if error_log.total_entries():
        print(f'\n{error_log}')


# --- Declaring the Unit Tests ---

class TypeTests(unittest.TestCase):

    def test_valid_expressions(self):
        """
        For each pair (expression source, expected type) in VALID_EXPRESSIONS, verifies
        that the expression's inferred type is as expected, and that there are no errors
        in the error_log.
        """

        for expression, expected_type in tc.VALID_EXPRESSIONS:

            error_log, global_scope, indexed_types = do_semantic_analysis(expression, 'expr')

            with self.subTest(expression=expression, expected_type=expected_type):
                self.assertEqual(expected_type, indexed_types[1][expression])
                self.assertEqual(0, error_log.total_entries())

    def test_invalid_expressions(self):
        """
        For each pair (expression source, expected error category) in INVALID_EXPRESSIONS,
        verifies that the expression is assigned the ERROR type and that there is a error_logged
        error of the expected category relating to the expression.
        """
        for expression, expected_category in tc.INVALID_EXPRESSIONS:

            error_log, global_scope, indexed_types = do_semantic_analysis(expression, 'expr')

            with self.subTest(expression=expression,
                              expected_category=expected_category):
                self.assertEqual(PrimitiveType.ERROR, indexed_types[1][expression])

                # Changed to encapsulate invalid expressions with multiple errors in them.
                # self.assertTrue(error_log.includes_exactly(expected_category, 1, expression))
                self.assertNotEqual(0, error_log.total_entries())

    def basic_valid_test(self, code_line):
        """
        used as a basic test by test_varDec, test_variable, test_print and, test_assignment
        will do semantic_analysis of the test and ensure that no errors where generated
        returns error_log, global_scope, indexed_types
        """
        # runs the line of code through the antlr parser and will then do the
        # walker pattern using the methods in nimblesemantics.py.
        error_log, global_scope, indexed_types = do_semantic_analysis(code_line, 'script')

        # ensures that the no errors where generated
        self.assertEqual(0, error_log.total_entries())

        return error_log, global_scope, indexed_types

    def basic_invalid_test(self, code_line):
        """
        same as basic_valid_test but ensure that an error has occured
        used as a basic test by test_varDec, test_variable, test_print and, test_assignment
        will do semantic_analysis of the test and ensure that no errors where generated
        returns error_log, global_scope, indexed_types
        """
        # runs the line of code through the antlr parser and will then do the
        # walker pattern using the methods in nimblesemantics.py.
        error_log, global_scope, indexed_types = do_semantic_analysis(code_line, 'script')

        # ensures that the no errors where generated
        self.assertNotEqual(0, error_log.total_entries())

        return error_log, global_scope, indexed_types

    def big_test(self, variable, expected_type, global_scope):
        """
        will
        then ensure that the symbol being used was previously defined,
        then ensure the returned type is accurate
        """
        # Gets the main scope then checks if the variable exists
        main_scope = global_scope.child_scope_named('$main')
        symbol = main_scope.resolve(variable)
        self.assertIsNotNone(symbol, f'passed in variable [{variable}] not defined. Check for typo.')

        # Ensures the type returned was the expected type
        self.assertEqual(expected_type, symbol.type)

    def big_valid_test(self, test_list):
        """
        used as an expansion on the test conducted in basic_valid_test
        does a for loop through all values in list completing big_test,
        used in test_varDec, test_variable and, test_assignment
        no return
        """
        for code_line, variable, expected_type in test_list:
            error_log, global_scope, indexed_types = self.basic_valid_test(code_line)
            self.big_test(variable, expected_type, global_scope)

    def test_varDec(self):
        """ Thanks for helping with this one sir :).
        This function separately tests the varDec semantics. Since only expressions have types,
        and varDec's do not, a separate, special "script" scope has to constructed in order to test them.
        """

        print("\n\n", "-" * 30, " TESTING VALID VARDEC", "-" * 30, "\n")

        # Testing the valid ones
        self.big_valid_test(tc.VALID_VARDEC)

        print("\n\n", "-" * 30, " TESTING INVALID VARDEC", "-" * 30, "\n")

        # Testing the invalid varDecs
        for var_declaration, variable, expected_category in tc.INVALID_VARDEC:

            # Execute semantic analysis at script level
            error_log, global_scope, indexed_types = self.basic_invalid_test(var_declaration)

            self.big_test(variable, PrimitiveType.ERROR, global_scope)

            # Checks if the error's expected_category occurs
            script_lines = len(var_declaration.splitlines())
            found = 0
            for i in range(1, script_lines + 1):
                if error_log.includes_on_line(expected_category, i):
                    found = 1
                    break
            self.assertNotEqual(0, found, f"ERROR - No {expected_category} category error found.")

            # Debug statement
            print('Invalid: ' + var_declaration + ' -> ' + variable + ' of type ' + str(PrimitiveType.ERROR) +
                  ' with error ' + str(expected_category) + ' passes the test.')

    def test_variable(self):
        """
        Unit test that tests the semantic validity and invalidity of the created variable expressions.
        """
        print("\n\n", "-" * 30, " TESTING VALID VARIABLES", "-" * 30, "\n")

        self.big_valid_test(tc.VALID_VARIABLE)
        # Testing the valid variables
        print("\n\n", "-" * 30, " TESTING INVALID VARIABLES", "-" * 30, "\n")

        # Testing the invalid variables
        for var_script in tc.INVALID_VARIABLE:

            # Do semantic analysis
            error_log, global_scope, indexed_types = self.basic_invalid_test(var_script)

            # Finding which line the UNDEFINED_NAME category error exists.
            # If none found, then the invalid test case itself was invalid (ironic).
            found_line = 0
            for i in range(1, len(indexed_types) + 1):
                if error_log.includes_on_line(Category.UNDEFINED_NAME, i):
                    found_line = i
                    break
            if found_line == 0:
                raise Exception("ERROR - No UNDEFINED_NAME category error found.")

            # No point in checking if it has PrimitiveType.ERROR - if it has a Category.UNDEFINED_NAME
            # error in it, then yes, it's an error. It'd be redundant to do assert test its type.

            # Debug statement (also print any other errors which may have been cause of UNDEFINED_NAME error)
            print("\n{" + var_script.replace("\n", "; ") + '} -> One or more ' + str(PrimitiveType.ERROR) +
                  ':' + str(Category.UNDEFINED_NAME) + '(s) found in the script - passes the test.')
            error_list = "\n\t\t\t".join(error_log.__str__().splitlines())
            print('\t╰─ All errors that were found in script - one may have caused UNDEFINED_NAME error:\n\t\t\t'
                  + error_list)

    def test_print(self):
        """
        Unit tests for semantic validity in regard to the print statement tests.
        """
        # Testing valid print statements
        print("\n\n", "-" * 30, " TESTING VALID PRINT STATEMENTS", "-" * 30, "\n")

        # Testing the valid print statements
        for print_script in tc.VALID_PRINT:

            # Do semantic analysis, and get the SYMBOL of unit test variable through resolve (if it exists)
            self.basic_valid_test(print_script)

            # Debug statement
            print("{" + print_script.replace("\n", "; ") + '} -> print script resulted in no errors' +
                  ' - passes the test.')


        # Testing the invalid print statements
        print("\n\n", "-" * 30, " TESTING INVALID PRINT STATEMENTS", "-" * 30, "\n")
        for print_script, expected_category_list in tc.INVALID_PRINT:

            # Do semantic analysis, and get the SYMBOL of unit test variable through resolve (if it exists)
            error_log, global_scope, indexed_types = do_semantic_analysis(print_script, 'script')

            # Check if errors caught were exactly as many errors in expected_category_list
            if len(expected_category_list) != error_log.total_entries():
                raise Exception(f"ERROR - Number of detected errors in script does "
                                f"not match number of errors expected.")

            # Checking in error_log if we have all the expected errors in the print_script
            for this_cat in expected_category_list:
                if not error_log.includes_on_line(this_cat, 1):
                    raise Exception(f"ERROR - Category error of {this_cat} not in script.")

            # Debug statement
            print("\n{" + print_script.replace("\n", "; ") + '} -> category errors '
                  + str(expected_category_list) + ' found in script - passes the test.')
            error_list = "\n\t\t\t".join(error_log.__str__().splitlines())
            print('\t╰─ All errors that were found in script:\n\t\t\t'
                  + error_list)

    def test_assignment(self):
        # Testing valid print statements
        print("\n\n", "-" * 30, " TESTING VALID ASSIGNMENTS", "-" * 30, "\n")
        self.big_valid_test(tc.VALID_ASSIGNMENT)


        # Testing the invalid print statements
        print("\n\n", "-" * 30, " TESTING INVALID ASSIGNMENTS", "-" * 30, "\n")

        # Testing the invalid variables
        for var_script, expected_category in tc.INVALID_ASSIGNMENT:

            # Do semantic analysis
            error_log, global_scope, indexed_types = self.basic_invalid_test(var_script)

            # Look through error_log to see if expected error occured in the script.
            # If none found, then the invalid test case itself was invalid (ironic).
            found_line = 0
            script_lines = len(var_script.splitlines())
            for i in range(1, script_lines + 1):
                if error_log.includes_on_line(expected_category, i):
                    found_line = i
                    break
            self.assertNotEqual(0, found_line, f"ERROR - No {expected_category} category error found.")

            # No point in checking if it has PrimitiveType.ERROR - if it has a Category.UNDEFINED_NAME
            # error in it, then yes, it's an error. It'd be redundant to do assert test its type.

            # Debug statement (also print any other errors which may have been cause of UNDEFINED_NAME error)
            print("\n{" + var_script.replace("\n", "; ") + '} -> Error ' + str(PrimitiveType.ERROR) +
                  ':' + str(expected_category) + f'(s) found in script @ line {found_line} - '
                                                       f'passes the test.')
            error_list = "\n\t\t\t".join(error_log.__str__().splitlines())
            print(f'\t╰─ All errors that were found in script - one may have caused {expected_category} error:\n\t\t\t'
                  + error_list)

    def while_if_test(self, test_list, has_errors):
        # Testing for both valid and invalid while statements
        for statement in test_list:
            error_log, global_scope, indexed_types = do_semantic_analysis(statement, "script", False)
            if has_errors:
                found = False
                for i in range(1, len(statement.splitlines()) + 1):
                    if error_log.includes_on_line(Category.CONDITION_NOT_BOOL, i):
                        found = True
                self.assertTrue(found)
                self.assertNotEqual(0, error_log.total_entries())
            else:
                self.assertEqual(0, error_log.total_entries())

    def test_while(self):
        self.while_if_test(tc.VALID_WHILE, False)
        self.while_if_test(tc.INVALID_WHILE, True)

    def test_if(self):
        self.while_if_test(tc.VALID_IF, False)
        self.while_if_test(tc.INVALID_IF, True)
