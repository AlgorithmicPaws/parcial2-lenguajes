# Generated from FourierTransform.g4 by ANTLR 4.13.1
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
        4,1,25,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        43,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,56,8,4,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,70,8,6,1,6,0,0,
        7,0,2,4,6,8,10,12,0,3,1,0,22,23,2,0,4,4,13,13,1,0,18,21,72,0,15,
        1,0,0,0,2,23,1,0,0,0,4,42,1,0,0,0,6,44,1,0,0,0,8,55,1,0,0,0,10,57,
        1,0,0,0,12,69,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,
        17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,20,3,4,2,0,20,21,5,24,
        0,0,21,24,1,0,0,0,22,24,5,24,0,0,23,19,1,0,0,0,23,22,1,0,0,0,24,
        3,1,0,0,0,25,26,5,1,0,0,26,27,3,6,3,0,27,28,5,2,0,0,28,29,3,6,3,
        0,29,43,1,0,0,0,30,43,3,12,6,0,31,32,5,3,0,0,32,33,5,4,0,0,33,43,
        5,5,0,0,34,35,5,6,0,0,35,36,5,3,0,0,36,37,5,4,0,0,37,38,5,7,0,0,
        38,39,5,8,0,0,39,40,5,9,0,0,40,41,7,0,0,0,41,43,5,5,0,0,42,25,1,
        0,0,0,42,30,1,0,0,0,42,31,1,0,0,0,42,34,1,0,0,0,43,5,1,0,0,0,44,
        45,3,8,4,0,45,46,5,10,0,0,46,47,3,10,5,0,47,7,1,0,0,0,48,49,5,11,
        0,0,49,50,5,12,0,0,50,51,5,13,0,0,51,52,5,14,0,0,52,56,7,0,0,0,53,
        56,5,22,0,0,54,56,5,15,0,0,55,48,1,0,0,0,55,53,1,0,0,0,55,54,1,0,
        0,0,56,9,1,0,0,0,57,58,7,1,0,0,58,59,7,2,0,0,59,60,7,0,0,0,60,11,
        1,0,0,0,61,62,5,16,0,0,62,63,5,22,0,0,63,64,5,4,0,0,64,70,5,5,0,
        0,65,66,5,17,0,0,66,67,5,22,0,0,67,68,5,4,0,0,68,70,5,5,0,0,69,61,
        1,0,0,0,69,65,1,0,0,0,70,13,1,0,0,0,5,17,23,42,55,69
    ]

class FourierTransformParser ( Parser ):

    grammarFileName = "FourierTransform.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'|'", "'dirac('", "'t'", "')'", 
                     "'SUM('", "'-'", "'k'", "'*'", "','", "'1 -'", "'('", 
                     "'|t|'", "'/'", "'-1'", "'cos('", "'sin('", "'<'", 
                     "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MN", "MNI", "MY", "MYI", 
                      "INT", "PULS", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_func = 2
    RULE_dec = 3
    RULE_res = 4
    RULE_cond = 5
    RULE_trigFunc = 6

    ruleNames =  [ "prog", "stat", "func", "dec", "res", "cond", "trigFunc" ]

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
    MN=18
    MNI=19
    MY=20
    MYI=21
    INT=22
    PULS=23
    NEWLINE=24
    WS=25

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
                return self.getTypedRuleContexts(FourierTransformParser.StatContext)
            else:
                return self.getTypedRuleContext(FourierTransformParser.StatContext,i)


        def getRuleIndex(self):
            return FourierTransformParser.RULE_prog

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

        localctx = FourierTransformParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.stat()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16973898) != 0)):
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
            return FourierTransformParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(FourierTransformParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func(self):
            return self.getTypedRuleContext(FourierTransformParser.FuncContext,0)

        def NEWLINE(self):
            return self.getToken(FourierTransformParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = FourierTransformParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 6, 16, 17]:
                localctx = FourierTransformParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.func()
                self.state = 20
                self.match(FourierTransformParser.NEWLINE)
                pass
            elif token in [24]:
                localctx = FourierTransformParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(FourierTransformParser.NEWLINE)
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


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FourierTransformParser.RULE_func

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SumatoriaContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(FourierTransformParser.INT, 0)
        def PULS(self):
            return self.getToken(FourierTransformParser.PULS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumatoria" ):
                listener.enterSumatoria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumatoria" ):
                listener.exitSumatoria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumatoria" ):
                return visitor.visitSumatoria(self)
            else:
                return visitor.visitChildren(self)


    class DeltaContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelta" ):
                listener.enterDelta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelta" ):
                listener.exitDelta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelta" ):
                return visitor.visitDelta(self)
            else:
                return visitor.visitChildren(self)


    class FuncionContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FourierTransformParser.DecContext)
            else:
                return self.getTypedRuleContext(FourierTransformParser.DecContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)


    class TrigonometricasContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def trigFunc(self):
            return self.getTypedRuleContext(FourierTransformParser.TrigFuncContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrigonometricas" ):
                listener.enterTrigonometricas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrigonometricas" ):
                listener.exitTrigonometricas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigonometricas" ):
                return visitor.visitTrigonometricas(self)
            else:
                return visitor.visitChildren(self)



    def func(self):

        localctx = FourierTransformParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = FourierTransformParser.FuncionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(FourierTransformParser.T__0)
                self.state = 26
                self.dec()
                self.state = 27
                self.match(FourierTransformParser.T__1)
                self.state = 28
                self.dec()
                pass
            elif token in [16, 17]:
                localctx = FourierTransformParser.TrigonometricasContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.trigFunc()
                pass
            elif token in [3]:
                localctx = FourierTransformParser.DeltaContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(FourierTransformParser.T__2)
                self.state = 32
                self.match(FourierTransformParser.T__3)
                self.state = 33
                self.match(FourierTransformParser.T__4)
                pass
            elif token in [6]:
                localctx = FourierTransformParser.SumatoriaContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.match(FourierTransformParser.T__5)
                self.state = 35
                self.match(FourierTransformParser.T__2)
                self.state = 36
                self.match(FourierTransformParser.T__3)
                self.state = 37
                self.match(FourierTransformParser.T__6)
                self.state = 38
                self.match(FourierTransformParser.T__7)
                self.state = 39
                self.match(FourierTransformParser.T__8)
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                self.match(FourierTransformParser.T__4)
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


    class DecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FourierTransformParser.RULE_dec

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaracionContext(DecContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.DecContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def res(self):
            return self.getTypedRuleContext(FourierTransformParser.ResContext,0)

        def cond(self):
            return self.getTypedRuleContext(FourierTransformParser.CondContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)



    def dec(self):

        localctx = FourierTransformParser.DecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dec)
        try:
            localctx = FourierTransformParser.DeclaracionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.res()
            self.state = 45
            self.match(FourierTransformParser.T__9)
            self.state = 46
            self.cond()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FourierTransformParser.RULE_res

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TriangularContext(ResContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.ResContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(FourierTransformParser.INT, 0)
        def PULS(self):
            return self.getToken(FourierTransformParser.PULS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTriangular" ):
                listener.enterTriangular(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTriangular" ):
                listener.exitTriangular(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTriangular" ):
                return visitor.visitTriangular(self)
            else:
                return visitor.visitChildren(self)


    class BlankedContext(ResContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.ResContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlanked" ):
                listener.enterBlanked(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlanked" ):
                listener.exitBlanked(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlanked" ):
                return visitor.visitBlanked(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ResContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.ResContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(FourierTransformParser.INT, 0)

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



    def res(self):

        localctx = FourierTransformParser.ResContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_res)
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = FourierTransformParser.TriangularContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(FourierTransformParser.T__10)
                self.state = 49
                self.match(FourierTransformParser.T__11)
                self.state = 50
                self.match(FourierTransformParser.T__12)
                self.state = 51
                self.match(FourierTransformParser.T__13)
                self.state = 52
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [22]:
                localctx = FourierTransformParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(FourierTransformParser.INT)
                pass
            elif token in [15]:
                localctx = FourierTransformParser.BlankedContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(FourierTransformParser.T__14)
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


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FourierTransformParser.RULE_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondicionContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.CondContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(FourierTransformParser.INT, 0)
        def PULS(self):
            return self.getToken(FourierTransformParser.PULS, 0)
        def MN(self):
            return self.getToken(FourierTransformParser.MN, 0)
        def MY(self):
            return self.getToken(FourierTransformParser.MY, 0)
        def MNI(self):
            return self.getToken(FourierTransformParser.MNI, 0)
        def MYI(self):
            return self.getToken(FourierTransformParser.MYI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)



    def cond(self):

        localctx = FourierTransformParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cond)
        self._la = 0 # Token type
        try:
            localctx = FourierTransformParser.CondicionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==4 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 58
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrigFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FourierTransformParser.RULE_trigFunc

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CosFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(FourierTransformParser.INT, 0)

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


    class SinFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(FourierTransformParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinFunc" ):
                listener.enterSinFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinFunc" ):
                listener.exitSinFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinFunc" ):
                return visitor.visitSinFunc(self)
            else:
                return visitor.visitChildren(self)



    def trigFunc(self):

        localctx = FourierTransformParser.TrigFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_trigFunc)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = FourierTransformParser.CosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(FourierTransformParser.T__15)
                self.state = 62
                self.match(FourierTransformParser.INT)
                self.state = 63
                self.match(FourierTransformParser.T__3)
                self.state = 64
                self.match(FourierTransformParser.T__4)
                pass
            elif token in [17]:
                localctx = FourierTransformParser.SinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(FourierTransformParser.T__16)
                self.state = 66
                self.match(FourierTransformParser.INT)
                self.state = 67
                self.match(FourierTransformParser.T__3)
                self.state = 68
                self.match(FourierTransformParser.T__4)
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





