# distill

distill is a Python utility to extract necessary third-party imports from a project. I created this utility since I develop projects with more packages (e.g. jupyter, pandas) than necessary for a final product. Note that package names may differ from their import names (e.g. scikit-learn:sklearn, beautifulsoup4:bs4). This is not easy to solve so it's left up to the user to handle.

## Features

## Installation
<!-- Distill can be installed via pypi
```bash
pip install distill
``` -->

Clone this repo and enter this command from the root directory
```
pip install .
```

*Note*: make sure you've activated your Python environment where you want distill to be installed.


## Using distill to clean up requirements
Go to the root of your project directory
```
cd path/to/project
```

```
Usage:
    distill [options]

Options:
    -d, --dir       Directory to perform distillation (defaults to current working directory).
    -s, --save      Save distilled requirements to file. (defaults to distill.txt in current working directory).

```

Output
```
Imports: ['cv2', 'numpy', 'PIL', 'tensorflow']
Writing distilled requirements to <save>/distill.txt
```

<!-- Features/ideas I would like to implement:
- [ ] Default file/dir exclusions
- [ ] A list of packages to uninstall that the user can uninstall via pip
- [ ] Find long names for packages. e.g. cv2:opencv-python, bs4:beautifulsoup4
- [ ] Find package versions
- [ ] Add tests
- [ ] Options
    - [ ] Verbose
    - [ ] Excludes
    - [ ] Override requirements.txt or output a distill.txt
    - [ ] Different output formats. e.g. yml, txt -->