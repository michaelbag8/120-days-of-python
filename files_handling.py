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
            
def match(fld, search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)

def glob_match(fld, search):
    p = Path(fld)
    for n in p.glob(search):
        print(n)


def get_date(timestmp):
    return datetime.fromtimestamp(timestmp, UTC).strftime("%d %b %Y")


def get_file_attrs(fld):
    with os.scandir(fld) as dir:
        for f in dir:
            if f.is_file():
                inf = f.stat()
                print(f"Modified {get_date(inf.st_mtime)} {f.name}")
