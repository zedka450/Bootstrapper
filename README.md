# Bootstrapper
An ultra-lightweight environment manager written in native Python. This script checks for missing dependencies, installs them via pip, and automatically runs your project.

#Features
1.Zero Dependencies: The bootstrapper uses only Python's standard library.

2.Auto-Installation: Detects whether a library is internal (standard) or external.

3.Smart Launch: Launches your main script once the environment is ready.

4.Debug Mode: Real-time tracking of what is being ignored or installed.

#Usage
Configure your PROJECT dictionary in bootstrap.py:
`PROJECT = {`
  `“LAUNCH_INFOS”: {`
    `“NAME”: “MyAwesomeProject”,`
    `“FULL_PATH”: r“C:\Path\To\Your\Script.py”`
        `},`
        `“REQUIRE”: {`
            `“IMPORTS”: [‘requests’,`
            `“colorama”] # Your libraries here`
  `}`
`}`
Simply run the bootstrapper:
`python bootstrap.py`
