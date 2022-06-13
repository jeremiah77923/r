import pandas
class Word():
    def __init__(self):
        self.user_name =input("What is your name?\n")
        self.data = pandas.read_csv("nato_phonetic_alphabet.csv")
        self.user_word = input("Enter the sentence or word that you want to say in the NATO Phonetic alphabet?\n")
        self.og_string = self.user_word
        self.user_word = self.user_word.upper()
        self.user_word = [letter for letter in self.user_word]
        self.phonetic_words = []
    def greet(self, user_name):
        print(f"Welcome to the NATO Phonetic Alphabet calculator, {user_name}!\n")
    def is_val(self):
        try:
            phonetic_words = {row.letter: row.code for index, row in self.data.iterrows()}
            output = [phonetic_words[letter] for letter in self.user_word]
            print(f"Say {self.og_string} using the following words: \n{output}")
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
            return False

