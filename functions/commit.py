import os
import subprocess

FILES=str(subprocess.check_output("git status -s", shell=True).decode('ascii'))
SERVICE=str(subprocess.check_output("git ls-remote --get-url | xargs basename -s .git", shell=True).rstrip().decode('ascii'))


GIT_CREATED_PREFIX="?"
GIT_UPDATED_PREFIX="M"
GIT_DELETED_PREFIX="D"

INTERNAL_CREATED_PREFIX="[FEAT]"
INTERNAL_UPDATED_PREFIX="[IMPROVEMENT]"
INTERNAL_DELETED_PREFIX="[FIX]"

BRANCH_NAME=str(subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True).decode("ascii"))
BRANCH_PREFIX_TO_REPLACE="gabrielAlonsoCabral/"

if(BRANCH_PREFIX_TO_REPLACE in BRANCH_NAME):
    BRANCH_NAME=BRANCH_NAME.replace(BRANCH_PREFIX_TO_REPLACE, "")

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

