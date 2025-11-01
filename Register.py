from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Registration form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #imageBG
        self.bg=ImageTk.PhotoImage(file="image/Register.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        #image left
        self.left=ImageTk.PhotoImage(file="image/Rnew.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        #Register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=850,height=500)

       # variables
        self.var_Name=StringVar()
        self.var_LName=StringVar()
        self.var_Conatact=StringVar()
        self.var_Email=StringVar()
        self.var_Password=StringVar()
        self.var_Cpassword=StringVar()
        #labels and entry fields
        lbl_Name=Label(self.root,text="First Name",font=("goudy old style",20,'bold'),bg="white").place(x=500,y=200)
        self.txt_Name=Entry(self.root,font=("goudy old style",20,'bold'),bg="lightyellow")
        self.txt_Name.place(x=640,y=200,width=200,height=35)

        lbl_LName=Label(self.root,text="Last Name",font=("goudy old style",20,'bold'),bg="white").place(x=870,y=200)
        self.txt_LName=Entry(self.root,font=("goudy old style",20,'bold'),bg="lightyellow")
        self.txt_LName.place(x=1000,y=200,width=200,height=35)

        lbl_Contact=Label(self.root,text="Contact No",font=("goudy old style",20,'bold'),bg="white").place(x=500,y=280)
        self.txt_Contact=Entry(self.root,font=("goudy old style",20,'bold'),bg="lightyellow")
        self.txt_Contact.place(x=640,y=280,width=200,height=35)
        
        lbl_Email=Label(self.root,text="Email Id",font=("goudy old style",20,'bold'),bg="white").place(x=870,y=280)
        self.txt_Email=Entry(self.root,font=("goudy old style",20,'bold'),bg="lightyellow")
        self.txt_Email.place(x=1000,y=280,width=200,height=35)
        
        lbl_Password=Label(self.root,text="Password",font=("goudy old style",20,'bold'),bg="white").place(x=500,y=360)
        self.txt_Password=Entry(self.root,font=("goudy old style",20,'bold'),bg="lightyellow")
        self.txt_Password.place(x=640,y=360,width=200,height=35)
        
        lbl_CPassword=Label(self.root,text="Confirm Password",font=("goudy old style",20,'bold'),bg="white").place(x=870,y=360)
        self.txt_CPassword=Entry(self.root,font=("goudy old style",20,'bold'),bg="lightyellow")
        self.txt_CPassword.place(x=1100,y=360,width=200,height=35)  
        
        lbl_RH=Label(self.root,text="REGISTER HERE",font=("goudy old style",30,'bold'),bg="white",fg="green").place(x=500,y=100) 
        lbl_PR=Label(self.root,text="WELCOME TO OUR \n RESULT MANAGMENT SYSTEM",font=("goudy old style",15,'bold'),bg="lightgrey",fg="green").place(x=125,y=150)    
      # button
        self.btn_Register=Button(self.root,text='Register Now --->',font=("goudy old style",15,'bold'),bg="green",fg="white",cursor="hand2",command=self.Register_data)
        self.btn_Register.place(x=750,y=500,width=200,height=40)
        self.btn_SignIn=Button(self.root,text='Sign In',font=("goudy old style",15,'bold'),bg="blue",fg="white",cursor="hand2",command=self.Login_window)
        self.btn_SignIn.place(x=180,y=500,width=200,height=40)
      
    def clear(self):
        self.txt_Name.delete(0,END)
        self.txt_LName.delete(0,END)
        self.txt_Contact.delete(0,END)
        self.txt_Email.delete(0,END)
        self.txt_Password.delete(0,END)
        self.txt_CPassword.delete(0,END)


    def Login_window(self):
        self.root.destroy()
        os.system("python Login.py")
    
    def Register_data(self):
        if self.txt_Name.get()=="" or self.txt_LName.get()=="" or self.txt_Contact.get()=="" or self.txt_Email.get()=="" or self.txt_Password.get()=="" or self.txt_CPassword.get()=="":
            messagebox.showerror("Error","Please Fill All Information",parent=self.root)
        elif self.txt_Password.get()!=self.txt_CPassword.get():
            messagebox.showerror("Error","Password and Confirm password Should be Same",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from Register where Email=?",(self.txt_Email.get(),))
                row=cur.fetchone()
               # print(row)
                if row!=None:
                    messagebox.showerror("Error","user already Exist,please try with another Emial",parent=self.root)
                else:
                    cur.execute("insert into Register(Name,LName,Contact,Email,Password,CPassword) values(?,?,?,?,?,?)",
                            (self.txt_Name.get(),
                             self.txt_LName.get(),
                             self.txt_Contact.get(),
                             self.txt_Email.get(),
                             self.txt_Password.get(),
                             self.txt_CPassword.get(),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Succesfull","Register Succesfull",parent=self.root)
                    os.system("python Login.py")
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
           
            
root=Tk()
obj=Register(root)
root.mainloop()