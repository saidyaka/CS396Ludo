import os
import sys
#Lets Start

show = sys.argv[1]

if show == "show":
    os.system('python3 simulate.py GUI 0 show')
else:

    os.system('pip3 install -r requirements.txt')
    os.system('python3 search.py')
