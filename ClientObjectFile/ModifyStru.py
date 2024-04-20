from ClientObjectFile.SocketClient import SocketClient

class ModifyStru():
    def __init__(self):
        self.stu_dict = {}

    def execute(self, client : SocketClient):
        stu_dict = self.stu_dict
        print("=============Modify==============")
        name = input("Please input a student's name or exit:")
        if name != 'exit':
            client.name_query(name)
            query_result = client.wait_response()
            if query_result['status'] == 'OK':# check if the student is on the list, if yes, execute modify func.
                print('Current subjects are:')
                for subject, _ in query_result['score'].items():# print the student's subject in list
                    print(subject)
                stu_dict['name'] = name
                stu_dict['score'] = dict()
                score = -1
                while True:
                    subject, score = input_subject(name)
                    if subject == 'exit':
                        return stu_dict
                    else:
                        if score < 0:
                            continue
                        else:
                            # add to dict
                            stu_dict['score'][subject] = score
            else:# The student is not in the list
                print(f"The name {name} is not found.")
                return stu_dict
        
        else:# name is exit
            return stu_dict

    def show_result(self, res):
        return
    
def input_score(name, subject):
    try:
        score = input(f"Please input {name}'s {subject} score or < 0 for discarding the subject:")

        return float(score)
    except:
        print(f"Wrong format with reason could not convert string to float: {score}, try again")

        return input_score(name, subject)

def input_subject(name):
    subject = input('Please input a subject name or exit for ending:')
    if subject != 'exit':
        score = input_score(name, subject)

        return subject, score
    else:
        return subject, -1