# Generated from PythonFunction.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonFunctionParser import PythonFunctionParser
else:
    from PythonFunctionParser import PythonFunctionParser

# This class defines a complete listener for a parse tree produced by PythonFunctionParser.
class PythonFunctionListener(ParseTreeListener):

    # Enter a parse tree produced by PythonFunctionParser#prog.
    def enterProg(self, ctx:PythonFunctionParser.ProgContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#prog.
    def exitProg(self, ctx:PythonFunctionParser.ProgContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#print_stat.
    def enterPrint_stat(self, ctx:PythonFunctionParser.Print_statContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#print_stat.
    def exitPrint_stat(self, ctx:PythonFunctionParser.Print_statContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#assign.
    def enterAssign(self, ctx:PythonFunctionParser.AssignContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#assign.
    def exitAssign(self, ctx:PythonFunctionParser.AssignContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#filter.
    def enterFilter(self, ctx:PythonFunctionParser.FilterContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#filter.
    def exitFilter(self, ctx:PythonFunctionParser.FilterContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#condition.
    def enterCondition(self, ctx:PythonFunctionParser.ConditionContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#condition.
    def exitCondition(self, ctx:PythonFunctionParser.ConditionContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#parens.
    def enterParens(self, ctx:PythonFunctionParser.ParensContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#parens.
    def exitParens(self, ctx:PythonFunctionParser.ParensContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#Abs.
    def enterAbs(self, ctx:PythonFunctionParser.AbsContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#Abs.
    def exitAbs(self, ctx:PythonFunctionParser.AbsContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#MulDiv.
    def enterMulDiv(self, ctx:PythonFunctionParser.MulDivContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#MulDiv.
    def exitMulDiv(self, ctx:PythonFunctionParser.MulDivContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#AddSub.
    def enterAddSub(self, ctx:PythonFunctionParser.AddSubContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#AddSub.
    def exitAddSub(self, ctx:PythonFunctionParser.AddSubContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#TrigFunction.
    def enterTrigFunction(self, ctx:PythonFunctionParser.TrigFunctionContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#TrigFunction.
    def exitTrigFunction(self, ctx:PythonFunctionParser.TrigFunctionContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#hex.
    def enterHex(self, ctx:PythonFunctionParser.HexContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#hex.
    def exitHex(self, ctx:PythonFunctionParser.HexContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#id.
    def enterId(self, ctx:PythonFunctionParser.IdContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#id.
    def exitId(self, ctx:PythonFunctionParser.IdContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#int.
    def enterInt(self, ctx:PythonFunctionParser.IntContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#int.
    def exitInt(self, ctx:PythonFunctionParser.IntContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#CosFunc.
    def enterCosFunc(self, ctx:PythonFunctionParser.CosFuncContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#CosFunc.
    def exitCosFunc(self, ctx:PythonFunctionParser.CosFuncContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#SenFunc.
    def enterSenFunc(self, ctx:PythonFunctionParser.SenFuncContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#SenFunc.
    def exitSenFunc(self, ctx:PythonFunctionParser.SenFuncContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#TanFunc.
    def enterTanFunc(self, ctx:PythonFunctionParser.TanFuncContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#TanFunc.
    def exitTanFunc(self, ctx:PythonFunctionParser.TanFuncContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#creacion_iterable.
    def enterCreacion_iterable(self, ctx:PythonFunctionParser.Creacion_iterableContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#creacion_iterable.
    def exitCreacion_iterable(self, ctx:PythonFunctionParser.Creacion_iterableContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#list.
    def enterList(self, ctx:PythonFunctionParser.ListContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#list.
    def exitList(self, ctx:PythonFunctionParser.ListContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#tuple.
    def enterTuple(self, ctx:PythonFunctionParser.TupleContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#tuple.
    def exitTuple(self, ctx:PythonFunctionParser.TupleContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#string.
    def enterString(self, ctx:PythonFunctionParser.StringContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#string.
    def exitString(self, ctx:PythonFunctionParser.StringContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#set.
    def enterSet(self, ctx:PythonFunctionParser.SetContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#set.
    def exitSet(self, ctx:PythonFunctionParser.SetContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#accion_list.
    def enterAccion_list(self, ctx:PythonFunctionParser.Accion_listContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#accion_list.
    def exitAccion_list(self, ctx:PythonFunctionParser.Accion_listContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#empty_list.
    def enterEmpty_list(self, ctx:PythonFunctionParser.Empty_listContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#empty_list.
    def exitEmpty_list(self, ctx:PythonFunctionParser.Empty_listContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#accion_tuple.
    def enterAccion_tuple(self, ctx:PythonFunctionParser.Accion_tupleContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#accion_tuple.
    def exitAccion_tuple(self, ctx:PythonFunctionParser.Accion_tupleContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#empty_tuple.
    def enterEmpty_tuple(self, ctx:PythonFunctionParser.Empty_tupleContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#empty_tuple.
    def exitEmpty_tuple(self, ctx:PythonFunctionParser.Empty_tupleContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#accion_string.
    def enterAccion_string(self, ctx:PythonFunctionParser.Accion_stringContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#accion_string.
    def exitAccion_string(self, ctx:PythonFunctionParser.Accion_stringContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#accion_set.
    def enterAccion_set(self, ctx:PythonFunctionParser.Accion_setContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#accion_set.
    def exitAccion_set(self, ctx:PythonFunctionParser.Accion_setContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#empty_set.
    def enterEmpty_set(self, ctx:PythonFunctionParser.Empty_setContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#empty_set.
    def exitEmpty_set(self, ctx:PythonFunctionParser.Empty_setContext):
        pass



del PythonFunctionParser