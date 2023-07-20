from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from os import system
from score_range import calculate_score
question_bank = []


score = 0

for each_question in question_data:
    question_text = each_question["text"]
    question_answer = each_question["answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)


length_questions = len(question_bank)

score = 0
system("cls")
while length_questions > 0:
    answer = quiz_brain.next_question()

    if length_questions == 1:
        system("cls")
        calculate_score(score=score, total_score=len(question_bank))
        break
    if answer:
        score += 1
        print(f"Total score: {score}/{len(question_bank)}")
        print("Your answer is right.")
    else:
        print(f"Total score: {score}/{len(question_bank)}")
        print(f"Your answer is wrong.")

    length_questions -= 1
