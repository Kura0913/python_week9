from ClientObjectFile.SocketClient import SocketClient

class PrintAll():
    def __init__(self):
        self.stu_dict = dict()


    def execute(self, client : SocketClient):
        return self.stu_dict        
    
    def show_result(self, res):
        stu_dict = self.stu_dict
        if res["status"] == "OK":
            stu_dict = res['parameters']
            print ("\n==== student list ====\n")
            for name in stu_dict.keys():
                print(f"Name: {stu_dict[name]['name']}")
                for subject, score in stu_dict[name]['score'].items():
                    print(f"  subject: {subject}, score: {score}")    
            print ("======================")
        else:
            print('Get students list failed!')
        return