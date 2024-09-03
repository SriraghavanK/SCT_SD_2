import tkinter as tk
from tkinter import messagebox
import random
def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    guess_entry.delete(0, tk.END)
    feedback_label.config(text="Guess a number between 1 and 100!", fg="blue")
    guess_entry.config(state=tk.NORMAL)
    guess_button.config(state=tk.NORMAL)
    start_button.config(text="Restart Game")
def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1
        if guess < secret_number:
            feedback_label.config(text="Too low! Try again.", fg="red")
            animate_label("Too low! Try again.")
        elif guess > secret_number:
            feedback_label.config(text="Too high! Try again.", fg="red")
            animate_label("Too high! Try again.")
        else:
            feedback_label.config(text=f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.", fg="green")
            guess_entry.config(state=tk.DISABLED)
            guess_button.config(state=tk.DISABLED)
            animate_label("Congratulations!")
    except ValueError:
        feedback_label.config(text="Please enter a valid integer.", fg="orange")
def animate_label(message):
    """ Create a simple animation by changing label colors """
    colors = ["red", "blue", "green", "purple", "orange", "pink"]
    def animate(index=0):
        feedback_label.config(text=message, fg=colors[index % len(colors)])
        if message == "Congratulations!":
            root.after(200, animate, index + 1)
    animate()
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.configure(bg="#f0f8ff")  
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=20)
title_label = tk.Label(frame, text="Number Guessing Game", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#333")
title_label.pack(pady=10)
guess_entry = tk.Entry(frame, font=("Arial", 16), justify="center")
guess_entry.pack(pady=10)
feedback_label = tk.Label(frame, text="Click 'Start Game' to begin!", font=("Arial", 14), bg="#f0f8ff", fg="blue")
feedback_label.pack(pady=10)
start_button = tk.Button(frame, text="Start Game", font=("Arial", 14), command=start_game)
start_button.pack(pady=5)
guess_button = tk.Button(frame, text="Check Guess", font=("Arial", 14), command=check_guess)
guess_button.pack(pady=5)
guess_button.config(state=tk.DISABLED)
root.mainloop()
