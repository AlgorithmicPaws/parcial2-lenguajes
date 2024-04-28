from FourierTransformVisitor import FourierTransformVisitor
from FourierTransformParser import FourierTransformParser
import math


class EvalVisitor(FourierTransformVisitor):
    resultados = []
    simbolos = []
    pulsos = []
    pulsoT = []

    def visitPrintExpr(self, ctx: FourierTransformParser.PrintExprContext):
        value = self.visit(ctx.func())
        print(value)
        return 0

    def visitInt(self, ctx: FourierTransformParser.IntContext):
        return int(ctx.INT().getText())

    def visitFuncion(self, ctx: FourierTransformParser.FuncionContext):
        transformada = self.visit(ctx(0))
        if self.pulsos[0] == self.pulsos[1]:
            if self.pulsoT:
                transformada = self.pulsos[0]+" * sinc²("+self.pulsos[0]+" * (w/(2 * pi)))"
            else: 
                if self.pulsos[0] == 0:
                    if '-1' in self.resultados:
                        transformada = "1/(j * pi * f)"
                    else: self.transformada = "1/(j * pi) + pi * dirac(w)"
                else: 
                    if 'T/2' in self.resultados:
                        transformada = "T * sinc(T * (w/(2 * pi)))"
                    elif 'T' in self.resultados:
                        transformada = "2 * T * sinc(T * (w/pi))"
                    else: 
                        transformada = self.pulsos[0]+" * T * sinc(T * (w/pi))"
        else: transformada = "los intervalos de la funcion no coinciden"
        return transformada

    def visitDeclaracion(self, ctx: FourierTransformParser.DeclaracionContext):
        if not self.pulsoT:
            resultado = self.visit(ctx.res())
            print(resultado)
            self.resultados.append(resultado)
        texto = ctx.getText()
        return texto
        
    def visitTriangular(self, ctx: FourierTransformParser.TriangularContext):
        pulso = self.visit(ctx.res())
        self.pulsoT.append(puslo)
        texto = ctx.getText()
        return texto

    def visitCondicion(self, ctx: FourierTransformParser.CondicionContext):
        print("entro")
        lonPulso = self.visit(ctx())
        print(lonPulso)
        self.pulsos.append(lonPulso)
        self.simbolos.append(ctx.op.type)
        texto = ctx.getText()
        return texto

    def visitDelta(self, ctx: FourierTransformParser.DeltaContext):
        transformada = '1'
        return transformada
        
    def visitSinFunc(self, ctx: FourierTransformParser.SinFuncContext):
        right = self.visit(ctx.trigFunc())
        transformada = "(pi/j) * dirac( w - "+right+" ) - (pi/j) * dirac( w + "+right+" )"
        return transformada

    def visitCosFunc(self, ctx: FourierTransformParser.CosFuncContext):
        right = self.visit(ctx.trigFunc())
        transformada = "pi * dirac( w - "+right+" ) + pi * dirac( w + "+right+" )"
        return transformada

    def visitSumatoria(self, ctx: FourierTransformParser.SumatoriaContext):
        right = self.visit(ctx.func())
        transformada = "(1/"+right+") * SUM(2 * pi * dirac(w - k((2 * pi)/"+right+")))"
        return transformada

