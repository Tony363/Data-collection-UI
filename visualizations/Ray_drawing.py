import tkinter as tk
from random import randrange
import time

database = []

def getorigin(eventorigin):
    
    x0 = eventorigin.x
    y0 = eventorigin.y
    print(x0,y0)
    return x0,y0


# def clicked_circle(event):
#     print("button was clicked")
    
#     circle = my_canvas.create_oval(
#         randrange(900),
#         randrange(900),
#         randrange(900),
#         randrange(900)
#         )
        
def move(event):
    x,y = event.x,event.y
    circle = my_canvas.create_oval(
    10,
    20,
    30,
    40
    )
    my_canvas.move(circle,x,y)
    # circle.update()
    coord = my_canvas.coords(circle)
    print(coord)
    database.append(coord)
    time.sleep(0.1)
    # my_canvas.update(circle)
    


root = tk.Tk()
my_canvas = tk.Canvas(root,width=1000,height=1000,background='white')
my_canvas.pack()

# my_canvas.create_line(0,0,300,300,fill='black')
root.bind('<B1-Motion>',move)
root.bind("<Button-3>",getorigin)
root.mainloop()
# circle.append(my_canvas.create_oval(10,20,50,90))
# circle.append(my_canvas.create_oval(20,30,40,50))

print(database)