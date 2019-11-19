## imports for Python 2.7, change as appropriate
from tkinter import *
import tkinter.simpledialog
import time, random, numpy, math


class PlayerSprite:
    def __init__(self, canvas):
        self.canvas = canvas
        self.endgame = False
        self.id = self.canvas.create_oval(350, 350, 400, 400, tag='User', fill=random.choice(colors))
        self.id2 = self.canvas.create_text(375, 375, text=nick, font=('Helvetica', 15), tag='User')
    def coords(self):
        print(self.canvas.coords('User'))
        return self.canvas.coords('User')
    def mouseCoords(self):
        rawMouseX, rawMouseY =   tk.winfo_pointerx(), tk.winfo_pointery()
        self.mousecoords = rawMouseX  - tk.winfo_rootx(), rawMouseY - tk.winfo_rooty()
        return self.mousecoords
    def moveTowardMouse(self):   # Problem function?
        ## Use center of the of the oval/player as selfx, selfy
        selfx, selfy = (self.coords()[0]+self.coords()[2])/2, (self.coords()[1]+self.coords()[3])/2
        mousex, mousey = self.mousecoords
        movex = (mousex-selfx)
        movey = (mousey-selfy)

        speed = 2 ## Player speed
        theta = math.atan2(movey, movex) ## angle between player and mouse position, relative to positive x

        ## Player speed in terms of x and y coordinates
        x = speed*math.cos(theta)
        y = speed*math.sin(theta)

        self.canvas.move('User', x, y)


tk = Tk()
nick = tkinter.simpledialog.askstring('nickname', 'Nickname')
tk.title("My Agar.io Clone")
tk.wm_attributes('-topmost', 1)
tk.resizable(0, 0)
canvas = Canvas(tk, width=750, height=750)
center =  (canvas.winfo_reqwidth()/2), (canvas.winfo_reqheight()/2)
colors = ['red', 'blue', 'green', 'yellow']

canvas.pack()

player = PlayerSprite(canvas)
player.mouseCoords()

while player.endgame == False:
    try:
        player.moveTowardMouse()
        player.mouseCoords()
        tk.update_idletasks()
        tk.update()
        time.sleep(.005)
    except:# KeyboardInterrupt:
        print('CRL-C recieved, quitting')
        tk.quit()
        break