from ClientObjectFile.AddStru import AddStru
from ClientObjectFile.PrintAll import PrintAll
from ClientObjectFile.DelStru import DelStru
from ClientObjectFile.ModifyStru import ModifyStru
from ClientObjectFile.SocketClient import SocketClient

host = "127.0.0.1"
port = 20001

action_list = {
        "add": AddStru,
        "show": PrintAll,
        "del": DelStru,
        "modify": ModifyStru,
    }
    
def print_menu():
    print ("======================")
    print("add: Add a student's name and score")
    print("del: Delete a student")
    print("modify:Modify a student's score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

    

if __name__ == '__main__':
    selection = "initial"
    client = SocketClient(host, port)

    while True:
        student_dict = dict()
        selection = print_menu()
        if selection == 'exit':
            client.send_command(selection, dict())
            break
        else:
            try:
                func = action_list[selection]()
                student_dict = func.execute(client)
            except Exception as e:
                print(e)
            if 'name' in student_dict.keys() or selection == 'show':
                client.send_command(selection, student_dict)
                result = client.wait_response()

                func.show_result(result)
        

        
