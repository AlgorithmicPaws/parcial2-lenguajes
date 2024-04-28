# Generated from PythonFunction.g4 by ANTLR 4.13.1
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
        4,1,35,136,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,3,4,64,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,72,8,
        4,10,4,12,4,75,9,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,83,8,5,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,3,7,93,8,7,1,8,1,8,1,8,1,8,5,8,99,8,8,10,8,
        12,8,102,9,8,1,8,1,8,3,8,106,8,8,1,9,1,9,1,9,1,9,5,9,112,8,9,10,
        9,12,9,115,9,9,1,9,1,9,3,9,119,8,9,1,10,1,10,1,11,1,11,1,11,1,11,
        5,11,127,8,11,10,11,12,11,130,9,11,1,11,1,11,3,11,134,8,11,1,11,
        0,1,8,12,0,2,4,6,8,10,12,14,16,18,20,22,0,3,1,0,6,11,1,0,26,27,1,
        0,28,29,143,0,25,1,0,0,0,2,37,1,0,0,0,4,39,1,0,0,0,6,46,1,0,0,0,
        8,63,1,0,0,0,10,82,1,0,0,0,12,84,1,0,0,0,14,92,1,0,0,0,16,105,1,
        0,0,0,18,118,1,0,0,0,20,120,1,0,0,0,22,133,1,0,0,0,24,26,3,2,1,0,
        25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,1,1,0,
        0,0,29,30,3,12,6,0,30,31,5,25,0,0,31,38,1,0,0,0,32,33,5,31,0,0,33,
        34,5,1,0,0,34,35,3,8,4,0,35,36,5,25,0,0,36,38,1,0,0,0,37,29,1,0,
        0,0,37,32,1,0,0,0,38,3,1,0,0,0,39,40,5,2,0,0,40,41,5,3,0,0,41,42,
        3,6,3,0,42,43,5,4,0,0,43,44,5,22,0,0,44,45,5,5,0,0,45,5,1,0,0,0,
        46,47,3,8,4,0,47,48,7,0,0,0,48,49,3,8,4,0,49,7,1,0,0,0,50,51,6,4,
        -1,0,51,64,3,10,5,0,52,53,5,12,0,0,53,54,3,8,4,0,54,55,5,12,0,0,
        55,64,1,0,0,0,56,64,5,32,0,0,57,64,5,31,0,0,58,64,5,33,0,0,59,60,
        5,3,0,0,60,61,3,8,4,0,61,62,5,5,0,0,62,64,1,0,0,0,63,50,1,0,0,0,
        63,52,1,0,0,0,63,56,1,0,0,0,63,57,1,0,0,0,63,58,1,0,0,0,63,59,1,
        0,0,0,64,73,1,0,0,0,65,66,10,8,0,0,66,67,7,1,0,0,67,72,3,8,4,9,68,
        69,10,7,0,0,69,70,7,2,0,0,70,72,3,8,4,8,71,65,1,0,0,0,71,68,1,0,
        0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,9,1,0,0,0,75,73,
        1,0,0,0,76,77,5,13,0,0,77,83,3,8,4,0,78,79,5,14,0,0,79,83,3,8,4,
        0,80,81,5,30,0,0,81,83,3,8,4,0,82,76,1,0,0,0,82,78,1,0,0,0,82,80,
        1,0,0,0,83,11,1,0,0,0,84,85,5,22,0,0,85,86,5,1,0,0,86,87,3,14,7,
        0,87,13,1,0,0,0,88,93,3,16,8,0,89,93,3,18,9,0,90,93,3,20,10,0,91,
        93,3,22,11,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,1,0,0,0,92,91,1,0,
        0,0,93,15,1,0,0,0,94,95,5,15,0,0,95,100,5,24,0,0,96,97,5,4,0,0,97,
        99,5,24,0,0,98,96,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,
        1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,106,5,16,0,0,104,106,
        5,17,0,0,105,94,1,0,0,0,105,104,1,0,0,0,106,17,1,0,0,0,107,108,5,
        3,0,0,108,113,5,24,0,0,109,110,5,4,0,0,110,112,5,24,0,0,111,109,
        1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,
        1,0,0,0,115,113,1,0,0,0,116,119,5,5,0,0,117,119,5,18,0,0,118,107,
        1,0,0,0,118,117,1,0,0,0,119,19,1,0,0,0,120,121,5,23,0,0,121,21,1,
        0,0,0,122,123,5,19,0,0,123,128,5,24,0,0,124,125,5,4,0,0,125,127,
        5,24,0,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,134,5,20,0,0,132,134,
        5,21,0,0,133,122,1,0,0,0,133,132,1,0,0,0,134,23,1,0,0,0,13,27,37,
        63,71,73,82,92,100,105,113,118,128,133
    ]

class PythonFunctionParser ( Parser ):

    grammarFileName = "PythonFunction.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'filter'", "'('", "','", "')'", 
                     "'=='", "'>'", "'<'", "'!='", "'>='", "'<='", "'|'", 
                     "'cos'", "'sen'", "'['", "']'", "'[]'", "'()'", "'{'", 
                     "'}'", "'{}'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'tan'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'    '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER", "STRING_LITERAL", 
                      "LITERAL", "NEWLINE", "MUL", "DIV", "ADD", "SUB", 
                      "TAN", "ID", "INT", "HEX", "WS", "INDENT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_filter = 2
    RULE_condition = 3
    RULE_expr = 4
    RULE_trigFunc = 5
    RULE_iterable_declaration = 6
    RULE_iterable_expression = 7
    RULE_list_expression = 8
    RULE_tuple_expression = 9
    RULE_string_expression = 10
    RULE_set_expression = 11

    ruleNames =  [ "prog", "stat", "filter", "condition", "expr", "trigFunc", 
                   "iterable_declaration", "iterable_expression", "list_expression", 
                   "tuple_expression", "string_expression", "set_expression" ]

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
    IDENTIFIER=22
    STRING_LITERAL=23
    LITERAL=24
    NEWLINE=25
    MUL=26
    DIV=27
    ADD=28
    SUB=29
    TAN=30
    ID=31
    INT=32
    HEX=33
    WS=34
    INDENT=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonFunctionParser.StatContext)
            else:
                return self.getTypedRuleContext(PythonFunctionParser.StatContext,i)


        def getRuleIndex(self):
            return PythonFunctionParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PythonFunctionParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.stat()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22 or _la==31):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonFunctionParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Print_statContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def iterable_declaration(self):
            return self.getTypedRuleContext(PythonFunctionParser.Iterable_declarationContext,0)

        def NEWLINE(self):
            return self.getToken(PythonFunctionParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stat" ):
                listener.enterPrint_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stat" ):
                listener.exitPrint_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stat" ):
                return visitor.visitPrint_stat(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PythonFunctionParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(PythonFunctionParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(PythonFunctionParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = PythonFunctionParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = PythonFunctionParser.Print_statContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.iterable_declaration()
                self.state = 30
                self.match(PythonFunctionParser.NEWLINE)
                pass
            elif token in [31]:
                localctx = PythonFunctionParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(PythonFunctionParser.ID)
                self.state = 33
                self.match(PythonFunctionParser.T__0)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(PythonFunctionParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(PythonFunctionParser.ConditionContext,0)


        def IDENTIFIER(self):
            return self.getToken(PythonFunctionParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PythonFunctionParser.RULE_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter" ):
                listener.enterFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter" ):
                listener.exitFilter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilter" ):
                return visitor.visitFilter(self)
            else:
                return visitor.visitChildren(self)




    def filter_(self):

        localctx = PythonFunctionParser.FilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(PythonFunctionParser.T__1)
            self.state = 40
            self.match(PythonFunctionParser.T__2)
            self.state = 41
            self.condition()
            self.state = 42
            self.match(PythonFunctionParser.T__3)
            self.state = 43
            self.match(PythonFunctionParser.IDENTIFIER)
            self.state = 44
            self.match(PythonFunctionParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonFunctionParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonFunctionParser.ExprContext,i)


        def getRuleIndex(self):
            return PythonFunctionParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = PythonFunctionParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.expr(0)
            self.state = 47
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 48
            self.expr(0)
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
            return PythonFunctionParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PythonFunctionParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class AbsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PythonFunctionParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbs" ):
                listener.enterAbs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbs" ):
                listener.exitAbs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs" ):
                return visitor.visitAbs(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonFunctionParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonFunctionParser.ExprContext,i)

        def MUL(self):
            return self.getToken(PythonFunctionParser.MUL, 0)
        def DIV(self):
            return self.getToken(PythonFunctionParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonFunctionParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonFunctionParser.ExprContext,i)

        def ADD(self):
            return self.getToken(PythonFunctionParser.ADD, 0)
        def SUB(self):
            return self.getToken(PythonFunctionParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class TrigFunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def trigFunc(self):
            return self.getTypedRuleContext(PythonFunctionParser.TrigFuncContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrigFunction" ):
                listener.enterTrigFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrigFunction" ):
                listener.exitTrigFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigFunction" ):
                return visitor.visitTrigFunction(self)
            else:
                return visitor.visitChildren(self)


    class HexContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEX(self):
            return self.getToken(PythonFunctionParser.HEX, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHex" ):
                listener.enterHex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHex" ):
                listener.exitHex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHex" ):
                return visitor.visitHex(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PythonFunctionParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PythonFunctionParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonFunctionParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 30]:
                localctx = PythonFunctionParser.TrigFunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 51
                self.trigFunc()
                pass
            elif token in [12]:
                localctx = PythonFunctionParser.AbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(PythonFunctionParser.T__11)
                self.state = 53
                self.expr(0)
                self.state = 54
                self.match(PythonFunctionParser.T__11)
                pass
            elif token in [32]:
                localctx = PythonFunctionParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(PythonFunctionParser.INT)
                pass
            elif token in [31]:
                localctx = PythonFunctionParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                self.match(PythonFunctionParser.ID)
                pass
            elif token in [33]:
                localctx = PythonFunctionParser.HexContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(PythonFunctionParser.HEX)
                pass
            elif token in [3]:
                localctx = PythonFunctionParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(PythonFunctionParser.T__2)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(PythonFunctionParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = PythonFunctionParser.MulDivContext(self, PythonFunctionParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 66
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = PythonFunctionParser.AddSubContext(self, PythonFunctionParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 69
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 70
                        self.expr(8)
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TrigFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonFunctionParser.RULE_trigFunc

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TanFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(PythonFunctionParser.TAN, 0)
        def expr(self):
            return self.getTypedRuleContext(PythonFunctionParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTanFunc" ):
                listener.enterTanFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTanFunc" ):
                listener.exitTanFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanFunc" ):
                return visitor.visitTanFunc(self)
            else:
                return visitor.visitChildren(self)


    class CosFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PythonFunctionParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosFunc" ):
                listener.enterCosFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosFunc" ):
                listener.exitCosFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosFunc" ):
                return visitor.visitCosFunc(self)
            else:
                return visitor.visitChildren(self)


    class SenFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PythonFunctionParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSenFunc" ):
                listener.enterSenFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSenFunc" ):
                listener.exitSenFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSenFunc" ):
                return visitor.visitSenFunc(self)
            else:
                return visitor.visitChildren(self)



    def trigFunc(self):

        localctx = PythonFunctionParser.TrigFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_trigFunc)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = PythonFunctionParser.CosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(PythonFunctionParser.T__12)
                self.state = 77
                self.expr(0)
                pass
            elif token in [14]:
                localctx = PythonFunctionParser.SenFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(PythonFunctionParser.T__13)
                self.state = 79
                self.expr(0)
                pass
            elif token in [30]:
                localctx = PythonFunctionParser.TanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.match(PythonFunctionParser.TAN)
                self.state = 81
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Iterable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonFunctionParser.RULE_iterable_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Creacion_iterableContext(Iterable_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.Iterable_declarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PythonFunctionParser.IDENTIFIER, 0)
        def iterable_expression(self):
            return self.getTypedRuleContext(PythonFunctionParser.Iterable_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreacion_iterable" ):
                listener.enterCreacion_iterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreacion_iterable" ):
                listener.exitCreacion_iterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreacion_iterable" ):
                return visitor.visitCreacion_iterable(self)
            else:
                return visitor.visitChildren(self)



    def iterable_declaration(self):

        localctx = PythonFunctionParser.Iterable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_iterable_declaration)
        try:
            localctx = PythonFunctionParser.Creacion_iterableContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(PythonFunctionParser.IDENTIFIER)
            self.state = 85
            self.match(PythonFunctionParser.T__0)
            self.state = 86
            self.iterable_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Iterable_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonFunctionParser.RULE_iterable_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TupleContext(Iterable_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.Iterable_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tuple_expression(self):
            return self.getTypedRuleContext(PythonFunctionParser.Tuple_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)


    class SetContext(Iterable_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.Iterable_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def set_expression(self):
            return self.getTypedRuleContext(PythonFunctionParser.Set_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet" ):
                listener.enterSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet" ):
                listener.exitSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet" ):
                return visitor.visitSet(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(Iterable_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.Iterable_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string_expression(self):
            return self.getTypedRuleContext(PythonFunctionParser.String_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class ListContext(Iterable_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.Iterable_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_expression(self):
            return self.getTypedRuleContext(PythonFunctionParser.List_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)



    def iterable_expression(self):

        localctx = PythonFunctionParser.Iterable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_iterable_expression)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 17]:
                localctx = PythonFunctionParser.ListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.list_expression()
                pass
            elif token in [3, 18]:
                localctx = PythonFunctionParser.TupleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.tuple_expression()
                pass
            elif token in [23]:
                localctx = PythonFunctionParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.string_expression()
                pass
            elif token in [19, 21]:
                localctx = PythonFunctionParser.SetContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.set_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonFunctionParser.RULE_list_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Accion_listContext(List_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.List_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(PythonFunctionParser.LITERAL)
            else:
                return self.getToken(PythonFunctionParser.LITERAL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccion_list" ):
                listener.enterAccion_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccion_list" ):
                listener.exitAccion_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccion_list" ):
                return visitor.visitAccion_list(self)
            else:
                return visitor.visitChildren(self)


    class Empty_listContext(List_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.List_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty_list" ):
                listener.enterEmpty_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty_list" ):
                listener.exitEmpty_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmpty_list" ):
                return visitor.visitEmpty_list(self)
            else:
                return visitor.visitChildren(self)



    def list_expression(self):

        localctx = PythonFunctionParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_expression)
        self._la = 0 # Token type
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = PythonFunctionParser.Accion_listContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(PythonFunctionParser.T__14)
                self.state = 95
                self.match(PythonFunctionParser.LITERAL)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 96
                    self.match(PythonFunctionParser.T__3)
                    self.state = 97
                    self.match(PythonFunctionParser.LITERAL)
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.match(PythonFunctionParser.T__15)
                pass
            elif token in [17]:
                localctx = PythonFunctionParser.Empty_listContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(PythonFunctionParser.T__16)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tuple_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonFunctionParser.RULE_tuple_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Empty_tupleContext(Tuple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.Tuple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty_tuple" ):
                listener.enterEmpty_tuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty_tuple" ):
                listener.exitEmpty_tuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmpty_tuple" ):
                return visitor.visitEmpty_tuple(self)
            else:
                return visitor.visitChildren(self)


    class Accion_tupleContext(Tuple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.Tuple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(PythonFunctionParser.LITERAL)
            else:
                return self.getToken(PythonFunctionParser.LITERAL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccion_tuple" ):
                listener.enterAccion_tuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccion_tuple" ):
                listener.exitAccion_tuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccion_tuple" ):
                return visitor.visitAccion_tuple(self)
            else:
                return visitor.visitChildren(self)



    def tuple_expression(self):

        localctx = PythonFunctionParser.Tuple_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tuple_expression)
        self._la = 0 # Token type
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = PythonFunctionParser.Accion_tupleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(PythonFunctionParser.T__2)
                self.state = 108
                self.match(PythonFunctionParser.LITERAL)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 109
                    self.match(PythonFunctionParser.T__3)
                    self.state = 110
                    self.match(PythonFunctionParser.LITERAL)
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 116
                self.match(PythonFunctionParser.T__4)
                pass
            elif token in [18]:
                localctx = PythonFunctionParser.Empty_tupleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(PythonFunctionParser.T__17)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonFunctionParser.RULE_string_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Accion_stringContext(String_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.String_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(PythonFunctionParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccion_string" ):
                listener.enterAccion_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccion_string" ):
                listener.exitAccion_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccion_string" ):
                return visitor.visitAccion_string(self)
            else:
                return visitor.visitChildren(self)



    def string_expression(self):

        localctx = PythonFunctionParser.String_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_string_expression)
        try:
            localctx = PythonFunctionParser.Accion_stringContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(PythonFunctionParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonFunctionParser.RULE_set_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Empty_setContext(Set_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.Set_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty_set" ):
                listener.enterEmpty_set(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty_set" ):
                listener.exitEmpty_set(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmpty_set" ):
                return visitor.visitEmpty_set(self)
            else:
                return visitor.visitChildren(self)


    class Accion_setContext(Set_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonFunctionParser.Set_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(PythonFunctionParser.LITERAL)
            else:
                return self.getToken(PythonFunctionParser.LITERAL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccion_set" ):
                listener.enterAccion_set(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccion_set" ):
                listener.exitAccion_set(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccion_set" ):
                return visitor.visitAccion_set(self)
            else:
                return visitor.visitChildren(self)



    def set_expression(self):

        localctx = PythonFunctionParser.Set_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_set_expression)
        self._la = 0 # Token type
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = PythonFunctionParser.Accion_setContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(PythonFunctionParser.T__18)
                self.state = 123
                self.match(PythonFunctionParser.LITERAL)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 124
                    self.match(PythonFunctionParser.T__3)
                    self.state = 125
                    self.match(PythonFunctionParser.LITERAL)
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 131
                self.match(PythonFunctionParser.T__19)
                pass
            elif token in [21]:
                localctx = PythonFunctionParser.Empty_setContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(PythonFunctionParser.T__20)
                pass
            else:
                raise NoViableAltException(self)

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
        self._predicates[4] = self.expr_sempred
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
         




