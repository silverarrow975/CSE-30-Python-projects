from tkinter import *
import tkinter.font as font

def change_text(event):
    global message
    if message.get()=='You clicked me!':
        message.set('Click me again!')
    else:
        message.set('You clicked me!')
    
# make a GUI window
gui = Tk()
message = StringVar()
message.set('Click me')
f = font.Font(family='Helveca', size='12', weight='bold')
button = Button(textvariable=message, font=f, width=30, height=15, bg='bisque', fg='black')
button.bind('<Button-1>', change_text)
button.pack()
mainloop()