from tkinter import *





window=Tk()

def myMethod():
    print(val.get()) 
    text.insert(END,val.get())


button = Button(window,text="Execute",command=myMethod)
button.grid(row=0,column=0)

val=StringVar()
entry=Entry(window,textvariable=val)
entry.grid(row=0,column=1)

text=Text(window,height=1,width=20)
text.grid(row=0,column=2)


window.mainloop()

