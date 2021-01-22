import datetime

today = datetime.date.today()
print(today.day, today.month)

now = datetime.datetime.now()
print(now.day, now.month, now.hour, ':', now.minute)