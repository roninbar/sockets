#!/bin/python3

import os
from argparse import ArgumentParser
from socket import socket
from time import sleep

EOT = b'\x04'


def read(sock: socket, bufsize: int = 1024):
    more = True
    while more:
        data = sock.recv(bufsize)
        yield data.removesuffix(EOT)
        more = not data.endswith(EOT)


if __name__ == '__main__':

    parser = ArgumentParser('server')
    parser.add_argument('--host', '-H', help='IP address or hostname to bind to', type=str, default='localhost')
    parser.add_argument('--port', '-p', help='port to bind to', type=int, default=os.getenv('PORT', 3000))
    args = parser.parse_args()

    local_addr = args.host, args.port

    lstn = socket()
    lstn.bind(local_addr)
    lstn.listen(1)
    while True:
        print(f'Listening on {lstn.getsockname()}...')
        conn, peer_addr = lstn.accept()
        print(f'Connected to {peer_addr}.')
        with conn:
            # raw_req = conn.recv(128)
            # while not raw_req.endswith(EOT):
            #     req = raw_req.decode()
            #     conn.sendall(req.upper().encode())
            #     raw_req = conn.recv(128)
            # else:
            #     req = raw_req.removesuffix(EOT).decode()
            #     conn.sendall(req.upper().encode())
            for data in read(conn, bufsize=32):
                sleep(1.0)
                conn.sendall(data.decode().upper().encode())
