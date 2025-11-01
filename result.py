from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("STUDENT RESULT MANAGMENT SYSTEM")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #title
        title=Label(self.root,text="Add Student Result",font=("goudy old style",20,"bold"),bg="orange").place(x=0,y=15,width=1200,height=60)
       # variables
        self.var_Roll=StringVar()
        self.var_Name=StringVar()
        self.var_Course=StringVar()
        self.var_Marks=StringVar()
        self.var_FullMarks=StringVar()
       # widgets
        lbl_Roll=Label(self.root,text="Student Roll No",font=("goudy old style",20,'bold'),bg='white').place(x=80,y=95)
        lbl_Name=Label(self.root,text="Name",font=("goudy old style",20,'bold'),bg='white').place(x=80,y=160)
        lbl_Course=Label(self.root,text="Course",font=("goudy old style",20,'bold'),bg='white').place(x=80,y=220)
        lbl_Marks=Label(self.root,text="Marks obtained",font=("goudy old style",20,'bold'),bg='white').place(x=80,y=280)
        lbl_FullMarks=Label(self.root,text="Full Marks",font=("goudy old style",20,'bold'),bg='white').place(x=80,y=340)
      # Entry fields
        self.Roll_list=[]
        self.fetch_Roll()
        self.txt_Roll=ttk.Combobox(self.root,textvariable=self.var_Roll,values=(self.Roll_list),font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_Roll.place(x=280,y=100,width=200)
        self.txt_Roll.set("Select")
        txt_Name=Entry(self.root,textvariable=self.var_Name,font=("goudy old style",20,'bold'),state='readonly',bg='lightyellow').place(x=280,y=160,width=340)
        txt_Course=Entry(self.root,textvariable=self.var_Course,font=("goudy old style",20,'bold'),state='readonly',bg='lightyellow').place(x=280,y=220,width=340)
        txt_Marks=Entry(self.root,textvariable=self.var_Marks,font=("goudy old style",20,'bold'),bg='lightyellow').place(x=280,y=280,width=340)
        txt_FullMarks=Entry(self.root,textvariable=self.var_FullMarks,font=("goudy old style",20,'bold'),bg='lightyellow').place(x=280,y=340,width=340)
     # Search panel
        self.var_search=StringVar()
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,'bold'),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=120,height=28) 
     #image
        self.bg_img=Image.open("image/result.jpg")
        self.bg_img=self.bg_img.resize((626,352),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=650,y=110,width=500,height=300)
    #Button
        self.btn_Submit=Button(self.root,text='Submit',font=("goudy old style",15,'bold'),bg="#067511",fg="white",cursor="hand2",command=self.add)
        self.btn_Submit.place(x=380,y=400,width=110,height=40)
        self.btn_Clear=Button(self.root,text='Clear',font=("goudy old style",15,'bold'),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_Clear.place(x=510,y=400,width=110,height=40)
    # fetch
    def fetch_Roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from Student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.Roll_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name,Course from Student where roll=?",(self.var_Roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_Name.set(row[0])
                self.var_Course.set(row[1])
            else:
                messagebox.showerror("Error","record not found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_Name.get()=="":
                messagebox.showerror("Error","please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where Roll=?",(self.var_Roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","result already present",parent=self.root)
                else:
                    per=(int(self.var_Marks.get())*100)/int(self.var_FullMarks.get())
                    cur.execute("insert into result (Roll,Name,Course,Marks_ob,FullMarks,per) values(?,?,?,?,?,?)",(
                        self.var_Roll.get(),
                        self.var_Name.get(),
                        self.var_Course.get(),
                        self.var_Marks.get(),
                        self.var_FullMarks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("success","result added succesfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def clear(self):
        self.var_Roll.set("Select"),
        self.var_Name.set(""),
        self.var_Course.set(""),
        self.var_Marks.set(""),
        self.var_FullMarks.set(""),

if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()