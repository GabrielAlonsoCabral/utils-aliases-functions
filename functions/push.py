import os

os.system("git push origin $(git rev-parse --abbrev-ref HEAD)")