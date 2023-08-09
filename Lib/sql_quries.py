import tkinter as tk
from tkinter import messagebox
import mysql.connector
import login_click
import datetime
from datetime import datetime,timedelta

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="R@nj!th66",
    database="lib"
)
cursor = conn.cursor()


def signup(user_id, user_name, department, designation, password):
    userid = user_id.get()
    usern = user_name.get()
    dept = department.get()
    desg = designation.get()
    passw = password.get()

    query = "INSERT INTO users (User_ID, User_Name, Dept, Designation, Password) values(%s,%s,%s,%s,%s)"
    val=(userid, usern, dept, desg, passw)
    cursor.execute(query,val)
    cursor.fetchall()
    messagebox.showinfo("Sucessful", "you are added !")
    conn.commit()

def abook(book_id,book_name,edition,author_name,volume,availability,quantity):
    bookid =book_id.get()
    bookname=book_name.get()
    edi=edition.get()
    auth=author_name.get()
    volu=volume.get()
    availa=availability.get()
    quant=quantity.get()
    query = "INSERT INTO books (book_id,book_name,edition,author_name,volumes,availability,quantity) values(%s,%s,%s,%s,%s,%s,%s)"
    val=(bookid,bookid,edi,auth,volu,availa,quant)
    cursor.execute(query,val)
    cursor.fetchall()
    messagebox.showinfo("Sucess","Book Added Successfully!")
    conn.commit()


def removebk(book_id):
    bookid =book_id.get()
    query="DELETE from books Where book_id=%s"
    val=(bookid,)
    cursor.execute(query,val)
    messagebox.showinfo("Sucess", "Book Removed Successfully!")
    conn.commit()



def retbook(borrow_id):
    borrowid =borrow_id.get()
    query="UPDATE  borrows set Return_date=curdate() where  Borrower_id=%s "
    val=(borrowid,)
    cursor.execute(query,val)
    messagebox.showinfo("Sucess", "Book Returned Successfully!")
    conn.commit()

def brbook(borrow_date,borrow_id,book_id):
    borrowdate = borrow_date.get()
    d=str(borrowdate)
    ye=int(d[:4])
    mon=int(d[5:7])
    da=int(d[8:])
    dur=datetime(year=ye,month=mon,day=da)
    print(dur)
    duedate=dur+timedelta(days=10)
    borrowid = borrow_id.get()
    bookid = book_id.get()
    query = "SELECT Availability FROM books WHERE Book_id = %s"
    val=(bookid,)

    cursor.execute(query,val)
    availability = cursor.fetchone()

    if availability[0]!=0:
        bookid = book_id.get()
        query = "UPDATE books SET Availability = Availability-1 WHERE Book_id =%s"
        val=(bookid,)

        cursor.execute(query,val)
        conn.commit()

        query = "INSERT INTO borrows (Borrow_date, Due_date, Borrower_id, Book_id) values(%s,%s,%s,%s)"
        val=(borrowdate, duedate, borrowid, bookid)
        cursor.execute(query,val)
        conn.commit()

        messagebox.showinfo("Success", "Book borrowed successfully!")
    else:
        messagebox.showerror("Error", "Book not available for borrowing")

def get_fine(id):
    query="select Due_date from borrows where Borrower_id=%s"
    val=(id,)
    try:
        cursor.execute(query,val)
        arr=cursor.fetchall()
        fin=0
        cur=datetime.now()
        for i in arr:
            d = datetime.combine(i[0], datetime.min.time())
            day = (cur - d).days
            print(day)
            if day>0:
                fin+=day*0.2
        return int(fin)
    except Exception as e:
        messagebox.showerror("Error",e)



def search(mn):
    bookname=mn.get()
    query=("select Book_name,Availability,Quantity from books where book_name=%s;")
    val=(bookname,)
    cursor.execute(query,val)
    return cursor.fetchall()