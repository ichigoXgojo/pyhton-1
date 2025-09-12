from datetime import date, datetime

today = date.today()
now = datetime.now()
print("Today's date is:", today)
print("n\Current date and time is:", now)

print("n\date components:", today.year, today.month, today.day)