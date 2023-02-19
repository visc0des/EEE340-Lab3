"""
Group members: OCdt Liethan Velasco and OCdt Aaron Brown

Version: TODO: completion date

TODO: read this description, implement to make it true.

The nimblesemantics module contains classes sufficient to perform a semantic analysis
of Nimble programs.

The analysis has two major tasks:

- to infer the types of all expressions in a Nimble program and to add appropriate type
annotations to the program's ANTLR-generated syntax tree by storing an entry in the `node_types`
dictionary for each expression node, where the key is the node and the value is a
`symboltable.PrimitiveType` or `symboltable.FunctionType`.

- to identify and flag all violations of the Nimble semantic specification
using the `errorlog.ErrorLog` and other classes in the `errorlog` module.

There are two phases to the analysis:

1. DefineScopesAndSymbols, and

2. InferTypesAndCheckSemantics.

In the first phase, `symboltable.Scope` objects are created for all scope-defining parse
tree nodes: the script, each function definition, and the main. These are stored in the
`self.scopes` dictionary. Also in this phase, all declared function types must be recorded
in the appropriate scope.

Parameter and variable types can be recorded in the appropriate scope in either the first
phase or the second phase.

In the second phase, type inference is performed and all other semantic constraints are
checked.

"""

from errorlog import ErrorLog, Category
from nimble import NimbleListener, NimbleParser
from symboltable import PrimitiveType, Scope


class DefineScopesAndSymbols(NimbleListener):

    def __init__(self, error_log: ErrorLog, global_scope: Scope, types: dict):
        self.error_log = error_log
        self.current_scope = global_scope
        self.type_of = types

    def enterMain(self, ctx: NimbleParser.MainContext):
        self.current_scope = self.current_scope.create_child_scope('$main', PrimitiveType.Void)

    def exitMain(self, ctx: NimbleParser.MainContext):
        self.current_scope = self.current_scope.enclosing_scope


class InferTypesAndCheckConstraints(NimbleListener):
    """
    The type of each expression parse tree node is calculated and stored in the
    `self.type_of` dictionary, where the key is the node object, and the value is
    an instance of `symboltable.PrimitiveType`.

    The types of declared variables are stored in `self.variables`, which is a dictionary
    mapping from variable names to `symboltable.PrimitiveType` instances.

    Any semantic errors detected, e.g., undefined variable names,
    type mismatches, etc., are logged in the `error_log`
    """

    def __init__(self, error_log: ErrorLog, global_scope: Scope, types: dict):
        self.error_log = error_log
        self.current_scope = global_scope
        self.type_of = types

    # --------------------------------------------------------
    # Program structure
    # --------------------------------------------------------

    def exitScript(self, ctx: NimbleParser.ScriptContext):
        pass

    def enterMain(self, ctx: NimbleParser.MainContext):
        self.current_scope = self.current_scope.child_scope_named('$main')

    def exitMain(self, ctx: NimbleParser.MainContext):
        self.current_scope = self.current_scope.enclosing_scope

    def exitBody(self, ctx: NimbleParser.BodyContext):
        pass

    def exitVarBlock(self, ctx: NimbleParser.VarBlockContext):
        pass

    def exitBlock(self, ctx: NimbleParser.BlockContext):
        pass

    # --------------------------------------------------------
    # Variable declarations
    # --------------------------------------------------------

    def exitVarDec(self, ctx: NimbleParser.VarDecContext):

        # TODO - handle duplicated names

        # Creating mini-lookup dictionary for verification
        type_dict = {'Int': PrimitiveType.Int, 'Bool': PrimitiveType.Bool, 'String': PrimitiveType.String}

        # Extracting variable type declared, its primitive type,
        # and the ID declared
        var_text = ctx.TYPE().getText();
        var_primtype = type_dict[var_text];
        this_ID = ctx.ID().getText();

        # Second, if there was an assignment, check if does not violate type constraint
        if ctx.expr() is not None:

            # Extract value of expression put for assignment
            expr_type = self.type_of[ctx.expr()];

            # Check if they match. If not, then there was a constraint violation
            if expr_type != var_primtype:

                self.current_scope.define(this_ID, PrimitiveType.ERROR, False);
                self.type_of[ctx] = PrimitiveType.ERROR;
                self.error_log.add(ctx, Category.ASSIGN_TO_WRONG_TYPE,
                                   f"Can't assign {str(expr_type)} to variable of type {var_text}");
                return;


        # If all input was good, set the variable type accordingly
        self.current_scope.define(this_ID, var_primtype, False);
        self.type_of[ctx] = self.current_scope.resolve(ctx.ID().getText());


    # --------------------------------------------------------
    # Statements
    # --------------------------------------------------------

    def exitAssignment(self, ctx: NimbleParser.AssignmentContext):
        pass

    def exitWhile(self, ctx: NimbleParser.WhileContext):
        pass

    def exitIf(self, ctx: NimbleParser.IfContext):
        pass

    def exitPrint(self, ctx: NimbleParser.PrintContext):
        pass

    # --------------------------------------------------------
    # Expressions
    # --------------------------------------------------------

    def exitIntLiteral(self, ctx: NimbleParser.IntLiteralContext):
        self.type_of[ctx] = PrimitiveType.Int

    def exitNeg(self, ctx: NimbleParser.NegContext):

        """ TODO: Extend to handle boolean negation. """

        if ctx.op.text == '-' and self.type_of[ctx.expr()] == PrimitiveType.Int:
            self.type_of[ctx] = PrimitiveType.Int

        else:
            self.type_of[ctx] = PrimitiveType.ERROR
            self.error_log.add(ctx, Category.INVALID_NEGATION,
                               f"Can't apply {ctx.op.text} to {self.type_of[ctx].name}")

    def exitParens(self, ctx: NimbleParser.ParensContext):



        pass;


    def exitMulDiv(self, ctx: NimbleParser.MulDivContext):
        left = self.type_of[ctx.expr(0)]
        right = self.type_of[ctx.expr(1)]
        if left == PrimitiveType.Int and right == PrimitiveType.Int:
            self.type_of[ctx] = PrimitiveType.Int
        else:
            self.type_of[ctx] = PrimitiveType.ERROR
            self.error_log.add(ctx, Category.INVALID_BINARY_OP,
                               f"Can't multiply or divide {self.type_of[ctx.expr(0)]} with {self.type_of[ctx.expr(1)]}")

    def exitAddSub(self, ctx: NimbleParser.AddSubContext):

        # If children types correct, set type of this token to Int
        if ((ctx.op.text == '+' or ctx.op.text == '-') and
            self.type_of[ctx.expr(0)] == PrimitiveType.Int and
                self.type_of[ctx.expr(1)] == PrimitiveType.Int):
            self.type_of[ctx] = PrimitiveType.Int;

        # Otherwise, set as error.
        else:
            self.type_of[ctx] = PrimitiveType.ERROR;
            self.error_log.add(ctx, Category.INVALID_BINARY_OP,
                               f"Can't apply {ctx.op.text} between non-integer type expression(s).");


    def exitCompare(self, ctx: NimbleParser.CompareContext):
        pass

    def exitVariable(self, ctx: NimbleParser.VariableContext):

        # Simply check if ID is an existing var, or non-error type var.
        # If not, set type of ctx to be ERROR.
        this_ID = ctx.ID().getText();
        symbol_type = self.current_scope.resolve(this_ID);

        if symbol_type is None:
            self.type_of[ctx] = PrimitiveType.ERROR;
            self.error_log.add(ctx, Category.UNDEFINED_NAME,
                               f"Variable {this_ID} is undefined.");
        else:
            self.type_of[ctx] = symbol_type;



        # var x : Int = ...
        # print x.                  <-- Testing needs these two together.

        # ^ x would be type Int
        # If a type for x exists in the dictionary, then this variable is set to that type.
        # This means varDec needs to be completed first.
        # !!! CONSIDER USING RESOLVE



    def exitStringLiteral(self, ctx: NimbleParser.StringLiteralContext):
        self.type_of[ctx] = PrimitiveType.String

    def exitBoolLiteral(self, ctx: NimbleParser.BoolLiteralContext):
        self.type_of[ctx] = PrimitiveType.Bool
