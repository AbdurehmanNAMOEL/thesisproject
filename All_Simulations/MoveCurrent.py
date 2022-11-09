from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-1)
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+1)
def move_right(event):
    label.place(x=label.winfo_x()+1, y=label.winfo_y())
def move_left(event):
    label.place(x=label.winfo_x()-1, y=label.winfo_y())

window = Tk()
window.geometry("500x500")
window.bind("8", move_up)
window.bind("2", move_down)
window.bind("4", move_left)
window.bind("6", move_right)

myimage = PhotoImage(file='Battery_icon.png')
label = Label(window, image=myimage)
label.place(x=0, y=0)

window.mainloop()