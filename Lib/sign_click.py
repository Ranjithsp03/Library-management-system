from tkinter import *
import sql_quries
import login_click
from PIL import ImageTk,Image

def snpg():

    ln = Tk()
    ln.title("Sign_up Page")
    ln.geometry("1920x1080")
    mf = Frame(ln, padx=580,pady=305, bd=10, width=995, height=750, relief=RIDGE, bg="sky blue")
    img = ImageTk.PhotoImage(Image.open("libimage6.jpg"))
    lab = Label(mf, image=img)
    lab.place(anchor="center")

    lf = Frame(mf, bd=10, width=500, height=500, relief=RIDGE, bg="#909229")
    mf.grid()
    lf.grid(row=1, column=1)

    user_i = Label(lf, text="USER_ID", bg="#909229", font=("Times", 15, 'bold')).grid(row=1, column=0, padx=20,pady=10)
    user_id = Entry(lf, bd=5)
    user_id.grid(row=1, column=1, padx=20, pady=10)

    user_n= Label(lf, text="USERNAME", bg="#909229", font=("Times", 15, 'bold')).grid(row=2, column=0, padx=20,pady=10)
    user_name= Entry(lf, bd=5)
    user_name.grid(row=2, column=1, padx=20, pady=10)

    dept = Label(lf, text="DEPARTMENT", bg="#909229", font=("Times", 15, 'bold')).grid(row=3, column=0, padx=20,pady=10)
    department = Entry(lf, bd=5)
    department.grid(row=3, column=1, padx=20, pady=10)

    desgn= Label(lf, text="DESIGNATION", bg="#909229", font=("Times", 15, 'bold')).grid(row=4, column=0, padx=20,pady=10)
    designation= Entry(lf, bd=5)
    designation.grid(row=4, column=1, padx=20, pady=10)

    pas = Label(lf, text="PASSWORD", bg="#909229", font=("Times", 15, 'bold')).grid(row=5, column=0, padx=20,pady=10)
    password = Entry(lf, bd=5)
    password.grid(row=5, column=1, padx=20, pady=10)
    def dest():
        sql_quries.signup(user_id, user_name, department, designation, password)
        ln.destroy()
        login_click.lnpg()

    Button(lf, text="SUBMIT", padx=20, pady=5,command=dest).grid(row=7, column=0, columnspan=4)
    ln.mainloop()
