def func(n, m):
    result = str(bin(n^m)).count('1')

    '''
    binary_n = str(bin(n))
    binary_m = str(bin(m))

    new_binary_m = new_binary_n = ''
    for i in range(len(binary_m)-1, 1, -1):
        new_binary_m += binary_m[i]
    for i in range(len(binary_n)-1, 1, -1):
        new_binary_n += binary_n[i]

    if len(new_binary_n) >= len(new_binary_m):
        num = len(new_binary_n)
    else:
        num = len(new_binary_m)

    for element in range(0, num):
        if num < 1
    return new_binary_m, new_binary_n
    '''
    return result

a = 117
b = 17

print(func(a, b))
print(bin(a))
print(bin(b))