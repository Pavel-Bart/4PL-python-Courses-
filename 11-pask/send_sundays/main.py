from datetime import datetime
import locale
import smtplib
import random
# locale.setlocale(locale.LC_TIME, "lt_LT")


MY_EMAIL = "kazincorp@gmail.com"
PASSWORD = ""

# num = random.randint(0, 9)
now = datetime.now()

if now.strftime('%A') == "Sunday":
    with open("data.txt") as file:
        quotes = file.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="bart.alex2003@gmail.com",
            msg=f"Subject: quote\n\n{random.choice(quotes)}"
        )

