import tokenize 
import ast

def to_nodes(node):
    return [x for x in ast.walk(node)]

def to_iter(node: ast.AST):
    return iter([x for x in ast.walk(node)])
 
