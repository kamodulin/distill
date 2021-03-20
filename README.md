# distill

distill is a Python utility to extract necessary third-party imports from a project. I created this utility since I develop projects with more packages (e.g. jupyter, pandas) than necessary for a final product.


## Installation
<!-- Distill can be installed via pypi
```bash
pip install distill
``` -->

Clone this repo and enter this command from the root directory
```bash
pip install .
```

*Note*: make sure you've activated your Python environment where you want distill to be installed.


## Using distill
*Make sure to activate the environment where distill is installed.*

Go to the root of your project directory
```bash
cd path/to/project
```

Run distill (options/flags will be added later)
```bash
distill
```

Output
```bash
Necessary imports:
cv2
numpy
PIL
tensorflow
```

Features/ideas I would like to implement:
- [ ] Default file/dir exclusions
- [ ] A list of packages to uninstall that the user can uninstall via pip
- [ ] Find long names for packages. e.g. cv2:opencv-python, bs4:beautifulsoup4
- [ ] Find package versions
- [ ] Add tests
- [ ] Options
    - [ ] Verbose
    - [ ] Excludes
    - [ ] Override requirements.txt or output a distill.txt
    - [ ] Different output formats. e.g. yml, txt