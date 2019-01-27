import sys
import os
import subprocess

cdir = os.path.dirname(os.path.realpath(__file__))
sdir = os.path.join(cdir,"tasks")

def execute_task(taskid):
    """execute task as below...
    """
    os.chdir(sdir)
    cmd = "python %s.py" % taskid
    logfile = "%s.log" % taskid
    fp = open(logfile,"w")
    p = subprocess.Popen(cmd,shell=True,stdout=fp,stderr=fp)
    flag = p.wait()
    fp.close()
    log = open(logfile,"r").read()
    os.chdir(cdir)
    
    return flag,log

if __name__ == "__main__":
    print execute_task(sys.argv[1])
