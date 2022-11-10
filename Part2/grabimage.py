#Original Author: Jonathan Hudson
#CPSC 501 F22

from tkinter import *
import pyscreenshot as ImageGrab

#State of mouse
b1 = "up"
def b1down(event):
    global b1
    b1 = "down"
def b1up(event):
    global b1
    b1 = "up"
def motion(event):
    if b1 == "down":
        event.widget.create_oval(event.x,event.y,event.x,event.y, width=16)

#Main to draw window, capture buttons events, and save image
def main():
    root = Tk()
    root.title("Draw")
    drawing_area = Canvas(root,bg="white",width=28*8,height=28*8)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    button=Button(root,fg="green",text="Save",command=lambda:getter(drawing_area))
    button.pack(side=LEFT)
    button=Button(root,fg="green",text="Clear",command=lambda:delete(drawing_area))
    button.pack(side=RIGHT)
    def delete(widget):
        widget.delete("all")
    def getter(widget):
        x=root.winfo_rootx()+widget.winfo_x()
        y=root.winfo_rooty()+widget.winfo_y()
        x1=x+widget.winfo_width()
        y1=y+widget.winfo_height()
        grabbed = ImageGrab.grab()
        grabbed = grabbed.crop((x,y,x1,y1))
        grabbed = grabbed.resize((28,28))
        grabbed = grabbed.convert(mode="L")
        grabbed.save("image.png")
    root.mainloop()
  
if __name__ == "__main__":
    main()
