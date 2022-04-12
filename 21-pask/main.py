import time
from tkinter import *
#from PIL import ImageTk,Image

window = Tk()
window.title("Pomodoro")
window.minsize(width=600, height=400)


status_label = Label(text="-", font=("Arial", 22, "bold"))
status_label.pack()

#canvas = Canvas(window, width = 300, height = 300)
#canvas.pack()
#img = PhotoImage(file="Pomodoro1.ppm")
#canvas.create_image(20, 20, anchor=NW, image=img)

pomodoro_label = Label(text=f"Pomodoro:", font=("Arial", 20, "bold"))
pomodoro_label.pack(side=LEFT)

time_label = Label(text="00", font=("Arial", 20, "bold"))
time_label.pack()


def start_clicked():
    button_start.destroy()
    for i in range(1, 5):

        pomodoro_label.config(text=f"Pomodoro:{i}")

        status_label.config(text="Work")
        for _ in range(0, 26):

            time_label.config(text=_)

            window.update()
            time.sleep(0.2)

        status_label.config(text="Break")
        for _ in range(0, 6):

            time_label.config(text=_)

            window.update()
            time.sleep(0.2)

    status_label.config(text="Long Break")
    for i in range(0, 31):
        time_label.config(text=i)

        window.update()
        time.sleep(0.2)

    pomodoro_label.config(text="Pomodoro - Done")
    time_label.config(text="-")
    status_label.config(text="-")


button_start = Button(text="Start", command=start_clicked, width=10, font=("Arial", 20, "bold"))
button_start.pack(side=BOTTOM)


window.mainloop()
