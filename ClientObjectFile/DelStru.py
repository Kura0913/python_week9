from ClientObjectFile.SocketClient import SocketClient

class DelStru():
    def __init__(self):
        self.stu_dict = {}

    def execute(self, client : SocketClient):
        stu_dict = self.stu_dict
        print("=============Del==============")
        name = input("Please input a student's name or exit:")
        if name != 'exit':
            client.name_query(name)
            query_result = client.wait_response()
            print(f"The client received data => {query_result}")
            if query_result['status'] == 'OK':# check if the student is on the list, if yes, execute modify func.
                sure_to_del = True if input("Confirm to delete (y/n):") == 'y' else False
                if sure_to_del:
                    stu_dict['name'] = name
            else:# The student is not in the list
                print(f"The name {name} is not found.")
                return stu_dict

        else:# name is exit
            return stu_dict


    def show_result(self, res):
        return