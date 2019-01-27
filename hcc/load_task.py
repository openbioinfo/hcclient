import requests
import json
import os
macid = 123
server = "127.0.0.1:5000"
cdir = os.path.dirname(os.path.realpath(__file__))
sdir = os.path.join(cdir,"tasks")

mdir = "mkdir -p %s" % sdir
os.system(mdir)

def load_task():
    """load most recent task.
    """
    url = "http://{server}/api/v1/tasks/".format(server=server)
    params  = {"macid":macid,"status":0}
    req = requests.get(url,params=params)
    task_list = json.loads(req.text)
    if not task_list:
        return 

    task = task_list[0]
    taskid = task["taskid"]
    cmdid = task["commandid"]

    url = "http://{server}/api/v1/cmds/{cmdid}/".format(server=server,\
                                                        cmdid=cmdid)
    req = requests.get(url)
    rd  = json.loads(req.text)
    pycont = rd["content"]
    pyfile = os.path.join(sdir,"%s.py" % taskid )
    fp = open(pyfile,"w")
    fp.write(pycont)
    fp.close()
    return taskid,pyfile

if __name__ == "__main__":
    print load_task()

