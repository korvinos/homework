def checkio(time_string):
    return list(map(lambda x: int(x), time_string.split(':')))

print(checkio("10:37:49"))
print(checkio("21:34:56"))
print(checkio("00:1:02"))
print(checkio("23:59:59"))