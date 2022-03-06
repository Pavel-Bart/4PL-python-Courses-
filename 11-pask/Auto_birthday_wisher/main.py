from datetime import datetime
import locale
import smtplib
import random

PLACEHOLDER = "[NAME]"

with open("./names/names.txt") as name_file:
    names = name_file.readlines()

print(names)
now = datetime.now()

with open("./letters/letters.txt") as letter_file:
    letter_content = letter_file.read()

    for x in names:
        name_date = x.strip().split(" ") # removes white spaces and splits
        bName = name_date[0]
        bDate = datetime.strptime(name_date[1], '%b %d %Y')
        print(bDate.day)
        # if bDate ==
        new_letter = letter_content.replace(PLACEHOLDER, bName)


