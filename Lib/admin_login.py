from tkinter import *
import add_click
import sql_quries
import removebook_click
from PIL import ImageTk,Image

def adln():

    def adbo():
        add_click.adbk()

    def rbk():
        removebook_click.rebk()

    ad = Tk()
    ad.title("Sign_up Page")
    ad.geometry("1920x1080")
    mf = Frame(ad, padx=590,pady=305, bd=10, width=995, height=750, relief=RIDGE, bg="powder blue")
    img = ImageTk.PhotoImage(Image.open("libimage7.jpg"))
    lab = Label(mf, image=img)
    lab.place(anchor="center")

    lf = Frame(mf, padx=100,pady=50,bd=10, width=500, height=500, relief=RIDGE, bg="#909229")
    mf.grid()
    lf.grid(row=1, column=0)

    b1=Button(lf, text="ADD BOOK", padx=25,width=10, pady=5,command=adbo).grid(pady=3,row=0, column=0, columnspan=6)
    b1 = Button(lf, text="REMOVE BOOK", padx=25, pady=5, width=10,command=rbk).grid(pady=3,row=4, column=0, columnspan=6)
    ad.mainloop()

