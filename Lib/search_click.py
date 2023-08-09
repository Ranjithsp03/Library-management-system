from tkinter import *
import sql_quries
def mov():
    sp=Tk()
    sp.title("Search")
    sp.geometry("1920x1080")
    sf=Frame(sp,padx=225,pady=240,bd=10,width=795,height=645,relief=RIDGE,bg="#114D77")
    sf.grid()
    bf = Frame(sf, bd=10, width=500, height=400, relief=RIDGE, padx=43, pady=50, bg="#909229")
    bf.grid(row=1, column=0)
    Label(bf, text="Enter the Book Name",font=("Times", 15),bg="#909229").grid(row=1, column=0, padx=20, pady=10)
    mn = Entry(bf, bd=5,width=25)
    mn.grid(row=1, column=1)
    def result():
        rf=Frame(sf,bd=10,width=500,height=400,relief=RIDGE,padx=43,pady=50,bg="#909229")
        rf.grid(row=1,column=2,padx=50)
        res=sql_quries.search(mn)
        lab=["NAME","AVAILABILITY","QUANTITY"]
        for i in range(3):
            Label(rf, font=("Times", 20, 'bold'), text=lab[i], bd=7, bg="#909229").grid(row=i, column=0)
            Label(rf, font=("Times", 20, 'bold'), text=" : ", bd=7, bg="#909229").grid(row=i, column=1)
            Label(rf,font=("Times",20),text=res[0][i],bd=7,bg="#909229").grid(row=i,column=2)

    Button(bf, text="SEARCH", bd=7,width=5, padx=30, pady=5,command=result).grid(row=5, column=0,columnspan=2)
    sp.mainloop()
