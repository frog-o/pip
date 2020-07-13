import subprocess
import sys
import click
import os 
from pathlib import Path
from spip.cvs import gittool

from spip.conf.defaults import *

@click.command('go')
@click.argument('goto_project',required=False)
def exe(goto_project):
   """ go to the source directory (wait for input)"""
   project_dir = os.listdir(spip_root_path)
   
   index = 0
   goto_wich =0
   project_list = []
   if (goto_project == None):
       goto_project=" " 
   
   for project in project_dir:
      index += 1
      project_list.append(str(project))
      if (goto_project in project.strip()):
         goto_wich = index
      
   print(goto_wich)
   if (goto_wich == 0 ):
       print ("\n\nYou have install the following sources:\n")
       for project in project_list:
          print (str(project_list.index(project) )+")\t"+ project)
       goto_wich = input("\nWich one should i goto? :")
   print(goto_wich)


   
   os.chdir(str(spip_root_path) +"/" +project_list[int(goto_wich)] + "/src/")
   print("cd "+ str(spip_root_path) +"/" +project_list[int(goto_wich)] + "/src/")
