from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="distill",
    version="0.0.1",
    description="distill is a Python utility to extract necessary third-party imports from a project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamodulin/distill",
    author="Kamran Ahmed",
    packages=find_packages(),
    zip_safe=False,
    entry_points = {
        "console_scripts": ["distill=distill.distill:main"],
    }
)
