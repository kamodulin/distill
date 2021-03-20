import pkgutil
import sys
import os

from itertools import chain


def flatten(array: list) -> list:
    """
    Return a flattened array from a list of lists.
    """
    return chain(*array)


def unique(array: list) -> list:
    """
    Return an array where each element appears only once.
    """
    return list(set(array))


def diff(array_A: list, array_B: list) -> list:
    """
    Return the difference between arrays A and B (A-B).
    """
    return list(set(array_A) - set(array_B))


def walk(path: str):
    """
    Yields a modified os.walk function which ignores hidden 
    elements and captures .py files.
    """
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not d[0] == "."]
        files = [f for f in files if not f[0] == "." and f.endswith(".py")]
        
        yield root, dirs[:], files


def remove_local_modules(modules: list, path: list) -> list:
    """
    Remove local modules from a list of modules.
    """
    locallib = []

    for root, dirs, files in walk(path):
        for d in dirs:
            locallib.append(d)
        for f in files:
            locallib.append(os.path.splitext(f)[0])
    
    return diff(modules, locallib)


def remove_std_modules(modules: list) -> list:
    """
    Remove built-in, standard from a list of modules.
    """
    stdlib = set(i.name for i in pkgutil.walk_packages()).union(sys.modules.keys())
    return diff(modules, stdlib)


def write(path: str, modules: list) -> None:
    """
    Write a distill.txt file with module names (similar to requirements.txt).
    """
    with open(path+'/distill.txt', "w") as f:
        for module in sorted(modules):
            f.write(module+'\n')

    # in the future maybe implement modules as class and extra information from them
    # such that we can add version numbers like a typical requirements.txt




