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


    # Visit a parse tree produced by PythonFunctionParser#stat.
    def visitStat(self, ctx:PythonFunctionParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#function_declaration.
    def visitFunction_declaration(self, ctx:PythonFunctionParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#function_name.
    def visitFunction_name(self, ctx:PythonFunctionParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#parameter_list.
    def visitParameter_list(self, ctx:PythonFunctionParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#parameter.
    def visitParameter(self, ctx:PythonFunctionParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#function_body.
    def visitFunction_body(self, ctx:PythonFunctionParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#statement_block.
    def visitStatement_block(self, ctx:PythonFunctionParser.Statement_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#statements.
    def visitStatements(self, ctx:PythonFunctionParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#statement.
    def visitStatement(self, ctx:PythonFunctionParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#expression_statement.
    def visitExpression_statement(self, ctx:PythonFunctionParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#expression.
    def visitExpression(self, ctx:PythonFunctionParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#iterable_declaration.
    def visitIterable_declaration(self, ctx:PythonFunctionParser.Iterable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#iterable_name.
    def visitIterable_name(self, ctx:PythonFunctionParser.Iterable_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#iterable_expression.
    def visitIterable_expression(self, ctx:PythonFunctionParser.Iterable_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#list_expression.
    def visitList_expression(self, ctx:PythonFunctionParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#tuple_expression.
    def visitTuple_expression(self, ctx:PythonFunctionParser.Tuple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#string_expression.
    def visitString_expression(self, ctx:PythonFunctionParser.String_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#set_expression.
    def visitSet_expression(self, ctx:PythonFunctionParser.Set_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonFunctionParser#expression_list.
    def visitExpression_list(self, ctx:PythonFunctionParser.Expression_listContext):
        return self.visitChildren(ctx)



del PythonFunctionParser