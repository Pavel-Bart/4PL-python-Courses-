from question import Question


question = Question()

is_on = True

while is_on:
    choice = input(f"Start new quiz?(Yes/No): ")

    if choice == "Yes":
        question.rand()
    else:
        is_on = False





