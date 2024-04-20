from ServerObjectFile.AddSrvStru import AddSrvStru
from ServerObjectFile.PrintAllSrvStru import PrintAllSrvStru
from ServerObjectFile.DelSrvStru import DelSrvStru
from ServerObjectFile.ModifySrvStru import ModifySrvStru
from ServerObjectFile.QuerySrvStru import QuerySrvStru
import json

class Parser():
    def __init__(self):
        self.srv_func = {
    "add": AddSrvStru,
    "show": PrintAllSrvStru,
    "del": DelSrvStru,
    "modify": ModifySrvStru
}
    def parser(self, message):
        keep_going = True
        if not message:
            keep_going = False
        message = json.loads(message)
        if message['command'] == "exit":
            reply_msg = 'closing'
            keep_going = False
        else:
            print(f'    The server recived data =>{message}')
            reply_msg = self.srv_func[message['command']]().execute(message['parameters'])
            print(f'    The server send adata =>{reply_msg}')

        return keep_going, reply_msg