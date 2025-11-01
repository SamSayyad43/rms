from tkinter import *
from PIL import Image,ImageTk
from course import Courseclass
from Student import StudentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import sqlite3
import sys
class dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title("STUDENT RESULT MANAGMENT SYSTEM")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #icon
        img=Image.open("Image/logo.png")
        img=img.resize((100,50),Image.LANCZOS)
        self.logo_dash=ImageTk.PhotoImage(img)

       #hello
        #title
        title=Label(self.root,text="STUDENT RESULT MANAGMENT SYSTEM",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #menu
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)
        #button
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#065377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_Student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#065377",fg="white",cursor="hand2",command=self.add_Student).place(x=240,y=5,width=200,height=40)
        btn_Result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#065377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_View=Button(M_Frame,text="View student result",font=("goudy old style",15,"bold"),bg="#065377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_Logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#065377",fg="white",cursor="hand2",command=self.Logout).place(x=900,y=5,width=200,height=40)
        btn_Exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#065377",fg="white",cursor="hand2",command=self.Exit).place(x=1120,y=5,width=200,height=40)
        #image
        self.bg_img=Image.open("image/bg.jpg")
        self.bg_img=self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)
        #deatil
        self.lbl_Course=Label(self.root, text="TOTAL COURSE\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white",cursor="hand2")
        self.lbl_Course.place(x=400, y=530, width=300, height=100)
        self.lbl_Student=Label(self.root, text="TOTAL STUDENTS\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white",cursor="hand2")
        self.lbl_Student.place(x=710, y=530, width=300, height=100)
        self.lbl_Result=Label(self.root, text="TOTAL RESULT\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white",cursor="hand2")
        self.lbl_Result.place(x=1020, y=530, width=300, height=100)
        #footer
        footer=Label(self.root, text="STUDENT RESULT MANAGEMENT SYSTEM\nIf any issue contact: 8317352806", font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.Update_details()

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Courseclass(self.new_win)
    def add_Student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def Logout(self):
        op=messagebox.askyesno("Confirm","Do you Realy want to Logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python Login.py")

    def Exit(self):
        op=messagebox.askyesno("Confirm","Do you Realy want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            sys.exit()
            



    def Update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_Course.config(text=f"TOTAL COURSES\n[{str(len(cr))}]")

            cur.execute("select * from Student")
            cr=cur.fetchall()
            self.lbl_Student.config(text=f"TOTAL STUDENTS\n[{str(len(cr))}]")
   
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_Result.config(text=f"TOTAL RESULTS\n[{str(len(cr))}]")
            self.lbl_Course.after(200,self.Update_details)

            

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    



if __name__=="__main__":
    root=Tk()
    obj=dashboard(root)
    root.mainloop()