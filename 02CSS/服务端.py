#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/11/8 14:35'
__author__ = 'likunkun'

import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8'))
    # client.send(bytes("Hello, Seven",encoding='utf-8'))
    client.send(bytes("<h1 style='background-color:red;'>Hello, Seven<h1>",encoding='utf-8'))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()