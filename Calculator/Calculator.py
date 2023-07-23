from tkinter import *
root = Tk()
root.geometry("300x400")
root.title("Calculator")
root.config(background="#dbf0fd")
def calc_logic(e):
    global display_section_value
    value =e.widget.cget("text")
    if value == "AC":
        display_section_value.set("")
    elif value == "=":
        if display_section_value.get().isdigit():
            value=int(display_section_value.get())
        else:
            value=eval(display_section_value.get())

        display_section_value.set(value)
    else:
        display_section_value.set(display_section_value.get()+value)

###changing theme
button_mode=True
def change_theme():
    global button_mode
    if button_mode:
        mode.config(image=dark_mode ,bg="#26242f",activebackground="#26242f")
        root.config(bg="#031321")
        button_seaction.config(bg="#031321")
        b.config(bg="orange")
        button_mode=False

    else:
        mode.config(image=light_mode,bg="#dbf0fd",activebackground="#dbf0fd")
        root.config(bg="#dbf0fd")
        button_seaction.config(bg="light blue")
        b.config(bg="#2c6fbb")
        button_mode=True


light_mode=PhotoImage(file="light.png")
dark_mode= PhotoImage(file="dark.png")

mode = Button(root,image=light_mode,bd=0,bg="#dbf0fd",activebackground="#dbf0fd",command=change_theme)
mode.pack(side=TOP)


###setting display window
display_section = Frame(root,bg="light blue")
display_section.pack(side=TOP, fill=X,pady=10)

display_section_value = StringVar()
display_section_data = Entry(display_section,textvariable=display_section_value,font="impact 30")
display_section_data.pack(fill=BOTH)

###setting button window
button_seaction = Frame(root,bg="light blue")
button_seaction.pack()

#button grid layout
k,j=0,0
for i in ['7','8','9','/',
          '4','5','6','*',
          '1','2','3','-',
          'AC','0','+','=']:
    b=Button(button_seaction,text=i,font="lucida 20 bold",width=3,padx=7,pady=8)
    b.grid(row=k,column=j,pady=1,padx=1)
    b.bind("<Button-1>",calc_logic)

    j+=1
    if j == 4:
        k+=1
        j=0
b.config(bg="#2c6fbb")
root.mainloop()