from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os, sys
from PIL import Image, ImageTk

def resource_path(relative_path):
    """Get the absolute path to resource for .exe compatibility"""
    try:
        base_path = sys._MEIPASS  # folder where PyInstaller stores temp files
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN WINDOW")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #imageone
        self.bg=ImageTk.PhotoImage(file=resource_path("image/Dbb.jpg"))
        
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        #imagetwo
        self.left=ImageTk.PhotoImage(file=resource_path("image/Db.jpg"))
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        #frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=650,height=500)
        #label
        lbl_Email=Label(self.root,text="Email Id",font=("goudy old style",20,'bold'),bg="white").place(x=550,y=200)
        self.txt_Email=Entry(self.root,font=("goudy old style",20,'bold'),bg="lightgrey")
        self.txt_Email.place(x=550,y=235,width=350,height=35)

        lbl_Password=Label(self.root,text="Password",font=("goudy old style",20,'bold'),bg="white").place(x=550,y=350)
        self.txt_Password=Entry(self.root,font=("goudy old style",20,'bold'),bg="lightgrey")
        self.txt_Password.place(x=550,y=385,width=350,height=35)
        #button
        self.btn_Register=Button(self.root,text='Login',font=("goudy old style",15,'bold'),bg="green",fg="white",command=self.Login)
        self.btn_Register.place(x=550,y=500,width=200,height=40)
        self.btn_NRegister=Button(self.root,text='Register New Account?',font=("goudy old style",15,'bold'),bg="red",fg="white",command=self.Register_window)
        self.btn_NRegister.place(x=550,y=450,width=200,height=40)

        lbl_style=Label(self.root,text="Welcome! your journey continues Here\nEvery login is a step toward growth",font=("goudy old style",15,'bold'),bg="darkblue",fg="white").place(x=110,y=130)


    def Register_window(self):
        self.root.destroy()
        os.system("python Register.py")


    def Login(self):
        if self.txt_Email.get()=="" or self.txt_Password.get()=="":
            messagebox.showerror("Error","Please Fill All Information",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from Register where Email=? and Password=?",(self.txt_Email.get(),self.txt_Password.get(),))
                row=cur.fetchone()
               # print(row)
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME OR PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("succesfull",f"welcome: {self.txt_Email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                    con.close()
              
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
           




root=Tk()
obj=Login(root)
root.mainloop()

