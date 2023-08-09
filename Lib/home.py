from tkinter import *
import login_click
import sign_click
from PIL import ImageTk,Image

w = Tk()

w.title("Welcome Page")

w.geometry("1920x1080")

mf = Frame(w, bd=10, width=995, height=750, relief=RIDGE, bg="powder blue")

img = ImageTk.PhotoImage(Image.open("libimage2.jpg"))
lab=Label(mf,image=img)
lab.place(anchor="nw")

lf = Frame(mf, padx=30,pady=20,bd=12, width=500,borderwidth=20, height=500, relief="groove", bg="#9e5e2c")
mf.grid()
lf.grid(row=1, column=0,padx=(300,300), pady=(20,210))



def goopt():
    w.destroy()
    login_click.lnpg()

def goosp():
    w.destroy()
    sign_click.snpg()

Label(lf, padx=50, pady=30, font=("Times", 50, 'bold italic'), text="Welcome to KCT Library", bg="white").grid(row=0, column=0)

bf = Frame(mf, padx=50,pady=30,bd=12, width=550, height=100, relief="groove", bg="#8694b2")
bf.grid(padx=10,pady=(150,43),row=2, column=0)

Button(bf,text="LOGIN",padx=20,pady=5,command=goopt).grid(padx=10, row=5,column=0,columnspan=4)
Button(bf,text="SIGN UP",padx=20,pady=5,command=goosp).grid(padx=20,row=5,column=20,columnspan=4)

w.mainloop()