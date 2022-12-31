#!/usr/bin/python3

import socket

servsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsoc.bind(("0.0.0.0", 1234))

# Basic Scoket Programming
def main():
    servsoc.listen()
    (clientsoc, (ip, port)) = servsoc.accept()
    clientsoc.send(b"\nPython Rocks...\n")
    data = clientsoc.recv(2048)
    print(data)


if __name__ == '__main__':
    main()
