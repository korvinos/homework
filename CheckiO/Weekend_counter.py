from datetime import date, timedelta

def checkio(from_date, to_date):
    delta = (to_date - from_date).days
    count = 0
    for day in [d for d in (from_date + timedelta(n) for n in range(delta + 1))]:
        if day.isoweekday() == 6 or day.isoweekday() == 7:
            count += 1
    return count

print(checkio(date(2013, 9, 18), date(2013, 9, 23)))
print(checkio(date(2013, 1, 1), date(2013, 2, 1)))
print(checkio(date(2013, 2, 2), date(2013, 2, 3)))