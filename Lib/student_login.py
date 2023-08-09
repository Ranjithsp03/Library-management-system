from tkinter import *
import bookent_click
import return_click
import sql_quries

import search_click
from PIL import ImageTk,Image


def stln(id):

    def bkentry():
        bookent_click.bkent()

    def retbk():
        return_click.rtbk()
    def search():
        search_click.mov()

    def get():
        fine=sql_quries.get_fine(id)
        Label(lf,text="Fine : "+str(fine)).grid(row=5,column=0)

    st = Tk()
    st.title("Student Page")
    st.geometry("1920x1080")
    mf = Frame(st, padx=580,pady=305, bd=10, width=995, height=750, relief=RIDGE, bg="powder blue")
    img = ImageTk.PhotoImage(Image.open("libimage7.jpg"))
    lab = Label(mf, image=img)
    lab.place(anchor="center")

    lf = Frame(mf, padx=100,pady=50,bd=10, width=500, height=500, relief=RIDGE, bg="#909229")
    mf.grid()
    lf.grid(row=1, column=1)



    b1 =Button(lf, text="SEARCH BOOKS", padx=25, width=10,pady=5,command=search).grid(pady=3,row=1, column=0, columnspan=6)
    b1 = Button(lf, text="BOOK ENTRY", padx=25, pady=5,width=10 ,command=bkentry).grid(row=2, pady=3,column=0, columnspan=6)
    b1 = Button(lf, text="RETURN BOOK", padx=25, width=10,pady=5,command=retbk ).grid(pady=3,row=3, column=0, columnspan=6)
    b1 = Button(lf, text="FINE", padx=25, pady=5, width=10,command=get).grid(pady=3,row=4, column=0, columnspan=6)
    st.mainloop()

