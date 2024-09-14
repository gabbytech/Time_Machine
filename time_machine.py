from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()
window.title("Time Machine")
window.resizable(False, False)
window.geometry("445x170")

day_label = Label(window, font=("Franklin Gothic", 14), fg="Dark red")
day_label.place(x="365", y="15")

lovely_label = Label(window, font=("Informal Roman", 16), fg="red", text="Have a lovely day!!!")

night_label = Label(window, font=("Informal Roman", 16), fg="red", text="Goodnight, sleep tight!!!")

if time() <= 5:
    night_label.place(x="260", y="43")
else:
    lovely_label.place(x="285", y="43")


date_label = Label(window, font=("Time New Roman", 30), fg="Dark Blue")
date_label.place(x="", y="0")

time_label = Label(window, font=("Franklin Gothic", 57), fg="lawn green", bg="black")
time_label.place(x="4", y="75")


def openNewWindow():
    newWindow = Toplevel(window)

    newWindow.title("Reminder")
    newWindow.geometry("445x170")
    newWindow.resizable(False, False)

    Label(newWindow, text="Reminder text:", font=("Franklin Gothic", 15)).grid(row=0, column=0)
    Entry(newWindow).grid(row=0, column=1)
    Label(newWindow, text="Time:", font=("Franklin Gothic", 15)).grid(row=1, column=0)
    Entry(newWindow).grid(row=1, column=1)


btn = Button(window, text="Reminder", fg="white", bg="black", command=openNewWindow)
btn.place(x="4", y="45")

update()

window.mainloop()
