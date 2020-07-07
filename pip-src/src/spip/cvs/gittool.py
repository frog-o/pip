"""Primary application entrypoint.
"""
import os
import subprocess
import sys
import time
import urllib
import click
from urllib.parse import urlparse ,ParseResult , urlunparse
from pathlib import Path
from datetime import datetime
from spip.conf.defaults import *


def update_source(git_url,source_path):
   """update source from source_dest if not found then clone it
   it updates the source by staching away your changes and doing a 
   rebass pull then reaply changes """

   # git rid of the .git on the end of the name
   source_path =  source_path  / Path(git_url).name[:-4] 
   print( source_path )

   if ( source_path.exists and  source_path.is_dir() ):
   
     # this file should git updated each time git is run we us the time modifyed to see
     #how old you last git pull was performed.
   
     gitfile_path =  Path( source_path  / '.git' / 'FETCH_HEAD')
     
     #this was diificualt for me to write becuase of what python calls the epoc time   
     #wich was return from the  pathlib.stat.st_mtime
     #this is the  time of file last modifued from the epoc    
     
     mod_time     = datetime.fromtimestamp(gitfile_path.stat().st_mtime) 
     nsync_time   = datetime.fromtimestamp( mod_time.timestamp() + nsync_hours* 3600 + nsync_mins*60)  
     current_time =  datetime.fromtimestamp( time.time())
    
    
     if(nsync_time < current_time ):
        try:
            subprocess.check_call(["git", "stash"],cwd = str( source_path ) )
            subprocess.check_call(["git", "pull", "--rebase","origin","master"],cwd = str( source_path ) )
            subprocess.check_call(["git", "stash","apply"],cwd = str( source_path ) )
        except:
          pass
     else:
       #time until next sync 
        tuns= nsync_time - current_time
        hours, tr    = divmod (tuns.seconds,3600)
        mins,seconds = divmod (tr,60)
        print ( 'Next sync in {} hours {} minutes and {} seconds'.format(int(hours), int(mins), seconds) )
        return False
   else:
      print("cloning url :",git_url)
      subprocess.check_call(["git","clone",git_url, str(source_path) ])


   return True

def git_remote_fork_url():
     """return the name of the Automaticlay created remote url"""
     clone_url = subprocess.check_output(["git" ,"remote",  "get-url","origin"]).decode("utf-8")  
     url = urlparse(clone_url)
     username =  subprocess.check_output(["git" ,"config",  "user.name"]).decode("utf-8")
     username = username.strip()
     
     fork_path = username +"/" + Path(url.path).name

     fork_url = urlunparse(
                         ParseResult(scheme=url.scheme, netloc=url.netloc, path=fork_path,params = "" 
                         ,query = "", fragment ="" ))
     return fork_url

def add_user_fork():
   """ add your fork to remote.  This function tries to guess your fork name by looking at \
       'git remote get-url origin of the current working directory'\\
       and adds your user name goten from running the command 'git config user.name' 
       after the https://github.com/
   """

   
   try:
      mypipfork  = subprocess.check_output(["git" ,"remote",  "show","mypipfork"]).decode("utf-8")
      print("already found mypipfork:"); 
   except:
      if "fatal: 'mypip' does not appear to be a git repository" in mypipfork:
          click.echo("create a git remote for user:",username); 
          subprocess.check_call(["git","remote","add","mypipfork",git_remote_fork_url ])
   
def find_project(project_path):
    """ This function look into all subdir for a setup.py or pipfile.lock and return the project path were the setup.py was found 
Return The project_root
""" 
    for project_root in Path(project_path).rglob('**/setup.py'):
        return str(project_root)[:-9]
    return project_path
def get_current_branch():
      """ return the name of currently active branch """ 
      mybranches  = subprocess.check_output(["git" ,"branch"]).decode("utf-8")
      for branch in mybranches:
          if("*" in branch):
               return branch[1:].strip() 




#"https://github.com/Username/pip.git"
#"https://github.com/OriginName/pip.git"

