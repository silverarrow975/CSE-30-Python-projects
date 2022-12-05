''' DO NOT FORGET TO ADD COMMENTS '''
from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
          
def clickButton():
    pass
def shuffle():
    pass
def closeWindow():
    pass
    
if __name__ == '__main__':    
    # make tiles
    tiles = Fifteen()
    # make a window
    gui = Tk()
    gui.title("Fifteen")
    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')
    for r in range(len(tiles.board)):
        for c in range(len(tiles.board[r])):
            if tiles.board[r][c] == 0:
                break
            # make buttons
            text = StringVar()
            text.set(str(tiles.board[r][c]))
            name = tiles.board[r][c]
            button = Button(gui, textvariable=text, name=str(name),
                            bg='white', fg='black', font=font, height=2, width=5,
                            command = lambda : clickButton())
            button.configure(bg='coral')
            
            # the key argument name is used to identify the button
            gui.nametowidget(name).configure(bg='white')
            # add buttons to the window
            # use .grid() or .pack() methods
            button.grid(row=r,column=c)
    
    # create shuffle and quit button
    text = StringVar()
    text.set('Shuffle')
    shuffleB = Button(gui, textvariable=text, name='shuffleB', bg='white', fg='black', font=font, height=1, width=5, command= lambda : shuffle())
    # the key argument name is used to identify the button
    gui.nametowidget('shuffleB').configure(bg='white')
    shuffleB.configure()
    # add buttons to the window
    shuffleB.grid(row=4,column=0)
    
    quitB = Button(gui, textvariable="Quit", name='quitB', bg='white', fg='black', font=font, height=1, width=5, command= lambda : closeWindow())
    # the key argument name is used to identify the button
    gui.nametowidget('quitB').configure(bg='white')
    quitB.configure()
    quitB.grid(row=4,column=3)
            
    # use .grid() or .pack() methods
    
    # update the window
    gui.mainloop()