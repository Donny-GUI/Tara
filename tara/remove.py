import ast


def remove_type_hints(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    tree = ast.parse(code)

    # Helper function to remove type hints from annotations
    def remove_annotations(node):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # node.returns = None  # Remove return type hint for functions
            for arg in node.args.args:
                arg.annotation = None  # Remove type hints for function arguments

    # Visit all nodes in the abstract syntax tree and remove type hints
    class TypeHintRemover(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            remove_annotations(node)
            self.generic_visit(node)
            return node

        def visit_AsyncFunctionDef(self, node):
            remove_annotations(node)
            self.generic_visit(node)
            return node

        #def visit_AnnAssign(self, node):
        #    node.annotation = None  # Remove type hints for variable assignments
        #    self.generic_visit(node)
        #    return node

    transformer = TypeHintRemover()
    modified_tree = transformer.visit(tree)

    # Generate modified code from the modified tree
    modified_code = ast.unparse(modified_tree)

    return modified_code

def remove_returns(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    tree = ast.parse(code)

    # Helper function to remove type hints from annotations
    def remove_annotations(node):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            node.returns = None  # Remove return type hint for functions
            #for arg in node.args.args:
            #    arg.annotation = None  # Remove type hints for function arguments

    # Visit all nodes in the abstract syntax tree and remove type hints
    class TypeHintRemover(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            remove_annotations(node)
            self.generic_visit(node)
            return node

        def visit_AsyncFunctionDef(self, node):
            remove_annotations(node)
            self.generic_visit(node)
            return node

        def visit_AnnAssign(self, node):
            node.annotation = None  # Remove type hints for variable assignments
            self.generic_visit(node)
            return node

    transformer = TypeHintRemover()
    modified_tree = transformer.visit(tree)

    # Generate modified code from the modified tree
    modified_code = ast.unparse(modified_tree)

    return modified_code


def remove_type_hints_and_returns(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    tree = ast.parse(code)

    # Helper function to remove type hints from annotations
    def remove_annotations(node):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            node.returns = None  # Remove return type hint for functions
            for arg in node.args.args:
                arg.annotation = None  # Remove type hints for function arguments

    # Visit all nodes in the abstract syntax tree and remove type hints
    class TypeHintRemover(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            remove_annotations(node)
            self.generic_visit(node)
            return node

        def visit_AsyncFunctionDef(self, node):
            remove_annotations(node)
            self.generic_visit(node)
            return node

        def visit_AnnAssign(self, node):
            node.annotation = None  # Remove type hints for variable assignments
            self.generic_visit(node)
            return node

    transformer = TypeHintRemover()
    modified_tree = transformer.visit(tree)

    # Generate modified code from the modified tree
    modified_code = ast.unparse(modified_tree)

    return modified_code

