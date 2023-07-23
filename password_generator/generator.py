import tkinter.ttk
from tkinter import *

import random

root=Tk()
root.geometry("300x400")
root.config(bg="green")

#password generated logic
def password():
    if password_length_value.get()==0:
        pass
    else:
        no=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        alphabets =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        Alphabets =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        symbol = ['!','@','$','%','&',';',':','<','>','?','/','~','`']
        if level.get() == 1:
            pass
        elif level.get() == 2:
            no = no + alphabets +Alphabets
        elif level.get() == 3:
            no = symbol+alphabets+no+Alphabets
        else:
            pass
        p=""
        for i in range(int(password_length_value.get())):
            p=p + random.choice(no)
        generated_password_value.set(p)
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(generated_password_value.get())

logo = Label(root,text="Password Generator",font="arial 22 bold",pady=7)
logo.pack(side=TOP,fill=X)

separator = tkinter.ttk.Separator(root,orient="horizontal")
separator.pack(fill=X)

# requesting the length of the password to be generated
password_length = Label(root,text="Password Length:",font="arial 15 italic",pady=10,bg="green")
password_length.place(x=5,y=80)

password_length_value = Entry(root,width=10,font="impact 15")
password_length_value.place(x=170,y=90)

#requesting level of the password to be generated
level_label = Label(root,text="-----------------Level------------------",font="arial 15 bold",bg="green",pady=10)
level_label.place(x=0,y=140)

level = IntVar()
l1 = Radiobutton(root,text="Level 1",value=1,variable=level,bg="green",font="arial 10 bold",activebackground="green")
l1.place(x=10,y=180)

l2 = Radiobutton(root,text="Level 2",value=2,variable=level,bg="green",font="arial 10 bold",activebackground="green")
l2.place(x=105,y=180)

l3 = Radiobutton(root,text="Level 3",value=3,variable=level,bg="green",font="arial 10 bold",activebackground="green")
l3.place(x=200,y=180)


submit = Button(root,text="GENERATE",font="arial 20",bg="#E6CE4D",command=password)
submit.place(x=60,y=220)

generated_password_value=StringVar()
generated_password_value.set("XYZ-ABC")
generated_password = Label(root,textvariable=generated_password_value,font="arial 12",bg="green")
generated_password.place(y=290,x=80)

copy = Button(root,text="Copy",font="arial 15",command=copy_password).place(x=150,y=320)
retry = Button(root,text="Retry",font="arial 15",command=password).place(x=80,y=320)


root.mainloop()