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
    - Currently waiting on reply from Greg about the varDec issue.
        Recap: Turns out we need to set rule_start_name to varDec in order to for this to be tested.
               Secondly, if I don't put spaces in the test case for a varDec, ANTLR does it even
               register this as a varDec, and does not run exitVarDec().
        Answer: So Greg apparently has provided us with a template on how to test these, since
        they need to be done separately (oh my god xD that's like the 5th time I don't look into things
        independently in this lab). We'll be using this to test.

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

    # Tests for MulDiv
    ('!!82*12', Category.INVALID_BINARY_OP),

    # ------------------ Velasco tests ------------------

    # AddSub
    ('"someString"+"nope"', Category.INVALID_BINARY_OP),
    ('true+99', Category.INVALID_BINARY_OP)

    # Variables
    


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

    # Not considering if passed in variable is mismatched as an error. ie. in
    # ('var myBool : Bool = 100', 'wrongVar', Category.ASSIGN_TO_WRONG_TYPE),
    # since this error is encapsulated in the unit tests, and not when doing
    # semantic analysis on the code.

]

VALID_VARIABLE = [

    ('var x : Int\nprint x', 'x', PrimitiveType.Int),
    ('var myBool : Bool = true\nprint myBool', 'myBool', PrimitiveType.Bool),

    # Putting mismatched variable one here
    # ('var someVar : String = "nope" \nprint nonExist', 'urMom', PrimitiveType.String)
]

INVALID_VARIABLE = [

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
                  '  passes the test.');


    def test_variable(self):
        """
        Unit test that tests the semantic validity and invalidity of the created variable expressions.
        """

        print("\n\n", "-" * 30, " TESTING VALID VARIABLES", "-" * 30, "\n");

        # Testing the valid variables
        for var_script, variable, expected_type in VALID_VARIABLE:

            # Do semantic analysis, and get the symbol of unit test variable (if it exists)
            # from index_types (symbol should generally be on line 2 in tests.)
            error_log, global_scope, indexed_types = do_semantic_analysis(var_script, 'script');
            try:
                symbol = indexed_types[2][variable];
            except KeyError:
                raise Exception("ERROR - Passed in unit test variable not found in script. Check for typo.");

            # Check if there were no errors in the script
            self.assertEqual(0, error_log.total_entries());

            # Ensure that variable is in fact defined (could be mistyped in VALID_VARIABLE)
            self.assertIsNotNone(symbol, 'variable [' + variable + '] not defined');

            # Check if variable symbol is correct type in indexed_types
            self.assertEqual(expected_type, symbol.type);

            # Debug statement
            print("{" + var_script.replace("\n", "; ") + '} -> ' + variable + ' of type ' + str(expected_type) +
                  ' passes the tset.');


        # Testing invalid variable uses
        # todo - next