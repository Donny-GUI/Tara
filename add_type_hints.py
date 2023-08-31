import ast
import sys 
import os
from util import BoolMap, StringMap, DictMap, ListMap, IntMap, BytesMap


selfflag = False
all_dicts = [StringMap, IntMap, BoolMap, ListMap, DictMap, BytesMap]


def make_type_representation(type:str):
    if type == "call":
        type = "any"
    return ast.Name(id=type, ctx=ast.Load())

def find_type(name):
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

def has_return_statement(node):
    for subnode in ast.walk(node):
        if isinstance(subnode, ast.Return):
            return True
    return False

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

def backup_generate(tree):
    strings = []
    for x in ast.walk(tree):
        try:
            string = ast.unparse(x)
        except:
            for subx in ast.walk(x):
                string = ast.unparse(subx)
                strings.append(string)
        strings.append(string)
    return "\n".join(strings)
            
def string_to_return_value(value):
    """ 
        example: Union[bool, str]
    """
    return ast.parse(value).body[0].value

def list_to_return_value(list):
    return ast.parse("|".join(list)).body[0].value

def add_type_hints(file_path):
    # open the file and get the content
    with open(file_path, 'r', encoding="utf-8", errors="ignore") as file:
        code = file.read()

    # attempt to parse the file
    try:tree = ast.parse(code)
    except SyntaxError:
        print(file_path)
        print("Syntax Error exists in file, skipping...")
        return
    
    # walk the nodes recursively looking for function definitions
    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            # FOUND Function definition

            # Fix the type hints for the params
            for arg in node.args.args:
                if arg.annotation is None:
                    arg_type_hint = find_type(ast.unparse(arg))
                    arg_type_hint_node = ast.Name(id=arg_type_hint, ctx=ast.Load())
                    arg.annotation = arg_type_hint_node
            
            # get the return types here
            if node.returns is None and has_return_statement(node) == True:

                rnodes = find_returned_variables_and_types(node)
                willreturn = []
                if rnodes == {}:
                    node.returns = string_to_return_value("None")
                else:
                    for x in rnodes.values():
                        if x not in willreturn:
                            willreturn.append(x)
                    
                    if len(willreturn) == 1:
                        node.returns = string_to_return_value(willreturn[0])
                    else:
                        node.returns = list_to_return_value(willreturn)
    
    try:modified_code = ast.unparse(tree)
    except AttributeError:
        print(file_path)
        print("unable to un parse tree, skipping")
        print("attempting backup generator...")
        modified_code = backup_generate(tree)
        
    file = os.path.basename(file_path)
    example_dir = os.getcwd() + os.sep + "output"
    example = example_dir + os.sep + file
    os.makedirs(example_dir, exist_ok=True)
    with open(example, "wb") as f:
        global selfflag
        if selfflag is True:
            f.write("from typing import Self\n".encode())
        f.write(modified_code.encode())

def cli():
    args = sys.argv[1:]
    if args == []:
        print("\nType And Return Automate   - Tara\n")
        print("  usage: \n    python add_type_hints.py <input file>")
        exit()
    for arg in args:
        add_type_hints(arg)


if __name__ == "__main__":
    cli()
