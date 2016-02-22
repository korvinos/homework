import socket
import time

timeout = 2.0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 2222))
s.listen(1)
while True:
    conn, addr = s.accept()
    conn.settimeout(timeout)
    try:
        data = conn.recv(1024)
        conn.send('ok')
    except socket.timeout:
        print('timeout')


import asyncore
import socket

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(1024)
        if data:
            self.send(data)
        if 'close' in data:
            self.close()



class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(10)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            handler = EchoHandler(sock)

while True:
    server = EchoServer('', 2222)
    server.handle_accept()
    asyncore.loop()