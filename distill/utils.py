import os


def walk(path: str):
    """Yields a modified os.walk function which ignores hidden elements and
    captures .py files.
    """
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not d[0] == "."]
        files = [f for f in files if not f[0] == "." and f.endswith(".py")]

        yield root, dirs, files


def get_files(path: str) -> list:
    """Walks through a directory and return a list of python files."""
    file_names = []

    for root, _, files in walk(path):
        for name in files:
            file_names.append(os.path.join(root, name))

    return file_names


def local_modules(path: str) -> set:
    """Return a set of local files and modules in project directory."""
    locallib = set()

    for _, dirs, files in walk(path):
        for d in dirs:
            locallib.add(d)
        for f in files:
            locallib.add(os.path.splitext(f)[0])

    return locallib


def stdlib_modules() -> set:
    """Returns a set of standard library modules."""
    stdlib = set()

    with open("stdlib", "rb") as f:
        for module in f:
            stdlib.add(module.rstrip())

    return stdlib


def write(path: str, modules: set) -> None:
    """Writes a distill.txt file with module names."""
    with open(path, "w") as f:
        f.write("# *WARNING* Module names may not match package names")
        for module in modules:
            f.write("\n" + module)
