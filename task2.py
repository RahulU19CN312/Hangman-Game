import random


class Hangman:
    def __init__(self, words):
        self.words = words
        self.max_attempts = 6
        self.selected_word = random.choice(words).upper()
        self.display_word = ['_'] * len(self.selected_word)
        self.guessed_letters = []
        self.remaining_attempts = self.max_attempts

    def display(self):
        print(" ".join(self.display_word))
        print(f"Attempts left: {self.remaining_attempts}")
        print("Guessed letters:", ", ".join(self.guessed_letters))

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            print("You've already guessed that letter.")
            return

        self.guessed_letters.append(letter)
        if letter in self.selected_word:
            for i in range(len(self.selected_word)):
                if self.selected_word[i] == letter:
                    self.display_word[i] = letter
            print("Correct guess!")
        else:
            self.remaining_attempts -= 1
            print("Incorrect guess!")

    def is_game_over(self):
        if "_" not in self.display_word:
            print("Congratulations! You guessed the word:", "".join(self.display_word))
            return True
        elif self.remaining_attempts <= 0:
            print("Game over! The word was:", self.selected_word)
            return True
        return False


words = []
for i in range(5):
    n = input(f"Enter the {i + 1}/5 words for guessing : ")
    words.append(n)

game = Hangman(words)

while not game.is_game_over():
    game.display()
    guess = input("Guess a letter: ")
    game.guess(guess)
