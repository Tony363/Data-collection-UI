import tkinter as tk
from random import randrange

    # circle.delete(circle)
    # if canvas.old_coords:
    #     x1, y1 = canvas.old_coords
        # canvas.create_oval(x, y, x1, y1)
    # canvas.old_coords = x, y

def clicked_circle(event):
    circle = canvas.create_oval(
        10,
        20,
        30,
        40
    )
    return circle
    
def myfunction(event,clicked_circle):
        x, y = event.x, event.y
        canvas.move(circle,x,y)  
    
def delete_lines(event):
    canvas.delete('all')

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.old_coords = None

root.bind('<B1-Motion>', myfunction)
root.bind('<Button-3>', delete_lines)
root.bind('<Button-1>', clicked_circle)
root.mainloop()