import ast
import sys 
import os
from util import BoolMap, StringMap, DictMap, ListMap, IntMap, BytesMap


selfflag = False
all_dicts = [StringMap, IntMap, BoolMap, ListMap, DictMap, BytesMap]


def find_type(name: str):
    if name == "self":
        global selfflag
        selfflag = True   
        return "Self"
    for dict in all_dicts:
        try:
            return dict[name]
        except:
            pass
    return "any"

def find_returned_variables_and_types(func):
    returned_variables = {}

    # Define a visitor class to traverse the AST
    class VariableVisitor(ast.NodeVisitor):
        def __init__(self):
            self.current_scope = {}
            self.visited_nodes = []

        def visit_Assign(self, node):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.current_scope[target.id] = node.value
            self.generic_visit(node)

        def visit_Return(self, node):
            if node.value and isinstance(node.value, ast.Name):
                variable_name = node.value.id
                if variable_name in self.current_scope:
                    returned_variables[variable_name] = ast.dump(self.current_scope[variable_name]).split("(")[0].lower()
            elif node.value and isinstance(node.value, ast.Str):
                returned_variables["str"] = "str"
            elif node.value and isinstance(node.value, ast.List):
                returned_variables["list"] = "list"
            elif node.value and isinstance(node.value, ast.Dict):
                returned_variables["dict"] = "dict"
            elif node.value and isinstance(node.value, ast.Set):
                returned_variables["set"] = "set"
            elif node.value and isinstance(node.value, ast.Constant):
                if node.value.value in [True, False]:
                    returned_variables["bool"] = "bool"
                else:
                    returned_variables["int"] = "int"
            self.generic_visit(node)

    # Create an instance of the visitor and visit the AST
    visitor = VariableVisitor()
    visitor.visit(func)
    return returned_variables

def add_type_hints(file_path):
    with open(file_path, 'r', encoding="utf-8", errors="ignore") as file:
        code = file.read()

    try:tree = ast.parse(code)
    except SyntaxError:
        print(file_path)
        print("Syntax Error exists in file, skipping...")
        return
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for arg in node.args.args:
                if arg.annotation is None:
                    arg_type_hint = find_type(ast.unparse(arg))
                    arg_type_hint_node = ast.Name(id=arg_type_hint, ctx=ast.Load())
                    arg.annotation = arg_type_hint_node
            # get the return types here
            if node.returns is None:
                rnodes = find_returned_variables_and_types(node)
                willreturn = []
                if rnodes == {}:
                    node.returns = " None"
                else:
                    return_string = ""
                    for x in rnodes.values():
                        if x not in willreturn:
                            willreturn.append(x)
                            return_string+=x+"|"
                    node.returns = " "+return_string[:-1]

    
    try:modified_code = ast.unparse(tree)
    except AttributeError:
        print(file_path)
        print("unable to un parse tree, skipping")
        return
    file = os.path.basename(file_path)
    example_dir = os.getcwd() + os.sep + "examples"
    example = example_dir + os.sep + file
    with open(example, "wb") as f:
        global selfflag
        if selfflag is True:
            f.write("from typing import Self\n".encode())
        f.write(modified_code.encode())


def cli():
    
    print("type hint writer")
    args = sys.argv[1:]
        
    if args == []:
        print("usage: python add_type_hints.py <input file>")
        exit()
    for arg in args:
        add_type_hints(arg)


if __name__ == "__main__":
    cli()

