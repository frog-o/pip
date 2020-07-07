import subprocess
import sys
import click
from pathlib import Path
from spip.cvs import gittool

from spip.conf.defaults import *

@click.command('install')
@click.argument('url')
def exe(url):
      """ Install <url>  clone the source code for program from <url> """
      project_name = Path(url).name[0:-4]
      env_full_path= spip_root_path / str(project_name +"-env")      
      print("Looking for source for ",env_full_path ) 
      
      if (not env_full_path.is_dir()):
         env_full_path.mkdir()

      #if you don't convert this to a string it will faill beacuse of the /n it puts in it.
      
      python_ver  = subprocess.check_output(
                             ["pyenv","which", "python"],
                             cwd = str(env_full_path) 
                        ).decode("utf-8").strip()
      project_dir = gittool.find_project(env_full_path ) 
      #print("check out source")
      gittool.update_source(sys.argv[2],env_full_path / 'src')
      print("create virtual enviorment for ",)
      print("python version=\t:" + str(python_ver))
      print("project in\t:" + str(env_full_path))
      print("project dir is\t:" + str(project_dir))
      subprocess.check_call(["pipenv", "--python="+str(python_ver) ],cwd = project_dir )
      #subprocess.check_call(["pipenv","run","pip","install", "-e", "."],cwd = project_dir )
      #print(e)
      #env_full_path.rmdir()

