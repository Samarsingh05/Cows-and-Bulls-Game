import random
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
def check_guess():
    global answer
    global bulls
    global cows
    global guess_count
    guess = guess_entry.get()
    if guess == answer:
        result_label.config(text="Congratulations! You guessed the number correctly.")
        guess_entry.config(state='disabled')
        submit_button.config(state='disabled')
    else:
        bulls = 0
        cows = 0
        for i in range(4):
            if guess[i] == answer[i]:
                bulls += 1
            elif guess[i] in answer:
                cows += 1
        result_label.config(text=f"{guess} => {bulls} bull(s) and {cows} cow(s).",bg='white')
        guess_count += 1
        previous_guesses.insert("", "end", text="", values=(guess, bulls, cows))
        if guess_count == 10:
            result_label.config(text=f"You have reached the maximum number of tries. The number was {answer}")
            guess_entry.config(state='disabled')
            submit_button.config(state='disabled')
            
def restart_game():
    global answer
    global guess_count
    answer = str(random.randint(1000, 9999))
    guess_count = 0
    previous_guesses.delete(*previous_guesses.get_children())
    guess_entry.config(state='normal')
    submit_button.config(state='normal')
    guess_entry.delete(0, 'end')
    result_label.config(text="")

# generate a random number with 4 digits import random
def generate_unique_number():
    digits = list(range(10))
    random.shuffle(digits)
    return "".join(map(str,digits[:4]))

answer = generate_unique_number()

def show_instructions():
    messagebox.showinfo("Instructions", "1. The computer will randomly generate a 4-digit number.\n2. You will enter your guess for the number.\n3. For each correct digit in the correct place, you get a bull.\n4. For each correct digit in the wrong place, you get a cow.\n5. You have 10 tries to guess the number.\n6. If you guess the number correctly, you win.\n7. If you reach 10 tries and haven't guessed the number, you lose.")

# create the main window
root = tk.Tk()
root.title("Cow and Bull Game")
root.configure(bg="white")

# create the widgets
guess_label = tk.Label(root, text="Enter your guess:")
guess_entry = tk.Entry(root)
submit_button = tk.Button(root, text="Submit", command=check_guess,bg='white')
result_label = tk.Label(root, text="")
previous_guesses = ttk.Treeview(root, columns=("Number", "Bulls", "Cows"), show="headings")
previous_guesses.heading("#0", text="Previous Guesses")
previous_guesses.heading("Number", text="Number")
previous_guesses.heading("Bulls", text="Bulls")
previous_guesses.heading("Cows", text="Cows")

play_again_button = tk.Button(root, text="Play Again", command=restart_game,bg='white')
play_again_button.grid(row=4,column=0,columnspan=2)
# add the widgets to the window
guess_label.grid(row=0, column=0)
guess_entry.grid(row=0, column=1)
submit_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label.grid(row=2, column=0, columnspan=2)
previous_guesses.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

instructions_button = tk.Button(root, text="Instructions", command=show_instructions, bg='white')
instructions_button.grid(row=5, column=0, columnspan=2)

black_frame = tk.Frame(root, bg="blue")






# set some variables
guess_count = 0
bulls = 0
cows = 0

# start the main loop

root.mainloop()
