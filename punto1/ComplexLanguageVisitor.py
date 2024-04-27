# Generated from ComplexLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ComplexLanguageParser import ComplexLanguageParser
else:
    from ComplexLanguageParser import ComplexLanguageParser

# This class defines a complete generic visitor for a parse tree produced by ComplexLanguageParser.

class ComplexLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComplexLanguageParser#prog.
    def visitProg(self, ctx:ComplexLanguageParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexLanguageParser#printExpr.
    def visitPrintExpr(self, ctx:ComplexLanguageParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexLanguageParser#blank.
    def visitBlank(self, ctx:ComplexLanguageParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexLanguageParser#comp.
    def visitComp(self, ctx:ComplexLanguageParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexLanguageParser#parens.
    def visitParens(self, ctx:ComplexLanguageParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexLanguageParser#MulDiv.
    def visitMulDiv(self, ctx:ComplexLanguageParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexLanguageParser#AddSub.
    def visitAddSub(self, ctx:ComplexLanguageParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexLanguageParser#int.
    def visitInt(self, ctx:ComplexLanguageParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexLanguageParser#complejo.
    def visitComplejo(self, ctx:ComplexLanguageParser.ComplejoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexLanguageParser#sumaCom.
    def visitSumaCom(self, ctx:ComplexLanguageParser.SumaComContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexLanguageParser#img.
    def visitImg(self, ctx:ComplexLanguageParser.ImgContext):
        return self.visitChildren(ctx)



del ComplexLanguageParser