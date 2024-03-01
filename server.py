# coding:utf-8
import socket
import threading


# class thread to manage client
class ClientThread(threading.Thread):
    def __init__(self, connexion):
        threading.Thread.__init__(self)
        self.connexion = connexion

    def run(self):
        # server receive client data
        data = self.connexion.recv(1024)
        data = data.decode("utf-8")
        print(data)

        # response of server
        response = "\n\n HTTP/1.1 200 OK \nthis is the message of server"
        response = response.encode("utf-8")
        connexion.sendall(response)
# ---------------------------------


port = 8000
host, port = ("", port)

# instance of socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# link socket to address and port
socket_server.bind((host, port))
print("server is reading ....")

while True:
    # socket is listening
    socket_server.listen(10)
    # socket getting client
    connexion, add = socket_server.accept()
    print("\n new client connexion by address: ", add)

    # instance ClientThread class
    my_thread = ClientThread(connexion)
    my_thread.start()

# close the socket
connexion.close()
socket_server.close()
