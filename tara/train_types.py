import os
import pickle
import ast
import re 
from tqdm import tqdm


def determine_variable_type(value:str):
    try:
        firstchar = value[0]
    except IndexError:
        return "?"
    try:
        if value.startswith("input("):
            return "str"
        var_type = type(eval(value))
        return str(var_type)[8:-2]
    except:
        pass
    if value in ["False", "True"]:
        return "bool"
    if firstchar in "123456789":
        return "int"
    elif firstchar in ['"', "'"]:
        return "str"
    elif firstchar == "[":
        return "list"
    elif firstchar == "{":
        return "dict"
    elif value.startswith("0x") or value.startswith("bytes(") or value.startswith("b'"):
        return "bytes"
    elif value.startswith("f'") or value.startswith('f"') or value.startswith("str("):
        return "str"
    elif value.startswith("int("):
        return "int"
    elif value.startswith("bytearray("):
        return "bytearray"
    elif value.startswith("set("):
        return "set"
    elif value.startswith("(") and "*+-/" not in value:
        return "tuple"

def find_string_variables_in_python_files():
    original_files = [x for x in os.listdir() if os.path.isfile(x)]
    string_variables = {}
    int_variables = {}
    float_variables = {}
    list_variables = {}
    tuple_variables = {}
    set_variables = {}
    complex_variables = {}
    any_variables = {}
    dict_variables = {}
    bytes_variables = {}
    boolean_variables = {}

    variables_processed = 0

    def visit_file(file_path: str):
        """ visit a python source file, find all the assignment nodes, and determine the type of 
        variables they are, and assign them to the type dict.
        """
        nonlocal variables_processed
        with open(file_path, 'r', encoding="utf-8", errors="ignore") as f:
            content = f.read()
            try:
                parsed_ast = ast.parse(content)
            except:
                print("ast parse failed")
                return
            
            has_determined = []
            for node in ast.walk(parsed_ast):
                
                if isinstance(node, ast.Assign):

                    source = ast.unparse(node)
                    objects = [x.strip() for x in source.split("=")]

                    if len(objects) > 1:
                        name = objects[0]
                        value = objects[1]

                        if name not in has_determined:
                            vartype = determine_variable_type(value)

                            if vartype is not None and vartype != "?":
                                
                                if vartype == "NoneType":
                                    continue
                                
                                match vartype:
                                    case "int":
                                        int_variables[name] = "int"
                                    case "str":
                                        string_variables[name] = "str"
                                    case "list":
                                        list_variables[name] = "list"
                                    case "dict":
                                        dict_variables[name] = "dict"
                                    case "set":
                                        set_variables[name] = "set"
                                    case "bytes":
                                        bytes_variables[name] = "bytes"
                                    case "bytesarray":
                                        bytes_variables[name] = "bytesarray"
                                    case "bool":
                                        boolean_variables[name] = "bool"
                                    case "tuple":
                                        tuple_variables[name] = "tuple"
                                    case "complex":
                                        complex_variables[name] = "complex"
                                variables_processed+=1
                                has_determined.append(name)

    filetargets = []    
    for root, _, files in os.walk("C:\\Program Files\\Python311\\"):
        
        for file_name in files:
            
            if file_name.endswith('.py'):
                # Skip tests
                if root.endswith("tests"):
                    continue

                file_path = os.path.join(root, file_name)
                filetargets.append(file_path)
    
    with tqdm(iterable=filetargets, total=len(filetargets), desc="Processing...", unit="file") as pbar:
        
        for index, ft in enumerate(filetargets):
            pbar.refresh()
            visit_file(ft)
            pbar.update(1)


    # Pickle the list of string variable names
    all_vars = [string_variables, int_variables, dict_variables, list_variables, float_variables, boolean_variables, bytes_variables]
    all_var_names = ["string_variables", "int_variables", "dict_variables", "list_variables", "float_variables", "boolean_variables", "bytes_variables"]
    for index, vs in enumerate(all_vars):
        name = os.getcwd() + os.sep + "data" + os.sep + all_var_names[index] + ".pkl"
        try:
            with open(name, 'rb') as f:
                data = pickle.load(f)
                for n, d in data.items():
                    vs[n] = d
        except:
            pass
        with open(name, 'wb') as f:
            pickle.dump(vs, f)
    print("variables processed successfully: ", variables_processed)

    new_files = [x for x in os.listdir() if x not in original_files and os.path.isfile(x)]
    for newfile in new_files:
        if newfile.endswith('.py') or newfile.endswith('.exe'):
            continue
        os.remove(newfile)


def add_type_hints_and_return(func_str):
    """
    Add type hints to function arguments and return value if missing.

    Parameters:
        func_str (str): The string containing the function code.

    Returns:
        str: The modified function code with added type hints.
    """
    # Pattern to match a function definition
    func_pattern = r"def\s+(\w+)\s*\((.*?)\):"

    # Pattern to match a return statement
    return_pattern = r"return\s+(.*?)$"

    # Find function definitions
    for match in re.finditer(func_pattern, func_str, re.MULTILINE):
        func_name = match.group(1)
        args = match.group(2)

        # Check if type hints are missing
        if ":" not in args:
            # Split arguments and add type hints
            args_list = args.split(",")
            args_with_hints = [f"{arg.strip()}: Any" for arg in args_list]

            # Add type hints to function definition
            args_str_with_hints = ", ".join(args_with_hints)
            func_str = func_str.replace(match.group(0), f"def {func_name}({args_str_with_hints}):", 1)

        # Check if return hint is missing
        if " -> " not in func_str:
            # Find return statement
            return_match = re.search(return_pattern, func_str, re.MULTILINE)
            if return_match:
                return_value = return_match.group(1)
                return_hint = f" -> Any"
                func_str = func_str.replace(return_match.group(0), f"\n    {return_match.group(0)}\n    {return_hint}", 1)

    return func_str

def train_model():
    find_string_variables_in_python_files()