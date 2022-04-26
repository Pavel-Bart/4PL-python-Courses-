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


class QuestionBank:

    def __init__(self, formed_questions):
        self.questions = formed_questions
        print(formed_questions)
        self.points = 0
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

    def ask_check(self):
        """ Prints the questions and checks the answers, if corrects adds point """
        self.points = 0

        for item in self.questions:

            print(item.question[0].upper() + item.question[1:])
            answer = (input(f"Answer(True/False): "))

            if item.correct_answer == answer.capitalize():
                self.points += 1

    def score(self):
        """ Prints the score """
        print(f"Score: {self.points} from {len(self.questions)} are correct")



