
# DALiuGE Components Project Template

This project template is the starting point for people who want to develop Python based **components** for the **[DALiuGE](https://daliuge.reqdthedocs.io)** workflow development and execution framework. It contains everything to get you started, including project setup, dependency installation and the actual installation procedure into the DALiuGE environment.

**NOTE: This template is based on the excellent work of Bruno Rocha (https://github.com/rochacbruno/python-project-template).**

### HOW TO USE THIS TEMPLATE

> **DO NOT FORK** this is meant to be used from **[Use this template](https://github.com/ICRAR/daliuge-component-template/generate)** feature, which also appears instead of the usual 'Code' button on the top-right of the repository page.

1. Click on **[Use this template](https://github.com/ICRAR/daliuge-component-template/generate)**
3. Give a name to your new DALiuGE components  
   (e.g. `my_awesome_components`, recommendation is to use all lowercase and underscores separation for repo names.)
3. **Wait until the first run of CI finishes(!)**
   (Github Actions will process the template and commit to your new repo)
4. If you want [codecov](https://about.codecov.io/sign-up/) Reports and Automatic Release to [PyPI](https://pypi.org)  
  On the new repository `settings->secrets` add your `PIPY_API_TOKEN` and `CODECOV_TOKEN` (get the tokens on respective websites)
5. Then clone your new project and happy coding!

> **AGAIN**: **WAIT** until first CI run on github actions **before** cloning your new project.

### What is included in this template?

- 🖼️ **Basic** Python components [use this template](https://github.com/ICRAR/daliuge-component-template/generate)
  **or Run `make init` after cloning to generate a new project based on a template.**
- 📦 A basic [setup.py](setup.py) file to provide installation, packaging and distribution for your component.  
  Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your component. (Try `make help`)
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🐋 A simple [Containerfile](Containerfile) to build a container image for your project.  
  `Containerfile` is a more open standard for building container images than Dockerfile, you can use buildah or docker with this file.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🎯 Entry points to execute your program using `python -m <project_name>` or `$ project_name` with basic CLI argument parsing.
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux and Mac environments.

> Curious about architectural decisions on this template? read [ABOUT_THIS_TEMPLATE.md](ABOUT_THIS_TEMPLATE.md)  
> If you want to contribute to this template please open an [issue](https://github.com/ICRAR/daliuge-component-template/issues) or fork and send a PULL REQUEST.

<!--  DELETE THE LINES ABOVE THIS AND WRITE YOUR PROJECT README BELOW -->

---
# my_awesome_component

[![codecov](https://codecov.io/gh/author_name/project_urlname/branch/main/graph/badge.svg?token=project_urlname_token_here)](https://codecov.io/gh/author_name/project_urlname)
[![CI](https://github.com/author_name/project_urlname/actions/workflows/main.yml/badge.svg)](https://github.com/author_name/project_urlname/actions/workflows/main.yml)

project_description

## Install it from PyPI

```bash
pip install my_component
```

## Usage

```py
from my_component import MyAppDROP

MyAppDROP('a','a').run()
```

```bash
$ python -m project_name
#or
$ project_name
```
