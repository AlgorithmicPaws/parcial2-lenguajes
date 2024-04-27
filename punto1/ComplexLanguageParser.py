# Generated from ComplexLanguage.g4 by ANTLR 4.13.1
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
        4,1,10,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        27,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,47,8,3,1,3,0,1,4,4,0,2,4,6,0,2,1,0,3,4,
        1,0,5,6,52,0,9,1,0,0,0,2,17,1,0,0,0,4,26,1,0,0,0,6,46,1,0,0,0,8,
        10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,
        12,1,1,0,0,0,13,14,3,4,2,0,14,15,5,9,0,0,15,18,1,0,0,0,16,18,5,9,
        0,0,17,13,1,0,0,0,17,16,1,0,0,0,18,3,1,0,0,0,19,20,6,2,-1,0,20,27,
        5,7,0,0,21,27,3,6,3,0,22,23,5,1,0,0,23,24,3,4,2,0,24,25,5,2,0,0,
        25,27,1,0,0,0,26,19,1,0,0,0,26,21,1,0,0,0,26,22,1,0,0,0,27,36,1,
        0,0,0,28,29,10,5,0,0,29,30,7,0,0,0,30,35,3,4,2,6,31,32,10,4,0,0,
        32,33,7,1,0,0,33,35,3,4,2,5,34,28,1,0,0,0,34,31,1,0,0,0,35,38,1,
        0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,5,1,0,0,0,38,36,1,0,0,0,39,
        40,5,7,0,0,40,41,7,1,0,0,41,47,5,8,0,0,42,43,5,8,0,0,43,44,7,1,0,
        0,44,47,5,8,0,0,45,47,5,8,0,0,46,39,1,0,0,0,46,42,1,0,0,0,46,45,
        1,0,0,0,47,7,1,0,0,0,6,11,17,26,34,36,46
    ]

class ComplexLanguageParser ( Parser ):

    grammarFileName = "ComplexLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "MUL", "DIV", 
                      "ADD", "SUB", "INT", "IMG", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_complex = 3

    ruleNames =  [ "prog", "stat", "expr", "complex" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    MUL=3
    DIV=4
    ADD=5
    SUB=6
    INT=7
    IMG=8
    NEWLINE=9
    WS=10

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
                return self.getTypedRuleContexts(ComplexLanguageParser.StatContext)
            else:
                return self.getTypedRuleContext(ComplexLanguageParser.StatContext,i)


        def getRuleIndex(self):
            return ComplexLanguageParser.RULE_prog

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

        localctx = ComplexLanguageParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 898) != 0)):
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
            return ComplexLanguageParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexLanguageParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(ComplexLanguageParser.NEWLINE, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexLanguageParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ComplexLanguageParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(ComplexLanguageParser.NEWLINE, 0)

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

        localctx = ComplexLanguageParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 7, 8]:
                localctx = ComplexLanguageParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(ComplexLanguageParser.NEWLINE)
                pass
            elif token in [9]:
                localctx = ComplexLanguageParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(ComplexLanguageParser.NEWLINE)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplexLanguageParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CompContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexLanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complex_(self):
            return self.getTypedRuleContext(ComplexLanguageParser.ComplexContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexLanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ComplexLanguageParser.ExprContext,0)


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


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexLanguageParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ComplexLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(ComplexLanguageParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ComplexLanguageParser.MUL, 0)
        def DIV(self):
            return self.getToken(ComplexLanguageParser.DIV, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexLanguageParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ComplexLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(ComplexLanguageParser.ExprContext,i)

        def ADD(self):
            return self.getToken(ComplexLanguageParser.ADD, 0)
        def SUB(self):
            return self.getToken(ComplexLanguageParser.SUB, 0)

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


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexLanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ComplexLanguageParser.INT, 0)

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
        localctx = ComplexLanguageParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ComplexLanguageParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.match(ComplexLanguageParser.INT)
                pass

            elif la_ == 2:
                localctx = ComplexLanguageParser.CompContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.complex_()
                pass

            elif la_ == 3:
                localctx = ComplexLanguageParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(ComplexLanguageParser.T__0)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(ComplexLanguageParser.T__1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ComplexLanguageParser.MulDivContext(self, ComplexLanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 29
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ComplexLanguageParser.AddSubContext(self, ComplexLanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 32
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        self.expr(5)
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComplexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplexLanguageParser.RULE_complex

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ImgContext(ComplexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexLanguageParser.ComplexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IMG(self):
            return self.getToken(ComplexLanguageParser.IMG, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImg" ):
                listener.enterImg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImg" ):
                listener.exitImg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImg" ):
                return visitor.visitImg(self)
            else:
                return visitor.visitChildren(self)


    class ComplejoContext(ComplexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexLanguageParser.ComplexContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ComplexLanguageParser.INT, 0)
        def IMG(self):
            return self.getToken(ComplexLanguageParser.IMG, 0)
        def ADD(self):
            return self.getToken(ComplexLanguageParser.ADD, 0)
        def SUB(self):
            return self.getToken(ComplexLanguageParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplejo" ):
                listener.enterComplejo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplejo" ):
                listener.exitComplejo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplejo" ):
                return visitor.visitComplejo(self)
            else:
                return visitor.visitChildren(self)


    class SumaComContext(ComplexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexLanguageParser.ComplexContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def IMG(self, i:int=None):
            if i is None:
                return self.getTokens(ComplexLanguageParser.IMG)
            else:
                return self.getToken(ComplexLanguageParser.IMG, i)
        def ADD(self):
            return self.getToken(ComplexLanguageParser.ADD, 0)
        def SUB(self):
            return self.getToken(ComplexLanguageParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumaCom" ):
                listener.enterSumaCom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumaCom" ):
                listener.exitSumaCom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaCom" ):
                return visitor.visitSumaCom(self)
            else:
                return visitor.visitChildren(self)



    def complex_(self):

        localctx = ComplexLanguageParser.ComplexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_complex)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = ComplexLanguageParser.ComplejoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(ComplexLanguageParser.INT)
                self.state = 40
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                self.match(ComplexLanguageParser.IMG)
                pass

            elif la_ == 2:
                localctx = ComplexLanguageParser.SumaComContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(ComplexLanguageParser.IMG)
                self.state = 43
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.match(ComplexLanguageParser.IMG)
                pass

            elif la_ == 3:
                localctx = ComplexLanguageParser.ImgContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(ComplexLanguageParser.IMG)
                pass


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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




