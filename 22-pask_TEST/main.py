from tkinter import *

window = Tk()
window.title("Hash")
window.minsize(width=800, height=400)

email_label = Label(text="Email:", font=("Arial", 16, "bold"))
email_label.grid(column=0, row=0)
email_entry = Entry(width=25, font=("Arial", 16))
email_entry.grid(column=1, row=0)

password_label = Label(text="Password:", font=("Arial", 16, "bold"))
password_label.grid(column=0, row=1)
password_entry = Entry(width=25, font=("Arial", 16))
password_entry.grid(column=1, row=1)


def checkbox_used():
    password_entry.config(text="")
    window.update()


def radio_used():
    pass


check_state = IntVar()
check_button = Checkbutton(text="Generate", font=("Arial", 14), variable=check_state, command=checkbox_used)
check_button.grid(column=0, row=2)

radio_state = IntVar()
radio_button_1 = Radiobutton(text="Option 1", font=("Arial", 14), value=1, variable=radio_state, command=radio_used)
radio_button_2 = Radiobutton(text="Option 2", font=("Arial", 14), value=2, variable=radio_state, command=radio_used)
radio_button_1.grid(column=1, row=2)
radio_button_2.grid(column=1, row=3)


def hash_clicked():
    #cezar shifr
    print(check_state.get())
    print(radio_state.get())


button_start = Button(text="Hash", command=hash_clicked, width=10, font=("Arial", 14, "bold"))
button_start.grid(column=0, row=5)

window.mainloop()
