from ComplexLanguageVisitor import ComplexLanguageVisitor
from ComplexLanguageParser import ComplexLanguageParser
import math


class EvalVisitor(ComplexLanguageVisitor):
    def visitPrintExpr(self, ctx: ComplexLanguageParser.PrintExprContext):
        value = self.visit(ctx.expr())
        value =str(value).replace('j', 'i')
        print(value)
        return 0

    def visitInt(self, ctx: ComplexLanguageParser.IntContext):
        return int(ctx.INT().getText())
    
    def visitImg(self, ctx: ComplexLanguageParser.ImgContext):
        texto = ctx.getText()
        numero_complejo = str(texto).replace('i', 'j')
        # Convertir el texto a un número complejo
        numero_complejo = complex(numero_complejo)
        return numero_complejo
    
    def visitComp(self, ctx: ComplexLanguageParser.CompContext):
        texto = ctx.getText()
        # Convertir el texto a un número complejo
        numero_complejo = str(texto).replace('i', 'j')
        numero_complejo = complex(numero_complejo)
        return numero_complejo

    def visitMulDiv(self, ctx: ComplexLanguageParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == ComplexLanguageParser.MUL:
            return left * right
        else:
            if right != 0:
                return left / right
            else:
                print("Error: División por cero")
                return 0

    def visitAddSub(self, ctx: ComplexLanguageParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left + right if ctx.op.type == ComplexLanguageParser.ADD else left - right

    def visitParens(self, ctx: ComplexLanguageParser.ParensContext):
        return self.visit(ctx.expr())

    def visitComplejo(self, ctx: ComplexLanguageParser.ComplejoContext):
        left = self.visit(ctx.complex(0))
        right = self.visit(ctx.complex(1))
        if ctx.op.type == ComplexLanguageParser.ADD:
            texto = str(left + '+' + right)
        else: texto = str(left + '-' + right)
        numero_complejo = str(texto).replace('i', 'j')
        numero_complejo = complex(texto)
        return numero_complejo
        
    def visitSumaCom(self, ctx: ComplexLanguageParser.SumaComContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left + right if ctx.op.type == ComplexLanguageParser.ADD else left - right
        

