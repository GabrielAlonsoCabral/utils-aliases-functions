import os
import subprocess
import sys

FILES=str(subprocess.check_output("git status -s", shell=True).decode('ascii'))
SERVICE=str(subprocess.check_output("git ls-remote --get-url | xargs basename -s .git", shell=True).rstrip().decode('ascii'))
GH_NAME=str(subprocess.check_output("gh api user | jq -r '.login'", shell=True).decode('ascii'))

if(len(FILES)==0):
    exit()

GIT_CREATED_PREFIX="?"
GIT_UPDATED_PREFIX="M"
GIT_DELETED_PREFIX="D"

INTERNAL_CREATED_PREFIX="[FEAT]"
INTERNAL_UPDATED_PREFIX="[IMPROVEMENT]"
INTERNAL_DELETED_PREFIX="[FIX]"

ORIGINAL_BRANCH_NAME=str(subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True).decode("ascii"))
BRANCH_NAME=str(subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True).decode("ascii"))

if(GH_NAME in BRANCH_NAME):
    BRANCH_NAME=BRANCH_NAME.replace("{}/".format(GH_NAME), "")

COMMIT_MESSAGE_PREFIX=""

if(FILES[1]==GIT_CREATED_PREFIX):
    COMMIT_MESSAGE_PREFIX=INTERNAL_CREATED_PREFIX

if(FILES[1]==GIT_UPDATED_PREFIX):
    COMMIT_MESSAGE_PREFIX=INTERNAL_UPDATED_PREFIX

if(FILES[1]==GIT_DELETED_PREFIX):
    COMMIT_MESSAGE_PREFIX=INTERNAL_DELETED_PREFIX

if(len(COMMIT_MESSAGE_PREFIX)==0):
    COMMIT_MESSAGE_PREFIX=INTERNAL_DELETED_PREFIX


COMMIT_MESSAGE ="{} - {} - {}".format(COMMIT_MESSAGE_PREFIX, SERVICE, BRANCH_NAME)
os.system("git add .")
os.system("git commit -m '{}' ".format(COMMIT_MESSAGE))

for index, arg in enumerate(sys.argv):
    if(arg=='--push'):
        os.system("git push origin $(git rev-parse --abbrev-ref HEAD)")

    if(arg=='--pr'):
        os.system("gh pr create --assignee @me --title '{}' --body '{}'".format(COMMIT_MESSAGE, FILES) )

