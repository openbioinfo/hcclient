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
        rd = json.loads(req.text)
        command = rd["content"]
        if command:
            commands.post(command)
    except Exception,e:
        print e


def load(ip,port):
    while True:
        time.sleep(2)
        load_command(ip)


if __name__ == "__main__":
    load("127.0.0.1",5001)
