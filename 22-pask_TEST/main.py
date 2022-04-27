from tkinter import *
import json
from user import User

user = User()

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
    if check_state.get() == 1:
        password_entry.delete(0, END)
        password_entry.configure(state=DISABLED)

        radio_button_1.configure(state=NORMAL)
        radio_button_2.configure(state=NORMAL)

    elif check_state.get() == 0:
        password_entry.configure(state=NORMAL)

        radio_button_1.configure(state=DISABLED)
        radio_button_2.configure(state=DISABLED)


def radio_used():
    pass


check_state = IntVar()
check_button = Checkbutton(text="Generate", font=("Arial", 14), variable=check_state, command=checkbox_used)
check_button.grid(column=0, row=2)

radio_state = IntVar()
radio_button_1 = Radiobutton(text="Characters", state=DISABLED, font=("Arial", 14), value=1, variable=radio_state, command=radio_used)
radio_button_2 = Radiobutton(text="Numbers", state=DISABLED, font=("Arial", 14), value=2, variable=radio_state, command=radio_used)
radio_button_1.grid(column=1, row=2)
radio_button_2.grid(column=1, row=3)


def hash_clicked():
    email = email_entry.get()
    password = password_entry.get()

    if check_state.get() != 0 and radio_state.get() != 0:
        password = user.generate_password(radio_state.get())
    if len(email) > 0 and len(password) > 0:
        user.hash_and_add_to_list(email, password)
        email_entry.delete(0, END)
        password_entry.delete(0, END)


button_hash = Button(text="Hash", command=hash_clicked, width=10, font=("Arial", 14, "bold"))
button_hash.grid(column=0, row=5)

#-----------------------
show_email_label = Label(text="Email:", font=("Arial", 16, "bold"))
show_email_label.grid(column=3, row=3)
show_email_entry = Entry(width=25, font=("Arial", 16))
show_email_entry.grid(column=4, row=3)


def unhash_clicked():
    show_password_text.config(text=user.find_unhash(show_email_entry.get()))


button_unhash = Button(text="UnHash&Show", command=unhash_clicked, width=12, font=("Arial", 14, "bold"))
button_unhash.grid(column=4, row=4)

show_password_label = Label(text="Password:", font=("Arial", 16, "bold"))
show_password_label.grid(column=3, row=5)
show_password_text = Label(text=".", font=("Arial", 16, "bold"))
show_password_text.grid(column=4, row=5)

window.mainloop()
