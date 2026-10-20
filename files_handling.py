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


def traverse(fld):
    for fldpath, dirs, fls in os.walk(fld):
        print(f"Folders: {fldpath}")
        for fn in fls:
            print(f"\t{fn}")

def copy_files(src, dst):
    shutil.copy(src, dst)

def copy_folder(src, dst):
    shutil.copytree(src, dst)

def move_files_folders(src, dst):
    shutil.move(src, dst)

def rename_file(src, dst):
    os.rename(src, dst)

def rename_file_with_path(src, dst):
    f = Path(src)
    f.rename(dst)

def remove_file(file):
    if os.path.isfile(file):
        try:
            os.remove(file)
        except OSError as e:
            print(f"Error: {file} : {e.strerror}")
    else:
        print(f"Error: {file} is not a valid file")

remove_file("./120-days-of-python/hof.py")
rename_file("./120-days-of-python/rps.py", "./120-days-of-python/rock.py")
ename_file_with_path("./120-days-of-python/rock.py", "./120-days-of-python/rps.py")
move_files_folders("./120-days-of-python/miz.py", "./120-days-of-python/new")
copy_files("./120-days-of-python/hof.py", "./120-days-of-python/test")
copy_folder("./120-days-of-python/test", "./120-days-of-python/new")
