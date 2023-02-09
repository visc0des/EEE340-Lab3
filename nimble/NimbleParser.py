# Generated from /Users/phillips/Sync/courses/EEE340/code/lab 3 start/Nimble.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,155,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,1,41,
        9,1,3,1,43,8,1,1,1,1,1,1,1,3,1,48,8,1,1,1,1,1,1,1,1,1,1,2,1,2,1,
        2,1,2,1,3,1,3,1,4,1,4,1,4,1,5,5,5,64,8,5,10,5,12,5,67,9,5,1,6,5,
        6,70,8,6,10,6,12,6,73,9,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,81,8,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,3,8,102,8,8,1,8,1,8,1,8,1,8,3,8,108,8,8,1,8,3,8,111,8,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,125,8,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,136,8,9,10,9,12,9,139,9,9,1,
        10,1,10,1,10,1,10,1,10,5,10,146,8,10,10,10,12,10,149,9,10,3,10,151,
        8,10,1,10,1,10,1,10,0,1,18,11,0,2,4,6,8,10,12,14,16,18,20,0,4,1,
        0,16,17,1,0,18,19,2,0,17,17,20,20,1,0,21,23,168,0,25,1,0,0,0,2,31,
        1,0,0,0,4,53,1,0,0,0,6,57,1,0,0,0,8,59,1,0,0,0,10,65,1,0,0,0,12,
        71,1,0,0,0,14,74,1,0,0,0,16,110,1,0,0,0,18,124,1,0,0,0,20,140,1,
        0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,
        26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,3,6,3,0,29,30,5,0,0,
        1,30,1,1,0,0,0,31,32,5,1,0,0,32,33,5,28,0,0,33,42,5,2,0,0,34,39,
        3,4,2,0,35,36,5,3,0,0,36,38,3,4,2,0,37,35,1,0,0,0,38,41,1,0,0,0,
        39,37,1,0,0,0,39,40,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,42,34,1,
        0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,47,5,4,0,0,45,46,5,5,0,0,46,
        48,5,26,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,6,
        0,0,50,51,3,8,4,0,51,52,5,7,0,0,52,3,1,0,0,0,53,54,5,28,0,0,54,55,
        5,8,0,0,55,56,5,26,0,0,56,5,1,0,0,0,57,58,3,8,4,0,58,7,1,0,0,0,59,
        60,3,10,5,0,60,61,3,12,6,0,61,9,1,0,0,0,62,64,3,14,7,0,63,62,1,0,
        0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,11,1,0,0,0,67,65,
        1,0,0,0,68,70,3,16,8,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,
        71,72,1,0,0,0,72,13,1,0,0,0,73,71,1,0,0,0,74,75,5,9,0,0,75,76,5,
        28,0,0,76,77,5,8,0,0,77,80,5,26,0,0,78,79,5,10,0,0,79,81,3,18,9,
        0,80,78,1,0,0,0,80,81,1,0,0,0,81,15,1,0,0,0,82,83,5,28,0,0,83,84,
        5,10,0,0,84,111,3,18,9,0,85,86,5,11,0,0,86,87,3,18,9,0,87,88,5,6,
        0,0,88,89,3,12,6,0,89,90,5,7,0,0,90,111,1,0,0,0,91,92,5,12,0,0,92,
        93,3,18,9,0,93,94,5,6,0,0,94,95,3,12,6,0,95,101,5,7,0,0,96,97,5,
        13,0,0,97,98,5,6,0,0,98,99,3,12,6,0,99,100,5,7,0,0,100,102,1,0,0,
        0,101,96,1,0,0,0,101,102,1,0,0,0,102,111,1,0,0,0,103,104,5,14,0,
        0,104,111,3,18,9,0,105,107,5,15,0,0,106,108,3,18,9,0,107,106,1,0,
        0,0,107,108,1,0,0,0,108,111,1,0,0,0,109,111,3,20,10,0,110,82,1,0,
        0,0,110,85,1,0,0,0,110,91,1,0,0,0,110,103,1,0,0,0,110,105,1,0,0,
        0,110,109,1,0,0,0,111,17,1,0,0,0,112,113,6,9,-1,0,113,114,5,2,0,
        0,114,115,3,18,9,0,115,116,5,4,0,0,116,125,1,0,0,0,117,118,7,0,0,
        0,118,125,3,18,9,9,119,125,3,20,10,0,120,125,5,28,0,0,121,125,5,
        24,0,0,122,125,5,25,0,0,123,125,5,27,0,0,124,112,1,0,0,0,124,117,
        1,0,0,0,124,119,1,0,0,0,124,120,1,0,0,0,124,121,1,0,0,0,124,122,
        1,0,0,0,124,123,1,0,0,0,125,137,1,0,0,0,126,127,10,8,0,0,127,128,
        7,1,0,0,128,136,3,18,9,9,129,130,10,7,0,0,130,131,7,2,0,0,131,136,
        3,18,9,8,132,133,10,6,0,0,133,134,7,3,0,0,134,136,3,18,9,7,135,126,
        1,0,0,0,135,129,1,0,0,0,135,132,1,0,0,0,136,139,1,0,0,0,137,135,
        1,0,0,0,137,138,1,0,0,0,138,19,1,0,0,0,139,137,1,0,0,0,140,141,5,
        28,0,0,141,150,5,2,0,0,142,147,3,18,9,0,143,144,5,3,0,0,144,146,
        3,18,9,0,145,143,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,
        1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,150,142,1,0,0,0,150,151,
        1,0,0,0,151,152,1,0,0,0,152,153,5,4,0,0,153,21,1,0,0,0,15,25,39,
        42,47,65,71,80,101,107,110,124,135,137,147,150
    ]

class NimbleParser ( Parser ):

    grammarFileName = "Nimble.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'('", "','", "')'", "'->'", 
                     "'{'", "'}'", "':'", "'var'", "'='", "'while'", "'if'", 
                     "'else'", "'print'", "'return'", "'!'", "'-'", "'*'", 
                     "'/'", "'+'", "'<'", "'<='", "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STRING", "INT", "TYPE", "BOOL", "ID", "WS", "COMMENT" ]

    RULE_script = 0
    RULE_funcDef = 1
    RULE_parameterDef = 2
    RULE_main = 3
    RULE_body = 4
    RULE_varBlock = 5
    RULE_block = 6
    RULE_varDec = 7
    RULE_statement = 8
    RULE_expr = 9
    RULE_funcCall = 10

    ruleNames =  [ "script", "funcDef", "parameterDef", "main", "body", 
                   "varBlock", "block", "varDec", "statement", "expr", "funcCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    STRING=24
    INT=25
    TYPE=26
    BOOL=27
    ID=28
    WS=29
    COMMENT=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(NimbleParser.MainContext,0)


        def EOF(self):
            return self.getToken(NimbleParser.EOF, 0)

        def funcDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NimbleParser.FuncDefContext)
            else:
                return self.getTypedRuleContext(NimbleParser.FuncDefContext,i)


        def getRuleIndex(self):
            return NimbleParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)




    def script(self):

        localctx = NimbleParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 22
                self.funcDef()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.main()
            self.state = 29
            self.match(NimbleParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NimbleParser.ID, 0)

        def body(self):
            return self.getTypedRuleContext(NimbleParser.BodyContext,0)


        def parameterDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NimbleParser.ParameterDefContext)
            else:
                return self.getTypedRuleContext(NimbleParser.ParameterDefContext,i)


        def TYPE(self):
            return self.getToken(NimbleParser.TYPE, 0)

        def getRuleIndex(self):
            return NimbleParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)




    def funcDef(self):

        localctx = NimbleParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(NimbleParser.T__0)
            self.state = 32
            self.match(NimbleParser.ID)
            self.state = 33
            self.match(NimbleParser.T__1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 34
                self.parameterDef()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 35
                    self.match(NimbleParser.T__2)
                    self.state = 36
                    self.parameterDef()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 44
            self.match(NimbleParser.T__3)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 45
                self.match(NimbleParser.T__4)
                self.state = 46
                self.match(NimbleParser.TYPE)


            self.state = 49
            self.match(NimbleParser.T__5)
            self.state = 50
            self.body()
            self.state = 51
            self.match(NimbleParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NimbleParser.ID, 0)

        def TYPE(self):
            return self.getToken(NimbleParser.TYPE, 0)

        def getRuleIndex(self):
            return NimbleParser.RULE_parameterDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterDef" ):
                listener.enterParameterDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterDef" ):
                listener.exitParameterDef(self)




    def parameterDef(self):

        localctx = NimbleParser.ParameterDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameterDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(NimbleParser.ID)
            self.state = 54
            self.match(NimbleParser.T__7)
            self.state = 55
            self.match(NimbleParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(NimbleParser.BodyContext,0)


        def getRuleIndex(self):
            return NimbleParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = NimbleParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varBlock(self):
            return self.getTypedRuleContext(NimbleParser.VarBlockContext,0)


        def block(self):
            return self.getTypedRuleContext(NimbleParser.BlockContext,0)


        def getRuleIndex(self):
            return NimbleParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = NimbleParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.varBlock()
            self.state = 60
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NimbleParser.VarDecContext)
            else:
                return self.getTypedRuleContext(NimbleParser.VarDecContext,i)


        def getRuleIndex(self):
            return NimbleParser.RULE_varBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarBlock" ):
                listener.enterVarBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarBlock" ):
                listener.exitVarBlock(self)




    def varBlock(self):

        localctx = NimbleParser.VarBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 62
                self.varDec()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NimbleParser.StatementContext)
            else:
                return self.getTypedRuleContext(NimbleParser.StatementContext,i)


        def getRuleIndex(self):
            return NimbleParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = NimbleParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 268490752) != 0:
                self.state = 68
                self.statement()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NimbleParser.ID, 0)

        def TYPE(self):
            return self.getToken(NimbleParser.TYPE, 0)

        def expr(self):
            return self.getTypedRuleContext(NimbleParser.ExprContext,0)


        def getRuleIndex(self):
            return NimbleParser.RULE_varDec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDec" ):
                listener.enterVarDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDec" ):
                listener.exitVarDec(self)




    def varDec(self):

        localctx = NimbleParser.VarDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(NimbleParser.T__8)
            self.state = 75
            self.match(NimbleParser.ID)
            self.state = 76
            self.match(NimbleParser.T__7)
            self.state = 77
            self.match(NimbleParser.TYPE)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 78
                self.match(NimbleParser.T__9)
                self.state = 79
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NimbleParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(NimbleParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)


    class AssignmentContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(NimbleParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(NimbleParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)


    class FuncCallStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcCall(self):
            return self.getTypedRuleContext(NimbleParser.FuncCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallStmt" ):
                listener.enterFuncCallStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallStmt" ):
                listener.exitFuncCallStmt(self)


    class WhileContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(NimbleParser.ExprContext,0)

        def block(self):
            return self.getTypedRuleContext(NimbleParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(NimbleParser.ExprContext,0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NimbleParser.BlockContext)
            else:
                return self.getTypedRuleContext(NimbleParser.BlockContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)


    class ReturnContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(NimbleParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)



    def statement(self):

        localctx = NimbleParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = NimbleParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(NimbleParser.ID)
                self.state = 83
                self.match(NimbleParser.T__9)
                self.state = 84
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = NimbleParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(NimbleParser.T__10)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(NimbleParser.T__5)
                self.state = 88
                self.block()
                self.state = 89
                self.match(NimbleParser.T__6)
                pass

            elif la_ == 3:
                localctx = NimbleParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(NimbleParser.T__11)
                self.state = 92
                self.expr(0)
                self.state = 93
                self.match(NimbleParser.T__5)
                self.state = 94
                self.block()
                self.state = 95
                self.match(NimbleParser.T__6)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 96
                    self.match(NimbleParser.T__12)
                    self.state = 97
                    self.match(NimbleParser.T__5)
                    self.state = 98
                    self.block()
                    self.state = 99
                    self.match(NimbleParser.T__6)


                pass

            elif la_ == 4:
                localctx = NimbleParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                self.match(NimbleParser.T__13)
                self.state = 104
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = NimbleParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 105
                self.match(NimbleParser.T__14)
                self.state = 107
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.expr(0)


                pass

            elif la_ == 6:
                localctx = NimbleParser.FuncCallStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 109
                self.funcCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NimbleParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NegContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(NimbleParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg" ):
                listener.enterNeg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg" ):
                listener.exitNeg(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(NimbleParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class CompareContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NimbleParser.ExprContext)
            else:
                return self.getTypedRuleContext(NimbleParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)


    class StringLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(NimbleParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(NimbleParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class IntLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(NimbleParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NimbleParser.ExprContext)
            else:
                return self.getTypedRuleContext(NimbleParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class FuncCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcCall(self):
            return self.getTypedRuleContext(NimbleParser.FuncCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallExpr" ):
                listener.enterFuncCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallExpr" ):
                listener.exitFuncCallExpr(self)


    class BoolLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(NimbleParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolLiteral" ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolLiteral" ):
                listener.exitBoolLiteral(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NimbleParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NimbleParser.ExprContext)
            else:
                return self.getTypedRuleContext(NimbleParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = NimbleParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = NimbleParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 113
                self.match(NimbleParser.T__1)
                self.state = 114
                self.expr(0)
                self.state = 115
                self.match(NimbleParser.T__3)
                pass

            elif la_ == 2:
                localctx = NimbleParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 118
                self.expr(9)
                pass

            elif la_ == 3:
                localctx = NimbleParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.funcCall()
                pass

            elif la_ == 4:
                localctx = NimbleParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(NimbleParser.ID)
                pass

            elif la_ == 5:
                localctx = NimbleParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.match(NimbleParser.STRING)
                pass

            elif la_ == 6:
                localctx = NimbleParser.IntLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(NimbleParser.INT)
                pass

            elif la_ == 7:
                localctx = NimbleParser.BoolLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 123
                self.match(NimbleParser.BOOL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 135
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = NimbleParser.MulDivContext(self, NimbleParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 126
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 127
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 128
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = NimbleParser.AddSubContext(self, NimbleParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 130
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 131
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = NimbleParser.CompareContext(self, NimbleParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 132
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 133
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 134
                        self.expr(7)
                        pass

             
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NimbleParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NimbleParser.ExprContext)
            else:
                return self.getTypedRuleContext(NimbleParser.ExprContext,i)


        def getRuleIndex(self):
            return NimbleParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)




    def funcCall(self):

        localctx = NimbleParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(NimbleParser.ID)
            self.state = 141
            self.match(NimbleParser.T__1)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 453181444) != 0:
                self.state = 142
                self.expr(0)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 143
                    self.match(NimbleParser.T__2)
                    self.state = 144
                    self.expr(0)
                    self.state = 149
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 152
            self.match(NimbleParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




