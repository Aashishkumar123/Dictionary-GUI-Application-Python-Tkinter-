#import modules
from tkinter import *
import tkinter as tk
from PyDictionary import PyDictionary


root = tk.Tk()
root.title('Dictionary Desktop App')
root.geometry("300x150")

enter = Entry(root,width=100)
enter.insert(0,"Type here to search any word")
enter.pack(ipady=2)

def dictionary():
    dictionary = PyDictionary()
    word = enter.get()
    result = dictionary.meaning(word)
    T = tk.Text(root, height=10, width=50)
    T.pack()
    T.insert(tk.END,result)


click = Button(root, text="Search",
                   fg="red",
                   command=dictionary)
click.pack()

root.mainloop()
