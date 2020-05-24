"""Primary application entrypoint.
"""
import os
import subprocess
import sys
import time
import urllib
from urllib.parse import urlparse ,ParseResult , urlunparse
from pathlib import Path
from datetime import datetime

clone_name="pip"
clone_url="https://github.com/pypa/pip.git"

pip_src_path = Path.home()/'pip-sources' / 'src'
git_src_path = pip_src_path / clone_name 
entry_point =  'src/pip'

#create our source dir 
pip_src_path.mkdir(parents = True,exist_ok = True )




#varibles nsynctime = nsync_hours + nsync_mins
nsync_hours = 8
nsync_mins = 8

def main():

    if (source_download()):

       subprocess.check_call([sys.executable, str(git_src_path  / entry_point),"--unstable-feature=resolver",*sys.argv[1:] ])
       
    else:

       print("cloning " + clone_name + " from " + clone_url + " to :\n")
       print("\t" + str(pip_src_path) + "failed")

def source_download():
   """Download source if already downloaded then update it
   it does this by staching away you changes rebass pull then reaply changes """

   if (git_src_path.exists and git_src_path.is_dir() ):
   


    gitfile_path =  Path( git_src_path / '.git' / 'FETCH_HEAD')

    #this was diificualt for me to write becuase of what python calls the epoc time 
    #wich was return from the  pathlib.stat.st_mtime
    #this is the  time of file last modifued from the epoc    
    
    mod_time     = datetime.fromtimestamp(gitfile_path.stat().st_mtime) 
    nsync_time   = datetime.fromtimestamp( mod_time.timestamp() + nsync_hours* 3600 + nsync_mins*60)  
    current_time =  datetime.fromtimestamp( time.time())


    if(nsync_time < current_time ):
        subprocess.check_call(["git", "stash"],cwd = str(git_src_path) )
        subprocess.check_call(["git", "pull", "--rebase","origin","master"],cwd = str(git_src_path) )
        subprocess.check_call(["git", "stash","apply"],cwd = str(git_src_path) )
    else:
       #time until next sync 
        tuns= nsync_time - current_time
        hours, tr    = divmod (tuns.seconds,3600)
        mins,seconds = divmod (tr,60)
        print ( 'Next sync in {} hours {} minutes and {} seconds'.format(int(hours), int(mins), seconds) )
   else:

      subprocess.check_call(["git","clone",clone_url,str(git_src_path) ])
      add_user_fork()


   return True
def add_user_fork():
   """ add your fork to remote.  This function tries to guess your fork name by looking at \
       the clone_url gotton it is also the same one from running 'git remote get-url origin'\\
       and adds your user name goten from running the command 'git config user.name' 
       after the https://github.com/
   """
   url = urlparse(clone_url)
   username =  subprocess.check_output(["git" ,"config",  "user.name"],cwd = git_src_path).decode("utf-8")
   username = username.strip()
   fork_path = username +"/" + Path(url.path).name
   
   fork_url = urlunparse(
                         ParseResult(scheme=url.scheme, netloc=url.netloc, path=fork_path,params = "" 
                         ,query = "", fragment ="" ))
   subprocess.check_call(["git","remote","add","mypipfork",fork_url ])
   


#"https://github.com/Username/pip.git"
#"https://github.com/OriginName/pip.git"

