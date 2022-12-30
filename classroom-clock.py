try:
    from tkinter import *
    import time
    import webbrowser
    import selenium
    from selenium import webdriver
    from datetime import datetime
    import json
except:
    print("Make sure you have installed all the dependencies")
    exit()

f = Tk()
f.config(bg="grey")
f.geometry("700x600")
f.resizable(0,0)
f.title("ClassroomClock")
icon = PhotoImage(file="./img/google-meet.png")
f.tk.call("wm", "iconphoto", f._w, icon)


timeNow = time.strftime("%H:%M")
greetings = 'Good Afternoon' if timeNow > '13:00' else 'Good Morning'

greetingsLabel = Label(f, text=greetings, height="3", width="500", font=(
    "Francisco", 15, 'bold'), bg="grey").pack()

timeLabel = Label(f, bg="grey", font=("Francisco", 15, 'bold'))
timeLabel.place(x="500", y="25")

def getCurrentWeekDay(number):
    days  = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5 :"Saturday",6:"Sunday"}
    return days[number]

def digital_clock():
    time_live = time.strftime("%H:%M")
    timeLabel.config(text=time_live)
    timeLabel.after(200, digital_clock)


def openLessonLink():
    choose = chooseLessonStr.get()
    try : 
        webbrowser.open(choose)
    except:
        print("Read the documentation for setting up the files correctly")
        exit()

digital_clock()


creditsLabel = Label(f, text="Created by gEth0", font=(
    "Francisco", 10), bg="grey").place(x="550", y="550")
chooseLessonStr = StringVar()
chooseLessonStr.set("Choose the class")

today = datetime.now()

nWeekDay = today.weekday()

day = getCurrentWeekDay(nWeekDay)

dayLabel  = Label(f, text=day, bg="grey", font=("Francisco" , 14,'bold')).place(x="80", y="250")

try:
    with open("lessonsSchedule.json","r") as lessons:
        data = json.loads(lessons.read())
        listLessons = data[day]
        
except:
    print("Read the documentation for set up the files")

selectMenu = OptionMenu(f, chooseLessonStr, *listLessons).place(x="270", y="250")
openButton = Button(f, text="Open", command=openLessonLink, font=("Francisco"),
       width="15", relief="sunken").place(x="500", y="250")


f.mainloop()
# gEth0
