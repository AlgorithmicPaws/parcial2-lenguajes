from PythonFunctionVisitor import PythonFunctionVisitor
from PythonFunctionParser import PythonFunctionParser
import math

class EvalVisitor(PythonFunctionVisitor):
    memory = {}
    def visitPrint_stat(self, ctx:PythonFunctionParser.StatContext):
        value = self.visit(ctx.iterable_declaration())
        print(type(value))
        print(len(value))
        value = str(value)
        print(value)
        
        return 0
    def visitCreacion_iterable(self, ctx:PythonFunctionParser.Creacion_iterableContext):
        id_ = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.iterable_expression())
        self.memory[id_] = value 
        return value
    
    # Visit a parse tree produced by PythonFunctionParser#list.
    def visitList(self, ctx:PythonFunctionParser.ListContext):
        return self.visit(ctx.list_expression())


    # Visit a parse tree produced by PythonFunctionParser#tuple.
    def visitTuple(self, ctx:PythonFunctionParser.TupleContext):
        return self.visit(ctx.tuple_expression())


    # Visit a parse tree produced by PythonFunctionParser#string.
    def visitString(self, ctx:PythonFunctionParser.StringContext):
        return self.visit(ctx.string_expression())


    # Visit a parse tree produced by PythonFunctionParser#set.
    def visitSet(self, ctx:PythonFunctionParser.SetContext):
        return self.visit(ctx.set_expression())

    def visitAccion_list(self, ctx:PythonFunctionParser.Accion_listContext):
        value = ctx.getText()
        list = []
        for character in value:
            if character != '[' and character != ']'  and character != ',' :
                list.append(int(character))
        return list

    # Visit a parse tree produced by PythonFunctionParser#empty_list.
    def visitEmpty_list(self, ctx:PythonFunctionParser.Empty_listContext):
        return []


    # Visit a parse tree produced by PythonFunctionParser#accion_tuple.
    def visitAccion_tuple(self, ctx:PythonFunctionParser.Accion_tupleContext):
        value = ctx.getText()
        tuple = ()
        for character in value:
            if character != '(' and character != ')'  and character != ',' :
                tuple = tuple + (int(character),)
        return tuple


    # Visit a parse tree produced by PythonFunctionParser#empty_tuple.
    def visitEmpty_tuple(self, ctx:PythonFunctionParser.Empty_tupleContext):
        return ()


    # Visit a parse tree produced by PythonFunctionParser#accion_string.
    def visitAccion_string(self, ctx:PythonFunctionParser.Accion_stringContext):
        return ctx.getText()


    # Visit a parse tree produced by PythonFunctionParser#accion_set.
    def visitAccion_set(self, ctx:PythonFunctionParser.Accion_setContext):
        value = ctx.getText()
        a = set({})
        for character in value:
            if character != '{' and character != '}'  and character != ',' :
                a.add(int(character))
        return a


    # Visit a parse tree produced by PythonFunctionParser#empty_set.
    def visitEmpty_set(self, ctx:PythonFunctionParser.Empty_setContext):
        return set({})
    