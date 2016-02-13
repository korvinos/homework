# не решено


def checkio(data):
    a = 10
    rez = list(map(lambda x: data.remove(x), data))
    return rez

print(checkio([1, 2, 3]))