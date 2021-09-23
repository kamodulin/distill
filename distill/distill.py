import argparse
import ast
import logging
import os

from utils import *


def extract_all_imports(files: list) -> set:
    """Extracts all import statements from a list of files."""
    imports = set()

    for f in files:
        with open(f) as data:
            try:
                content = data.read()
                tree = ast.parse(content)

                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for sub in node.names:
                            imports.add(sub.name)

                    elif isinstance(node, ast.ImportFrom):
                        imports.add(node.module)

            except Exception as e:
                raise e

    imports = set(i.split(".")[0] for i in imports if i)

    return imports


def main():
    parser = argparse.ArgumentParser(
        description="Utility to extract necessary imports from a project.")

    parser.add_argument(
        "-d",
        "--dir",
        action="store",
        default=os.getcwd(),
        help="Directory to perform distillation.")

    parser.add_argument(
        "-s",
        "--save",
        action="store",
        help="Save distilled requirements to file.")

    args = parser.parse_args()

    logging.basicConfig(format='%(message)s', level=logging.INFO)

    if not os.path.isdir(args.dir):
        logging.error("Invalid directory.")
        return

    files = get_files(args.dir)

    raw_imports = extract_all_imports(files)
    local = local_modules(args.dir)
    stdlib = stdlib_modules()
    imports = sorted(raw_imports - local - stdlib)

    if not imports:
        logging.info("No imports found!")

    else:
        logging.info(f"Imports: {imports}")

        save_file = args.save if args.save else args.dir + "/distill.txt"
        logging.info(f"Writing distilled requirements to {save_file}")
        write(save_file, imports)