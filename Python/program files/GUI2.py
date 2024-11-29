from tkinter import *

root=Tk()

root.geometry("400x300")
frame1=Label(root,bg="grey",borderwidth="6",relief="sunken")
frame1.pack(fill="x")
F1=Label(frame1,text="Hello Pankaj")
F1.pack()

frame2=Label(root,bg="gray",borderwidth=6,relief="sunken")
frame2.pack(side=LEFT,fill="y")
F2=Label(frame2,text="Wow")
F2.pack(fill="y")

frame3=Label(bg="grey",borderwidth=10,relief=SUNKEN)
frame3.pack(side="right",fill=Y)
F3=Label(frame3,bg="green",borderwidth=5,relief="sunken")
F3.pack()
S1=Label(F3,text="Hello")
S1.pack()

F4=Label(frame3,bg="green",borderwidth=5,relief="sunken")
F4.pack()
S2=Label(F4,text="What Is your Name")
S2.pack()
F5=Label(frame3,bg="green",borderwidth=5,relief="sunken")
F5.pack()

S3=Label(F5,text="Bolo")
S3.pack()



root.mainloop()