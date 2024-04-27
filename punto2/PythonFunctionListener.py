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


    # Enter a parse tree produced by PythonFunctionParser#stat.
    def enterStat(self, ctx:PythonFunctionParser.StatContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#stat.
    def exitStat(self, ctx:PythonFunctionParser.StatContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#function_declaration.
    def enterFunction_declaration(self, ctx:PythonFunctionParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#function_declaration.
    def exitFunction_declaration(self, ctx:PythonFunctionParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#function_name.
    def enterFunction_name(self, ctx:PythonFunctionParser.Function_nameContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#function_name.
    def exitFunction_name(self, ctx:PythonFunctionParser.Function_nameContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#parameter_list.
    def enterParameter_list(self, ctx:PythonFunctionParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#parameter_list.
    def exitParameter_list(self, ctx:PythonFunctionParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#parameter.
    def enterParameter(self, ctx:PythonFunctionParser.ParameterContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#parameter.
    def exitParameter(self, ctx:PythonFunctionParser.ParameterContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#function_body.
    def enterFunction_body(self, ctx:PythonFunctionParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#function_body.
    def exitFunction_body(self, ctx:PythonFunctionParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#statement_block.
    def enterStatement_block(self, ctx:PythonFunctionParser.Statement_blockContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#statement_block.
    def exitStatement_block(self, ctx:PythonFunctionParser.Statement_blockContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#statements.
    def enterStatements(self, ctx:PythonFunctionParser.StatementsContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#statements.
    def exitStatements(self, ctx:PythonFunctionParser.StatementsContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#statement.
    def enterStatement(self, ctx:PythonFunctionParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#statement.
    def exitStatement(self, ctx:PythonFunctionParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#expression_statement.
    def enterExpression_statement(self, ctx:PythonFunctionParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#expression_statement.
    def exitExpression_statement(self, ctx:PythonFunctionParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#expression.
    def enterExpression(self, ctx:PythonFunctionParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#expression.
    def exitExpression(self, ctx:PythonFunctionParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#iterable_declaration.
    def enterIterable_declaration(self, ctx:PythonFunctionParser.Iterable_declarationContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#iterable_declaration.
    def exitIterable_declaration(self, ctx:PythonFunctionParser.Iterable_declarationContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#iterable_name.
    def enterIterable_name(self, ctx:PythonFunctionParser.Iterable_nameContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#iterable_name.
    def exitIterable_name(self, ctx:PythonFunctionParser.Iterable_nameContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#iterable_expression.
    def enterIterable_expression(self, ctx:PythonFunctionParser.Iterable_expressionContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#iterable_expression.
    def exitIterable_expression(self, ctx:PythonFunctionParser.Iterable_expressionContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#list_expression.
    def enterList_expression(self, ctx:PythonFunctionParser.List_expressionContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#list_expression.
    def exitList_expression(self, ctx:PythonFunctionParser.List_expressionContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#tuple_expression.
    def enterTuple_expression(self, ctx:PythonFunctionParser.Tuple_expressionContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#tuple_expression.
    def exitTuple_expression(self, ctx:PythonFunctionParser.Tuple_expressionContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#string_expression.
    def enterString_expression(self, ctx:PythonFunctionParser.String_expressionContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#string_expression.
    def exitString_expression(self, ctx:PythonFunctionParser.String_expressionContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#set_expression.
    def enterSet_expression(self, ctx:PythonFunctionParser.Set_expressionContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#set_expression.
    def exitSet_expression(self, ctx:PythonFunctionParser.Set_expressionContext):
        pass


    # Enter a parse tree produced by PythonFunctionParser#expression_list.
    def enterExpression_list(self, ctx:PythonFunctionParser.Expression_listContext):
        pass

    # Exit a parse tree produced by PythonFunctionParser#expression_list.
    def exitExpression_list(self, ctx:PythonFunctionParser.Expression_listContext):
        pass



del PythonFunctionParser