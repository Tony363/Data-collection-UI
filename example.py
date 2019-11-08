import tkinter
from random import randint
tk=tkinter.Tk() 
canvas=tkinter.Canvas(width=1250, height=700)
canvas.configure(background='red')
frame=canvas.create_rectangle(10,10,1240,690, fill="white")
om=canvas.create_oval(50,50,75,75, fill="blue")
lis=[]
count=0
on=0 
def move1():
    global lis, count, on
    count=count+1
    if(count%100==0):
        c1=randint(10,1235)
        c2=randint(10,685)
        o=canvas.create_oval(c1,c2,c1+5,c2+5, fill="green")
        lis1=[]
        lis1.append(c1)
        lis1.append(c2)
        lis1.append(c1+5)
        lis1.append(c2+5)
        lis.append(lis1)
 
    x1, y1, x2, y2=canvas.coords(om)

    canvas.after(1,move1)
move1()
def cursor(event):
    m1=event.x
    m2=event.y
    return m1, m2
tk.bind("<B1-Motion>", cursor)
canvas.pack()
print(cursor)
tk.mainloop()