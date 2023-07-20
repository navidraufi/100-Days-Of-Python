class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list
        current_question_answer = self.question_list[self.question_number].answer.lower()
        user_answer = input(f"Q.{self.question_number + 1}: {current_question[self.question_number].question} ('True' or 'False')? ").lower()

        self.question_number += 1

        if current_question_answer == user_answer:
            return True
        else:
            return False



