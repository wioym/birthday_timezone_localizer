import datetime
import pytz
from check_timezone_lib import check_timezone
import tzlocal

day = input('What was the day? (format: 07 or 20) \n')
month = input('What was the month of your bday? (format: 1 for January) \n')
year = input('What year were you born? (format: 2000)\n')
time = input("What was the time? (format: 14:20 or 07:30) \n")

while True: 
    country = input('''What was the country you were born in?\nCould specify the closest Major City and/or State\n''')
    country = check_timezone(country)
    if country != None:
        break
    else:
        print('Invalid input.')

country_timezone = pytz.timezone(country)
hour, minute = time.split(':')

birthday = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), 00, 00, country_timezone)

print(('You were born on: {}, {}, {} at {}:{} in {}').format(day, month, year, hour, minute, country))

current_timezone = tzlocal.get_localzone()
current_timezone = pytz.timezone(str(current_timezone))
local_birthday = birthday.astimezone(current_timezone)

print(("In your local timezone you were born on: {}, {}, {} at {}:{}").format(local_birthday.day, local_birthday.month, local_birthday.year, local_birthday.hour, local_birthday.minute))