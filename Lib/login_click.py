from tkinter import *
import admin_login
import student_login
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="R@nj!th66",
    database="lib"
)

cursor = conn.cursor()
def lnpg():

    ln=Tk()
    ln.title("Login Page")
    ln.geometry("1920x1080")
    mf = Frame(ln, padx=590,pady=305, bd=10, width=995, height=750, relief=RIDGE, bg="powder blue")

    img = ImageTk.PhotoImage(Image.open("libimage2.jpg"))
    lab = Label(mf, image=img)
    lab.image=img
    lab.place(anchor="center")

    lf = Frame(mf, bd=10, width=500, height=500,pady=20,padx=20, relief=RIDGE, bg="#909229")
    mf.grid()
    lf.grid(row=1, column=0)

    def check(usern, password):
        username = usern.get()
        passw = password.get()
        query = "SELECT user_id,designation FROM users where user_name=%s and password=%s"
        val=(username,passw)
        cursor.execute(query,val)
        user = cursor.fetchall()

        if(user):
            if (user[0][1]=="ADMIN"):
                messagebox.showinfo("Login Sucessful", "Welcome " + username + "!")
                ln.destroy()
                admin_login.adln()
            else:
                messagebox.showinfo("Login Sucessful", "Welcome " + username + "!")
                ln.destroy()
                student_login.stln(user[0][0])
        else:
            messagebox.showerror("Authentication Error", "Invalid username or password")

    c=IntVar(value=0)
    def show():
        if(c.get()==1):
            password.config(show='')
        else:
            password.config(show='*')

    c1=Checkbutton(lf,text="show password",variable=c,onvalue=1,bg="#909229",offvalue=0,command=show)
    c1.grid(row=3,column=1)

    user_n = Label(lf, text="Username", bg="#909229", font=("Times", 15, 'bold')).grid(row=1, column=0, padx=20,pady=10)
    user = Entry(lf, bd=5)
    user.grid(row=1, column=1, padx=20, pady=10)

    pas = Label(lf, text="Password", bg="#909229", font=("Times", 15, 'bold')).grid(row=2, column=0, padx=20,pady=10)
    password = Entry(lf, show="*", bd=5)
    password.grid(row=2, column=1, padx=20, pady=10)


    Button(lf, text="LOGIN", padx=20, pady=5,font=("Times", 15, 'bold'), command=lambda: check(user,password)).grid(row=7, column=0,pady=6, columnspan=4)
    ln.mainloop()
