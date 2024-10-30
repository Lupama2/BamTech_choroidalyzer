
#Doy acceso a directorios arriba

import sys
import os

# Get the directory two levels up from the current file (project root)
repo_directory = os.getcwd()

project_root_father = os.path.abspath(os.path.join(os.path.dirname("__file__"), '..'))
lib_root = os.path.abspath(os.path.join(project_root_father, 'lib'))
models_root = os.path.abspath(os.path.join(project_root_father, 'models'))
utility_root = os.path.abspath(os.path.join(project_root_father, 'utility'))

project_root_grandfather = os.path.abspath(os.path.join(os.path.dirname("__file__"), '..', '..'))

data_root = os.path.abspath(os.path.join(project_root_grandfather, 'data'))

project_roots = [project_root_father, lib_root, utility_root, project_root_grandfather, data_root, models_root]

# Add the project root to the Python path
for root in project_roots:
    print(root)
    if root not in sys.path:
        sys.path.append(root)