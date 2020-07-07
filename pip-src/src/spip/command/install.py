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
      source_dir = gittool.get_source_dir() 
      print("Looking for source for ",source_dir ) 
      
      if (not source_dir.is_dir()):
         source_dir.mkdir()

      #if you don't convert this to a string it will faill beacuse of the /n it puts in it.
      
      python_ver  = subprocess.check_output(
                             ["pyenv","which", "python"],
                             cwd = str(env_full_path) 
                        ).decode("utf-8").strip()
      project_dir = gittool.find_project(source_dir ) 
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

