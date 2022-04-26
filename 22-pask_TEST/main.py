from tkinter import *
import json
from user import User

#user = User()

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
        password_entry.config(text="Auto")
    elif check_state.get() == 0:
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
    email = email_entry.get()
    password = password_entry.get()

    if len(email) > 0 and len(password)> 0:

        split_pass = list(password)
        new_password = ""
        for item in split_pass:
            str = ""

            if ord(item) > 64 and ord(item) < 91:
                str = ord(item)+3
                if str > 90:
                    str = str-25
                str = chr(str)

            if ord(item) > 96 and ord(item) < 123:
                str = ord(item)+3
                if str > 122:
                    str = str-25
                str = chr(str)

            new_password = new_password + str


        my_user = {
            "Email": email,
            "Password": new_password,
        }

        with open("data.txt", "a") as file:
            file.write(f"{json.dumps(my_user)}\n")


button_hash = Button(text="Hash", command=hash_clicked, width=10, font=("Arial", 14, "bold"))
button_hash.grid(column=0, row=5)


#-----------------------
show_email_label = Label(text="Email:", font=("Arial", 16, "bold"))
show_email_label.grid(column=3, row=3)
show_email_entry = Entry(width=25, font=("Arial", 16))
show_email_entry.grid(column=4, row=3)


def unhash_clicked():
    All_users = []
    with open("data.txt") as file:
        data = file.read()
        data = data.strip()
        data = data.split("\n")
        print(data)
        for item in data:
            js = json.loads(item)
            All_users.append(js)# error nes tuscia eilute nereikalinga

    for item in All_users:
        if item["Email"] == show_email_entry.get():
            show_password_text.config(text=item["Password"])



button_unhash = Button(text="UnHash&Show", command=unhash_clicked, width=12, font=("Arial", 14, "bold"))
button_unhash.grid(column=4, row=4)

show_password_label = Label(text="Password:", font=("Arial", 16, "bold"))
show_password_label.grid(column=3, row=5)
show_password_text = Label(text=".", font=("Arial", 16, "bold"))
show_password_text.grid(column=4, row=5)

window.mainloop()
