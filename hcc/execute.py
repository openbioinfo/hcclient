
from commands import commands
import time



def execute_command():

    cmd = commands.get()
    exec(cmd)


def execute():
    while True:
        execute_command()

