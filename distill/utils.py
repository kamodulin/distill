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
    modules = set()

    for _, dirs, files in walk(path):
        for d in dirs:
            modules.add(d)
        for f in files:
            modules.add(os.path.splitext(f)[0])

    return modules


def stdlib_modules() -> set:
    """Returns a set of standard library modules."""
    modules = set()
    
    stdlib = os.path.join(os.path.dirname(__file__), "stdlib")

    with open(stdlib, "r") as f:
        for module in f:
            modules.add(module.rstrip())

    return modules


def write(path: str, modules: set) -> None:
    """Writes a distill.txt file with module names."""
    with open(path, "w") as f:
        for module in modules:
            f.write(module + "\n")
