"""
    Description:

        This python file contains all the test cases of all the functions
        in nimblesemantics.py.

    Authors: OCdt Aaron Brown and OCdt Liethan Velasco

"""

# Import Section
from errorlog import Category
from symboltable import PrimitiveType



VALID_EXPRESSIONS = [
    # Each entry is a pair: (expression source, expected type)
    # Due to the way the inferred_types are stored, using ctx.getText() as the key,
    # expressions must contain NO WHITE SPACE for the tests to work. E.g.,
    # '59+a' is fine, '59 + a' won't work.

    # Note here to acknowledge that there is no point testing integer
    # or boolean literals as any errors will be detected by the parser.

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
    ('(32*45)*(30/2)', PrimitiveType.Int),
    ('(45+10)', PrimitiveType.Int),

    # Tests for MulDiv
    ('12*62', PrimitiveType.Int),
    ('1*33*(-23)', PrimitiveType.Int),
    ('17*4/(12*-1)', PrimitiveType.Int),

    # ------------------ Velasco tests ------------------

    # AddSub
    ('23+49', PrimitiveType.Int),
    ('(16-0)+(-3)', PrimitiveType.Int),

    # Boolean Negation and Int negation
    ('!true', PrimitiveType.Bool),
    ('!!(!false)', PrimitiveType.Bool),
    ('--(-3)', PrimitiveType.Int),

    # Compare Binary Operator
    ('(-23)<=48', PrimitiveType.Bool),
    ('1==1', PrimitiveType.Bool),
    ('(20+38)*56<92', PrimitiveType.Bool),

]

INVALID_EXPRESSIONS = [

    # Each entry is a pair: (expression source, expected error category)
    # As for VALID_EXPRESSIONS, there should be NO WHITE SPACE in the expressions.

    # Tests for negation
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
    ('a/b', Category.INVALID_BINARY_OP),

    # ------------------ Velasco tests ------------------

    # AddSub
    ('"someString"+"nope"', Category.INVALID_BINARY_OP),
    ('true+99', Category.INVALID_BINARY_OP),

    # Negation
    ('!!!20', Category.INVALID_NEGATION),
    ('!"Im a string"', Category.INVALID_NEGATION),
    ('-false', Category.INVALID_NEGATION),
    ('-"some string eh"', Category.INVALID_NEGATION),

    # Compare Binary Operator
    ('false==true', Category.INVALID_BINARY_OP),
    ('("Cant believe youve done this.")<(30+2)', Category.INVALID_BINARY_OP),

]


# Creating custom list of VarDec - by Velasco
VALID_VARDEC = [

    ('var myBool : Bool', 'myBool', PrimitiveType.Bool),
    ('var myInt : Int', 'myInt', PrimitiveType.Int),
    ('var myString : String', 'myString', PrimitiveType.String),
    ('var myBool : Bool = !true', 'myBool', PrimitiveType.Bool),
    ('var myInt : Int = -100', 'myInt', PrimitiveType.Int),
    ('var myString : String = "SomeString"', 'myString', PrimitiveType.String),
    ('var myInt : Int = 100 / 12', 'myInt', PrimitiveType.Int),
    ('var myVar : Int = ((100 + 13) * 5)', 'myVar', PrimitiveType.Int),

]

INVALID_VARDEC = [

    # Can only invalidate constraints.
    ('var myBool : Bool = 100', 'myBool', Category.ASSIGN_TO_WRONG_TYPE),
    ('var veryWrong : Int = "absolutely!"', 'veryWrong', Category.ASSIGN_TO_WRONG_TYPE),
    ('var nooope : String = false', 'nooope', Category.ASSIGN_TO_WRONG_TYPE),
    ('var duplicateThis : Bool = true\nvar duplicateThis : Int = 30', 'duplicateThis', Category.DUPLICATE_NAME),

    # Including mismatched variable declaration here to acknowledge its existence.
    # Leaving commented out though since its considered a real test case. Refer to Notes 1 for more info.
    # ('var myBool : Bool = 100', 'wrongVar', Category.ASSIGN_TO_WRONG_TYPE),


]

VALID_VARIABLE = [

    ('var x : Int\nprint x', 'x', PrimitiveType.Int),
    ('var myBool : Bool = true\nvar y : String\nprint myBool\nprint y', 'myBool', PrimitiveType.Bool),
    ('var myBool : Bool = true\nvar y : String\nprint myBool\nprint y', 'y', PrimitiveType.String),
    ('var someVar : Bool = (30 == 40)\nprint someVar', 'someVar', PrimitiveType.Bool),
    ('var anExpre : Bool = (12 < 10)\nif (anExpre) { }', 'anExpre', PrimitiveType.Bool),

]

INVALID_VARIABLE = [

    # Testing for this will be carried out a little differently - we want
    # to find all the UNDEFINED_NAME errors that exist in the script,
    # not just highlight ones specifically and completely ignore the rest.

    'var varA : String = "varA String"\nprint varB',
    'var anInt : String = 100 / "String"\nprint anInt',
    'var newVar : String = "WasCompEngWorthIt?"\nprint newVar\nprint x',

    # Here's one with an error in declaration.
    'var anExpre : Bool = (12 < false)\nif (anExpre) { }',

    # Leaving commented out a poorly designed test of invalid variables to acknowledge its existence -
    # this one does not even have an undefined name error. It's literally in the wrong testing list.
    # ('var someVar : String = 12', Category.UNDEFINED_NAME)

]


# Making a custom list of print statements to include print statements with variables.
VALID_PRINT = [

    # Will only be putting in non-variable print scripts. The ones with variables
    # have already been tested in VALID_VARIABLE

    'print "ChocolateRain"',
    'print (1 + 3) * 12',
    'print !(12 < -20)',
    'var testVar : Int print testVar',

]

INVALID_PRINT = [

    # Print statements with variables already tested in VARIABLE tests
    ('print "" == -false', [Category.INVALID_BINARY_OP, Category.INVALID_NEGATION, Category.UNPRINTABLE_EXPRESSION]),
    ('print (1 + 3) * "Im an integer"', [Category.INVALID_BINARY_OP, Category.UNPRINTABLE_EXPRESSION]),
    ('print (12 < !20)', [Category.INVALID_BINARY_OP, Category.INVALID_BINARY_OP,
                          Category.INVALID_NEGATION, Category.UNPRINTABLE_EXPRESSION]),

]

VALID_ASSIGNMENT = [

    ('var myInt : Int\nmyInt = -100', 'myInt', PrimitiveType.Int),
    ('var myString : String\nmyString = "SomeString"', 'myString', PrimitiveType.String),
    ('var myInt : Int\nmyInt = 100 / 12', 'myInt', PrimitiveType.Int),
    ('var myBool : Bool\nmyBool = !true', 'myBool', PrimitiveType.Bool),
    ('var myInt : Int\nvar myGuy : String\nmyInt = (10 - 20)', 'myInt', PrimitiveType.Int),
    ('var setThrice : Int = 30\nsetThrice = 31\nsetThrice = 32', 'setThrice', PrimitiveType.Int),

]

INVALID_ASSIGNMENT = [

    ('myInt = 12', Category.UNDEFINED_NAME),
    ('var myString : String\nmyString = true', Category.ASSIGN_TO_WRONG_TYPE),
    ('var myInt : Int\nvar myGuy : String\nmyPerson = (10 - 20)', Category.UNDEFINED_NAME),
    ('var myVar : Int\nvar myVar : Bool\nmyVar = !true', Category.DUPLICATE_NAME),
    ('var x : Bool = true\n var y : Int = 10\n print x * y', Category.UNPRINTABLE_EXPRESSION),

]


# For invalid test cases below, just look for the Category.CONDITION_NOT_BOOL error

VALID_WHILE = [
    'while true { }',
    'while 10 == 10 { print 10 + 10 }',
    'while false { while 10 < 5 { print "string" } }',
]

INVALID_WHILE = [
    'while 10 + 10 {}',
    'while !10 == 5 {}',
    'while "string" {}',
    'while "str" + 10 { myInt = 12 }',
]

VALID_IF = [

    'var X : Bool = false\nif X {} else {}',
    'if !(90 < 100) {}',
    'if (true) { if (123 < 23) { } else { } }'

]

INVALID_IF = [

    'var X : Int = 30\nif X - 30 {} else {}',
    'if !"Totally a bool" {}',
    'if (true) { if (123) { } }',

]