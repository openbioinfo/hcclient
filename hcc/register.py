import requests
import json
import subprocess
import sys
import time

def load_command(ip,port=5001):

    """get commands from server

    """

    url = "http://%s:%s/register/" % (ip,port)
    pass


def load(ip,port):
    while True:
        time.sleep(2)
        load_command(ip)




