from tkinter import *

window = Tk()
window.title("Note")
window.minsize(width=500, height=500)

title_entry = Entry(font=("Arial", 20, "bold"))
title_entry.pack(side=TOP, fill=X)

text_entry = Entry(font=("Arial", 16, "bold"))
text_entry.pack(side=BOTTOM, fill=X)


def add_clicked():
    with open("data.txt", "a") as file:
        file.write(f"{title_entry.get()}-{text_entry.get()}\n")
    title_entry.delete(first=0,last=END)
    text_entry.delete(first=0,last=END)


def find_clicked():
    text_entry.delete(first=0, last=END)
    with open("data.txt", "r") as file:
        data = file.readlines()
        for line in data:
            source = line.strip().split("-")
            title = source[0]
            text = source[1]

            if title_entry.get() == title:
                text_entry.insert(END, string=text)


button_add = Button(text="ADD", command=add_clicked, width=20, font=("Arial", 16, "bold"))
button_add.pack(side=LEFT, fill=X)

button_find = Button(text="Find", command=find_clicked, width=20, font=("Arial", 16, "bold"))
button_find.pack(side=RIGHT, fill=X)


window.mainloop()
