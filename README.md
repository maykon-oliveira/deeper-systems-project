deeper-system-project
=====================

Getting Started
---------------

- Inside the project create a Python virtual environment.

`$ python3 -m venv env`

- Upgrade packaging tools.

`$ env/bin/pip install --upgrade pip setuptools`

- Install the dependecies.

`$ env/bin/pip install -e .`

- Run your project in develop mode.

`$ env/bin/pserve development.ini --reload`