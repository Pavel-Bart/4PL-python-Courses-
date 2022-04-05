from tkinter import *
import json


is_on = True

while is_on:

    window = Tk()
    window.title("Choose")
    window.minsize(width=500, height=500)

    def quit_used():
        global is_on
        is_on = False
        window.destroy()


    button_quit = Button(text="Quit", command=quit_used)
    button_quit.grid(column=1, row=3)

    def register():
        window.destroy()

        windowReg = Tk()
        windowReg.title("Register")
        windowReg.minsize(width=500, height=500)

        name_label = Label(text="Name:", font=("Arial", 14, "bold"))
        name_label.grid(column=0, row=0)
        name_entry = Entry(width=15)
        name_entry.grid(column=1, row=0)

        username_label = Label(text="Username:", font=("Arial", 14, "bold"))
        username_label.grid(column=0, row=1)
        username_entry = Entry(width=15)
        username_entry.grid(column=1, row=1)

        email_label = Label(text="Email:", font=("Arial", 14, "bold"))
        email_label.grid(column=0, row=2)
        email_entry = Entry(width=15)
        email_entry.grid(column=1, row=2)

        password_label = Label(text="Password:", font=("Arial", 14, "bold"))
        password_label.grid(column=0, row=3)
        password_entry = Entry(width=15)
        password_entry.grid(column=1, row=3)

        repeatPassword_label = Label(text="Repeat password:", font=("Arial", 14, "bold"))
        repeatPassword_label.grid(column=0, row=4)
        repeatPassword_entry = Entry(width=15)
        repeatPassword_entry.grid(column=1, row=4)

        def register_used():
            name = name_entry.get()
            username = username_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            rpassword = repeatPassword_entry.get()

            check_label = Label(font=("Arial", 14, "bold"))
            check_label.grid(column=3, row=3)

            if len(name) > 0 and len(username) > 0 and len(email) > 0 and len(password) > 0 and len(rpassword) > 0:

                if password == rpassword:
                    check_label.config(text="Succsesfully!")

                    my_user = {
                        "Name": name,
                        "Email": email,
                        "Username": username,
                        "Password": password,
                    }

                    with open("data.txt", "a") as file:
                        file.write(f"{json.dumps(my_user)}\n")

                else:
                    check_label.config(text="Passwords are not same!")

            else:
                check_label.config(text="All labels must be filled")

        button_reg = Button(text="Register", command=register_used)
        button_reg.grid(column=1, row=5)

        button_reg_quit = Button(text="Quit", command=windowReg.destroy)
        button_reg_quit.grid(column=0, row=7)

        windowReg.mainloop()


    def login():
        window.destroy()

        windowLogin = Tk()
        windowLogin.title("Login")
        windowLogin.minsize(width=500, height=500)

        label_username = Label(text="Username:", font=("Arial", 14, "bold"))
        label_username.grid(column=0, row=0)
        entry_username = Entry(width=15)
        entry_username.grid(column=1, row=0)

        label_password = Label(text="Password:", font=("Arial", 14, "bold"))
        label_password.grid(column=0, row=1)
        entry_password = Entry(width=15)
        entry_password.grid(column=1, row=1)

        check_label = Label(font=("Arial", 14, "bold"))
        check_label.grid(column=3, row=3)

        def login_used():
            All_users = []
            with open("data.txt") as file:
                data = file.read()
                data = data.split("\n")

                for item in data:
                    js = json.loads(item)
                    All_users.append(js)


        button_log = Button(text="Login", command=login_used)
        button_log.grid(column=1, row=5)

        button_log_quit = Button(text="Quit", command=windowLogin.destroy)
        button_log_quit.grid(column=0, row=7)

        windowLogin.mainloop()


    RegButton = Button(text="Register", command=register)
    RegButton.grid(column=0, row=0)
    LoginButton = Button(text="Login", command=login)
    LoginButton.grid(column=1, row=0)
    window.mainloop()

