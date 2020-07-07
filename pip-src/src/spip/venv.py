def create(env_name):
    """create a virtual enviorment if one dose not exsists"""
    if (not env_name.is_dir()):
       subprocess.check_call([sys.executable,"-mvenv" , str(env_name ) ])
       return true
    else: 
       print("already has dir '"+ str(env_name) + "` not creating") 



