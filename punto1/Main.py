from antlr4 import *
from ComplexLanguageLexer import ComplexLanguageLexer
from ComplexLanguageParser import ComplexLanguageParser
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

    lexer = ComplexLanguageLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ComplexLanguageParser(tokens)
    tree = parser.prog()  # parse

    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()

