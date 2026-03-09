import socket
import json 



class Server():

    def __init__(self,host,port):
        # configuration
        self.host = host
        self.port = port     

    def blind_server(self):
        # socket creation (IPv4, TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host,self.port))
            s.listen()

            # wait for a connection
            conn, addr = s.accept()
            while True:
                data = conn.recv(1024) 
                if not data:
                    break
                
                # get data
                data = data.decode('utf-8')
                return data
        