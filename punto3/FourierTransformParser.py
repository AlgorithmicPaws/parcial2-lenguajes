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
        4,1,25,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,62,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,3,6,78,8,6,1,7,1,7,3,7,82,8,7,1,8,1,8,3,8,86,8,8,1,8,
        0,0,9,0,2,4,6,8,10,12,14,16,0,2,2,0,4,4,13,13,1,0,17,20,87,0,19,
        1,0,0,0,2,27,1,0,0,0,4,47,1,0,0,0,6,49,1,0,0,0,8,61,1,0,0,0,10,63,
        1,0,0,0,12,77,1,0,0,0,14,81,1,0,0,0,16,85,1,0,0,0,18,20,3,2,1,0,
        19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,
        0,0,23,24,3,4,2,0,24,25,5,24,0,0,25,28,1,0,0,0,26,28,5,24,0,0,27,
        23,1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,0,29,30,5,1,0,0,30,31,3,6,3,
        0,31,32,5,2,0,0,32,33,3,6,3,0,33,48,1,0,0,0,34,48,3,12,6,0,35,36,
        5,3,0,0,36,37,5,4,0,0,37,48,5,5,0,0,38,39,5,6,0,0,39,40,5,3,0,0,
        40,41,5,4,0,0,41,42,5,7,0,0,42,43,5,8,0,0,43,44,5,9,0,0,44,45,3,
        14,7,0,45,46,5,5,0,0,46,48,1,0,0,0,47,29,1,0,0,0,47,34,1,0,0,0,47,
        35,1,0,0,0,47,38,1,0,0,0,48,5,1,0,0,0,49,50,3,8,4,0,50,51,5,10,0,
        0,51,52,3,10,5,0,52,7,1,0,0,0,53,54,5,11,0,0,54,55,5,12,0,0,55,56,
        5,13,0,0,56,57,5,14,0,0,57,58,3,14,7,0,58,59,5,5,0,0,59,62,1,0,0,
        0,60,62,5,22,0,0,61,53,1,0,0,0,61,60,1,0,0,0,62,9,1,0,0,0,63,64,
        7,0,0,0,64,65,7,1,0,0,65,66,3,14,7,0,66,11,1,0,0,0,67,68,5,15,0,
        0,68,69,3,16,8,0,69,70,5,4,0,0,70,71,5,5,0,0,71,78,1,0,0,0,72,73,
        5,16,0,0,73,74,3,16,8,0,74,75,5,4,0,0,75,76,5,5,0,0,76,78,1,0,0,
        0,77,67,1,0,0,0,77,72,1,0,0,0,78,13,1,0,0,0,79,82,5,22,0,0,80,82,
        5,23,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,15,1,0,0,0,83,86,5,22,0,
        0,84,86,5,21,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,17,1,0,0,0,7,21,
        27,47,61,77,81,85
    ]

class FourierTransformParser ( Parser ):

    grammarFileName = "FourierTransform.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'|'", "'dirac('", "'t'", "')'", 
                     "'SUM('", "'-'", "'k'", "'*'", "','", "'1 -'", "'('", 
                     "'|t|'", "'/'", "'cos('", "'sin('", "'<'", "'<='", 
                     "'>'", "'>='", "'w'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "MN", "MNI", "MY", "MYI", "FRE", "INT", 
                      "PULS", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_func = 2
    RULE_dec = 3
    RULE_res = 4
    RULE_cond = 5
    RULE_trigFunc = 6
    RULE_pul = 7
    RULE_frec = 8

    ruleNames =  [ "prog", "stat", "func", "dec", "res", "cond", "trigFunc", 
                   "pul", "frec" ]

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
    MN=17
    MNI=18
    MY=19
    MYI=20
    FRE=21
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
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.stat()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16875594) != 0)):
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
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 6, 15, 16]:
                localctx = FourierTransformParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.func()
                self.state = 24
                self.match(FourierTransformParser.NEWLINE)
                pass
            elif token in [24]:
                localctx = FourierTransformParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
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

        def pul(self):
            return self.getTypedRuleContext(FourierTransformParser.PulContext,0)


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
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = FourierTransformParser.FuncionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(FourierTransformParser.T__0)
                self.state = 30
                self.dec()
                self.state = 31
                self.match(FourierTransformParser.T__1)
                self.state = 32
                self.dec()
                pass
            elif token in [15, 16]:
                localctx = FourierTransformParser.TrigonometricasContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.trigFunc()
                pass
            elif token in [3]:
                localctx = FourierTransformParser.DeltaContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(FourierTransformParser.T__2)
                self.state = 36
                self.match(FourierTransformParser.T__3)
                self.state = 37
                self.match(FourierTransformParser.T__4)
                pass
            elif token in [6]:
                localctx = FourierTransformParser.SumatoriaContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(FourierTransformParser.T__5)
                self.state = 39
                self.match(FourierTransformParser.T__2)
                self.state = 40
                self.match(FourierTransformParser.T__3)
                self.state = 41
                self.match(FourierTransformParser.T__6)
                self.state = 42
                self.match(FourierTransformParser.T__7)
                self.state = 43
                self.match(FourierTransformParser.T__8)
                self.state = 44
                self.pul()
                self.state = 45
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
            self.state = 49
            self.res()
            self.state = 50
            self.match(FourierTransformParser.T__9)
            self.state = 51
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

        def pul(self):
            return self.getTypedRuleContext(FourierTransformParser.PulContext,0)


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
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = FourierTransformParser.TriangularContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(FourierTransformParser.T__10)
                self.state = 54
                self.match(FourierTransformParser.T__11)
                self.state = 55
                self.match(FourierTransformParser.T__12)
                self.state = 56
                self.match(FourierTransformParser.T__13)
                self.state = 57
                self.pul()
                self.state = 58
                self.match(FourierTransformParser.T__4)
                pass
            elif token in [22]:
                localctx = FourierTransformParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(FourierTransformParser.INT)
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

        def pul(self):
            return self.getTypedRuleContext(FourierTransformParser.PulContext,0)

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
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==4 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 64
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1966080) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 65
            self.pul()
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

        def frec(self):
            return self.getTypedRuleContext(FourierTransformParser.FrecContext,0)


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

        def frec(self):
            return self.getTypedRuleContext(FourierTransformParser.FrecContext,0)


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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = FourierTransformParser.CosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(FourierTransformParser.T__14)
                self.state = 68
                self.frec()
                self.state = 69
                self.match(FourierTransformParser.T__3)
                self.state = 70
                self.match(FourierTransformParser.T__4)
                pass
            elif token in [16]:
                localctx = FourierTransformParser.SinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(FourierTransformParser.T__15)
                self.state = 73
                self.frec()
                self.state = 74
                self.match(FourierTransformParser.T__3)
                self.state = 75
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


    class PulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FourierTransformParser.RULE_pul

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LongPContext(PulContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.PulContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PULS(self):
            return self.getToken(FourierTransformParser.PULS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLongP" ):
                listener.enterLongP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLongP" ):
                listener.exitLongP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLongP" ):
                return visitor.visitLongP(self)
            else:
                return visitor.visitChildren(self)


    class IntsContext(PulContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.PulContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(FourierTransformParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInts" ):
                listener.enterInts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInts" ):
                listener.exitInts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInts" ):
                return visitor.visitInts(self)
            else:
                return visitor.visitChildren(self)



    def pul(self):

        localctx = FourierTransformParser.PulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_pul)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = FourierTransformParser.IntsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(FourierTransformParser.INT)
                pass
            elif token in [23]:
                localctx = FourierTransformParser.LongPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(FourierTransformParser.PULS)
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


    class FrecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FourierTransformParser.RULE_frec

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FrecuencyContext(FrecContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.FrecContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FRE(self):
            return self.getToken(FourierTransformParser.FRE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrecuency" ):
                listener.enterFrecuency(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrecuency" ):
                listener.exitFrecuency(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrecuency" ):
                return visitor.visitFrecuency(self)
            else:
                return visitor.visitChildren(self)


    class IntegerContext(FrecContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierTransformParser.FrecContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(FourierTransformParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)



    def frec(self):

        localctx = FourierTransformParser.FrecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_frec)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = FourierTransformParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(FourierTransformParser.INT)
                pass
            elif token in [21]:
                localctx = FourierTransformParser.FrecuencyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(FourierTransformParser.FRE)
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





