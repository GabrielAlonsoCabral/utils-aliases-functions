import os
import sys

REPO_FLAG ="--repo"

if REPO_FLAG not in sys.argv:
    print("{} is a required flag \n".format(REPO_FLAG))
    exit()

REPO_INDEX = sys.argv.index("--repo")
REPO_VALUE=""

try:
    if not sys.argv[REPO_INDEX+1]:
        exit()
    
    REPO_VALUE = sys.argv[REPO_INDEX+1]
    if "--" in REPO_VALUE:
        exit()

    os.system(
    "echo 'going to {}...' && cd ~/workspace/tmob/{} && echo 'Updating submodules...' && git submodule update --remote --recursive && echo 'Saving to git...' && git add . && git commit -m 'FEAT: UPDATE' && git push origin master".format(REPO_VALUE, REPO_VALUE)
    )

except Exception as error:
    print(error)
    exit()
