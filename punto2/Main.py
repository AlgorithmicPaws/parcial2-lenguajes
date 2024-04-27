from antlr4 import *
from PythonFunctionLexer import PythonFunctionLexer
from PythonFunctionParser import PythonFunctionParser
from EvalVisitor import EvalVisitor
import sys

def main():
    input_file = None
    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    if input_file:
        input_stream = FileStream(input_file)
    else:
        input_stream = InputStream(input())

    lexer = PythonFunctionLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PythonFunctionParser(tokens)
    tree = parser.prog()  # parse

    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()