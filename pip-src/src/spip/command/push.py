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
      try:
          subprocess.check_call(["git", "commit","-a" ])
      except:
           print("failed to commit maybe already comitted")
      subprocess.check_call(["git", "commit","-a" ])

      subprocess.check_call(["git", "push","mypipfork",gittool.get_current_branch() ])


      
