#!/bin/python3

from argparse import ArgumentParser
from socket import socket

EOT = b'\x04'


def read(filename: str):
    with open(filename) as file:
        return file.read()


if __name__ == '__main__':

    parser = ArgumentParser('client')
    parser.add_argument('--host', '-H', help='host to connect to (IP address or hostname)', type=str, default='localhost')
    parser.add_argument('--port', '-p', help='port to connect to on the host', type=int, default=3000)
    parser.add_argument('--text', '-t', help='text to send to the server', type=str)
    parser.add_argument('--file', '-f', help='file from which to send text', type=str)
    args = parser.parse_args()

    peer_addr = args.host, args.port

    assert not (args.text and args.file)

    if args.file:
        req = read(args.file)
    else:
        req = args.text or input('Enter some text: ')

    conn = socket()
    conn.connect(peer_addr)
    print(conn.getsockname() + conn.getpeername())
    conn.sendall(req.encode())
    conn.send(EOT)
    while res := conn.recv(1024).decode():
        print(res, end='')
