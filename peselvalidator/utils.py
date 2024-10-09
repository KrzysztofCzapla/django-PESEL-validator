import datetime


def get_info_from_pesel(pesel):
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900

    birth_date = datetime.date(year, month, day)
    gender = 'Male' if int(pesel[9]) % 2 == 1 else 'Female'

    return birth_date, gender