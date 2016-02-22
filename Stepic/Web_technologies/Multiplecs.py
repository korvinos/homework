# Пример мультиплексирования TCP сервера на python из первого модуля курса по Web технологиям от mail.ru

readsocks, writesocks = [...], [...]  # сокеты
while True:
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    for sockobj in readables:
        data = sockobj.recv(512)
        if not data:
            sockobj.close()
            readsocks.remove(sockobj)
        else:
            print('\tgot', data, 'on', id(sockobj))
