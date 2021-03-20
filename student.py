from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x750+0+0")

        title=Label(root, text="STUDENT MANAGEMENT SYSTEM", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"),bg="yellow", fg="red")
        title.pack(side=TOP,fill=X)

#===========All Variables=============

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

#==========Manage Frame================

        manage_frame=Frame(self.root, bd=4, relief=RIDGE,bg='red')
        manage_frame.place(x=20, y=100, width=450, height=660)

        m_title=Label(manage_frame, text='Manage Students',bg='red',fg='white',font=('times new roman',30,'bold'))
        m_title.grid(row=0, columnspan=2, padx=10,pady=20)

        lbl_roll=Label(manage_frame, text='Roll No.', bg='red', fg='white', font=('times new roman',20,'bold'))
        lbl_roll.grid(row=1,column=0,padx=10,pady=10,sticky='w')

        txt_roll=Entry(manage_frame, textvariable=self.Roll_No_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,padx=10,pady=10)

        lbl_name=Label(manage_frame,text='Name',bg='red', fg='white',font=('times new roman',20,'bold'))
        lbl_name.grid(row=2,column=0,padx=10,pady=10,sticky='w')

        txt_name=Entry(manage_frame, textvariable=self.name_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,padx=10,pady=10)

        lbl_email=Label(manage_frame,text='Email',bg='red', fg='white',font=('times new roman',20,'bold'))
        lbl_email.grid(row=3,column=0,padx=10,pady=10,sticky='w')

        txt_email=Entry(manage_frame,textvariable=self.email_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1)

        lbl_gender=Label(manage_frame,text='Gender', bg='red',fg='white',font=('times new roman',20,'bold'))
        lbl_gender.grid(row=4,column=0,padx=10,pady=10,sticky='w')

        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var,font=('times new roman',13,'bold'),state='readonly')
        combo_gender['values']=('Male','Female','Others')
        combo_gender.grid(row=4,column=1,padx=10,pady=10,sticky='w')

        lbl_contact=Label(manage_frame,text='Contact', bg='red',fg='white',font=('times new roman',20,'bold'))
        lbl_contact.grid(row=5,column=0,padx=10,pady=10,sticky='w')

        txt_contact=Entry(manage_frame,textvariable=self.contact_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1)

        lbl_DOB=Label(manage_frame,text='D.O.B', bg='red',fg='white',font=('times new roman',20,'bold'))
        lbl_DOB.grid(row=6,column=0,padx=10,pady=10,sticky='w')

        txt_DOB=Entry(manage_frame, textvariable=self.dob_var, font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1)

        lbl_address=Label(manage_frame,text='Address', bg='red',fg='white',font=('times new roman',20,'bold'))
        lbl_address.grid(row=7,column=0,padx=10,pady=10,sticky='w')

        self.txt_address=Text(manage_frame,width=30,height=5,font=("",10))
        self.txt_address.grid(row=7,column=1,padx=10,pady=10,sticky='w')

#=========Button Frame===========

        btn_frame=Frame(manage_frame, bd=4, relief=RIDGE,bg='red')
        btn_frame.place(x=15, y=570, width=420)

        addbtn=Button(btn_frame,text='ADD',width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text='UPDATE',command=self.update_data,width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_frame,text='DELETE',command=self.delete_data,width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text='CLEAR',command=self.clear,width=10).grid(row=0,column=3,padx=10,pady=10)


#===========Detail Frame================

        detail_frame=Frame(self.root, bd=4, relief=RIDGE, bg='red')
        detail_frame.place(x=500,y=100, width=1000, height=660)

        lbl_search=Label(detail_frame,text='Search by', bg='red',fg='white',font=('times new roman',20,'bold'))
        lbl_search.grid(row=0,column=0,padx=10,pady=10,sticky='w')

        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=('times new roman',14,'bold'),state='readonly')
        combo_search['values']=('Roll_no','Name','Contact')
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search=Entry(detail_frame,textvariable=self.search_txt,width=20,font=('times new roman',12,'bold'),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,padx=10,pady=10)

        searchbtn=Button(detail_frame,command=self.search_data,text='Search',width=10,pady=5).grid(row=0,column=3,padx=15,pady=10)
        showbtn=Button(detail_frame,text='Show all',command=self.search_data,width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)


#=================Table Frame===========

        Table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg='red')
        Table_frame.place(x=10,y=70,width=950,height=550)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,columns=('roll','name','email','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('roll',text='Roll No.')
        self.student_table.heading('name',text='Name')
        self.student_table.heading('email',text='Email')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('contact',text='Contact')
        self.student_table.heading('dob',text='D.O.B')
        self.student_table.heading('address',text='Address')
        self.student_table['show']='headings'
        self.student_table.column('roll',width=50)
        self.student_table.column('name',width=100)
        self.student_table.column('email',width=150)
        self.student_table.column('gender',width=80)
        self.student_table.column('contact',width=100)
        self.student_table.column('dob',width=80)
        self.student_table.column('address',width=400)

        self.student_table.pack(fill=BOTH,expand=2)
        self.student_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

#============hosting databse===========
    def add_students(self):
        if self.Roll_No_var.get()=='' or self.name_var.get()=='' or self.email_var.get()=='' or self.gender_var.get()=='' or self.contact_var.get()=='' or self.dob_var.get()=='' or self.txt_address.delete('1.0',END)!='':
            messagebox.showerror('ERROR','All fields are required!!')
        else:
            con=pymysql.connect(host='localhost',user='root',password='',database='stm')            #database connection
            cur=con.cursor()
            cur.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s)',(self.Roll_No_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_address.get('1.0',END)
                                                                            ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo('SUCCESS','Record has been inserted Successfully!')
        
   
    def fetch_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute('select * from students')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

   
    def clear(self):
        self.Roll_No_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.gender_var.set('')
        self.contact_var.set('')
        self.dob_var.set('')
        self.txt_address.delete('1.0',END)

    
    def get_cursor(self,event):                             #where event is an argument
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        # print(row)
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[6])


    def update_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute('update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s',(
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_address.get('1.0',END),
                                                                         self.Roll_No_var.get()
                                                                        ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo('UPDATE', 'Record has been inserted Successfully!')


    def delete_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute('delete from students where roll_no=%s',self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo('DELETE','Rescord has been deleted Successfully!')



    def search_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute('select * from students where '+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()






        

root=Tk()
ob=Student(root)
root.mainloop()
