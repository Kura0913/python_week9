from DBObjectFile.StudentInfoTable import StudentInfoTable
from DBObjectFile.SubjectInfoTable import SubjectInfoTable

class DelSrvStru():
    def __init__(self):
        pass

    def execute(self, parameters):
        reply_msg = {'status': ''}
        
        stu_id = StudentInfoTable().select_a_student(parameters['name'])

        SubjectInfoTable().delete_subjects(stu_id)
        StudentInfoTable().delete_a_student(stu_id)
        reply_msg['status'] = 'OK'

        return reply_msg