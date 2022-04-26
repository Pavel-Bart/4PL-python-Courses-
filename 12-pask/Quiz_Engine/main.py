from question import QuestionBank
from question import QuestionItem
from data import question_data
from login import Login

print(question_data)
formed_questions = []
for item in question_data:
    formed_questions.append(QuestionItem(category=item["category"], type=item["type"],
                                       difficulty=item["difficulty"], question=item["question"],
                                       correct_answer=item["correct_answer"],
                                       incorrect_answers=item["incorrect_answers"]))

question = QuestionBank(formed_questions)
login = Login()

is_on = True
user = None

while is_on:

    # while user is None:
    #     username = input("Login:")
    #     password = input("Password:")
    #     user = login.Check_log(username, password)

    choice = input(f"Start new quiz game?(Yes/No): ")

    if choice.capitalize() == "Yes":
        question.ask_check()
        question.score()
    else:
        is_on = False





