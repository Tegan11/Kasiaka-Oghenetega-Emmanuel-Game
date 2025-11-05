import random
import tkinter as tk
from tkinter import messagebox

# simple rock,paper, scissors game using   tkinter
  # generated the ASCI art from    https://www.ascii-art-generator.org/
# BUILT BY KASIAKA OGHENETEGA EMMANUEL
 # ASCII art for Rock, Paper, Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''



scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


images = [rock, paper, scissors]

player_score = 0
com_score = 0

# Function to play the game
def play(player_choice):
    global player_score , com_score ,score_label

    com_choice = random.randint(0, 2)
    
    # Shows the choices
    player_label.config(text=f" You chose:\n{images[player_choice]}")

    com_label.config(text=f" Computer chose:\n{images[com_choice]}")
    
    # Determines the  winner
    if player_choice == com_choice:

        result_label.config(text=" It's a draw!", fg="#FFA500")

    elif (player_choice == 0 and com_choice == 2) or \
         (player_choice == 1 and com_choice == 0) or \
         (player_choice == 2 and com_choice == 1):
        player_score +=1
        result_label.config(text=" You win! 🎉", fg="green")
    else:
        com_score +=1
        result_label.config(text=" You lose 😢", fg="red")

    score_label.config(text=f'score - you: {player_score} computer:{com_score}')   

   




# this Creates the window
root = tk.Tk()
root.title(" Rock Paper Scissors")
root.geometry("800x750")
root.config(bg="#1E1E2F")
root.resizable(False, False)

# Header
header = tk.Label(

    root,
    text=" 🪨 Rock • 📄 Paper • ✂️ Scissors",
    font=("Helvetica", 20, "bold"),

    bg="#1E1E2F",
    fg="#00CED1",

)
header.pack(pady=20)

# Player and Computer choice labels
player_label = tk.Label(

    root, text="", font=(" Courier", 12), justify="left", bg="#1E1E2F", fg="#FFFFFF"
)
player_label.pack(pady=10)

com_label = tk.Label(

    root, text="", font=("Courier", 12), justify="left", bg="#1E1E2F", fg="#FFFFFF"
)
com_label.pack(pady=10)

# Result label
result_label = tk.Label(

    root, text="", font=("Helvetica", 18, "bold"), bg="#1E1E2F", fg="white"
)
result_label.pack(pady=30)
score_label = tk.Label(
     root,text="score -you :0 , computer:0 ",
     font =('Helvetica',14 ), bg = '#1E1E2F', fg ='white' )
     
score_label.pack(pady = 10)

# Frame for buttons
button_frame = tk.Frame(root, bg="#1E1E2F")
button_frame.pack(pady=20)

# this function creates and styles the buttons
def button_create( text, command, color):

    btn = tk.Button(

        button_frame,
        text=text,
        font=("Helvetica", 14, "bold"),
        bg=color,
        fg="white",
        activebackground="#333",
        width=10,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=command

    )
    
    # creates cool Hover effect for the buttons
    def on_enter(e): btn.config(bg="#555")
    def on_leave(e): btn.config(bg=color)
    
    btn.bind(" <Enter>", on_enter)
    btn.bind(" <Leave>", on_leave)
    return btn

# calls the button creation function to create The three Buttons 
rock_btn = button_create(" Rock", lambda: play(0), "#4CAF50")

paper_btn = button_create(" Paper", lambda: play(1), "#2196F3")

scissors_btn = button_create(" Scissors", lambda: play(2), "#E91E63")

rock_btn.grid( row=0, column=0, padx=15, pady=10)

paper_btn.grid(row=0, column=1, padx=15, pady=10)
scissors_btn.grid(  row=0,  column=2, padx=15, pady=10)

# Footer
footer = tk.Label(

    root,
    text="  Developed by kasiaka oghenetega Emmanuel 💻",
    font=("Helvetica", 10, "italic"),
    bg="#1E1E2F",
    fg="#888",
)
footer.pack(side="bottom", pady=10)

root.mainloop()
