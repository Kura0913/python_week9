from ServerObjectFile.SocketServer import SocketServer
from DBObjectFile.DBConnection import DBConnection
from DBObjectFile.DBInitializer import DBInitializer

host = "127.0.0.1"
port = 20001

def main():
    DBConnection.db_file_path = "students_score_DB.db"
    DBInitializer().execute()
    server = SocketServer(host, port)
    server.daemon = True
    server.serve()

    # because we set daemon is true, so the main thread has to keep alive
    print(f'Server start...')
    print('====================')
    while True:
        command = input()
        if command == "finish":
            break
    
    server.server_socket.close()
    print("leaving ....... ")

if __name__ == '__main__':
    main()