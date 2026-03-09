import socket


class Client():

    def __init__(self,username,ip):
        # set base variable
        self.username = username
        self.ip = ip
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_message(self,message,server_dest,server_port):

        # connect to server
        self.sock.connect((server_dest,server_port))

        # forge requested message 
        payload = {
            "username":self.ip,
            "ip":self.ip,
            "content":message
        }

        payload = str(payload)

        # send something
        packet = payload.encode("utf-8")
        self.sock.send(packet)

        # Close connection
        self.sock.close()