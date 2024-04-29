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
        self.resultados = []
        self.simbolos = []
        self.pulsos = []
        self.pulsoT = []
        return 0

    def visitInt(self, ctx: FourierTransformParser.IntContext):
        return int(ctx.INT().getText())
        
    def visitInts(self, ctx: FourierTransformParser.IntsContext):
        return int(ctx.INT().getText())
    
    def visitInteger(self, ctx: FourierTransformParser.IntegerContext):
        return int(ctx.INT().getText())
    
    def visitLongP(self, ctx: FourierTransformParser.LongPContext):
        return ctx.PULS().getText()
     
    def visitFrecuency(self, ctx: FourierTransformParser.FrecuencyContext):
        return ctx.FRE().getText()

    def visitFuncion(self, ctx: FourierTransformParser.FuncionContext):
        transformada = self.visit(ctx.dec(0))+'|'+self.visit(ctx.dec(1))
        if not self.comprobarSimbolo():
            transformada = "las desigualdades de las condiciones no están bien establecidos"
            return transformada
        if self.pulsos[0] == self.pulsos[1]:
            if self.pulsoT:
                transformada = self.pulsos[0]+" * sinc²("+self.pulsos[0]+" * (w/(2 * pi)))"
            else: 
                if self.pulsos[0] == 0:
                    if (-1) in self.resultados:
                        transformada = "1/(j * pi * f)"
                    else: transformada = "1/(j * pi) + pi * dirac(w)"
                else: 
                    if 'T/2' in self.pulsos:
                        transformada = "T * sinc(T * (w/(2 * pi)))"
                    elif 'T' in self.pulsos:
                        transformada = "2 * T * sinc(T * (w/pi))"
                    else: 
                        transformada = str(self.pulsos[0])+" * T * sinc(T * (w/pi))"
        else: transformada = "los intervalos de la funcion no coinciden"
        return transformada

    def visitDeclaracion(self, ctx: FourierTransformParser.DeclaracionContext):
        resultado = self.visit(ctx.res())
        self.resultados.append(resultado)
        self.visit(ctx.cond())
        texto = ctx.getText()
        return texto
        
    def visitTriangular(self, ctx: FourierTransformParser.TriangularContext):
        pulso = self.visit(ctx.pul())
        self.pulsoT.append(pulso)
        texto = ctx.getText()
        return texto

    def visitCondicion(self, ctx: FourierTransformParser.CondicionContext):
        lonPulso = self.visit(ctx.pul())
        self.pulsos.append(lonPulso)
        self.simbolos.append(ctx.op.text)
        texto = ctx.getText()
        return texto

    def visitDelta(self, ctx: FourierTransformParser.DeltaContext):
        transformada = '1'
        return transformada
        
    def visitSinFunc(self, ctx: FourierTransformParser.SinFuncContext):
        right = str(self.visit(ctx.frec()))
        transformada = "(pi/j) * dirac( w' - "+right+" ) - (pi/j) * dirac( w' + "+right+" )"
        return transformada

    def visitCosFunc(self, ctx: FourierTransformParser.CosFuncContext):
        right = str(self.visit(ctx.frec()))
        transformada = "pi * dirac( w' - "+right+" ) + pi * dirac( w' + "+right+" )"
        return transformada

    def visitSumatoria(self, ctx: FourierTransformParser.SumatoriaContext):
        right = self.visit(ctx.pul())
        transformada = "(1/"+right+") * SUM(2 * pi * dirac(w - k((2 * pi)/"+right+")))"
        return transformada
        
    def comprobarSimbolo(self):
        lonPrimero = len(self.simbolos[0])
        if lonPrimero == 1:
            if self.simbolos[1][0] != self.simbolos[0][0]:
                return True
        else:
            if '=' not in self.simbolos[1]:
                if  self.simbolos[0][0] != self.simbolos[1][0]:
                    return True
        return False
                

