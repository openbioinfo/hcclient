import json
import os

sdir = os.path.dirname(os.path.realpath(__file__))
db = os.path.join(sdir,"commands.json")

class commands():

    @staticmethod
    def post(command):
        command_list = []
        try:
            command_list = json.loads(open(db).read())
        except Exception,err:
            print err
        command_list.append(command)
        fp = open(db,"w")
        fp.write(json.dumps(command_list))
        fp.close()
 
    @staticmethod
    def get():
        command_list = []
        try:
            command_list = json.loads(open(db).read()) 
        except Exception,err:
            print err
        cmd = ""
        if command_list :
            cmd = command_list[0] 
        command_list = command_list[1:]
        fp = open(db,"w") 
        fp.write(json.dumps(command_list)) 
        return cmd
