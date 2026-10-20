import os, fnmatch
from pathlib import Path
from datetime import datetime, UTC
import shutil

def list_diff(folder):
    for fn in os.listdir(folder):
        print(fn)


def ends_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)

def start_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)
