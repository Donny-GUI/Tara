import ast
import os
from tara.util import BoolMap, StringMap, DictMap, ListMap, IntMap, BytesMap


# Global Flags

selfflag = False

# Global Collections

all_dicts = [StringMap, IntMap, BoolMap, ListMap, DictMap, BytesMap]


def make_type_representation(type:str) -> ast.Name:
    """
    Create a type representation for a given type
    NOTE:
        This ensures that the ast.Module can 
        be reparsed/unparsed into readable python

    Returns:
        ast.Name: the ast representation of the type to return. 
    """
    if type == "call":
        type = "any"
    return ast.Name(id=type, ctx=ast.Load())

def find_type(name: str) -> str:
    """ 
    takes a parameter name and returns a type
    """
    if name == "self":
        global selfflag
        selfflag = True   
        return "Self"
    
    global all_dicts
    for dict in all_dicts:
        try:
            return dict[name]
        except:
            pass
    
    return "any"

def has_return_statement(node: ast.AST) -> bool:
    """
    determines if a function returns an object or None.

    Parameters:
      node (ast.AST): any ast.AST but it helps if it is a function definition.
    
    Returns: bool -> True if the function returns an object that isnt None
    """
    for subnode in ast.walk(node):
        if isinstance(subnode, ast.Return):
            return True
    return False

def find_returned_variables_and_types(func: ast.AST) -> dict:
    returned_variables = {}

    # Define a visitor class to traverse the AST
    class VariableVisitor(ast.NodeVisitor):

        def __init__(self) -> None:
            self.current_scope = {}
            self.visited_nodes = []

        def visit_Assign(self, node: ast.Assign) -> None:

            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.current_scope[target.id] = node.value
            self.generic_visit(node)

        def visit_Return(self, node: ast.Return):
            
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

def backup_generate(tree: ast.AST) -> str:
    """
    Returns a rewritten version of the file IF the file CANNOT be generated from the ast tree
    """
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

def string_to_return_value(value: str):
    """ 
        example: Union[bool, str]
    """
    return ast.parse(value).body[0].value

def list_to_return_value(list: list) -> str:
    return ast.parse("|".join(list)).body[0].value

def create_modified_code(tree, file_path) -> str:
    try:
        modified_code = ast.unparse(tree)
    except AttributeError:
        print(file_path)
        print("unable to un parse tree, skipping")
        print("attempting backup generator...")
        modified_code = backup_generate(tree)
    finally:
        return modified_code 

def ensure_save_directory(file_path:str):
    """ UNUSED """
    file = os.path.basename(file_path)
    example_dir = os.getcwd() + os.sep + "output"
    os.makedirs(example_dir, exist_ok=True)
    return example_dir + os.sep + file


def add_type_hints(file_path:str) -> None:
    """
    Add type hints to a python file
    """
    
    # open the file and get the content
    try:
        with open(file_path, 'r', encoding="utf-8", errors="ignore") as file:
            code = file.read()
    except FileNotFoundError as fnfe:
        print("Could not open and read file: %s" % file_path)
        exit()

    # attempt to parse the file
    try:
        tree = ast.parse(code)
    except SyntaxError:
        print(file_path)
        print("Syntax Error exists in file, skipping...")
        return
    
    # walk the nodes recursively looking for function definitions
    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            # FOUND Function definition &&
            # Fix the type hints for the params
            for arg in node.args.args:
                
                # If no annonation exists we will have to create them
                if arg.annotation is None:
                    arg_type_hint = find_type(ast.unparse(arg))
                    arg_type_hint_node = ast.Name(id=arg_type_hint, ctx=ast.Load())
                    arg.annotation = arg_type_hint_node
            
            # " if the ast node does not have a return type and the function that determines if there is a return type, fix the return type "
            if node.returns is None and has_return_statement(node) == True:

                rnodes = find_returned_variables_and_types(node)
                
                willreturn = []
                
                if rnodes == {}:
                    node.returns = string_to_return_value("None")
                else:
                    for x in rnodes.values():
                        if x not in willreturn:
                            willreturn.append(x)
                    
                    # count the number of returned items (which is a set to a list). If greater than one, use the list to return function, else use the string version. 
                    if len(willreturn) == 1:
                        node.returns = string_to_return_value(willreturn[0])
                    else:
                        node.returns = list_to_return_value(willreturn)
    
    modified_code = create_modified_code(tree, file_path)
    
    # ensure_save_directory would go here
    file = os.path.basename(file_path)
    example_dir = os.getcwd() + os.sep + "output"
    example = example_dir + os.sep + file
    os.makedirs(example_dir, exist_ok=True)

    with open(example, "wb") as f:

        # ask if selfflag exists in order to write the typing import
        global selfflag
        if selfflag is True:
            f.write("from typing import Self\n".encode())
        f.write(modified_code.encode())

def new_file_with_type_hints(file_path:str, output_file_path:str) -> None:
    # open the file and get the content
    with open(file_path, 'r', encoding="utf-8", errors="ignore") as file:
        code = file.read()

    # attempt to parse the file
    try:tree = ast.parse(code)
    except SyntaxError:
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
        print("attribute error")
        modified_code = backup_generate(tree)

    with open(output_file_path, "wb") as f:
        global selfflag
        if selfflag is True:
            f.write("from typing import Self\n".encode())
        f.write(modified_code.encode())
