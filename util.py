from __future__ import print_function
import os

def make_path(*paths):
    return os.path.abspath(os.path.join(*[p for p in paths if p is not None]))

def try_pop(d, key, default):
    value = d.get(key, default)
    if key in d:
      d.pop(key)
    return value

def unpack_args(*args):
    l = list(args)
    return l[0] if len(l) == 1 and isinstance(l[0], list) else l
