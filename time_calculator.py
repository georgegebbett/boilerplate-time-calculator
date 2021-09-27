import re

daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def add_time(start, duration, dayOfWeek=None):
    print(start, duration, dayOfWeek)

    startHour = re.search('^(\d{1,2})', start).group()
    startMinute = re.search(':(\d{1,2})', start).group(1)
    startDayPart = re.search('(AM)|(PM)', start).group()
    durationHour = re.search('^(\d+)', duration).group()
    durationMinute = re.search(':(\d{1,2})', duration).group(1)

    if startDayPart == 'PM':
        startHour = int(startHour) + 12


    finishMinute = int(startMinute) + int(durationMinute)
    finishHour = int(startHour) + int(durationHour)
    dayIncrement = 0

    if finishMinute > 59:
        finishHour = finishHour + 1
        finishMinute = finishMinute - 60

    if finishHour > 23:
        dayIncrement = int(finishHour / 24)
        finishHour = finishHour % 24

    if finishHour > 11:
        finishDayPart = 'PM'
        finishHour = finishHour - 12
    else:
        finishDayPart = 'AM'

    if finishHour == 0:
        finishHour = 12


    if dayOfWeek == None:
        if dayIncrement == 0:
            finishDay = ''
        elif dayIncrement == 1:
            finishDay = ' (next day)'
        else:
            finishDay = ' (' + str(dayIncrement) + ' days later)'
    else:
        dayOfWeek = dayOfWeek[0].upper() + dayOfWeek[1:].lower()
        if dayIncrement == 0:
            finishDay = ', ' + dayOfWeek
        elif dayIncrement == 1:
            finishDay = ', ' + daysOfWeek[daysOfWeek.index(dayOfWeek)+1] + ' (next day)'
        else:
            finishDay = ', ' + daysOfWeek[(daysOfWeek.index(dayOfWeek) + dayIncrement) % 7] + ' (' + str(dayIncrement) + ' days later)'

    finishString = (
        str(str(finishHour) + ':' + str(finishMinute).rjust(2, '0') + ' ' + finishDayPart + finishDay))
    print(finishString)

    return finishString
