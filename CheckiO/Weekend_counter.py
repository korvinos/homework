from datetime import date

def checkio(from_date, to_date):
    return from_date - to_date


print(checkio(date(2013, 9, 18), date(2013, 9, 23)))
print(checkio(date(2013, 1, 1), date(2013, 2, 1)))
print(checkio(date(2013, 2, 2), date(2013, 2, 3)))