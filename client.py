# coding:utf-8
import socket

port = 8000
host, port = ("localhost", port)

# instance of socket
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connect client to sever
    socket_client.connect((host, port))
    print("connexion has been established !!!!")

    # sending data to a server
    data = input(str("enter server message:"))
    data = data.encode("utf-8")
    socket_client.sendall(data)

    data = socket_client.recv(1024)
    data = data.decode("utf-8")
    print(data)


except ConnectionRefusedError as e:
    print(f"connection to server denied: {e}")
finally:
    socket_client.close()
