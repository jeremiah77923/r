from question_model import Question
from Data import question_data
from quiz_brain import QuizBrain
import time

question_bank = []
quiz = QuizBrain(question_bank=question_bank)

for dict in question_data:
    new_question = Question(text=dict['text'], answer=dict['answer'])
    question_bank.append(new_question)

while quiz.still_has_questions():
    quiz.next_question()
    print("")
print("The quiz is finished now. ")
print(quiz.calc_percent())
