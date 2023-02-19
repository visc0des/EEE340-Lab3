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
    ('true+99', Category.INVALID_BINARY_OP)


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

    ('var x : Int\nprint x', 'x', PrimitiveType.Int),
    ('var myBool : Bool = true\nprint myBool', 'myBool', PrimitiveType.Bool), # todo - figure out this issue.


]

INVALID_VARIABLE = [


    ('var varA : String = "varA String"\nprint varB', 'varB', Category.UNDEFINED_NAME),
    ('var anInt : String = 100\nprint anInt', 'anInt', Category.UNDEFINED_NAME)

    # Including mismatched variable to acknowledge its existence. Leaving commented out
    # though since its considered a real test case. Refer to Notes 1 for more info.
    # ('var someVar : String = "nope" \nprint nonExist', 'urMom', PrimitiveType.String)

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

            if expression == 'varmyBool:Bool':
                print("What's up");

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
                self.assertTrue(error_log.includes_exactly(expected_category, 1, expression))


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

            # Do semantic analysis, and get the SYMBOL of unit test variable (if it exists)
            # from index_types (symbol should generally be on line 2 in tests.)
            error_log, global_scope, indexed_types = do_semantic_analysis(var_script, 'script');
            try:
                symbol = indexed_types[2][variable];
            except KeyError:
                raise Exception("ERROR - Passed in unit test variable not found in script. Check for typo.");

            # Check if there were no errors in the script
            self.assertEqual(0, error_log.total_entries());

            # Check if variable symbol is correct type in indexed_types
            self.assertEqual(expected_type, symbol.type);

            # Debug statement
            print("{" + var_script.replace("\n", "; ") + '} -> ' + variable + ' of type ' + str(expected_type) +
                  ' passes the test.');


        print("\n\n", "-" * 30, " TESTING INVALID VARIABLES", "-" * 30, "\n");

        # Testing the valid variables
        for var_script, variable, expected_category in INVALID_VARIABLE:

            # Do semantic analysis, and get the TYPE (should be error) of unit test variable (if it exists)
            # from index_types (symbol should generally be on line 2 in tests.)
            error_log, global_scope, indexed_types = do_semantic_analysis(var_script, 'script');
            try:
                var_type = indexed_types[2][variable];
            except KeyError:
                raise Exception("ERROR - Passed in unit test variable not found in script. Check for typo.");

            # Check to make sure at least 1 error is generated
            self.assertNotEqual(0, error_log.total_entries());

            # Check if var_declaration gives variable type ERROR, and
            # if error category generated was ASSIGN_TO_WRONG_TYPE.
            self.assertTrue(error_log.includes_exactly(expected_category, 2, variable))
            self.assertEqual(PrimitiveType.ERROR, var_type);

            # Debug statement
            print("{" + var_script.replace("\n", "; ") + '} -> ' + variable + ' of type ' + str(PrimitiveType.ERROR) +
                  ' with error ' + str(expected_category) + ' passes the test.');