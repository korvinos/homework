#  Пример TCP сервера на python из первого модуля курса по Web технологиям от mail.ru
#  Это эхо сервер - отвечает тем же, что и принимает
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))  # Данный сокет связываем с адресом
s.listen(10)  # Необходимо начать принимать сетевые соединения на данном адресе
# 10 - длина очереди
while True:
    conn, addr = s.accept()  # Метод accept возвращается когда установлено новое соединение
    # conn - сокет, addr - адрес клиента
    while True:
        data = conn.recv(1024)
        if not data:
            break
        if 'close' in data:
            conn.send(data)
            conn.close()
            break
        else: s.send(data)



def myreceive(sock, msglen):  # Как правильно читать данные из соткета

    msg = ''
    while len(msg) < msglen:
        chunk = sock.recv(msglen - len(msg))
        if chunk == '':
            raise RuntimeError("broken")
        msg = msg + chunk
    return msg


def mysend(sock, msg):  # Как правильно записывать данные в сокет
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("broken")
        totalsent = totalsent + sent

