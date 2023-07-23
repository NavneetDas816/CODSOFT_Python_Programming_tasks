from tkinter import *
root=Tk()
root.geometry("700x450")
root.config(bg="#068488")
task_no=1

def hover_effect(source,hover_in,hover_out):
    source.bind("<Enter>", func=lambda e: source.config(bg=hover_in))
    source.bind("<Leave>", func=lambda e: source.config(source.config(bg=hover_out)))

def insert(e):
    value=task_value.get()
    if value == "":
        pass
    else:
        list_panel.insert(END,value)
        task_value.set("")
def delete_task(e):
    element = list_panel.curselection()
    if element ==():
        pass
    else:
        list_panel.delete(element)
def update(e):
    print("hi")
    confirm.place(x=100,y=500)
    edit.place(x=135,y=150)

def reset(e):
    confirm.place(x=100,y=150)
    edit.place(x=130,y=500)

def edit_val(e):
    list_panel.insert(list_panel.curselection(),task_value.get())
    list_panel.delete(list_panel.curselection())



heading = Label(root,text="To-Do LIST",font="Arial 40 italic bold",padx=2,pady=3,bg="#068488")
heading.place(x=200,y=0)

#Tast addition panel
add_panel = Frame(root,width=400,height=400,bg="#068488",highlightbackground="black",highlightthickness=2)
add_panel.place(x=-20,y=70)

task_heading = Label(add_panel,text="Task",font="Arial 20 bold",pady=2,bg="#068488")
task_heading.place(x=60,y=40)

task_value = StringVar()
task_entry = Entry(add_panel,textvariable=task_value,font="arial 20 bold",width=20)
task_entry.place(x=60,y=75)

confirm = Button(add_panel,text="CONFIRM",relief=RAISED,bg="#324B4C",fg="#ffffff",font="Arial 25",activebackground="#324B4C")
confirm.place(x=100,y=150)
confirm.bind("<Button-1>",insert)
hover_effect(confirm,"green","#324B4C")

delete = Button(add_panel,text="delete",relief=RAISED,bg="#324B4C",fg="#ffffff",font="Arial 25",activebackground="#324B4C")
delete.place(x=130,y=250)
delete.bind("<Button-1>",delete_task)
hover_effect(delete,"red","#324B4C")

edit = Button(add_panel,text="EDIT",relief=RAISED,bg="#324B4C",fg="#ffffff",font="Arial 25",activebackground="#324B4C")
edit.place(x=130,y=500)
edit.bind("<Button-1>",edit_val)
hover_effect(edit,"green","#324B4C")

#Task listing panel
list_panel = Listbox(root,width=350,height=400,bg="#00c6cf",highlightbackground="black",highlightthickness=2,font="arial 20 bold")
list_panel.place(x=380,y=70)
list_panel.bind("<FocusIn>",update)
list_panel.bind("<FocusOut>",reset)

root.mainloop()