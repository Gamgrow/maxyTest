# Maxy
import datetime
import sys
import os
from tkinter import *

wind = Tk()
from PIL import ImageTk, Image





def doooo(text):
    
    pass

if __name__ == '__main__':
    def karo():
                
        pass
       

    def func():
        x = var.get().lower()
        doooo(x)

    #  for photo set without using your local system photo
    def resource_path(relative_path):
        # Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)



    # for title
    wind.title("Maxy")

#  for icon
    path1 = resource_path("mic.png")
    imj = PhotoImage(file=path1)
    wind.iconphoto(False, imj)

    # // window size

    # wind.maxsize(width=800, height=400)
    # wind.minsize(width=30, height=30)
    wind.geometry("900x600")
    wind.colormapwindows()
   
    wind.config(background='#108cff')
    # label 1
    mylabel = Label(wind,font=("arial",20),bg='#1570CB',justify="left" ,border=1)
    mylabel.place(x=890,y=130)
    # show image
    path2 = resource_path("mic.png")
    my_pic5 = Image.open(path2)

    resize_pic5 = my_pic5.resize((60,60
                                  ), Image.ANTIALIAS)
    new_pic5 = ImageTk.PhotoImage(resize_pic5)
    
    lbl=Label(wind,bg="#108cff").place(x=290,y=60)
    
    # label 2
    mylabel2 = Label(wind,font=("arial",20 ),bg="#1570CB",justify="left",border=1   )
    mylabel2.place(x=60,y=130)


    path3 = resource_path("searchicon.png")
    my_pic = Image.open(path3)

    resize_pic = my_pic.resize((43, 42), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resize_pic)

    
    # wlcome to maxy
    path4 = resource_path("wctm.png")
    my_pic_wctm = Image.open(path4)

    resize_pic_wctm = my_pic_wctm.resize((388, 124), Image.ANTIALIAS)
    my_pic_wctm = ImageTk.PhotoImage(resize_pic_wctm)

    # Maxy
    mylabel2wctm = Label(wind,text = "MAXY",bg="#108cff",font=("Arial Black",28 ) , fg="white")
    mylabel2wctm.pack()

    # welcome
    mylabel2wctm3 = Label(wind,text = "WELCOME",bg="#108cff",font=("Arial Black",13 ) , fg="white")
    mylabel2wctm3.pack(side='top')

    def about():
        pass
    # menu bar
    menuBar= Menu(wind)
    wind.config(menu=menuBar)

    file_manu = Menu(menuBar)
    menuBar.add_cascade(label="About", menu=file_manu,activeforeground="#108cff",activebackground="#108cff")
    file_manu.add_cascade(label="Made by \n Lalit Max", command=about)

    # lebel for exit
    file_manu2 = Menu(menuBar)
    menuBar.add_cascade(label="Close",menu=file_manu2,activeforeground="#108cff",activebackground="#108cff")
    file_manu2.add_cascade(label="Exit",command=wind.quit)
    #  Add gmail
    file_manu3 = Menu(menuBar)
    menuBar.add_cascade(label="Gmail",menu=file_manu3,activeforeground="#108cff",activebackground="#108cff")
    # make attendancer
    def makeatd():
        # atd.makeAt()
        pass
    #  open excel file
    # def openexcel():
    #     os.startfile('Attendancer.xlsx')

    # file_manu4 = Menu(menuBar)
    # menuBar.add_cascade(label="Attendancer", menu=file_manu4,activeforeground="#108cff",activebackground="#108cff")
    # file_manu4.add_cascade(label="Add Name Of Student",command=openexcel)
    # file_manu4.add_cascade(label="Start", command=makeatd)

    def onReturn(event):
        func()
        ent.delete(0,'end')
   
    def click(event):
        ent.config(state=NORMAL)
        ent.delete(0,END)

    var = StringVar()
    ent = Entry(wind, width=85, font=("Arial", 23), textvariable=var,justify="left")
    ent.insert(0,"Search Something")
    ent.bind("<Return>",onReturn)
    ent.bind("<Button-1>",click)
    
    ent.pack(side="bottom",pady=2)
    btn = Button(wind, image=new_pic,cursor="hand2", command=func,activebackground="#108cff",border=2,bg="white")
    btn.pack()
   

    btn2 = Button(wind, image=new_pic5,cursor="hand2", command=karo,activebackground="#108cff",bg="#108cff",border=2).pack(side='bottom',pady=84)
    btn = Button(wind, image=new_pic,cursor="hand2", command=func,activebackground="#108cff",border=2,bg="white")
    # btn.pack(side="left")
    
  



   






   
   
  
    wind.mainloop()
