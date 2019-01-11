
from commands import commands
import time
import os

sdir = os.path.dirname(os.path.realpath(__file__))
sdir = os.path.join(sdir,"tasks")

def execute_command():

    cmd = commands.get()
    if not cmd:
        return

    pyfile = str(time.time()) + ".py"
    pyfile = os.path.join(sdir,pyfile)
    fp = open(pyfile,"w")
    fp.write(cmd)
    fp.close()

    cmd = "/data/user/0/com.hipipal.qpyplus/files/bin/python-android5 %s" % pyfile
    print cmd
    os.system(cmd)


def execute():
    while True:
        time.sleep(1)
        try:
            execute_command()
        except Exception,err:
            print err


if __name__ == "__main__":
    execute()
