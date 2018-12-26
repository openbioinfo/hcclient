
from commands import commands
import time



def execute():
    

    cmd = commands.get()
    exec(cmd)


if __name__ == "__main__":

    for i in range(10):
        time.sleep(5)
        execute()



