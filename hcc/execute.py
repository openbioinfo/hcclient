
from commands import commands
import time
import os


def execute_command():

    cmd = commands.get()
    if not cmd:
        return

    pyfile = str(time.time()) + ".py"
    pyfile = os.path.join("tasks",pyfile)
    fp = open(pyfile,"w")
    fp.write(cmd)
    fp.close()

    cmd = "python %s" % pyfile
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
