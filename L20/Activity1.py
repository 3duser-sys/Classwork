from datetime import date, time, datetime

today = date.today()
now = datetime.now()
print("Todays date is,", today)
print("\n current date and time is", now)

print("\n Date components", today.year, today.month, today.day)