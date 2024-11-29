import tkinter as tk
from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("400x300")


pankaj=Label(text="hello world",fg="blue",pady=30,font=("Arial",20,"bold"),relief="sunken")
pankaj.pack(side=BOTTOM,fill="x")


photo=PhotoImage(file=r"C:\Users\kumar\OneDrive\Desktop\my.png")
pk=Label(image=photo)
pk.pack()

root.mainloop()