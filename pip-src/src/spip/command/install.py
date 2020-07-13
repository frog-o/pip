from spip.conf.defaults import *
from spip.project import create_project
from libvcs.shortcuts import create_repo_from_pip_url, create_repo

import click 

@click.command('install')
@click.argument('url')
def exe(url):
      """ Install <url>  clone the source code for project from <url> """
      project = create_project(url)
      
      source_dir = project.get_source_dir()
      virt_dir   = project.get_virt_dir() 
      
      print("Looking for virtual enviorment for project in:",virt_dir) 
      if (not virt_dir.is_dir()):
            print("Can't find virtual environment creating") 
            virt_dir.mkdir(parents=True)
            project.create_venv()
            print("test")
    
      print("Looking for source for :",source_dir ) 
      
      if (not source_dir.is_dir()):
         print("source dir not found creating clone url:",url)
         source_dir.mkdir(parents=True)
      repo = create_repo(url=url,
                 vcs='git',
                 repo_dir=str(source_dir))  
         
      repo.update_repo()
         
      return
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

