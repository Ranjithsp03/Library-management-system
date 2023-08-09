from tkinter import *
import sql_quries


def rtbk():





    re=Tk()
    re.title("ADD BOOK")
    re.geometry("1920x1080")
    mf = Frame(re, padx=580,pady=305, bd=10, width=995, height=750, relief=RIDGE, bg="#114D77")
    lf = Frame(mf, bd=10, width=500, height=500, relief=RIDGE, bg="#909229")
    mf.grid()
    lf.grid(row=1, column=1)


    book_i = Label(lf, text="BOOK_ID", bg="#909229", font=("Times", 15, 'bold')).grid(row=1, column=0, padx=20,pady=10)
    book_id = Entry(lf, bd=5)
    book_id.grid(row=1, column=1, padx=20, pady=10)

    borrow_i= Label(lf, text="BORROW ID", bg="#909229", font=("Times", 15, 'bold')).grid(row=2, column=0, padx=20,pady=10)
    borrow_id= Entry(lf, bd=5)
    borrow_id.grid(row=2, column=1, padx=20, pady=10)


    def rtbook():
        sql_quries.retbook(borrow_id)
        re.destroy()

    Button(lf, text="SUBMIT", padx=20, pady=5,command=rtbook).grid(row=7, column=0, columnspan=4)
    re.mainloop()
