from datetime import datetime

print("Enter your NEXT b_date")
year = int(input("Year:"))
month = int(input("Month:"))
day = int(input("Day:"))

b_date = datetime(year,month,day)
now = datetime.now()

delta = b_date - now
print(delta.days)