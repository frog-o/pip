import os
from spip.conf.defaults import *


def get_virt_dir(url):
   """ return the project directory were pip-source store the virtual enviorment for project in the url """
   if "WORKON_HOME" in os.enviorment
     return os.environ['WORKON_HOME'] / get_project_name() + "-env" 
   if "PIPENV_VENV_IN_PROJECT" in os.enviorment 
     return os.environ["PIPENV_VENV_IN_PROJECT"] / get_project_name() + "-env")
   return spip_root_path / get_project_name() + "-env") 



