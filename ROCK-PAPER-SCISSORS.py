#rock,paper,scissor game

import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors Game")

        self.user_choice = ""
        self.computer_choice = ""

        self.label = tk.Label(self.master, text="Choose rock, paper, or scissors:")
        self.label.pack()

        self.rock_button = tk.Button(self.master, text="Rock", command=lambda: self.make_choice("rock"))
        self.rock_button.pack()

        self.paper_button = tk.Button(self.master, text="Paper", command=lambda: self.make_choice("paper"))
        self.paper_button.pack()

        self.scissors_button = tk.Button(self.master, text="Scissors", command=lambda: self.make_choice("scissors"))
        self.scissors_button.pack()

    def make_choice(self, choice):
        self.user_choice = choice
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])
        self.display_result()

    def display_result(self):
        result = self.determine_winner()
        messagebox.showinfo("Result", result)

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return "It's a tie!"
        elif (self.user_choice == 'rock' and self.computer_choice == 'scissors') or \
             (self.user_choice == 'paper' and self.computer_choice == 'rock') or \
             (self.user_choice == 'scissors' and self.computer_choice == 'paper'):
            return "You win!"
        else:
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
