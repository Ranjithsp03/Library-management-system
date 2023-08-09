from tkinter import *
import sql_quries
import admin_login

def adbk():


    add=Tk()
    add.title("ADD BOOK")
    add.geometry("1920x1080")
    mf = Frame(add, padx=590,pady=305, bd=10, width=995, height=750, relief=RIDGE, bg="#114D77")

    lf = Frame(mf, bd=10, width=500, height=500, relief=RIDGE, bg="#909229")
    mf.grid()
    lf.grid(row=1, column=0)


    book_i = Label(lf, text="BOOK_ID", bg="#909229", font=("Times", 15, 'bold')).grid(row=1, column=0, padx=20,pady=10)
    book_id = Entry(lf, bd=5)
    book_id.grid(row=1, column=1, padx=20, pady=10)

    book_n= Label(lf, text="BOOK NAME", bg="#909229", font=("Times", 15, 'bold')).grid(row=2, column=0, padx=20,pady=10)
    book_name= Entry(lf, bd=5)
    book_name.grid(row=2, column=1, padx=20, pady=10)

    editi = Label(lf, text="EDITION", bg="#909229", font=("Times", 15, 'bold')).grid(row=3, column=0, padx=20,pady=10)
    edition= Entry(lf, bd=5)
    edition.grid(row=3, column=1, padx=20, pady=10)

    author= Label(lf, text="AUTHOR NAME", bg="#909229", font=("Times", 15, 'bold')).grid(row=4, column=0, padx=20,pady=10)
    author_name= Entry(lf, bd=5)
    author_name.grid(row=4, column=1, padx=20, pady=10)

    vol= Label(lf, text="VOLUME", bg="#909229", font=("Times", 15, 'bold')).grid(row=5, column=0, padx=20,pady=10)
    volume= Entry(lf, bd=5)
    volume.grid(row=5, column=1, padx=20, pady=10)

    avail = Label(lf, text="AVAILABILITY", bg="#909229", font=("Times", 15, 'bold')).grid(row=6, column=0, padx=20,                                                                                      pady=10)
    availability = Entry(lf, bd=5)
    availability.grid(row=6, column=1, padx=20, pady=10)

    quan= Label(lf, text="QUANTITY", bg="#909229", font=("Times", 15, 'bold')).grid(row=7, column=0, padx=20, pady=10)
    quantity = Entry(lf, bd=5)
    quantity.grid(row=7, column=1, padx=20, pady=10)

    def addbk():
        sql_quries.abook(book_id,book_name,edition,author_name,volume,availability,quantity)
        add.destroy()
    Button(lf, text="SUBMIT", padx=20, pady=5,command=addbk).grid(row=8, column=0, columnspan=4)
    add.mainloop()
