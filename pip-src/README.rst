pip-src -  Pip source code installer
===============================================


pip-src tries to make your life easy by doing a lot of things for you it does the following.

1.) clone the reposiory for you and put all sourcecode in ~/pip-source/src/program-name(from the git url program-name.git)
2.) create a virtual enviorment in  ~/virtualenvs/program-name (simmilar to pipx)
3.) add your fork of the repository to the list of remotes. (It names it mypipfork)
4.) install you program in the virtual env 
5.) automaticaly stash git changes and update the source on programe run every n hours. 

An example session
==========================

Let say your are work on pip source code one aproach to this proccess would be
 

1.) clone 

git clone  https://github.com/pypa/pip.git

2.) create a virtual enviorment to install into so it won't mess up the system pip 

python3 -m venv pip

3.) git remote add mypipfork https://github.com/username/pip.git


now let say you create your branch and done some work some days latter a want to run

git pull --rebase origin master

To make sure your work with the current source but your not ready to commit you changes so you run

git stash
git pull --rebase origin master
git stash apply


you test you devolment version of pip with 

python src/pip 

You work slowly so you have to run these command frequenlty would it be nice not to have to 
just run 

python src/pip

and have it update your source on start up or better yet when you type 

pip

on the command line but just with a prefix such a d for devolpment so all you 
have to do is type

dpip 


now you can with (pip-src) spip

with one command 

spip insall https://github.com/pypa/pip.git

It does all above(execept for fork pip and create your devloment branch) now you can work on your pip code and not worry 
about keeping it uptodate and working with old code. 

Every time you run dpip to test your code it check to see when it was updated an update it if need be.       


 

