# GUI
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from random_word import RandomWords
from tkinter import font

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

# This is the background for all of the elements
color = '#34cfeb'

# This picks the word
raw_word = r.get_random_word(maxLength=10, hasDictionaryDef='true')
raw_word = raw_word.lower()

# Turns that randomly picked word into an array
word = list(raw_word)

# This is what the user will see, the line represents a blank spot
for x in range(len(raw_word)):
    user_guessed_word.append("一")


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
    Label(root, text=user_guessed_word, font=("Courier", 25, 'bold'), bg=color).pack(side='bottom')
    
    # This happens when the user wins
    if user_guessed_word == word:
        messagebox.showinfo("Nice", "You won")
        root.destroy()

root = Tk()
root.geometry('800x800')
root.title('Hangman')
root.config(bg=color)

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
                    messagebox.showinfo("Wrong", "your bad at guessing, try again")
                    x = user_input
                    Label(root, text=x, font=("Courier", 12), bg=color).pack(side='top')
                
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

# Getting user input
e = Entry(root, font=('default', 40))
e.pack(side='top')
e.focus_set()

# Clears the input after every time the button is clicked
def clear_text():
    global e
    e.delete(0, END)
    e.insert(0, "")

# This button takes the input
b = Button(root,text='OKAY', font=('default', 15), command=lambda:[check_len_user_input(), clear_text()], width=10, height=3, bg='#71f740')
b.pack()

# This shows the failed guesses
Label(root, text="Guesses", font=("Courier", 15, 'bold', 'underline'), bg=color).pack(side='top')

# This shows the blanks
Label(root, text=user_guessed_word, font=("Courier", 25, 'bold'), bg=color).pack(side='bottom')

# Runs the loop
root.mainloop()
