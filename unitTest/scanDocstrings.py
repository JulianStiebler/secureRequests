import os
import ast

class DocstringChecker(ast.NodeVisitor):
    def __init__(self):
        self.total_functions = 0
        self.functions_without_docstrings = 0
        self.missing_docstrings = []

    def visit_FunctionDef(self, node):
        self.total_functions += 1
        if not ast.get_docstring(node):
            self.functions_without_docstrings += 1
            self.missing_docstrings.append(f"{node.name} in {self.current_file} at line {node.lineno}")
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.visit_FunctionDef(node)

    def check_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read(), filename=file_path)
            self.current_file = file_path
            self.visit(tree)

def get_python_files(base_dir):
    python_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py") and not file.endswith(".pyi"):
                python_files.append(os.path.join(root, file))
    return python_files

def main():
    base_directory = "../secureRequests"
    checker = DocstringChecker()
    python_files = get_python_files(base_directory)
    
    for python_file in python_files:
        checker.check_file(python_file)
    
    total_functions = checker.total_functions
    functions_without_docstrings = checker.functions_without_docstrings
    docstring_coverage = ((total_functions - functions_without_docstrings) / total_functions) * 100 if total_functions > 0 else 0
    
    print(f"Total functions: {total_functions}")
    print(f"Total functions without docstrings: {functions_without_docstrings}")
    print(f"Docstring coverage: {docstring_coverage:.2f}%")
    
    if functions_without_docstrings > 0:
        print("\nFunctions without docstrings:")
        for func in checker.missing_docstrings:
            print(func)

if __name__ == "__main__":
    main()
