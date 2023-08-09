from tkinter import *
import datetime
from tkcalendar import *
import time
import sql_quries

from PIL import ImageTk,Image

def bkent():

    def bkentry():
        sql_quries.brbook(borrow_date,borrow_id,book_id)

    bent = Tk()
    bent.title("REMOVE BOOK")
    bent.geometry("1920x1080")
    mf = Frame(bent, padx=585, pady=305, bd=10, width=995, height=750, relief=RIDGE, bg="#114D77")

    lf = Frame(mf, bd=10, width=500, height=500, relief=RIDGE, bg="#909229")
    mf.grid()
    lf.grid(row=1, column=1)

    borr_date = Label(lf, text="BORROW DATE", bg="#909229", font=("Times", 15, 'bold')).grid(row=1, column=0, padx=20,pady=10)
    borrow_date = DateEntry(lf,date_pattern="yyyy-mm-dd")
    borrow_date.grid(row=1, column=1, padx=20, pady=10)


    b_id = Label(lf, text="BORROW_ID", bg="#909229", font=("Times", 15, 'bold')).grid(row=2, column=0, padx=20,pady=10)
    borrow_id = Entry(lf, bd=5)
    borrow_id.grid(row=2, column=1, padx=20, pady=10)


    book_i = Label(lf, text="BOOK_ID", bg="#909229", font=("Times", 15, 'bold')).grid(row=3, column=0, padx=20,pady=10)
    book_id = Entry(lf, bd=5)
    book_id.grid(row=3, column=1, padx=20, pady=10)
    cf=Frame(mf)
    cf.grid(row=1,column=2)

    Button(lf, text="SUBMIT", padx=20, pady=5, command=bkentry).grid(row=4, column=0, columnspan=4)

    bent.mainloop()


