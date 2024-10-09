import datetime

from django.core.exceptions import ValidationError

def validate_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        raise ValidationError('PESEL number must be 11 chars long')

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10)) % 10
    checksum = (10 - checksum) % 10

    if checksum != int(pesel[10]):
        raise ValidationError('PESEL number is not valid.')

    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900

    try:
        datetime.date(year, month, day)
    except ValueError:
        raise ValidationError('Date of birth is invalid.')