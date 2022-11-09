# Python install library local

## Work on and test environment

Ubuntu 20.04

## Install

Create a virtual environment with e.g. `virtualenv` and activate it.
```bash
virtualenv -p /usr/bin/python3.8 venv3.8
```
After that install the tools 

```bash
python<your-version-of-python> setup.py install 
```
## Purposes
This is a script that allows you to install your own custom library locally. You can create a python class, function, variable, etc. and install it locally. This allows you to use your own custom library in your project. 
The main purpose of this script it's to avoid import error between different python files and folder.

## How it's work

It will create a symlink of the file specified in argument to the python virtual environment library folder.

## Usage
Go to the folder where you have your python file and run the following command:
```bash 
install_lib.py -i <input_file> -p <path_to_virtual_env>
```

