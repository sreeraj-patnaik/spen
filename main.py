from lexer import tokenize
from parser import parse
from interpreter import Interpreter


with open("program.sp") as f:
    code = f.read()

tokens = tokenize(code)

ast = parse(tokens)

interpreter = Interpreter()

interpreter.run(ast)