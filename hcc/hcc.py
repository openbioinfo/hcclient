
#coding=utf-8
__author__ = "D J.Kong"

from load_task import load_task
from execute_task import execute_task
from return_task import return_task
import time

def hcc():
    taskid,cmd = load_task()
    if not taskid: return 
    status,log = execute_task(taskid)
    return_task(taskid,status,log)

if __name__ == "__main__":
    while True:
        time.sleep(2)
        try:
            hcc()
        except Exception,err:
            print err
