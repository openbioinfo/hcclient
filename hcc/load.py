import requests
import json
import subprocess
import sys
import time
from commands import commands

def get_command(ip,port=5001):

    """get commands from server

    """
    url = "http://%s:%s/commands/" % (ip,port)
    req = requests.get(url)
    code = req.status_code
    rd = json.loads(req.text)
    command = rd["content"]
    commands.post(command)


if __name__ == "__main__":
    ip = sys.argv[1]
    for i in range(100):
        time.sleep(5)
        get_command(ip)




