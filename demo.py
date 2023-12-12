"""
Author:     Blake McBride (blakepm2@illinois.edu)
Created:    12/02/2023

Overview:   This file contains a demo script to open sample webpages and start running the server so the user can demo Historian
"""

# standard imports
import subprocess 

# check dependencies
subprocess.run(['python', 'setup.py'])

# open the sample webpages 
subprocess.run(['python', 'src/helpers/openSampleWebpages.py'])

# start running the server
subprocess.run(['python', 'server.py'])