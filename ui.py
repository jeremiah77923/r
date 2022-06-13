THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface():
    def __init__(self, text, quiz_brain: QuizBrain):
        self.text = text
        self.quiz = quiz_brain
        self.new_text = ""
        self.canvas_text = ""
        self.window = Tk()
        self.window.title("Trivia")
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, width=200, text=self.text, font=20)
        self.canvas.grid(row=0, column=0, pady=50)
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.false_img = PhotoImage(file="./images/false.png")
        self.true_img = PhotoImage(file="./images/true.png")
        self.button = Button(image=self.true_img, command=self.check)
        self.button.grid(row=2, column=0, sticky=W)
        self.button1 = Button(image=self.false_img, command=self.x)
        self.button1.grid(row=2, column=0, sticky=E)
        self.user_ans = ""
        self.next_question()
        self.is_right = False
        self.score_lab = Label(text=f"Score: {int(self.quiz.score/len(self.quiz.question_list)*100)}%", highlightthickness=0, fg="white", bg=THEME_COLOR, font=50)
        self.score_lab.grid(row=0, column=1, sticky=N)
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())
        if self.quiz.still_has_questions() == False:
            self.button.config(state="disabled")
            self.button1.config(state="disabled")
            self.canvas.config(bg=THEME_COLOR)
            self.score_lab.config( text=f"You finished the quiz, \n Percent Score: {int(self.quiz.score/len(self.quiz.question_list)*100)}%\n{self.quiz.score} questions correct out of {len(self.quiz.question_list)} questions.",fg = "white")
            self.score_lab.grid(row = 0, column = 0, sticky = S)
            self.canvas.itemconfig(self.canvas_text,text="")

    def check(self):
        self.user_ans = "True"
        self.give_feedback(self.quiz.check_answer("True"))

    def x(self):
        self.user_ans = "False"
        self.is_right = self.quiz.check_answer("False")
        self.give_feedback(self.is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.score_lab.config(text=f"Score: {int(self.quiz.score/len(self.quiz.question_list)*100)}%")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.next_question)
