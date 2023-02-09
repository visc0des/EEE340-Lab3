# Generated from /Users/phillips/Sync/courses/EEE340/code/lab 3 start/Nimble.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NimbleParser import NimbleParser
else:
    from NimbleParser import NimbleParser

# This class defines a complete listener for a parse tree produced by NimbleParser.
class NimbleListener(ParseTreeListener):

    # Enter a parse tree produced by NimbleParser#script.
    def enterScript(self, ctx:NimbleParser.ScriptContext):
        pass

    # Exit a parse tree produced by NimbleParser#script.
    def exitScript(self, ctx:NimbleParser.ScriptContext):
        pass


    # Enter a parse tree produced by NimbleParser#funcDef.
    def enterFuncDef(self, ctx:NimbleParser.FuncDefContext):
        pass

    # Exit a parse tree produced by NimbleParser#funcDef.
    def exitFuncDef(self, ctx:NimbleParser.FuncDefContext):
        pass


    # Enter a parse tree produced by NimbleParser#parameterDef.
    def enterParameterDef(self, ctx:NimbleParser.ParameterDefContext):
        pass

    # Exit a parse tree produced by NimbleParser#parameterDef.
    def exitParameterDef(self, ctx:NimbleParser.ParameterDefContext):
        pass


    # Enter a parse tree produced by NimbleParser#main.
    def enterMain(self, ctx:NimbleParser.MainContext):
        pass

    # Exit a parse tree produced by NimbleParser#main.
    def exitMain(self, ctx:NimbleParser.MainContext):
        pass


    # Enter a parse tree produced by NimbleParser#body.
    def enterBody(self, ctx:NimbleParser.BodyContext):
        pass

    # Exit a parse tree produced by NimbleParser#body.
    def exitBody(self, ctx:NimbleParser.BodyContext):
        pass


    # Enter a parse tree produced by NimbleParser#varBlock.
    def enterVarBlock(self, ctx:NimbleParser.VarBlockContext):
        pass

    # Exit a parse tree produced by NimbleParser#varBlock.
    def exitVarBlock(self, ctx:NimbleParser.VarBlockContext):
        pass


    # Enter a parse tree produced by NimbleParser#block.
    def enterBlock(self, ctx:NimbleParser.BlockContext):
        pass

    # Exit a parse tree produced by NimbleParser#block.
    def exitBlock(self, ctx:NimbleParser.BlockContext):
        pass


    # Enter a parse tree produced by NimbleParser#varDec.
    def enterVarDec(self, ctx:NimbleParser.VarDecContext):
        pass

    # Exit a parse tree produced by NimbleParser#varDec.
    def exitVarDec(self, ctx:NimbleParser.VarDecContext):
        pass


    # Enter a parse tree produced by NimbleParser#assignment.
    def enterAssignment(self, ctx:NimbleParser.AssignmentContext):
        pass

    # Exit a parse tree produced by NimbleParser#assignment.
    def exitAssignment(self, ctx:NimbleParser.AssignmentContext):
        pass


    # Enter a parse tree produced by NimbleParser#while.
    def enterWhile(self, ctx:NimbleParser.WhileContext):
        pass

    # Exit a parse tree produced by NimbleParser#while.
    def exitWhile(self, ctx:NimbleParser.WhileContext):
        pass


    # Enter a parse tree produced by NimbleParser#if.
    def enterIf(self, ctx:NimbleParser.IfContext):
        pass

    # Exit a parse tree produced by NimbleParser#if.
    def exitIf(self, ctx:NimbleParser.IfContext):
        pass


    # Enter a parse tree produced by NimbleParser#print.
    def enterPrint(self, ctx:NimbleParser.PrintContext):
        pass

    # Exit a parse tree produced by NimbleParser#print.
    def exitPrint(self, ctx:NimbleParser.PrintContext):
        pass


    # Enter a parse tree produced by NimbleParser#return.
    def enterReturn(self, ctx:NimbleParser.ReturnContext):
        pass

    # Exit a parse tree produced by NimbleParser#return.
    def exitReturn(self, ctx:NimbleParser.ReturnContext):
        pass


    # Enter a parse tree produced by NimbleParser#funcCallStmt.
    def enterFuncCallStmt(self, ctx:NimbleParser.FuncCallStmtContext):
        pass

    # Exit a parse tree produced by NimbleParser#funcCallStmt.
    def exitFuncCallStmt(self, ctx:NimbleParser.FuncCallStmtContext):
        pass


    # Enter a parse tree produced by NimbleParser#neg.
    def enterNeg(self, ctx:NimbleParser.NegContext):
        pass

    # Exit a parse tree produced by NimbleParser#neg.
    def exitNeg(self, ctx:NimbleParser.NegContext):
        pass


    # Enter a parse tree produced by NimbleParser#parens.
    def enterParens(self, ctx:NimbleParser.ParensContext):
        pass

    # Exit a parse tree produced by NimbleParser#parens.
    def exitParens(self, ctx:NimbleParser.ParensContext):
        pass


    # Enter a parse tree produced by NimbleParser#compare.
    def enterCompare(self, ctx:NimbleParser.CompareContext):
        pass

    # Exit a parse tree produced by NimbleParser#compare.
    def exitCompare(self, ctx:NimbleParser.CompareContext):
        pass


    # Enter a parse tree produced by NimbleParser#stringLiteral.
    def enterStringLiteral(self, ctx:NimbleParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by NimbleParser#stringLiteral.
    def exitStringLiteral(self, ctx:NimbleParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by NimbleParser#variable.
    def enterVariable(self, ctx:NimbleParser.VariableContext):
        pass

    # Exit a parse tree produced by NimbleParser#variable.
    def exitVariable(self, ctx:NimbleParser.VariableContext):
        pass


    # Enter a parse tree produced by NimbleParser#intLiteral.
    def enterIntLiteral(self, ctx:NimbleParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by NimbleParser#intLiteral.
    def exitIntLiteral(self, ctx:NimbleParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by NimbleParser#addSub.
    def enterAddSub(self, ctx:NimbleParser.AddSubContext):
        pass

    # Exit a parse tree produced by NimbleParser#addSub.
    def exitAddSub(self, ctx:NimbleParser.AddSubContext):
        pass


    # Enter a parse tree produced by NimbleParser#funcCallExpr.
    def enterFuncCallExpr(self, ctx:NimbleParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by NimbleParser#funcCallExpr.
    def exitFuncCallExpr(self, ctx:NimbleParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by NimbleParser#boolLiteral.
    def enterBoolLiteral(self, ctx:NimbleParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by NimbleParser#boolLiteral.
    def exitBoolLiteral(self, ctx:NimbleParser.BoolLiteralContext):
        pass


    # Enter a parse tree produced by NimbleParser#mulDiv.
    def enterMulDiv(self, ctx:NimbleParser.MulDivContext):
        pass

    # Exit a parse tree produced by NimbleParser#mulDiv.
    def exitMulDiv(self, ctx:NimbleParser.MulDivContext):
        pass


    # Enter a parse tree produced by NimbleParser#funcCall.
    def enterFuncCall(self, ctx:NimbleParser.FuncCallContext):
        pass

    # Exit a parse tree produced by NimbleParser#funcCall.
    def exitFuncCall(self, ctx:NimbleParser.FuncCallContext):
        pass



del NimbleParser