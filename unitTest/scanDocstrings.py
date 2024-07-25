import os
import ast

class DocstringChecker(ast.NodeVisitor):
    """
    A class to check for missing docstrings in Python functions.

    Attributes:
        total_functions (int): The total number of functions found.
        functions_without_docstrings (int): The number of functions without docstrings.
        missing_docstrings (list): A list of functions that are missing docstrings.
    """
    
    def __init__(self):
        """
        Initializes the DocstringChecker with default values.
        """
        self.total = 0
        self.withoutDoc = 0
        self.missingDoc = []

    def visit_FunctionDef(self, node):
        """
        Visits each function definition in the AST.

        Args:
            node (ast.FunctionDef): The current function definition node.
        """
        self.total += 1
        if not ast.get_docstring(node):
            self.withoutDoc += 1
            self.missingDoc.append(f"{node.name} in {self.currentFile} at line {node.lineno}")
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        """
        Visits each async function definition in the AST.

        Args:
            node (ast.AsyncFunctionDef): The current async function definition node.
        """
        self.visit_FunctionDef(node)

    def check_file(self, filePath):
        """
        Parses a Python file and visits its AST nodes.

        Args:
            file_path (str): The path to the Python file to check.
        """
        with open(filePath, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read(), filename=filePath)
            self.currentFile = filePath
            self.visit(tree)

def get_python_files(baseDir):
    """
    Recursively gets all Python files in the given directory.

    Args:
        base_dir (str): The base directory to start the search.

    Returns:
        list: A list of paths to Python files.
    """
    pyFiles = []
    for root, _, files in os.walk(baseDir):
        for file in files:
            if file.endswith(".py") and not file.endswith(".pyi"):
                pyFiles.append(os.path.join(root, file))
    return pyFiles

def main():
    """
    The main function to run the docstring checker on all Python files
    in the specified base directory.
    """
    baseDir = "../"
    checker = DocstringChecker()
    pyFiles = get_python_files(baseDir)
    
    for python_file in pyFiles:
        checker.check_file(python_file)
    
    total = checker.total
    withoutDoc = checker.withoutDoc
    docCoverage = ((total - withoutDoc) / total) * 100 if total > 0 else 0
    
    print(f"Total functions: {total}")
    print(f"Total functions without docstrings: {withoutDoc}")
    print(f"Docstring coverage: {docCoverage:.2f}%")
    
    if withoutDoc > 0:
        print("\nFunctions without docstrings:")
        for func in checker.missingDoc:
            print(func)

if __name__ == "__main__":
    main()
