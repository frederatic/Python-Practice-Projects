# This script calculates the number of days between 2 dates

# calculates if current year is a leap year
def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


# number of days in the month
def daysInMonth(year, month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 31

# what the date for the next day is
def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

# check whether first date happens before the second date; important for birthdates
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

# calculate number of days between 2 dates
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


# test example
print(daysBetweenDates(1996, 5, 2, 2018, 4, 5))