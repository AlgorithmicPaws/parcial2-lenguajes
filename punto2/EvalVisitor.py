from PythonFunctionVisitor import PythonFunctionVisitor
from PythonFunctionParser import PythonFunctionParser
import math

class EvalVisitor(PythonFunctionVisitor):
    memory_iterables = {}
    memory_iterables_funtion = {}
    memory_parametro = {}

    def visitPrint_stat(self, ctx:PythonFunctionParser.StatContext):
        value = self.visit(ctx.iterable_declaration())
        value = str(value)
        print(value)
        
        return 0
    
    def visitCreacion_iterable(self, ctx:PythonFunctionParser.Creacion_iterableContext):
        id_ = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.iterable_expression())
        self.memory_iterables[id_] = value 
        return value
    
    # Visit a parse tree produced by PythonFunctionParser#list.
    def visitList(self, ctx:PythonFunctionParser.ListContext):
        return self.visit(ctx.list_expression())


    # Visit a parse tree produced by PythonFunctionParser#tuple.
    def visitTuple(self, ctx:PythonFunctionParser.TupleContext):
        return self.visit(ctx.tuple_expression())



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
    
    def visitAssign_filter(self, ctx:PythonFunctionParser.Assign_filterContext):
        value = self.visit(ctx.filter_())
        print(value)
        return 0
    def visitExecute_filter(self, ctx:PythonFunctionParser.Execute_filterContext):
        print(ctx.getText())
        if ctx.IDENTIFIER(1).getText() in self.memory_iterables:
            iterable = self.memory_iterables[ctx.IDENTIFIER(1).getText()] 
        else:
            return 0
        if ctx.IDENTIFIER(0).getText() in self.memory_iterables_funtion:
            condition = self.memory_iterables_funtion[ctx.IDENTIFIER(0).getText()] 
        else:
            return 0
        
        def logical_op_list(condition, i, iterable_filtered):
            if condition[i] == '==':
                if condition[0] == condition[1]:
                    iterable_filtered.append(elemento)
            if condition[i] == '!=':
                if condition[0] != condition[1]:
                    iterable_filtered.append(elemento)
            if condition[i] == '>':
                if condition[0] > condition[1]:
                    iterable_filtered.append(elemento)
            if condition[i] == '<':
                if condition[0] < condition[1]:
                    iterable_filtered.append(elemento)
            if condition[i] == '>=':
                if condition[0] >= condition[1]:
                    iterable_filtered.append(elemento)
            if condition[i] == '<=':
                if condition[0] <= condition[1]:
                    iterable_filtered.append(elemento)            
        
        iterable_type = type(iterable)
        if iterable_type == list:
            iterable_filtered = []
            for elemento in iterable:
                for i in range(len(condition)):
                    if condition[i] == self.memory_parametro[ctx.IDENTIFIER(0).getText()]:
                        condition[i] = elemento 
                        pos_parametro = i
                        parametro = True 
                    elif condition[i] in ['==','!=','>','<','>=','<=']:
                        logical_op_list(condition,i,iterable_filtered)
                    else:
                        parametro = False 
                if parametro:
                    condition[pos_parametro] = self.memory_parametro[ctx.IDENTIFIER(0).getText()]
        elif iterable_type == tuple:

            iterable_filtered = ()
            for elemento in iterable:
                for i in range(len(condition)):
                    if condition[i] == self.memory_parametro[ctx.IDENTIFIER(0).getText()]:
                        condition[i] = elemento 
                        pos_parametro = i
                        parametro = True 
                    elif condition[i] in ['==','!=','>','<','>=','<=']:
                        if condition[i] == '==':
                            if condition[0] == condition[1]:
                                iterable_filtered += (elemento,)
                        if condition[i] == '!=':
                            if condition[0] != condition[1]:
                                iterable_filtered += (elemento,)
                        if condition[i] == '>':
                            if condition[0] > condition[1]:
                                iterable_filtered += (elemento,)
                        if condition[i] == '<':
                            if condition[0] < condition[1]:
                                iterable_filtered += (elemento,)
                        if condition[i] == '>=':
                            if condition[0] >= condition[1]:
                                iterable_filtered += (elemento,)
                        if condition[i] == '<=':
                            if condition[0] <= condition[1]:
                                iterable_filtered += (elemento,)
                    else:
                        parametro = False 
                if parametro:
                    condition[pos_parametro] = self.memory_parametro[ctx.IDENTIFIER(0).getText()]
        elif iterable_type == set:
            iterable_filtered = set()
            for elemento in iterable:
                for i in range(len(condition)):
                    if condition[i] == self.memory_parametro[ctx.IDENTIFIER(0).getText()]:
                        condition[i] = elemento 
                        pos_parametro = i
                        parametro = True 
                    elif condition[i] in ['==','!=','>','<','>=','<=']:
                        if condition[i] == '==':
                            if condition[0] == condition[1]:
                                iterable_filtered.add(elemento)
                        elif condition[i] == '!=':
                            if condition[0] != condition[1]:
                                iterable_filtered.add(elemento)
                        elif condition[i] == '>':
                            if condition[0] > condition[1]:
                                iterable_filtered.add(elemento)
                        elif condition[i] == '<':
                            if condition[0] < condition[1]:
                                iterable_filtered.add(elemento)
                        elif condition[i] == '>=':
                            if condition[0] >= condition[1]:
                                iterable_filtered.add(elemento)
                        elif condition[i] == '<=':
                            if condition[0] <= condition[1]:
                                iterable_filtered.add(elemento)
                    else:
                        parametro = False 
                if parametro:
                    condition[pos_parametro] =  self.memory_parametro[ctx.IDENTIFIER(0).getText()]
        return iterable_filtered

    def visitDef(self, ctx:PythonFunctionParser.DefContext):
        print(ctx.getText())
        id_ = ctx.IDENTIFIER(0).getText()
        self.memory_parametro[id_] = ctx.IDENTIFIER(1).getText()
        global id_actual 
        id_actual = ctx.IDENTIFIER(0).getText()
        value = self.visit(ctx.condition()) 
        self.memory_iterables_funtion[id_] = value 
        return value
    




    # Visit a parse tree produced by PythonFunctionParser#always_condition.
    def visitAlways_condition(self, ctx:PythonFunctionParser.Always_conditionContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == PythonFunctionParser.IGUAL:
            operator = '=='
        elif ctx.op.type == PythonFunctionParser.NOIGUAL:
            operator = '!='
        elif ctx.op.type == PythonFunctionParser.MAYOR:
            operator = '>'
        elif ctx.op.type == PythonFunctionParser.MENOR:
            operator = '<'
        elif ctx.op.type == PythonFunctionParser.MAYORIGUAL:
            operator = '>='
        elif ctx.op.type == PythonFunctionParser.MENORIGUAL:
            operator = '<='
        return [left, right, operator ]


    # Visit a parse tree produced by PythonFunctionParser#parameter_condition.
    def visitParameter_condition(self, ctx:PythonFunctionParser.Parameter_conditionContext):
        if self.memory_parametro[id_actual] == ctx.IDENTIFIER().getText():
            left = ctx.IDENTIFIER().getText()
        else:
            return 0
        right = self.visit(ctx.expr())
        if ctx.op.type == PythonFunctionParser.IGUAL:
            operator = '=='
        elif ctx.op.type == PythonFunctionParser.NOIGUAL:
            operator = '!='
        elif ctx.op.type == PythonFunctionParser.MAYOR:
            operator = '>'
        elif ctx.op.type == PythonFunctionParser.MENOR:
            operator = '<'
        elif ctx.op.type == PythonFunctionParser.MAYORIGUAL:
            operator = '>='
        elif ctx.op.type == PythonFunctionParser.MENORIGUAL:
            operator = '<='
        return [left, right, operator ]


    # Visit a parse tree produced by PythonFunctionParser#condition_parameter.
    def visitCondition_parameter(self, ctx:PythonFunctionParser.Condition_parameterContext):
        if self.memory_parametro[id_actual] == ctx.IDENTIFIER().getText():
            right = ctx.IDENTIFIER().getText()
        else:
            return 0
        left = self.visit(ctx.expr())
        if ctx.op.type == PythonFunctionParser.IGUAL:
            operator = '=='
        elif ctx.op.type == PythonFunctionParser.NOIGUAL:
            operator = '!='
        elif ctx.op.type == PythonFunctionParser.MAYOR:
            operator = '>'
        elif ctx.op.type == PythonFunctionParser.MENOR:
            operator = '<'
        elif ctx.op.type == PythonFunctionParser.MAYORIGUAL:
            operator = '>='
        elif ctx.op.type == PythonFunctionParser.MENORIGUAL:
            operator = '<='
        return [left, right, operator ]




    def visitAssign(self, ctx: PythonFunctionParser.AssignContext):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory_iterables[id_] = value
        return value


    def visitInt(self, ctx: PythonFunctionParser.IntContext):
        return int(ctx.INT().getText())

    def visitId(self, ctx: PythonFunctionParser.IdContext):
        id_ = ctx.ID().getText()
        if id_ in self.memory_iterables:
            return self.memory_iterables[id_]
        return 0

    def visitHex(self, ctx: PythonFunctionParser.HexContext):
        hex_value = ctx.getText()
        decimal_value = int(hex_value[2:], 16)
        return decimal_value

    def visitMulDiv(self, ctx: PythonFunctionParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == PythonFunctionParser.MUL:
            return left * right
        else:
            if right != 0:
                return left / right
            else:
                print("Error: División por cero")
                return 0

    def visitAddSub(self, ctx: PythonFunctionParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left + right if ctx.op.type == PythonFunctionParser.ADD else left - right

    def visitParens(self, ctx: PythonFunctionParser.ParensContext):
        return self.visit(ctx.expr())

    def visitSenFunc(self, ctx: PythonFunctionParser.SenFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return round(math.sin(arg))

    def visitCosFunc(self, ctx: PythonFunctionParser.CosFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return round(math.cos(arg))

    def visitTanFunc(self, ctx: PythonFunctionParser.TanFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return round(math.tan(arg))

    def visitAbs(self, ctx: PythonFunctionParser.AbsContext):
        value = self.visit(ctx.expr())
        return abs(value)
