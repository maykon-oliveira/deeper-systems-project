deeper-system-project
=====================

Getting Started
---------------

- Change directory into your newly created project.

    cd deeper_system_project

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini

Running:
```
$ export VENV=~/projects/quick_tutorial/env
$ $VENV/bin/pip install cookiecutter
$ $VENV/bin/cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout 1.10-branch
$ cd deeper_system_project/
$ python3 -m venv env
$ env/bin/pip install --upgrade pip setuptools
$ env/bin/pip install -e .
$ env/bin/pserve development.ini --reload
```