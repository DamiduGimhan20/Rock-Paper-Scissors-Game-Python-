import tkinter as tk
import random

# initialize the score variables
user_score = 0
computer_score = 0

def rock():
    global user_choice
    user_choice = "rock"
    computer_choice_func()

def paper():
    global user_choice
    user_choice = "paper"
    computer_choice_func()

def scissors():
    global user_choice
    user_choice = "scissors"
    computer_choice_func()

def computer_choice_func():
    global computer_choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    determine_winner()
    display_computer_choice()
    update_scores()

def determine_winner():
    global user_choice, computer_choice, label, user_score, computer_score
    if user_choice == computer_choice:
        message = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        message = "You win! 🏆🏆🏆🏆"
        user_score += 1
    else:
        message = "You lose!😭😭😭😭"
        computer_score += 1
    label.config(text=message)
    update_scores()

def display_computer_choice():
    global computer_img
    if computer_choice == "rock":
        computer_img = tk.PhotoImage(file="rock.png")
    elif computer_choice == "paper":
        computer_img = tk.PhotoImage(file="paper.png")
    else:
        computer_img = tk.PhotoImage(file="scissors.png")
    
    computer_button = tk.Button(img_frame, image=computer_img, compound="center", borderwidth=3, relief="solid", padx=20, pady=20)
    computer_button.grid(row=1, column=3, padx=(20, 20), pady=(10, 10))

def update_scores():
    global user_score_label, computer_score_label
    user_score_label.config(text=f"Your score: {user_score}")
    computer_score_label.config(text=f"Computer score: {computer_score}")

main_window = tk.Tk()
main_window.title("✨🎮 Rock, Paper, Scissors Game 🎮✨")

# create a frame for the images and labels using grid
img_frame = tk.Frame(main_window)
img_frame.grid(row=0, column=0, padx=20, pady=20)

# create the user and computer choice labels
user_label = tk.Label(img_frame, text=" 🧒 User Choice 🧒", font=("Helvetica", 14), anchor="center")
user_label.grid(row=0, column=1, padx=(0, 20))

computer_label = tk.Label(img_frame, text=" 💻Computer Choice💻 ", font=("Helvetica", 14), anchor="center")
computer_label.grid(row=0, column=3, padx=(20, 20), pady=(10,10))

# horizontal separator line
separator_horizontal = tk.Frame(main_window, height=5, bd=5, relief="sunken")
separator_horizontal.grid(row=1, column=0, columnspan=3, sticky="ew", padx=20, pady=(10, 20))

# create a frame for the result label and scores using grid
result_frame = tk.Frame(main_window)
result_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=(0, 20))

# create the final result label
label = tk.Label(result_frame, text="", font=("Helvetica", 14), anchor="center")
label.grid(row=0, column=0, columnspan=2, sticky="ew")

# create the user and computer score labels
user_score_label = tk.Label(result_frame, text="Your score: 0", font=("Helvetica", 14), anchor="center")
user_score_label.grid(row=1, column=0, padx=(20, 0), pady=(20,10))

computer_score_label = tk.Label(result_frame, text="Computer score: 0", font=("Helvetica", 14), anchor="center")
computer_score_label.grid(row=1, column=1, padx=(0, 20), pady=(20,10))

# add images for each choice
rock_img = tk.PhotoImage(file="rock.png", width=200, height=200)
rock_button = tk.Button(img_frame, image=rock_img, text="", command=rock, compound="center", borderwidth=0, relief="solid", padx=20, pady=20)
rock_button.grid(row=1, column=0, padx=(15, 20), pady=(20, 10))

paper_img = tk.PhotoImage(file="paper.png", width=200, height=200)
paper_button = tk.Button(img_frame, image=paper_img, text="", command=paper, compound="center", borderwidth=0, relief="solid", padx=20, pady=20)
paper_button.grid(row=1, column=1, padx=(15, 20), pady=(20, 10))

scissors_img = tk.PhotoImage(file="scissors.png", width=200, height=200)
scissors_button = tk.Button(img_frame, image=scissors_img, text="", command=scissors, compound="center", borderwidth=0, relief="solid", padx=20, pady=20)
scissors_button.grid(row=1, column=2, padx=(15, 20), pady=(20, 10))

main_window.mainloop()
