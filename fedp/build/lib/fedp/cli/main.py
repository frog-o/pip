"""Primary application entrypoint.
"""
import os
import subprocess
import sys
from pathlib import Path

#dpip is pip command withe the  --unstable-feature=resolver flag set and other optimzing
#it update itself once per day on use

# Running pip in-process is unsupported and unsafe. This is
# elaborated in detail at
# https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program.
# That document also provides suggestions that should work for nearly
# all users that are considering importing and using main() directly.

# However, we know that certain users will still want to invoke pip
# in-process. If you understand and accept the implications of using pip
# in an unsupported manner, the best approach is to use runpy to avoid
# depending on the exact location of this entry point.

# The following example shows how to use runpy to invoke pip in that
# case:
#
#     sys.argv = ["pip", your, args, here]
#     runpy.run_module("pip", run_name="__main__")
#
# Note that this will exit the process after running, unlike a direct
# call to main. As it is not safe to do any processing after calling
# main, this should not be an issue in practice.

fedp_src_path = Path.home()/'fedp' / 'src'
pip_path_from_git = fedp_src_path / 'pip' / 'src'/ 'pip'

def main():

    if (downloaded_pip()):
       pipPath=str(pip_path_from_git)
       subprocess.check_call([sys.executable, str(pip_path_from_git),"--unstable-feature=resolver",*sys.argv[1:] ])
    else:
       print(pip_from_git)
def downloaded_pip():
    return pip_path_from_git.is_dir()
