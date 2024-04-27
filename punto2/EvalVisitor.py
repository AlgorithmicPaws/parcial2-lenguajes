from PythonFunctionVisitor import PythonFunctionVisitor
from PythonFunctionParser import PythonFunctionParser
import math

class EvalVisitor(PythonFunctionVisitor):
    memory = {}
    def visitStat(self, ctx:PythonFunctionParser.StatContext):
        
        pass
