import os
import sys
#Lets Start

show = sys.argv[1]

os.system('pip3 install -r requirements.txt')
if show == "show":
    os.system('python3 simulate.py GUI 0 E')
    os.system('python3 simulate.py GUI 0 show')

else:
    os.system('python3 search.py')
