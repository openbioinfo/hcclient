#coding=utf-8

import requests
import json
macid = 123
server = "127.0.0.1:5000"

def return_task(taskid,flag,log=None):
    """update task status...
    """
    url = "http://{server}/api/v1/tasks/{taskid}/".format(server=server,\
                                                          taskid=taskid )
    data = {"status": flag,"detail":log }
    req = requests.put(url,data=json.dumps(data))
    print req.text

if __name__ == "__main__": 
    import sys
    return_task(sys.argv[1],0)

