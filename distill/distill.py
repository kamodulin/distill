import argparse
import os
import re

from .utils import *


def get_files(path: str) -> list:
    """
    Walk through a directory and return a list of python files.
    """
    py_files = []

    for root, dirs, files in walk(path):
        for name in files:
            py_files.append(os.path.join(root, name))

    return py_files


def parse_file(content: str) -> list:
    """
    Parse a python file and extract import statements.
    """
    return re.findall(r"^(?:from|import)[\s*](\w*)\b", content, flags=re.MULTILINE)


def extract_all_imports(files: list) -> list:
    """
    Extract all import statements from a list of files and exclude local imports.
    """
    imports = []

    for f in files:
        with open(f) as data:
            try:
                content = data.read()
                modules = [m for m in parse_file(content) if m not in files] # move this out to a filter fn
                imports.append(modules)
            except:
                pass            
    
    return unique(flatten(imports))


def main():
    parser = argparse.ArgumentParser(description="Utility to extract necessary imports from a project.")
    parser.add_argument("-d", "--dir", action="store", default=os.getcwd(), help="Directory to perform distillation.")
    args = parser.parse_args()

    files = get_files(args.dir)
    raw_imports = extract_all_imports(files)
    nonlocal_imports = remove_local_modules(raw_imports, args.dir)
    imports = remove_std_modules(nonlocal_imports)

    if imports:
        print("Necessary imports:")

        for i in imports:
            print(i)

    else:
        print("No imports found!")