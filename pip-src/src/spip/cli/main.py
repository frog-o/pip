import subprocess
import sys
import click
from spip.command import install,push,go
from pathlib import Path
from spip.conf.defaults import *

	
@click.group()
@click.version_option()
def main():

   spip_root_path.mkdir(parents = True,exist_ok = True )
  # main()

   print("running python :",sys.version)

def find_project(project_path):
    """ This function look into all subdir for a setup.py or pipfile.lock and return inside project_path the directory with this file in it  
Return The project_root
""" 
    for project_root in Path(project_path).rglob('**/setup.py'):
        return str(project_root)[:-9]
    return str(project_path)

#if __name__ == '__main__':
#     main()

main.add_command(install.exe)
main.add_command(push.exe)
main.add_command(go.exe)

