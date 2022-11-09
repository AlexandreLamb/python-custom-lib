import os

import sys

import getopt
import argparse
 
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-i", "--Input-File", help = "Path to local input library file to install in virutal python environment")
parser.add_argument("-p", "--Python-Path", help = "Path to python virtual environment")
 
# Read arguments from command line
args = parser.parse_args()
 

#check if local python lib file is provided
if args.Input_File:
    input_file = args.Input_File
else:
    input_file = input("Please enter path to local input library file to install in virutal python environment")

#check if python path is provided
if args.Python_Path:
    python_path = args.Python_Path
else:
    print("Please provide python path with -p option")
    sys.exit(1)
    
# check if python local lib file exists and is a python file
if not (os.path.isfile(input_file) and input_file.endswith(".py")):
    print("Please provide a valid python file")
    sys.exit(1)

# check if python path is valid path
if not os.path.isdir(python_path):
    print("Please provide valid python path")
    sys.exit(1)
    
# Check if python path is a virtual environment
if not os.path.isfile(os.path.join(python_path, "pyvenv.cfg")):
    print("Please provide valid python virtual environment path")
    sys.exit(1)
    
# Check if python path lib folder exists
if not os.path.isdir(os.path.join(python_path, "lib")):
    print("Please provide valid python virtual environment path")
    sys.exit(1)
    
# Find python version in virtual environment
python_version_from_sys_info = "python"+ str(sys.version_info[0]) + "."  + str(sys.version_info[1])

python_version_from_dir = os.listdir(os.path.join(python_path, "lib"))[0]

# Check if python path lib python version site-packages folder exists
if not os.path.isdir(os.path.join(python_path, "lib", python_version_from_dir, "site-packages")):
    print("Please provide valid python virtual environment path")
    sys.exit(1)
    
# path to site-packages folder
path_to_site_packages = os.path.join(os.getcwd(), python_path, "lib", python_version_from_dir, "site-packages",input_file)
input_file = os.path.join(os.getcwd(), input_file)

#Check if input file is already present in site-packages folder
if os.path.exists(os.path.join(path_to_site_packages, os.path.basename(input_file))):
    print("File" + os.path.basename(input_file) + "already exists in site-packages folder")
    print("Input file is at path: " + input_file)
    print("Site-packages folder is at path: " + path_to_site_packages)
    sys.exit(1)
    
print("Installing library file in virtual environment")
print("Creating lib file at path : ", path_to_site_packages)
print("With input file: ", input_file)



# create a symbolic link to local python lib file in site-packages folder
try : 
    os.symlink(input_file, path_to_site_packages)
    
    print("Library file installed successfully")
    print("Input file is at path: " + input_file)
    print("Site-packages folder is at path: " + path_to_site_packages)
    print("You can now import the library in your python code with e.g. : from "+input_file+" import *")
    
except OSError as e: 
    print(e)
    print("Error creating symbolic link, please contact :insert email here")
