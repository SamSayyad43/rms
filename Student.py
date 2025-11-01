from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("STUDENT RESULT MANAGMENT SYSTEM")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        title=Label(self.root,text="MANAGE STUDENT DETAILS",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)
       #variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_Email=StringVar()
        self.var_Gender=StringVar()
        self.var_state=StringVar()
        self.var_Address=StringVar()
        self.var_DOB=StringVar()
        self.var_Contact=StringVar()
        self.var_SelectCourse=StringVar()
        self.var_AdmissionDate=StringVar()
        self.var_City=StringVar()
        #widgets
        lbl_roll=Label(self.root,text="roll No",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=60)
        lbl_DOB=Label(self.root,text="D.O.B(dd-mm-yy)",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=60)
        lbl_name=Label(self.root,text="name",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=100)
        lbl_Contact=Label(self.root,text="Contact No",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=100)
        lbl_Email=Label(self.root,text="Email",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=140)
        lbl_Course=Label(self.root,text="Course",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=140)
        lbl_Gender=Label(self.root,text="Gender",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=180)
        lbl_AdmissionDate=Label(self.root,text="Admission Date",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=180)
        lbl_state=Label(self.root,text="state",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=220)
        lbl_City=Label(self.root,text="City",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=220)
        lbl_Address=Label(self.root,text="Address",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=260)
        #Entry fealds
        self.Course_list=[]
        self.fetch_Course()
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_roll.place(x=150,y=60,width=200)
        txt_DOB=Entry(self.root,textvariable=self.var_DOB,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=510,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=150,y=100,width=200)
        txt_Contact=Entry(self.root,textvariable=self.var_Contact,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=510,y=100,width=200)
        txt_Email=Entry(self.root,textvariable=self.var_Email,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=150,y=140,width=200)
        self.txt_Course=ttk.Combobox(self.root,textvariable=self.var_SelectCourse,values=(self.Course_list ),font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_Course.place(x=510,y=140,width=200)
        self.txt_Course.set("Empty")
        self.txt_Gender=ttk.Combobox(self.root,textvariable=self.var_Gender,values=("Select","Male","Female","Other"),font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_Gender.place(x=150,y=180,width=200)
        self.txt_Gender.current(0)
        txt_AdmissionDate=Entry(self.root,textvariable=self.var_AdmissionDate,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=510,y=180,width=200)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=150,y=220,width=200)
        txt_City=Entry(self.root,textvariable=self.var_City,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=510,y=220,width=200)
        self.txt_Address=Text(self.root,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_Address.place(x=150,y=260,width=560,height=100)
        #buttons
        self.btn_add=Button(self.root,text='Save',font=("goudy old style",15,'bold'),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_Update=Button(self.root,text='Update',font=("goudy old style",15,'bold'),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_Update.place(x=270,y=400,width=110,height=40)
        self.btn_Delete=Button(self.root,text='Delete',font=("goudy old style",15,'bold'),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_Delete.place(x=390,y=400,width=110,height=40)
        self.btn_Clear=Button(self.root,text='Clear',font=("goudy old style",15,'bold'),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_Clear.place(x=510,y=400,width=110,height=40)
        #search pannel
        self.var_search=StringVar()
        lbl_roll=Label(self.root,text="roll No",font=("goudy old style",15,'bold'),bg='white').place(x=790,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=870,y=60,width=180)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,'bold'),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
        #content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","Email","Gender","state","Address","DOB","Contact","City","Course","AdmissionDate"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll",text="roll")
        self.CourseTable.heading("name",text="name")
        self.CourseTable.heading("Email",text="Email")
        self.CourseTable.heading("Gender",text="Gender")
        self.CourseTable.heading("state",text="state")
        self.CourseTable.heading("Address",text="Address")
        self.CourseTable.heading("DOB",text="DOB")
        self.CourseTable.heading("Contact",text="Contact")
        self.CourseTable.heading("City",text="City")
        self.CourseTable.heading("Course",text="Course")
        self.CourseTable.heading("AdmissionDate",text="AdmissionDate")
        self.CourseTable["show"]='headings'

        self.CourseTable.column("roll",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("Email",width=100)
        self.CourseTable.column("Gender",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("Address",width=100)
        self.CourseTable.column("DOB",width=100)
        self.CourseTable.column("Contact",width=100)
        self.CourseTable.column("City",width=100)
        self.CourseTable.column("Course",width=100)
        self.CourseTable.column("AdmissionDate",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #=======
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_Email.set("")
        self.var_Gender.set("Select")
        self.var_state.set("")
        self.txt_Address.delete('1.0',END)
        self.txt_Address.config(state=NORMAL)
        self.var_DOB.set("")
        self.var_Contact.set("")
        self.var_SelectCourse.set("Select")
        self.var_City.set("")
        self.var_AdmissionDate.set("")
        self.var_search.set("")
    def delete(self):
         con=sqlite3.connect(database="rms.db")
         cur=con.cursor()
         try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","roll number should be required",parent=self.root)
            else:
                cur.execute("select * from Student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","please select Student from list first",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from Student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("delete","Student deleted succesfully",parent=self.root)
                        self.clear()
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        
    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        self.txt_roll
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
       # print(row)
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_Email.set(row[2])
        self.var_Gender.set(row[3])
        self.var_state.set(row[4])
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END,row[5])
        self.var_DOB.set(row[6])
        self.var_Contact.set(row[7])
        self.var_City.set(row[8])
        self.var_SelectCourse.set(row[9])
        self.var_AdmissionDate.set(row[10])
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","roll No should be required",parent=self.root)
            else:
                cur.execute("select * from Student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","roll No already present",parent=self.root)
                else:
                    cur.execute("insert into Student(roll,name,Email,Gender,state,Address,DOB,Contact,City,Course,AdmissionDate) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_Email.get(),
                        self.var_Gender.get(),
                        self.var_state.get(),
                        self.txt_Address.get("1.0",END),
                        self.var_DOB.get(),
                        self.var_Contact.get(),
                        self.var_City.get(),
                        self.var_SelectCourse.get(),
                        self.var_AdmissionDate.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("success","Student added succesfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Student roll number should be required",parent=self.root)
            else:
                cur.execute("select * from Student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select Student from list",parent=self.root)
                else:
                    cur.execute("update Student set name=?,Email=?,Gender=?,state=?,Address=?,DOB=?,Contact=?,AdmissionDate=?,City=?,Course=? where roll=?",(
                        self.var_name.get(),
                        self.var_Email.get(),
                        self.var_Gender.get(),
                        self.var_state.get(),
                        self.txt_Address.get("1.0",END),
                        self.var_DOB.get(),
                        self.var_Contact.get(),
                        self.var_AdmissionDate.get(),
                        self.var_City.get(),
                        self.var_SelectCourse.get(),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("success","Student update succesfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from Student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def fetch_Course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from Course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.Course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from Student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","record not found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()