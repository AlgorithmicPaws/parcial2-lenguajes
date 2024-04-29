# Generated from FourierTransform.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FourierTransformParser import FourierTransformParser
else:
    from FourierTransformParser import FourierTransformParser

# This class defines a complete generic visitor for a parse tree produced by FourierTransformParser.

class FourierTransformVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FourierTransformParser#prog.
    def visitProg(self, ctx:FourierTransformParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#printExpr.
    def visitPrintExpr(self, ctx:FourierTransformParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#blank.
    def visitBlank(self, ctx:FourierTransformParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#funcion.
    def visitFuncion(self, ctx:FourierTransformParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#trigonometricas.
    def visitTrigonometricas(self, ctx:FourierTransformParser.TrigonometricasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#delta.
    def visitDelta(self, ctx:FourierTransformParser.DeltaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#sumatoria.
    def visitSumatoria(self, ctx:FourierTransformParser.SumatoriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#declaracion.
    def visitDeclaracion(self, ctx:FourierTransformParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#triangular.
    def visitTriangular(self, ctx:FourierTransformParser.TriangularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#int.
    def visitInt(self, ctx:FourierTransformParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#condicion.
    def visitCondicion(self, ctx:FourierTransformParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#CosFunc.
    def visitCosFunc(self, ctx:FourierTransformParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#SinFunc.
    def visitSinFunc(self, ctx:FourierTransformParser.SinFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#ints.
    def visitInts(self, ctx:FourierTransformParser.IntsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#longP.
    def visitLongP(self, ctx:FourierTransformParser.LongPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#integer.
    def visitInteger(self, ctx:FourierTransformParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierTransformParser#frecuency.
    def visitFrecuency(self, ctx:FourierTransformParser.FrecuencyContext):
        return self.visitChildren(ctx)



del FourierTransformParser