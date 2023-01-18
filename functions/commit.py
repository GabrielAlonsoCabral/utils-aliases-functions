import os
import subprocess

FILES=str(subprocess.check_output("git status -s", shell=True).decode('ascii'))
SERVICE=str(subprocess.check_output("git ls-remote --get-url | xargs basename -s .git", shell=True).rstrip().decode('ascii'))


GIT_CREATED_PREFIX="??"
GIT_UPDATED_PREFIX="^ M"
GIT_DELETED_PREFIX="^ D"

INTERNAL_CREATED_PREFIX="[FEAT]"
INTERNAL_UPDATED_PREFIX="[IMPROVEMENT]"
INTERNAL_DELETED_PREFIX="[FIX]"

BRANCH_NAME=str(subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True).decode("ascii"))
BRANCH_PREFIX_TO_REPLACE="gabrielAlonsoCabral/"

if(BRANCH_PREFIX_TO_REPLACE in BRANCH_NAME):
    BRANCH_NAME=BRANCH_NAME.replace(BRANCH_PREFIX_TO_REPLACE, "")

COMMIT_MESSAGE_PREFIX=""

if(GIT_CREATED_PREFIX in FILES):
    COMMIT_MESSAGE_PREFIX=INTERNAL_CREATED_PREFIX

if(GIT_UPDATED_PREFIX in FILES):
    COMMIT_MESSAGE_PREFIX=INTERNAL_UPDATED_PREFIX

if(GIT_DELETED_PREFIX in FILES):
    COMMIT_MESSAGE_PREFIX=INTERNAL_DELETED_PREFIX

if(len(FILES)==0):
    COMMIT_MESSAGE_PREFIX=INTERNAL_DELETED_PREFIX


COMMIT_MESSAGE ="{} - {} - {}".format(COMMIT_MESSAGE_PREFIX, SERVICE, BRANCH_NAME)
print(COMMIT_MESSAGE)
os.system("git add .")
os.system("git commit -m '{}' ".format(COMMIT_MESSAGE))
