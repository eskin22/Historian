import subprocess 

# open the sample webpages 
subprocess.run(['python', 'src/helpers/openSampleWebpages.py'])

# start running the server
subprocess.run(['python', 'server.py'])