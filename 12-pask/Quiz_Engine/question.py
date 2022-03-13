from data import question_data


class QuestionItem:
    """ Models each question Item """

    def __init__(self, category, type, difficulty, question, correct_answer, incorrect_answers):
            self.category = category
            self.type = type
            self.difficulty = difficulty
            self.question = question
            self.correct_answer = correct_answer
            self.incorrect_answers = incorrect_answers


class Question:

    def __init__(self):
        self.questions = []
        for item in question_data:
            self.questions.append(QuestionItem(category=item["category"], type=item["type"],
                                               difficulty=item["difficulty"], question=item["question"],
                                               correct_answer=item["correct_answer"],
                                               incorrect_answers=item["incorrect_answers"]))



        # self.questions = [
        #
        #     QuestionItem(category="Science: Computers",type="boolean",difficulty="medium",
        #                  question="The HTML5 standard was published in 2014.",correct_answer="True",incorrect_answers=["False"]),
        #     QuestionItem(category="Science: Computers", type="boolean", difficulty="medium",
        #                  question="The HTML5 standard was published in 2014.", correct_answer="True",
        #                  incorrect_answers=["False"]),
        #     QuestionItem(category="Science: Computers", type="boolean", difficulty="medium",
        #                  question="The HTML5 standard was published in 2014.", correct_answer="True",
        #                  incorrect_answers=["False"])
        #]

    def ask_questions(self):
        for item in self.questions:
            print(item.question)
            answer = (input(f"Answer(True/False): "))

    def rand(self):
        for item in self.questions:
            print(f"{item.question}\n")


