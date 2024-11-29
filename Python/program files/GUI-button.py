from tkinter import *

root=Tk()
root.geometry("633x333")



def pk():
    print("Hello Pankaj I am Shubham")

fram=Label(root,bg="grey",borderwidth=5,relief="sunken")
fram.pack()

b1=Button(fram,fg="red",text="Print")
b1.pack(side="right")
b2=Button(fram,fg="red",text="Print")
b2.pack(side="right")
b3=Button(fram,fg="red",text="Print",command=pk)
b3.pack(side="right")
b4=Button(fram,fg="red",text="Print")
b4.pack(side="right")
b5=Button(fram,fg="red",text="Print")
b5.pack(side="right")


root.mainloop()