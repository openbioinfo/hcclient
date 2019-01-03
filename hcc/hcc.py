
from execute import execute 
from load import load
from threading import Thread
import signal
import sys
import time


def myHandler(signum, frame):
    sys.exit()

signal.signal(signal.SIGINT, myHandler)

def main(ip,port):

    t1 = Thread(target=load,args=(ip,port))
    t2 = Thread(target=execute,args=())
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()

    while True:
        time.sleep(10)
        f1 = t1.isAlive()
        f2 =  t2.isAlive
        if not f1:
            break
        if not f2:
            break

if __name__ == "__main__":
    main("127.0.0.1",5001)

