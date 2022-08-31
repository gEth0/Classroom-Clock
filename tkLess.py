from tkinter import *
import time
import webbrowser
import selenium
from selenium import webdriver
f = Tk()
f.config(bg="grey")
f.geometry("550x400")
f.title("ClassroomClock")
f.resizable(0, 0)
icon = PhotoImage(file="google-meet.png")
f.tk.call("wm", "iconphoto", f._w, icon)


ita = ""
mate = ""
spa = ""
mus = ""
ing = ""
arte = ""
scien = ""
tec = ""
rel = ""
ed = ""


time1 = time.strftime("%H:%M")
saluto = ''
if time1 > '13:00':
    saluto = 'BuonPomeriggio'
else:
    saluto = 'Buongiorno'

Label(f, text=saluto, height="3", width="500", font=(
    "Francisco", 15, 'bold'), bg="grey").pack()
Label(f, text="Created by Gabbo", height="3", width="500",
      font=("Francisco", 10), bg="grey").place(x="30", y="70")
label = Label(f, bg="grey", font=("Francisco", 15, 'bold'))
label.place(x="380", y="25")


def digital_clock():
    time_live = time.strftime("%H:%M")
    label.config(text=time_live)
    label.after(200, digital_clock)


digital_clock()


def butt():
    scelta = stri.get()
    if scelta == "1°Ora":
        webbrowser.open(ita)
    if scelta == "2°Ora":
        webbrowser.open(ita)
    if scelta == "3°Ora":
        webbrowser.open(ed)
    if scelta == "4°Ora":
        webbrowser.open(ing)
    if scelta == "5°Ora":
        webbrowser.open(rel)


def butt1():
    scelta = stri1.get()
    if scelta == "1°Ora":
        webbrowser.open(ing)
    if scelta == "2°Ora":
        pass
    if scelta == "3°Ora":
        webbrowser.open(ita)
    if scelta == "4°Ora":
        webbrowser.open(spa)
    if scelta == "5°Ora":
        webbrowser.open(scien)


def butt2():
    scelta = stri2.get()
    if scelta == "1°Ora":
        webbrowser.open(ita)
    if scelta == "2°Ora":
        webbrowser.open(ita)
    if scelta == "3°Ora":
        webbrowser.open(mate)
    if scelta == "4°Ora":
        webbrowser.open(tec)
    if scelta == "5°Ora":
        webbrowser.open(mate)


def butt3():
    scelta = stri3.get()
    if scelta == "1°Ora":
        webbrowser.open(ita)
    if scelta == "2°Ora":
        webbrowser.open(mate)
    if scelta == "3°Ora":
        webbrowser.open(ita)
    if scelta == "4°Ora":
        webbrowser.open(mus)
    if scelta == "5°Ora":
        webbrowser.open(ita)


def butt4():
    scelta = stri4.get()
    if scelta == "1°Ora":
        pass
    if scelta == "2°Ora":
        webbrowser.open(arte)
    if scelta == "3°Ora":
        p = webbrowser.open(ita)

    if scelta == "4°Ora":
        webbrowser.open(spa)
    if scelta == "5°Ora":
        webbrowser.open(ing)


Label(f, text="Lunedì", bg="grey", font=("Francisco")).place(x="70", y="80")
Label(f, text="Martedì", bg="grey", font=("Francisco")).place(x="70", y="125")
Label(f, text="Mercoledì", bg="grey", font=(
    "Francisco")).place(x="70", y="170")
Label(f, text="Giovedì", bg="grey", font=("Francisco")).place(x="70", y="215")
Label(f, text="Venerdì", bg="grey", font=("Francisco")).place(x="70", y="260")
Label(f, text="Created by Gabbo", font=(
    "Francisco", 10), bg="grey").place(x="390", y="370")
stri = StringVar()
stri.set("Scegli l'ora")
OptionMenu(f, stri, "1°Ora", "2°Ora", "3°Ora",
           "4°Ora", "5°Ora").place(x="200", y="80")
Button(f, text="Apri Classroom", command=butt, font=("Francisco"),
       width="15", relief="sunken").place(x="320", y="80")
stri1 = StringVar()
stri1.set("Scegli l'ora")
OptionMenu(f, stri1, "1°Ora", "2°Ora", "3°Ora",
           "4°Ora", "5°Ora").place(x="200", y="125")
Button(f, text="Apri Classroom", command=butt1, font=("Francisco"),
       width="15", relief="sunken").place(x="320", y="125")
stri2 = StringVar()
stri2.set("Scegli l'ora")
OptionMenu(f, stri2, "1°Ora", "2°Ora", "3°Ora",
           "4°Ora", "5°Ora").place(x="200", y="170")
Button(f, text="Apri Classroom", command=butt2, font=("Francisco"),
       width="15", relief="sunken").place(x="320", y="170")
stri3 = StringVar()
stri3.set("Scegli l'ora")
OptionMenu(f, stri3, "1°Ora", "2°Ora", "3°Ora",
           "4°Ora", "5°Ora").place(x="200", y="215")
Button(f, text="Apri Classroom", command=butt3, font=("Francisco"),
       width="15", relief="sunken").place(x="320", y="215")
stri4 = StringVar()
stri4.set("Scegli l'ora")
OptionMenu(f, stri4, "1°Ora", "2°Ora", "3°Ora",
           "4°Ora", "5°Ora").place(x="200", y="260")
Button(f, text="Apri Classroom", command=butt4, font=("Francisco"),
       width="15", relief="sunken").place(x="320", y="260")

Label(f, text="Created by Gabbo", height="3", width="500",
      font=("Francisco", 10), bg="grey").place(x='300', y="300")


f.mainloop()
