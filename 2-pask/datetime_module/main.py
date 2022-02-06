from datetime import datetime
import locale
# locale to change language
locale.setlocale(locale.LC_TIME, "lt_LT")

# now = datetime.now()
# current_year = now.year
# current_month= now.month
# current_day = now.day
# current_weekday = now.weekday()
# current_hour = now.hour
# current_minute = now.minute
# current_second = now.second
#
# print(f"Year: \t\t{current_year}")
# print(f"Month: \t\t{current_month}")
# print(f"Day: \t\t{current_day}")
# print(f"Hour: \t\t{current_hour}")
# print(f"Minute: \t{current_minute}")
# print(f"Second: \t{current_second}")

# print(f"Weekday: \t{current_weekday}\n\n")

# past = datetime(1990, 9, 20)
# print(past.weekday())

# future = datetime(2099, 12, 31)
# print(future.weekday())


now = datetime.now()

custom_date = f"Year: {now.strftime('%Y')} \n" \
              f"Month: {now.strftime('%B')}\n" \
              f"Weekday: {now.strftime('%A')}"

print(custom_date)