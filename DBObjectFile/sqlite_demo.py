from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
from SubjectInfoTable import SubjectInfoTable

DBConnection.db_file_path = "example.db"
DBInitializer().execute()

# StudentInfoTable().insert_a_student("Bill")
# StudentInfoTable().insert_a_student("John")
# StudentInfoTable().insert_a_student("Joe")
SubjectInfoTable().update_a_subject(2, "python", 70)



student_id = StudentInfoTable().select_a_student("Joe")
print("student_id: {}".format(student_id))

# StudentInfoTable().delete_a_student(student_id)
# StudentInfoTable().update_a_student("1", "Test")
