# Install instructions
Unit9 test installation instructions for unix/linux machines.
If you want to see this file as markup, open it in

- https://dillinger.io/
- https://jbt.github.io/markdown-editor/

or any online markup viewer.

## Pre-requisites

  - Python 3.6 installed
    - https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7
    - check that python3 binary is executable on your system.
        ```bash
        bash$ python3 -V
        Python 3.6.1

## Installation process

First of all we need to create a virtual environment (sandbox) in order to not polluting the system default installation directorios. So:
1. create a folder where everything is gonna be stored/installed.
    ```bash
    bash$ mkdir -p /home/user/.virtualenvs
2. create the unit9 specific virtualenv
    ```bash
    bash$ python3 -m venv /home/user/.virtualenvs/unit9
3. activate the virtual environment
    ```bash
    bash$ source /home/user/.virtualenvs/unit9/bin/activate
    (unit9) bash$
4. install pre-requisites
    ```bash
    (unit9) bash$ pip install -r requirements.txt
5. install the tool
    ```bash
    (unit9) bash$ python setup.py install
6. Use it!
    ```bash
    (unit9) bash$ unit9

## Generate binary distribution for docker vendor

1. do it!
    ```bash
    bash$ python setup.py bdist_wheel
    ```
