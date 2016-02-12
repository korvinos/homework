def checkio(numbers_array):
    return sorted(numbers_array, key=lambda x: abs(x))

print(checkio((-20, -5, 10, 15)))