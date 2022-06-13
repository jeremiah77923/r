class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.ans = ""
        self.score = 0
        self.question_count = 0
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.question_count += 1
        self.ans = input(f"Question {self.question_number}: {current_question.text}\n"
                         f"type \"True\" if you think the question is True or \"False\" if you think the question is "
                         f"False. "
                         f"\nEnter \"True\" or \"False\"\n").upper()
        if self.still_has_questions():
            self.check_answer()
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    def calc_percent(self):
        return f"You got {self.score} questions right out {self.question_count} total questions \nYour final score is {int(self.score/len(self.question_list)*100)}%"
    def check_answer(self):
        if self.ans == self.question_list[self.question_number].answer.upper():
            self.score += 1
            print("You got it right!!!!!")
            print(f"The correct answer was {self.question_list[self.question_number].answer}.")
            print(f"Your current score is: {self.score}/{self.question_count}.")
        elif self.ans != self.question_list[self.question_number].answer.upper():
            print("You got it wrong!!!!!")
            print(f"The correct answer was {self.question_list[self.question_number].answer}.")
            print(f"Your current score is: {self.score}/{self.question_count}.")
