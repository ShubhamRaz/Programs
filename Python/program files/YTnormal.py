import tkinter as tk

def button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()
