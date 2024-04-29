# Generated from PythonFunction.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonFunctionParser import PythonFunctionParser
else:
    from PythonFunctionParser import PythonFunctionParser

# This class defines a complete generic visitor for a parse tree produced by PythonFunctionParser.

class PythonFunctionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonFunctionParser#prog.
    def visitProg(self, ctx:PythonFunctionParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#creacion_function_fillter.
    def visitCreacion_function_fillter(self, ctx:PythonFunctionParser.Creacion_function_fillterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#print_stat.
    def visitPrint_stat(self, ctx:PythonFunctionParser.Print_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#assign.
    def visitAssign(self, ctx:PythonFunctionParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#assign_filter.
    def visitAssign_filter(self, ctx:PythonFunctionParser.Assign_filterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#def.
    def visitDef(self, ctx:PythonFunctionParser.DefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#execute_filter.
    def visitExecute_filter(self, ctx:PythonFunctionParser.Execute_filterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#always_condition.
    def visitAlways_condition(self, ctx:PythonFunctionParser.Always_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#parameter_condition.
    def visitParameter_condition(self, ctx:PythonFunctionParser.Parameter_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#condition_parameter.
    def visitCondition_parameter(self, ctx:PythonFunctionParser.Condition_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#parens.
    def visitParens(self, ctx:PythonFunctionParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#Abs.
    def visitAbs(self, ctx:PythonFunctionParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#MulDiv.
    def visitMulDiv(self, ctx:PythonFunctionParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#AddSub.
    def visitAddSub(self, ctx:PythonFunctionParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#TrigFunction.
    def visitTrigFunction(self, ctx:PythonFunctionParser.TrigFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#hex.
    def visitHex(self, ctx:PythonFunctionParser.HexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#id.
    def visitId(self, ctx:PythonFunctionParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#int.
    def visitInt(self, ctx:PythonFunctionParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#CosFunc.
    def visitCosFunc(self, ctx:PythonFunctionParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#SenFunc.
    def visitSenFunc(self, ctx:PythonFunctionParser.SenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#TanFunc.
    def visitTanFunc(self, ctx:PythonFunctionParser.TanFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#creacion_iterable.
    def visitCreacion_iterable(self, ctx:PythonFunctionParser.Creacion_iterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#list.
    def visitList(self, ctx:PythonFunctionParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#tuple.
    def visitTuple(self, ctx:PythonFunctionParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#set.
    def visitSet(self, ctx:PythonFunctionParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#accion_list.
    def visitAccion_list(self, ctx:PythonFunctionParser.Accion_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#empty_list.
    def visitEmpty_list(self, ctx:PythonFunctionParser.Empty_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#accion_tuple.
    def visitAccion_tuple(self, ctx:PythonFunctionParser.Accion_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#empty_tuple.
    def visitEmpty_tuple(self, ctx:PythonFunctionParser.Empty_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#accion_set.
    def visitAccion_set(self, ctx:PythonFunctionParser.Accion_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#empty_set.
    def visitEmpty_set(self, ctx:PythonFunctionParser.Empty_setContext):
        return self.visitChildren(ctx)



del PythonFunctionParser