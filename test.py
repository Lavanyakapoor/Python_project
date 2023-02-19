from tkinter import *
wind = Tk()
from PIL import ImageTk, Image
def func():
        x = var.get().lower()
        

    # for title
wind.title("Maxy")

#  for icon
imj = PhotoImage(file='mic.png')
wind.iconphoto(False, imj)

    # // window size

wind.maxsize(width=1000, height=750)
wind.minsize(width=1000, height=750)
wind.colormapwindows()
wind.geometry('400x350')



btn = Button(wind, text="Submit", bg='green', command=func)
btn.place(x=160, y=60)
    

my_pic = Image.open("search3.png")

resize_pic = my_pic.resize((54, 52), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resize_pic)

var = StringVar()
ent = Entry(wind, width=25, font=("Arial", 23), textvariable=var)
ent.place(x=134, y=610)

btn = Button(wind,image=new_pic, command=func)
btn.place(x=789, y=608)

wind.mainloop()
