name = "Vardenis"
surname = "Pavardenis"

print(f"{name.lower()} - {surname.upper()}")

# quote = f"\tHello. \n This is quote \nAuthor:  {name.capitalize()} {surname.capitalize()}"
quote = f""" Hello
This is quote.
Author: {name.capitalize()} {surname.capitalize()}\n\n"""
print(quote)

b_day_wish = """Cheers to you [NAME], for another trip around the sun!
Today is about you, [NAME]. I cant wait to celebrate you all day long!
My wish for you, [NAME], is that you get all of your birthday wishes this year!"""

wish = b_day_wish.replace("[NAME]", "Vardenis" )
print(wish)