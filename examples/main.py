from typing import Self
import os
import ast
from typing import Set, Dict, List

def source_to_string(filename: str):
    """
    Read and return the content of a file.

    Args:
        filename (str): The path to the file to read.

    Returns:
        str: The content of the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except (FileNotFoundError, FileExistsError) as e:
        print(e)
        exit(1)
    return content

def python_to_tree(string: str) -> ast.Module:
    """
    Parse Python source code into an AST module.

    Args:
        string (str): The Python source code.

    Returns:
        ast.Module: The parsed AST module.
    """
    return ast.parse(string)

def python_to_nodes(string: str) -> List[ast.AST]:
    """
    Extract a list of AST nodes from Python source code.

    Args:
        string (str): The Python source code.

    Returns:
        List[ast.AST]: A list of AST nodes extracted from the code.
    """
    return [x for x in ast.walk(python_to_tree(string))]

def infer_variable_type(node: ast.AST):
    """
    Infer the data type of an AST node representing a Python expression.

    This function examines the given AST node and attempts to infer its data type.
    It covers simple built-in data types like integers, floats, strings, and various
    container types like lists, tuples, dictionaries, and sets. If the type cannot
    be inferred, the function returns "unknown".

    Args:
        node (ast.AST): The AST node representing a Python expression.

    Returns:
        str: A string indicating the inferred data type, or "unknown" if not determinable.
    """
    if isinstance(node, ast.Num):
        return 'int' if isinstance(node.n, int) else 'float'
    elif isinstance(node, ast.Str):
        return 'str'
    elif isinstance(node, ast.NameConstant):
        return str(node.value)
    elif isinstance(node, ast.List):
        return 'list'
    elif isinstance(node, ast.Tuple):
        return 'tuple'
    elif isinstance(node, ast.Dict):
        return 'dict'
    elif isinstance(node, ast.Set):
        return 'set'
    else:
        return 'unknown'

def extract_variable_types(node: ast.AST) -> Dict[str, str]:
    """
    Extract and infer variable types from an AST node.

    This function analyzes the given AST node and attempts to extract and infer the types
    of variables defined within it. It specifically targets variable assignments inside
    a function definition's body and infers their types using the `infer_variable_type`
    function. The extracted variable names and their inferred types are returned as a
    dictionary.

    Args:
        node (ast.AST): The AST node representing a Python code block.

    Returns:
        Dict[str, str]: A dictionary mapping variable names to their inferred types.
    """
    variable_types = {}
    if isinstance(node, ast.FunctionDef):
        for stmt in node.body:
            if isinstance(stmt, ast.Assign):
                for target in stmt.targets:
                    if isinstance(target, ast.Name):
                        variable_name = target.id
                        if variable_name not in variable_types:
                            variable_types[variable_name] = infer_variable_type(stmt.value)
    return variable_types

def get_function_variable_types(func_ast: ast.FunctionDef) -> Dict[str, str]:
    """
    Get inferred variable types within a function definition.

    This function takes an AST node representing a function definition and uses the
    `extract_variable_types` function to extract and infer the types of variables
    defined within the function's body. The function definition AST is expected as
    the input parameter, and the extracted variable names and their inferred types
    are returned as a dictionary.

    Args:
        func_ast (ast.FunctionDef): The AST node representing the function definition.

    Returns:
        Dict[str, str]: A dictionary mapping variable names to their inferred types.
    Raises:
        ValueError: If the input is not a function definition AST node.
    """
    if not isinstance(func_ast, ast.FunctionDef):
        raise ValueError('Input should be a function definition AST node.')
    return extract_variable_types(func_ast)

def extract_variables(node: ast.AST) -> set[str]:
    """
    Recursively extract variable names from an AST node.

    Args:
        node (ast.AST): The AST node to analyze.

    Returns:
        Set[str]: A set of variable names used within the given AST node.
    """
    variables = set()
    if isinstance(node, ast.Name):
        variables.add(node.id)
    elif isinstance(node, ast.Attribute):
        variables.add(node.attr)
    elif isinstance(node, ast.Subscript):
        variables |= extract_variables(node.value)
    elif isinstance(node, ast.Call):
        for arg in node.args:
            variables |= extract_variables(arg)
        for keyword in node.keywords:
            variables |= extract_variables(keyword.value)
    elif isinstance(node, ast.BinOp):
        variables |= extract_variables(node.left)
        variables |= extract_variables(node.right)
    elif isinstance(node, ast.UnaryOp):
        variables |= extract_variables(node.operand)
    elif isinstance(node, ast.BoolOp):
        for value in node.values:
            variables |= extract_variables(value)
    elif isinstance(node, ast.Compare):
        variables |= extract_variables(node.left)
        for comparator in node.comparators:
            variables |= extract_variables(comparator)
    elif isinstance(node, ast.Assign):
        for target in node.targets:
            variables |= extract_variables(target)
    elif isinstance(node, ast.For):
        variables |= extract_variables(node.target)
        variables |= extract_variables(node.iter)
    elif isinstance(node, ast.With):
        for item in node.items:
            variables |= extract_variables(item.context_expr)
    elif isinstance(node, ast.If):
        variables |= extract_variables(node.test)
    elif isinstance(node, ast.Return):
        if node.value:
            variables |= extract_variables(node.value)
    elif isinstance(node, ast.Expr):
        variables |= extract_variables(node.value)
    elif isinstance(node, ast.Raise):
        if node.exc:
            variables |= extract_variables(node.exc)
        if node.cause:
            variables |= extract_variables(node.cause)
    for child_node in ast.iter_child_nodes(node):
        variables |= extract_variables(child_node)
    return variables

def get_function_variables(func_ast: any):
    """
    Extract variable names used within a function's AST.

    Args:
        func_ast (ast.FunctionDef): The AST node representing the function.

    Returns:
        Set[str]: A set of variable names used within the function's AST.
    Raises:
        ValueError: If the input is not a function definition AST node.
    """
    if not isinstance(func_ast, ast.FunctionDef):
        raise ValueError('Input should be a function definition AST node.')
    return extract_variables(func_ast)

def convert_variable_to_nim(name: str, var_type: str):
    nim_type = ''
    if var_type == 'int':
        nim_type = 'int'
    elif var_type == 'float':
        nim_type = 'float'
    elif var_type == 'str':
        nim_type = 'string'
    elif var_type == 'list':
        nim_type = 'seq'
    elif var_type == 'tuple':
        nim_type = 'tuple'
    elif var_type == 'dict':
        nim_type = 'Table'
    elif var_type == 'set':
        nim_type = 'set'
    else:
        nim_type = 'auto'
    return f'var {name}: {nim_type}'

def convert_assignments_to_nim(func_ast: ast.FunctionDef):
    nim_code = ''
    for stmt in func_ast.body:
        if isinstance(stmt, ast.Assign):
            for target in stmt.targets:
                if isinstance(target, ast.Name):
                    variable_name = target.id
                    variable_type = infer_variable_type(stmt.value)
                    nim_equivalent = convert_variable_to_nim(snake_to_camel_case(variable_name), variable_type)
                    nim_code += nim_equivalent + '\n'
    return nim_code

def read_python_file_to_ast_nodes(filename: str) -> list[ast.AST]:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    try:
        tree = ast.parse(content)
        return ast.walk(tree)
    except SyntaxError as e:
        print(f'Syntax error in {filename}: {e}')
        return []

def snake_to_camel_case(snake_str: str):
    parts = snake_str.split('_')
    return parts[0] + ''.join((part.title() for part in parts[1:]))

def convert_function_def_to_nim(func_ast: ast.FunctionDef):
    func_name = snake_to_camel_case(func_ast.name)
    nim_args = []
    for arg in func_ast.args.args:
        arg_name = arg.arg
        arg_type = infer_variable_type(arg)
        if arg_type == 'unknown':
            arg_type = 'auto'
        nim_args.append(arg_name + ': ' + arg_type)
    return_type = ''
    if func_ast.returns:
        return_type = ': ' + infer_variable_type(func_ast.returns)
    if return_type == ': unknown':
        return_type = ': auto'
    nim_returns = return_type
    nim_args_str = ', '.join(nim_args)
    nim_definition = f'proc {func_name}({nim_args_str}){nim_returns} ='
    return nim_definition

class NimFunctionDefinition:

    def __init__(self: Self, node: ast.FunctionDef) -> None:
        self.node = node
        self.name = snake_to_camel_case(self.node.name)
        self.assignments = convert_assignments_to_nim(self.node)

    def setNode(self: Self, node: ast.FunctionDef):
        self.node = node

def convert_python_function_definition(node: ast.FunctionDef):
    header = convert_function_def_to_nim(node)
    print(header)
    assigns = convert_assignments_to_nim(node)
    for ass in assigns.split('\n'):
        print('  ', ass)

def main():
    filename = 'main.py'
    nodes = read_python_file_to_ast_nodes(filename)
    for node in nodes:
        if isinstance(node, ast.FunctionDef):
            convert_python_function_definition(node)
main()