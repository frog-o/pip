from pathlib import Path
from spip.conf.defaults import *
from virtualenvapi.manage import VirtualEnvironment


import os

def create_project(url):
    return project(url)

class project:

  def __init__(self, url):
    """create a pip-source project from url"""
    self.url = url
    self.name = str( Path(url).name[0:-4] )
  def create_venv(self):
    venv_path = str( self.get_virt_dir())
    print("Creating virtual environment in :",venv_path)
    #this does not do anything untill used 
    self.env = VirtualEnvironment(venv_path)
    self.env.is_installed('mezzanine')
  def get_name(self):
   """ return the project name for url """
   return self.name 
  
  def update_source(self):
   """update source for the url.  If not found then clone it.
   It updates the source by staching away your changes and doing a 
   rebass pull then reaply changes """

   # git rid of the .git on the end of the name
   source_path =  get_source_dir(url)  
   print( source_path )
  
  def get_virt_dir(self):
   """ return the project directory were pip-source store the virtual enviorment for project in the url """
  
   if "WORKON_HOME" in os.environ:
     return os.environ['WORKON_HOME'] / self.name / 'venv' 
  
   if "PIPENV_VENV_IN_PROJECT" in os.environ: 
     return os.environ["PIPENV_VENV_IN_PROJECT"] / self.name / 'venv' 
  
   return spip_root_path / (self.name) / 'venv'
  
  def get_source_dir(self):
     """ return the project directory were pip-source store the source code """
     return spip_root_path / (self.name) / 'src'
  
 

