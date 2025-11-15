import tkinter as tk
from tkinter import messagebox
from random import randint

# --------------------
# Game Logic
# --------------------
class NumberGuesser:
    def __init__(self):
        self.answer = randint(1, 100)
        self.turns = 10  # default

    def set_difficulty(self, level):
        if level == "easy":
            self.turns = 10
        else:
            self.turns = 5

    def check(self, guess):
        if guess > self.answer:
            return "Too high!"
        elif guess < self.answer:
            return "Too low!"
        else:
            return "correct"


# --------------------
# UI Setup
# --------------------
game = NumberGuesser()

root = tk.Tk()
root.title("Number Guesser")
root.geometry("400x420")
root.config(bg="black")

title = tk.Label(root, text="NUMBER GUESSER", fg="white", bg="black",
                 font=("Arial", 20, "bold"))
title.pack(pady=10)

instructions = tk.Label(root, text="Guess a number between 1 and 100",
                        fg="white", bg="black", font=("Arial", 12))
instructions.pack()

difficulty_frame = tk.Frame(root, bg="black")
difficulty_frame.pack(pady=10)

def set_easy():
    game.set_difficulty("easy")
    messagebox.showinfo("Difficulty", "Easy mode selected (10 attempts).")

def set_hard():
    game.set_difficulty("hard")
    messagebox.showinfo("Difficulty", "Hard mode selected (5 attempts).")

easy_btn = tk.Button(difficulty_frame, text="Easy", width=10,
                     command=set_easy, bg="#4CAF50", fg="white")
easy_btn.grid(row=0, column=0, padx=5)

hard_btn = tk.Button(difficulty_frame, text="Hard", width=10,
                     command=set_hard, bg="#E53935", fg="white")
hard_btn.grid(row=0, column=1, padx=5)

attempts_label = tk.Label(root, text=f"Attempts Remaining: {game.turns}",
                          fg="white", bg="black", font=("Arial", 12))
attempts_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Arial", 16), width=10, justify="center")
guess_entry.pack(pady=10)

feedback_label = tk.Label(root, text="", fg="yellow",
                          bg="black", font=("Arial", 14))
feedback_label.pack(pady=10)

def make_guess():
    try:
        guess = int(guess_entry.get())
    except:
        messagebox.showwarning("Invalid", "ENTER A NUMBER!")
        return
    
    result = game.check(guess)

    if result == "correct":
        feedback_label.config(text=f"You got it! The answer was {game.answer}.")
        messagebox.showinfo("Winner!", f"You won! The answer was {game.answer}.")
        root.destroy()
    else:
        game.turns -= 1
        attempts_label.config(text=f"Attempts Remaining: {game.turns}")
        feedback_label.config(text=result)

        if game.turns == 0:
            messagebox.showinfo("Game Over", f"You lost!\nThe answer was {game.answer}.")
            root.destroy()

guess_button = tk.Button(root, text="Guess", width=10,
                         command=make_guess, bg="#2196F3", fg="white")
guess_button.pack(pady=10)

exit_button = tk.Button(root, text="Quit", width=10,
                        command=root.destroy, bg="gray", fg="white")
exit_button.pack(pady=10)

root.mainloop()
