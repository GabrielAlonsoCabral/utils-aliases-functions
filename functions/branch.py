import os
import sys
import subprocess

GH_NAME=str(subprocess.check_output("echo $GH_NAME", shell=True).decode('ascii').rstrip())

NAME_FLAG ="--name"

if NAME_FLAG not in sys.argv:
    print("{} is a required flag \n".format(NAME_FLAG))
    exit()

NAME_INDEX = sys.argv.index("--name")
NAME_VALUE=""

try:
    if not sys.argv[NAME_INDEX+1]:
        exit()
    
    NAME_VALUE = sys.argv[NAME_INDEX+1]

    if "--" in NAME_VALUE:
        exit()

    if(GH_NAME in NAME_VALUE):
        NAME_VALUE=NAME_VALUE.replace("{}/".format(GH_NAME), "")
    
    BRANCH_NAME="{}/{}".format(GH_NAME, NAME_VALUE)

    os.system("git checkout -b {}".format(BRANCH_NAME) )
except:
    print("you must to pass a correct value for {} flag \n".format(NAME_FLAG))
    exit()