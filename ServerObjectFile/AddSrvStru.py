from DBObjectFile.DBConnection import DBConnection
from DBObjectFile.DBInitializer import DBInitializer
from DBObjectFile.StudentInfoTable import StudentInfoTable
from DBObjectFile.SubjectInfoTable import SubjectInfoTable

class AddSrvStru():
    def __init__(self):
        pass

    def execute(self, parameters):
        DBConnection.db_file_path = "students_score_DB.db"
        DBInitializer().execute()

        stu_dict = {}
        reply_msg = {'status':''}

        StudentInfoTable().insert_a_student(parameters['name'])
        stu_id = StudentInfoTable().select_a_student(parameters['name'])
        for subject, score in parameters['scores'].items():
            SubjectInfoTable().insert_a_subject(stu_id, subject, score)

        reply_msg['status'] = "OK"
        
        return reply_msg