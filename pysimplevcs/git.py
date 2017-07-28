############################################################
#
# pysimplevcs.git
# Copyright (C) 2017, Richard Cook
# Released under MIT License
# https://github.com/rcook/pysimplevcs
#
############################################################

from __future__ import print_function
import os

from pyprelude.file_system import make_path
from pyprelude.process import execute, proxy_command

class Git(object):
    def __init__(self, cwd=None):
        if cwd is None:
            cwd = os.getcwd()

        cwd = os.path.abspath(cwd)

        self._is_bare = execute("git", "rev-parse", "--is-bare-repository", cwd=cwd).strip() == "true"

        if self._is_bare:
            self._repo_dir = cwd
        else:
            self._repo_dir = execute("git", "rev-parse", "--show-toplevel", cwd=cwd).strip()

        self._git_dir = \
            self._repo_dir if self._is_bare \
            else make_path(self._repo_dir, ".git")

    @property
    def is_bare(self): return self._is_bare

    @property
    def repo_dir(self): return self._repo_dir

    @property
    def git_dir(self): return self._git_dir

    def __getattr__(self, name):
        def _missing_method(*args, **kwargs):
            return proxy_command(name, self._repo_dir, lambda n, args: ["git", n] + args, *args, **kwargs)

        return _missing_method
