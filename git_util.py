from __future__ import print_function
import os

from pyvcs.git import Git
from pyvcs.process import execute

def git_init(repo_dir):
    if os.path.isdir(repo_dir):
        raise RuntimeError("Git repo directory {} already exists".format(repo_dir))

    output = execute("git", "init", repo_dir).strip()
    if "Initialized empty Git repository" not in output:
        raise RuntimeError("git init failed with unexpected output: {}".format(output))

    return Git(repo_dir)
