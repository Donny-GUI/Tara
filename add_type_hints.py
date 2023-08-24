import ast
import astor
import pickle
import sys 
import os




with open('boolean_variables.pkl', 'rb') as file:
    boolean_dict = pickle.load(file)
with open('bytes_variables.pkl', 'rb') as file:
    bytes_dict = pickle.load(file)
with open('dict_variables.pkl', 'rb') as file:
    dict_dict = pickle.load(file)
with open('int_variables.pkl', 'rb') as file:
    int_dict = pickle.load(file)
with open('list_variables.pkl', 'rb') as file:
    list_dict = pickle.load(file)
with open('string_variables.pkl', 'rb') as file:
    string_dict = pickle.load(file)

all_dicts = [string_dict, int_dict, boolean_dict, list_dict, dict_dict, bytes_dict]

def find_type(name: str):
    if name == "self":
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
                returned_variables[variable_name] = "str"
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

def get_return_nodes_and_types(func):
    return_nodes = []

    # Define a visitor class to traverse the AST
    class ReturnVisitor(ast.NodeVisitor):
        def visit_Return(self, node):
            return_nodes.append(node)

    # Create an instance of the visitor and visit the AST
    visitor = ReturnVisitor()
    visitor.visit(func)

    # Get the types of what each return node returns
    return_types = []
    for return_node in return_nodes:
        if return_node.value:
            return_type = ast.dump(return_node.value)
        else:
            return_type = "NoneType"
        return_types.append(return_type)

    return return_nodes, return_types

def add_type_hints(file_path):
    with open(file_path, 'r', encoding="utf-8", errors="ignore") as file:
        code = file.read()

    tree = ast.parse(code)
    
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

    
    modified_code = astor.to_source(tree)
    print(modified_code)
    file = os.path.basename(file_path)
    file = os.path.dirname(file_path) + "\\typed_" + file
    with open(file, "w") as f:
        f.write(modified_code)

if __name__ == "__main__":
    print("type hint writer")
    args = sys.argv[1:]
        
    if args == []:
        print("usage: python add_type_hints.py <input file>")
        exit()
    for arg in args:
        add_type_hints(arg)


