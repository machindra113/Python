#!/usr/bin/python3

#We create a client server socket where client sends some data
#to the server and the server returns back the same data to the
#client

#i.e client -> server then server sends the data back to client

import socket

def main():
    servsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servsocket.bind(("0.0.0.0", 1235))

    servsocket.listen()
    (clientsocket, (ip, port)) = servsocket.accept()

    while True:
            data = clientsocket.recv(2048)
            print(data)
            clientsocket.send(data)


if __name__ == '__main__':
    main()
