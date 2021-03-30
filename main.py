# GUI
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter import font

# Imports the random word generator
from random_word import RandomWords

# Other imports 
import time
import random

# Variables that have to be declared on the global scope for functions
e = None
tmp = None
L = None
user_input = None
entries = []
guess = 0
x = None
r = RandomWords()
amount_of_guesses = 6
user_guessed_word = []
hangman= None

f = open('./hangman2/word_selection.txt').read().splitlines()

# This is the background for all of the elements
color = '#E69A8D'
button_color = '#5F4B8B'

# This picks the word
try:
    raw_word = r.get_random_word(maxLength=10, hasDictionaryDef='true')
except:
    raw_word = random.choice(f)

raw_word = raw_word.lower()

# Turns that randomly picked word into an array
word = list(raw_word)

# This is what the user will see, the line represents a blank spot
for x in range(len(raw_word)):
    user_guessed_word.append("一")




root = Tk()
root.geometry('800x800')
root.title('Hangman')
root.config(bg=color)
root.resizable(width=False, height=False)

# Getting user input
e = Entry(root, font=('default', 40))
e.pack()
e.focus_set()


b = Button(root,text='OKAY', font=('default', 15), command=lambda:[check_len_user_input(), clear_text()], width=10, height=3, bg=button_color, relief=RIDGE)
b.pack()

# This shows the blanks
Label(root, text=user_guessed_word, font=("Courier", 25, 'bold'), bg=color).pack(side='bottom')

# This is the frame for the guesses
guess_frame = Frame(root)
guess_frame.pack(side = RIGHT)
guess_frame.config(bg=color)

# Hangman frame
hangman_frame = Frame(root)
hangman_frame.pack(side= LEFT)
hangman_frame.config(bg=color)

def change_display_word():
    global L
    global user_guessed_word
    global user_input
    global word
    global x

    # This sees if the guessed letter repeats more than once in the word
    for x in range(len(word)):
        if word[x] == user_input:
            
            # This changes the known letters
            user_guessed_word.pop(x)
            user_guessed_word.insert(x, user_input)
    x += 1
    
    # This will add a new label with the updated known letters
    guess_frame.pack_forget()
    hangman_frame.pack_forget()
    Label(root, text=user_guessed_word, font=("Courier", 25, 'bold'), bg=color).pack(side='bottom')
    guess_frame.pack(side = RIGHT)
    hangman_frame.pack(side = LEFT)
    
    # This happens when the user wins
    if user_guessed_word == word:
        messagebox.showinfo("Nice", "You won")
        root.destroy()

# This is the starting point for the hangman
L = Label(hangman_frame, text="*", font=("Courier", 25, 'bold'), fg='black', bg=color)
L.pack(side= LEFT)


# This shows the failed guesses
guess_frame.pack(side = RIGHT)
Label(guess_frame, text="Guesses", font=("Courier", 20, 'bold', 'underline'), bg=color).pack()

def check_len_user_input():
    global guess
    global entries
    global user_guessed_word
    global e
    global tmp
    global user_input
    
    # This if gate makes sure that the input is less than 2 characters
    if guess <= amount_of_guesses:
        
        # tmp variable is to change around data types
        tmp = e.get() 
        tmp = str(tmp)
        if len(tmp) == 1:
            user_input = tmp
            
            # This gate makes sure that the letter hasn't already been guessed
            if (user_input in entries) == True:
                messagebox.showinfo("Alert", "Already guessed")
                
            # If the letter hasn't been guessed, then this will add that letter to the list of entries
            elif (user_input in entries) == False:
                entries.append(user_input)
                
                # If the letter that was guessed is not in the word, then it will increase the guess value
                if (user_input in word) == False:
                    guess += 1

                    # This runs the function that changes the hangman visual
                    hangman_visual()
                    x = user_input
                    Label(guess_frame, text=x, font=("Courier", 12), bg=color).pack(anchor='e', pady='1')

                    # Checks to make sure that the game hasn't been lost
                    if guess >= amount_of_guesses:
                        losing_var = "You lost :(\nThe word was: " + raw_word
                        messagebox.showinfo("You Lost", losing_var)
                        sys.exit()
                    else:
                        messagebox.showinfo("Wrong", "your bad at guessing, try again")

                    
                # If the letter is in the word, then it will change the word on the display acordingly.
                if (user_input in word) == True:
                    change_display_word()

        # This else gate will show when the input is not 1 character
        else:
            messagebox.showinfo("Alert", "No")

    # This happens when the user loses
    else:
        losing_var = "You lost :(\nThe word was: " + raw_word
        messagebox.showinfo("You Lost", losing_var)
        sys.exit()





# Clears the input after every time the button is clicked
def clear_text():
    global e
    e.delete(0, END)
    e.insert(0, "")


def hangman_visual():
    global hangman
    global guess
    global L

    # These if gates destroy the old label, and then replace it with the updated hangman figure
    if guess == 1:
        hangman_destroy()
        hangman = 'O'

        L = Label(hangman_frame, text=hangman, font=("Courier", 25, 'bold'), fg='black', bg=color)
        L.pack(side='left', pady=1)

    if guess == 2:
        hangman_destroy()
        hangman = 'O\n|'

        L = Label(hangman_frame, text=hangman, font=("Courier", 25, 'bold'), fg='black', bg=color)
        L.pack(side='left', pady=1)
    
    if guess == 3:
        hangman_destroy()
        hangman = ' O\n/|'

        L = Label(hangman_frame, text=hangman, font=("Courier", 25, 'bold'), fg='black', bg=color)
        L.pack(side='left', pady=1)
    
    if guess == 4:
        hangman_destroy()
        hangman = 'O\n/|\\'

        L = Label(hangman_frame, text=hangman, font=("Courier", 25, 'bold'), fg='black', bg=color)
        L.pack(side='left', pady=1)
    
    if guess == 5:
        hangman_destroy()
        hangman = 'O\n/|\\\n/'

        L = Label(hangman_frame, text=hangman, font=("Courier", 25, 'bold'), fg='black', bg=color)
        L.pack(side='left', pady=1)
    
    if guess == 6:
        hangman_destroy()
        hangman = 'O\n/|\\\n/\\'

        L = Label(hangman_frame, text=hangman, font=("Courier", 25, 'bold'), fg='black', bg=color)
        L.pack(side='left', pady=1)



# This function destroys the old hangman figure
def hangman_destroy():
    global L
    L.destroy()


# Runs the loop
root.mainloop()
