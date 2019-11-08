import tkinter as tk
from random import randrange

circle=[]


def getorigin(eventorigin):
    global x0,y0
    x0 = eventorigin.x
    y0 = eventorigin.y
    #print(x0,y0)
    return x0,y0

def move(event):
    
    my_canvas.move(circle,10,10)
    # my_canvas.move(circle,i,i)
    # get the coordinates
    coord = my_canvas.coords(circle)
    print(coord)
    # my_canvas.after(33,move)
   

def clicked_circle(event):
    print("button was clicked")
    
    circle = my_canvas.create_oval(
        randrange(900),
        randrange(900),
        randrange(900),
        randrange(900)
        )
    return circle
i = 1
root = tk.Tk()

my_canvas = tk.Canvas(root,width=1000,height=1000,background='white')
my_canvas.pack()

my_canvas.create_line(0,0,300,300,fill='black')
x = 10+i

root.bind('<Button-3>', clicked_circle)
root.bind('<Button-1>', move)
# my_canvas.bind("<Button-1>",getorigin)
root.mainloop()
# circle.append(my_canvas.create_oval(10,20,50,90))
# circle.append(my_canvas.create_oval(20,30,40,50))
# print(i)
# print(circle)