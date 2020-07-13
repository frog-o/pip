import subprocess
import sys
import click
from pathlib import Path
from spip.cvs import gittool
from spip.project import create_project

from spip.conf.defaults import *

@click.command('push')
def exe():
      """ pushes the source code for program back to github """
      gittool.add_user_fork()
      #url = gittool.git_remote_origan_url())
      #proj = create_project

      #print(url)
     
      try:
          subprocess.check_call(["git", "commit","-a" ])
          
      except:
           print("failed to commit maybe already comitted")
      print("pushing branch:" +  gittool.get_current_branch()+"to user fork")
      subprocess.check_call(["git", "push","-f", "mypipfork",gittool.get_current_branch() ])
      

      
