import tkinter
import random
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import time
from random_word import RandomWords
from tkinter import font
e = None
tmp = None
L = None
user_input = None
entries = []
guess = 0
x = None
r = RandomWords()
amount_of_guesses = 13

user_guessed_word = []

color = '#34cfeb'


raw_word = r.get_random_word(maxLength=10, hasDictionaryDef='true')
raw_word = raw_word.lower()



word = list(raw_word)




for x in range(len(raw_word)):
    user_guessed_word.append("一")

def change_display_word():
    global L
    global user_guessed_word
    global user_input
    global word
    global x

    for x in range(len(word)):
        if word[x] == user_input:
            user_guessed_word.pop(x)
            user_guessed_word.insert(x, user_input)
    x += 1
    Label(root, text=user_guessed_word, font=("Courier", 25, 'bold'), bg=color).pack(side='bottom')
    if user_guessed_word == word:
        messagebox.showinfo("Nice", "You won")
        root.destroy()

root = Tk()
root.geometry('800x800')
root.title('Hangman')
root.config(bg='#34cfeb')

def check_len_user_input():
    global guess
    global entries
    global user_guessed_word
    global e
    global tmp
    global user_input

    if guess <= amount_of_guesses:
        tmp = e.get() 
        tmp = str(tmp)
        if len(tmp) == 1:
            user_input = tmp
            if (user_input in entries) == True:
                messagebox.showinfo("Alert", "Already guessed")
            elif (user_input in entries) == False:
                entries.append(user_input)
                if (user_input in word) == False:
                    guess += 1
                    messagebox.showinfo("Wrong", "your bad at guessing, try again")
                    x = user_input
                    Label(root, text=x, font=("Courier", 12), bg=color).pack(side='top')
                if (user_input in word) == True:
                    change_display_word()

                #print(user_input, user_guessed_word)
        else:
            messagebox.showinfo("Alert", "No")

    else:
        losing_var = "You lost :(\nThe word was: " + raw_word
        messagebox.showinfo("You Lost", losing_var)


e = Entry(root, font=('default', 40))
e.pack(side='top')
e.focus_set()

def clear_text():
    global e
    e.delete(0, END)
    e.insert(0, "")





b = Button(root,text='OKAY', font=('default', 15), command=lambda:[check_len_user_input(), clear_text()], width=10, height=3, bg='#71f740')
b.pack()

Label(root, text="Guesses", font=("Courier", 15, 'bold', 'underline'), bg=color).pack(side='top')

Label(root, text=user_guessed_word, font=("Courier", 25, 'bold'), bg=color).pack(side='bottom')


root.mainloop()