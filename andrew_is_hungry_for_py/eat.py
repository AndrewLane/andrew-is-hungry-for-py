from dateutil.parser import parse


def feedme(inputdate):
    datetime = parse(inputdate).date()
    day = datetime.day
    month = datetime.month

    if day == 31 and month == 10:
        return "Birthday Cake"

    if day == 1 and month == 11:
        return "Leftover Birthday Cake"

    if day == 14 and month == 11:
        return "Stale Birthday Cake"

    if day == 29 and month == 2:
        return "Leap Day Cake"

    return "Cake"
