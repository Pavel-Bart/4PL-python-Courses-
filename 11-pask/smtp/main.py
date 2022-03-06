import smtplib

MY_EMAIL = "kazincorp@gmail.com"
PASSWORD = "x64aTo!coM50%"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="bart.alex2003@gmail.com",
        msg="Subject: this is subject\n\nHello from python"
    )














