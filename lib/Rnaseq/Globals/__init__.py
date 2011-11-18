#-*-python-*-

globals={};

import os

def get(k):
    return globals[k]

def set(k, v):
    globals[k]=v
    return v

def delete(k):
    v=globals[k]
    del globals[k]
    return v

def init():
    dir=os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"/../../..")
    set('rnaseq_dir', dir)


init()
