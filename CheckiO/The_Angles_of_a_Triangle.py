from math import acos, degrees


def checkio(a, b, c):
    line = sorted([a, b, c])
    if line[2] - line[1] - line[0] == 0:
        return [0, 0, 0]

    try:
        alfa = round(degrees(acos((line[2]**2 - line[1]**2 - line[0]**2)/(-2 * line[1] * line[0]))))
        beta = round(degrees(acos((line[0]**2 - line[2]**2 - line[1]**2)/(-2 * line[2] * line[1]))))
        gamma = round(degrees(acos((line[1]**2 - line[0]**2 - line[2]**2)/(-2 * line[2] * line[0]))))
        return sorted([alfa, beta, gamma])
    except:
        return [0, 0, 0]


print(checkio(4, 4, 4))
print(checkio(3, 4, 5))
print(checkio(10, 20, 30))