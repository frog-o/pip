import subprocess
import sys
import click
from pathlib import Path
from spip.cvs import gittool

from spip.conf.defaults import *

@click.command('push')
def exe():
      """ pushes the source code for program back to github """
      gittool.add_user_fork()
      gittool.update_source(gittool.git_remote_origan_url())
      print(gittool.git_remote_origan_url())
      try:
          subprocess.check_call(["git", "commit","-a" ])
          
      except:
           print("failed to commit maybe already comitted")
      print("pushing branch:" +  gittool.get_current_branch()+"to user fork")
      subprocess.check_call(["git", "push","-f", "mypipfork",gittool.get_current_branch() ])
      

      
