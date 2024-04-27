# Generated from ComplexLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ComplexLanguageParser import ComplexLanguageParser
else:
    from ComplexLanguageParser import ComplexLanguageParser

# This class defines a complete listener for a parse tree produced by ComplexLanguageParser.
class ComplexLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by ComplexLanguageParser#prog.
    def enterProg(self, ctx:ComplexLanguageParser.ProgContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#prog.
    def exitProg(self, ctx:ComplexLanguageParser.ProgContext):
        pass


    # Enter a parse tree produced by ComplexLanguageParser#printExpr.
    def enterPrintExpr(self, ctx:ComplexLanguageParser.PrintExprContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#printExpr.
    def exitPrintExpr(self, ctx:ComplexLanguageParser.PrintExprContext):
        pass


    # Enter a parse tree produced by ComplexLanguageParser#blank.
    def enterBlank(self, ctx:ComplexLanguageParser.BlankContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#blank.
    def exitBlank(self, ctx:ComplexLanguageParser.BlankContext):
        pass


    # Enter a parse tree produced by ComplexLanguageParser#comp.
    def enterComp(self, ctx:ComplexLanguageParser.CompContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#comp.
    def exitComp(self, ctx:ComplexLanguageParser.CompContext):
        pass


    # Enter a parse tree produced by ComplexLanguageParser#parens.
    def enterParens(self, ctx:ComplexLanguageParser.ParensContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#parens.
    def exitParens(self, ctx:ComplexLanguageParser.ParensContext):
        pass


    # Enter a parse tree produced by ComplexLanguageParser#MulDiv.
    def enterMulDiv(self, ctx:ComplexLanguageParser.MulDivContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#MulDiv.
    def exitMulDiv(self, ctx:ComplexLanguageParser.MulDivContext):
        pass


    # Enter a parse tree produced by ComplexLanguageParser#AddSub.
    def enterAddSub(self, ctx:ComplexLanguageParser.AddSubContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#AddSub.
    def exitAddSub(self, ctx:ComplexLanguageParser.AddSubContext):
        pass


    # Enter a parse tree produced by ComplexLanguageParser#int.
    def enterInt(self, ctx:ComplexLanguageParser.IntContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#int.
    def exitInt(self, ctx:ComplexLanguageParser.IntContext):
        pass


    # Enter a parse tree produced by ComplexLanguageParser#complejo.
    def enterComplejo(self, ctx:ComplexLanguageParser.ComplejoContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#complejo.
    def exitComplejo(self, ctx:ComplexLanguageParser.ComplejoContext):
        pass


    # Enter a parse tree produced by ComplexLanguageParser#sumaCom.
    def enterSumaCom(self, ctx:ComplexLanguageParser.SumaComContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#sumaCom.
    def exitSumaCom(self, ctx:ComplexLanguageParser.SumaComContext):
        pass


    # Enter a parse tree produced by ComplexLanguageParser#img.
    def enterImg(self, ctx:ComplexLanguageParser.ImgContext):
        pass

    # Exit a parse tree produced by ComplexLanguageParser#img.
    def exitImg(self, ctx:ComplexLanguageParser.ImgContext):
        pass



del ComplexLanguageParser