"""
Test cases for Nimble semantic analysis. See also the `testhelpers`
module.

Test harnesses have been provided for testing correct semantic
analysis of valid and invalid expressions.

**You will need to provide your own testing mechanisms for varDecs,
statements and higher-level constructs as appropriate.**

TODO: Complete test cases for Nimble semantic analysis, less function definitions and calls

Group members: OCdt Liethan Velasco and OCdt Aaron Brown
Version: TODO: Submission date here


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
import sys
import unittest

from errorlog import Category
from symboltable import PrimitiveType
from testhelpers import do_semantic_analysis, pretty_types

VALID_EXPRESSIONS = [
    # Each entry is a pair: (expression source, expected type)
    # Due to the way the inferred_types are stored, using ctx.getText() as the key,
    # expressions must contain NO WHITE SPACE for the tests to work. E.g.,
    # '59+a' is fine, '59 + a' won't work.


    ('37', PrimitiveType.Int),
    ('-37', PrimitiveType.Int),

    # Brown tests
    # Tests for strings
    ('"hello"', PrimitiveType.String),
    (r'"Hello\nWorld"', PrimitiveType.String),
    (r'"Hello\rWorld"', PrimitiveType.String),
    (r'"Hello\aWorld"', PrimitiveType.String),
    (r'"Hello\bWorld"', PrimitiveType.String),
    (r'"Hello\fWorld"', PrimitiveType.String),
    (r'"Hello\tWorld"', PrimitiveType.String),
    (r'"Hello\vWorld"', PrimitiveType.String),
    (r'"Hello\\World"', PrimitiveType.String),
    (r'"Hello\'World"', PrimitiveType.String),
    (r'"Hello\?World"', PrimitiveType.String),
    (r'"Hello            World"', PrimitiveType.String),
    (r'"HELLO WORLD"', PrimitiveType.String),

    # Tests for Bools
    ('true', PrimitiveType.Bool),
    ('false', PrimitiveType.Bool),

    # Tests for Parens
    ('("Hello World")', PrimitiveType.String),
    ('(true)', PrimitiveType.Bool),
    ('(false)', PrimitiveType.Bool),
    ('(32*45)', PrimitiveType.Int),
    ('(45+10)', PrimitiveType.Int),

    # Tests for MulDiv
    ('12*62', PrimitiveType.Int),
    ('1*33', PrimitiveType.Int),
    ('17*4', PrimitiveType.Int),

    # ------------------ Velasco tests ------------------

    # AddSub
    ('23+49', PrimitiveType.Int),
    ('16-0', PrimitiveType.Int),

    # Boolean Negation
    ('!true', PrimitiveType.Bool),
    ('!!(!false)', PrimitiveType.Bool),

    # Compare Binary Operator
    ('(-23)<=48', PrimitiveType.Bool),
    ('1==1', PrimitiveType.Bool),
    ('(20+38)*56<92', PrimitiveType.Bool),





]

INVALID_EXPRESSIONS = [
    # Each entry is a pair: (expression source, expected error category)
    # As for VALID_EXPRESSIONS, there should be NO WHITE SPACE in the expressions.

    ('!37', Category.INVALID_NEGATION),
    ('!!37', Category.INVALID_NEGATION),

    # Brown tests
    # Can't make invalid tests for literals as it won't go into the method

    # Tests for Parens
    ('("string"*12)', Category.INVALID_BINARY_OP),
    ('(!30)', Category.INVALID_BINARY_OP),
    ('(33+true)', Category.INVALID_BINARY_OP),

    # Tests for MulDiv
    ('!!82*12', Category.INVALID_BINARY_OP),
    ('"string"*12', Category.INVALID_BINARY_OP),

    # ------------------ Velasco tests ------------------

    # AddSub
    ('"someString"+"nope"', Category.INVALID_BINARY_OP),
    ('true+99', Category.INVALID_BINARY_OP),

    # Boolean Negation (can't think of anymore for now)
    ('!!!20', Category.INVALID_NEGATION),
    ('!"Im a string"', Category.INVALID_NEGATION),

    # Compare Binary Operator
    ('false==true', Category.INVALID_NEGATION),
    ('("Cant believe youve done this.")<30', Category.INVALID_NEGATION),

]

# Creating custom list of VarDec - by Velasco
VALID_VARDEC = [


    ('var myBool : Bool', 'myBool', PrimitiveType.Bool),
    ('var myInt : Int', 'myInt', PrimitiveType.Int),
    ('var myString : String', 'myString', PrimitiveType.String),
    ('var myBool : Bool = true', 'myBool', PrimitiveType.Bool),
    ('var myInt : Int = -100', 'myInt', PrimitiveType.Int),
    ('var myString : String = "SomeString"', 'myString', PrimitiveType.String),
    ('var myInt : Int = 100 / 12', 'myInt', PrimitiveType.Int),

    # todo: ^ add some concatenated strings up there. And parens

]

INVALID_VARDEC = [

    # Can only invalidate constraints.
    ('var myBool : Bool = 100', 'myBool', Category.ASSIGN_TO_WRONG_TYPE),
    ('var veryWrong : Int = "absolutely!"', 'veryWrong', Category.ASSIGN_TO_WRONG_TYPE),
    ('var nooope : String = false', 'nooope', Category.ASSIGN_TO_WRONG_TYPE),

    # Including mismatched variable declaration here to acknowledge its existence.
    # Leaving commented out though since its considered a real test case. Refer to Notes 1 for more info.
    # ('var myBool : Bool = 100', 'wrongVar', Category.ASSIGN_TO_WRONG_TYPE),


]

VALID_VARIABLE = [

    # Note: Try to think of other ways that we can use variables...

    ('var x : Int\nprint x', 'x', PrimitiveType.Int),
    ('var myBool : Bool = true\nvar y : String\nprint myBool\nprint y', 'myBool', PrimitiveType.Bool),
    ('var myBool : Bool = true\nvar y : String\nprint myBool\nprint y', 'y', PrimitiveType.String),
    ('var someVar : Bool = (30 == 40)\nprint someVar', 'someVar', PrimitiveType.Bool),

]

INVALID_VARIABLE = [

    # Note: Try to think of other ways that we can use variables...

    # Testing for this will be carried out a little differently - we want
    # to find all the UNDEFINED_NAME errors that exist in the script,
    # not just highlight ones specifically and completely ignore the rest.

    'var varA : String = "varA String"\nprint varB',
    'var anInt : String = 100 / "String"\nprint anInt',
    'var newVar : String = "WasCompEngWorthIt?"\nprint newVar\nprint x',

    # Leaving commented out a poorly designed test of invalid variables to acknowledge its existence -
    # this one does not even have an undefined name error. Safe to say it's in the wrong testing list.
    # ('var someVar : String = 12', Category.UNDEFINED_NAME)

]


# Making a custom list of print statements to include print statements with variables.
# Yeah turns out it needs to be put here since its root start rule is 'script', not 'expr'
VALID_PRINT = [

    # Will only be putting in non-variable print scripts. The ones with variables
    # have already been tested in VALID_VARIABLE

    # Non-variable print statements. NEED TO PUT PARENTHESES, OR SOME
    # CHARACTER SEPARATOR FROM PRINT IN ORDER FOR IT TO PARSE PROPERLY
    ('print"ChocolateRain"', PrimitiveType.String),
    ('print(1+3)*12', PrimitiveType.Int),
    ('print!(12<-20)', PrimitiveType.Bool),

]

INVALID_PRINT = [

    # Let's see if we can incur multiple errors into it
    ('print""==-false', [Category.INVALID_BINARY_OP, Category.INVALID_NEGATION]),
    ('print(1+3)*"Im an integer"', [Category.INVALID_BINARY_OP]),
    ('print(12<!20)', [Category.INVALID_BINARY_OP, Category.INVALID_BINARY_OP, Category.INVALID_NEGATION]),
    # ^ right yeah, there would be two invalid binary op, one from 12<!20 and another from (12<!20)


]


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


class TypeTests(unittest.TestCase):

    def test_valid_expressions(self):
        """
        For each pair (expression source, expected type) in VALID_EXPRESSIONS, verifies
        that the expression's inferred type is as expected, and that there are no errors
        in the error_log.
        """
        for expression, expected_type in VALID_EXPRESSIONS:

            error_log, global_scope, indexed_types = do_semantic_analysis(expression, 'expr')

            """
            # this is an example of how to use the print_debug_info function to understand errors
            if expression == 'varmyBool:Bool':
                print_debug_info(expression, indexed_types, error_log)
            """

            with self.subTest(expression=expression, expected_type=expected_type):
                self.assertEqual(expected_type, indexed_types[1][expression])
                self.assertEqual(0, error_log.total_entries())

        # Running tests for variables
        # self.test_simple_var_dec();


    def test_invalid_expressions(self):
        """
        For each pair (expression source, expected error category) in INVALID_EXPRESSIONS,
        verifies that the expression is assigned the ERROR type and that there is a error_logged
        error of the expected category relating to the expression.
        """
        for expression, expected_category in INVALID_EXPRESSIONS:
            error_log, global_scope, indexed_types = do_semantic_analysis(expression, 'expr')
            # if expression == '!!37':
            #     print_debug_info(expression, indexed_types, error_log)
            with self.subTest(expression=expression,
                              expected_category=expected_category):
                self.assertEqual(PrimitiveType.ERROR, indexed_types[1][expression])

                # Changed to encapsulate invalid expressions with multiple errors in them.
                # self.assertTrue(error_log.includes_exactly(expected_category, 1, expression))
                self.assertNotEqual(0, error_log.total_entries());

    def test_varDec(self):
        """ Thanks for helping with this one sir :).

        This function separately tests the varDec semantics. Since only expressions have types,
        and varDec's do not, a separate, special "script" scope has to constructed in order to test them.

        """

        print("\n\n", "-" * 30, " TESTING VALID VARDEC", "-" * 30, "\n");

        # Testing the valid ones
        for var_declaration, variable, expected_type in VALID_VARDEC:

            # Execute semantic analysis at script level
            error_log, global_scope, indexed_types = do_semantic_analysis(var_declaration, 'script');

            # Check if there were no errors
            self.assertEqual(0, error_log.total_entries());

            # Get the main child scope from within the script scope
            main_scope = global_scope.child_scope_named('$main');

            # Acquiring type given to variable. Test if it's not none first
            # (test if it was given a type), and if it is right type.
            symbol = main_scope.resolve(variable);
            self.assertIsNotNone(symbol, 'passed in variable [' + variable + '] not defined. Check for typo.');
            self.assertEqual(expected_type, symbol.type);

            # Debug statement
            print(var_declaration + ' -> ' + variable + ' of type ' + str(expected_type) + ' passes the tset.');


        print("\n\n", "-" * 30, " TESTING INVALID VARDEC", "-" * 30, "\n");

        # Testing the invalid varDecs
        for var_declaration, variable, expected_category in INVALID_VARDEC:

            # Execute semantic analysis at script level
            error_log, global_scope, indexed_types = do_semantic_analysis(var_declaration, 'script');

            # Check to make sure at least 1 error is generated
            self.assertNotEqual(0, error_log.total_entries());

            # Get the main child scope from within the script scope
            main_scope = global_scope.child_scope_named('$main');

            # Check if passed in variable was not incorrect (nothing to test if it was incorrect)
            symbol = main_scope.resolve(variable);
            self.assertIsNotNone(symbol, 'passed in variable [' + variable + '] not defined. Check for typo.');

            # Check if var_declaration gives variable type ERROR, and
            # if error category generated was ASSIGN_TO_WRONG_TYPE.
            self.assertTrue(error_log.includes_exactly(expected_category, 1, var_declaration.replace(" ", "")))
            self.assertEqual(PrimitiveType.ERROR, symbol.type);


            # Debug statement
            print('Invalid: ' + var_declaration + ' -> ' + variable + ' of type ' + str(PrimitiveType.ERROR) +
                  ' with error ' + str(expected_category) + ' passes the test.');


    def test_variable(self):
        """
        Unit test that tests the semantic validity and invalidity of the created variable expressions.
        """

        print("\n\n", "-" * 30, " TESTING VALID VARIABLES", "-" * 30, "\n");

        # Testing the valid variables
        for var_script, variable, expected_type in VALID_VARIABLE:

            # Do semantic analysis, and get the SYMBOL of unit test variable through resolve (if it exists)
            error_log, global_scope, indexed_types = do_semantic_analysis(var_script, 'script');
            main_scope = global_scope.child_scope_named('$main');
            symbol = main_scope.resolve(variable);

            # Check if symbol is not NoneType. If it is, means passed
            # in unit test variable was never declared.
            if symbol is None:
                raise Exception(f"ERROR - Passed in unit test variable <{variable}> not found in script. "
                                f"Check for typo.");

            # Check if there were no errors in the script
            self.assertEqual(0, error_log.total_entries());

            # Check if variable symbol is correct type in indexed_types
            self.assertEqual(expected_type, symbol.type);

            # Debug statement
            print("{" + var_script.replace("\n", "; ") + '} -> ' + variable + ' of type ' + str(expected_type) +
                  ' exists - passes the test.');


        print("\n\n", "-" * 30, " TESTING INVALID VARIABLES", "-" * 30, "\n");


        # Testing the invalid variables
        for var_script in INVALID_VARIABLE:

            # Do semantic analysis
            error_log, global_scope, indexed_types = do_semantic_analysis(var_script, 'script');

            # Check to make sure at least 1 error is generated
            self.assertNotEqual(0, error_log.total_entries());

            # Finding which line the UNDEFINED_NAME category error exists.
            # If none found, then the invalid test case itself was invalid (ironic).
            found_line = 0;
            for i in range(1, len(indexed_types) + 1):
                if error_log.includes_on_line(Category.UNDEFINED_NAME, i):
                    found_line = i;
                    break;
            if found_line == 0:
                raise Exception("ERROR - No UNDEFINED_NAME category error found.");

            # No point in checking if it has PrimitiveType.ERROR - if it has a Category.UNDEFINED_NAME
            # error in it, then yes, it's an error. It'd be redundant to do assert test its type.

            # Debug statement (also print any other errors which may have been cause of UNDEFINED_NAME error)
            print("\n{" + var_script.replace("\n", "; ") + '} -> One or more ' + str(PrimitiveType.ERROR) +
                  ':' + str(Category.UNDEFINED_NAME) + '(s) found in the script - passes the test.');
            error_list = "\n\t\t\t".join(error_log.__str__().splitlines());
            print('\t╰─ All errors that were found in script - one may have caused UNDEFINED_NAME error:\n\t\t\t'
                  + error_list);


    def test_print(self):
        """
        Unit tests for semantic validity in regard to the print statement tests.
        """

        # Testing valid print statements
        print("\n\n", "-" * 30, " TESTING VALID PRINT STATEMENTS", "-" * 30, "\n");

        # Testing the valid print statements
        for print_script, expected_type in VALID_PRINT:

            # Do semantic analysis, and get the SYMBOL of unit test variable through resolve (if it exists)
            error_log, global_scope, indexed_types = do_semantic_analysis(print_script, 'script');
            main_scope = global_scope.child_scope_named('$main');


            # Check if there were no errors in the script
            self.assertEqual(0, error_log.total_entries());

            # Check if variable symbol is correct type in indexed_types
            self.assertEqual(expected_type, indexed_types[1][print_script]);

            # Debug statement
            print("{" + print_script.replace("\n", "; ") + '} -> script is of type ' + str(expected_type) +
                  ' - passes the test.');


        # Testing the invalid print statements
        print("\n\n", "-" * 30, " TESTING INVALID PRINT STATEMENTS", "-" * 30, "\n");
        for print_script, expected_category_list in INVALID_PRINT:

            # Do semantic analysis, and get the SYMBOL of unit test variable through resolve (if it exists)
            error_log, global_scope, indexed_types = do_semantic_analysis(print_script, 'script');
            main_scope = global_scope.child_scope_named('$main');

            # Check if errors caught were exactly as many errors in expected_category_list
            if len(expected_category_list) != error_log.total_entries():
                raise Exception(f"ERROR - Number of detected errors in script does "
                                f"not match number of errors expected.");

            # Checking in error_log if we have all the expected errors in the print_script
            for this_cat in expected_category_list:
                if not error_log.includes_on_line(this_cat, 1):
                    raise Exception(f"ERROR - Category error of {this_cat} not in script.");

            # Debug statement
            print("{" + print_script.replace("\n", "; ") + '} -> category errors '
                  + str(expected_category_list) + ' found in script - passes the test.');













