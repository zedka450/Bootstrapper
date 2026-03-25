import os
import sys
import subprocess
import time

PROJECT = {
    "LAUNCH_INFOS": {
    },
    "REQUIRE": {
        "IMPORTS": [
        ]
    }
}

BASE_LIB = [
    "os", "sys", "pathlib", "shutil", "json", "csv", "sqlite3",
    "re", "math", "random", "datetime", "time", "statistics",
    "collections", "itertools", "functools", "logging", "threading",
    "multiprocessing", "asyncio", "subprocess", "urllib", "hashlib",
    "base64", "pickle", "argparse"
]

DEBUG_MODE = True

def project_info(itc):
    if itc == "name":
        return PROJECT["LAUNCH_INFOS"]["NAME"]
    elif itc == "path":
        return PROJECT["LAUNCH_INFOS"]["FULL_PATH"]
    elif itc == "libs":
        return PROJECT["REQUIRE"]["IMPORTS"]

def _import_():
    libs = project_info("libs")
    print(f"Imports needed for {project_info('name')}: {libs}")
    
    for lib in libs[:]: 
        if lib in BASE_LIB:
            libs.remove(lib)
            if DEBUG_MODE:
                print(f"Lib '{lib}' ignored (it's a default lib)")
        else:
            print(f"Installing {lib}...")
            subprocess.run([sys.executable, "-m", "pip", "install", lib])

    print(f"All external libs for {project_info('name')} are installed.")
    time.sleep(1.8)
    
    subprocess.run([sys.executable, "-u", project_info("path")])
    sys.exit(0)
if __name__ == "__main__":
    _import_()
