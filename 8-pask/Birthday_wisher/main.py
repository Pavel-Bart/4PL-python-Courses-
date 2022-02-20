PLACEHOLDER = "[NAME]"

with open("./names/names.txt") as name_file:
    names = name_file.readlines()

# print(names)

with open("./letters/letters.txt") as letter_file:
    letter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip() # removes white spaces
        # print(stripped_name)
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        with open(f"./output/letter-{stripped_name.lower()}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
