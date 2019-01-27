
#coding=utf-8
__author__ = "D J.Kong"

from load_task import load_task
from execute_task import execute_task
from return_task import return_task

def hcc():
    taskid,cmd = load_task()
    status = execute_task(cmd)
    return_task(status,taskid)

while True:
    try:
        hcc()
    except Exception,err:
        print err
