from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("student")

        ##########Variable#########
        self.var_dep = StringVar()
        
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_name = StringVar()
        self.var_std_id = StringVar()
        self.var_email = StringVar()
        self.var_num = StringVar()
        self.var_address = StringVar()
        self.var_dob = StringVar()
        self.var_gender = StringVar()

        self.var_roll = StringVar()

        # first image
        img = Image.open(r"D:\Face Recoginition Attendance system\Images\student.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(r"D:\Face Recoginition Attendance system\Images\mid.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"D:\Face Recoginition Attendance system\Images\student1.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # bg image

        img3 = Image.open(r"D:\Face Recoginition Attendance system\Images\bg.jpg")
        img3 = img3.resize((1500, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1500, height=710)

        # Title
        title_lbl = Label(
            bg_img,
            text="STUDENT'S MANAGEMENT SYSTEM ",
            font=("times new  roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1350, height=45)

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1480, height=600)

        # Left frame

        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Students Detail",
            font=("times new  roman", 18, "bold"),
            fg="green",
        )
        left_frame.place(x=10, y=10, width=660, height=560)

        # Right frame

        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Students Detail",
            font=("times new  roman", 18, "bold"),
            fg="black",
        )
        right_frame.place(x=700, y=10, width=560, height=580)

        # current course
        current_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Course Information",
            font=("times new  roman", 18, "bold"),
            fg="black",
        )
        current_frame.place(x=10, y=0, width=620, height=140)

        # Department
        dep_label = Label(
            current_frame,
            text="Department",
            font=("times new  roman", 18, "bold"),
            fg="black",
        )
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(
            current_frame,
            textvariable=self.var_dep,
            font=("times new  roman", 10, "bold"),
            state="readonly",
        )
        dep_combo["values"] = (
            "Select Department",
            "Computer",
            "Civil",
            "Mechanical",
            "Electrical",
            "Agricultural",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # year
        year_label = Label(
            current_frame,
            text="Year",
            font=("times new  roman", 18, "bold"),
            fg="black",
        )
        year_label.grid(row=0, column=3, padx=10, sticky=W)

        year_combo = ttk.Combobox(
            current_frame,
            textvariable=self.var_year,
            font=("times new  roman", 10, "bold"),
            state="readonly",
        )
        year_combo["values"] = (
            "Select Year",
            "First",
            "Second",
            "Third",
            "Fourth",
            "Fifth",
        )
        year_combo.current(0)
        year_combo.grid(row=0, column=4, padx=2, pady=10, sticky=W)

        # semester
        semester_label = Label(
            current_frame,
            text="Semester",
            font=("times new  roman", 18, "bold"),
            fg="black",
        )
        semester_label.grid(row=2, column=0, padx=10, sticky=W)

        semester_combo = ttk.Combobox(
            current_frame,
            textvariable=self.var_semester,
            font=("times new  roman", 10, "bold"),
            state="readonly",
        )
        semester_combo["values"] = (
            "Select Semester",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
        )
        semester_combo.current(0)
        semester_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # student information
        class_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student's Information",
            font=("times new  roman", 16, "bold"),
            fg="red",
        )
        class_frame.place(x=10, y=140, width=640, height=320)

        # Student ID
        studentid_label = Label(
            class_frame,
            text="StudentID:",
            font=("times new  roman", 13, "bold"),
            fg="black",
        )
        studentid_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentid_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_std_id,
            width=16,
            font=("times new  roman", 13, "bold"),
        )
        studentid_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        studentname_label = Label(
            class_frame,
            text="Student Name:",
            font=("times new  roman", 13, "bold"),
            fg="black",
        )
        studentname_label.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        studentname_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_std_name,
            width=19,
            font=("times new  roman", 13, "bold"),
        )
        studentname_entry.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        # Rollnu
        studentrollnum_label = Label(
            class_frame,
            text="Roll No:",
            font=("times new  roman", 13, "bold"),
            fg="black",
        )
        studentrollnum_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        studentrollnum_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_roll,
            width=16,
            font=("times new  roman", 13, "bold"),
        )
        studentrollnum_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Gender
        studentgender_label = Label(
            class_frame,
            text="Gender:",
            font=("times new  roman", 13, "bold"),
            fg="black",
        )
        studentgender_label.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # studentgender_entry = ttk.Entry(
        #     class_frame,
        #     textvariable=self.var_gender,
        #     width=16,
        #     font=("times new  roman", 13, "bold"),
        # )
        # studentgender_entry.grid(row=2, column=4, padx=10, pady=5, sticky=W)
        
        studentgender_combo = ttk.Combobox(
            class_frame,
            textvariable=self.var_semester,
            font=("times new  roman", 10, "bold"),
            state="readonly",
        )
        
        studentgender_combo["values"] = (
            "Male",
            "Female",
            "Others",
            
        )
        studentgender_combo.current(0)
        studentgender_combo.grid(row=2, column=4, padx=2, pady=10, sticky=W)

        
        
        

        # DOB
        studentrolldob_label = Label(
            class_frame, text="DOB:", font=("times new  roman", 13, "bold"), fg="black"
        )
        studentrolldob_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        studentrolldob_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_dob,
            width=16,
            font=("times new  roman", 13, "bold"),
        )
        studentrolldob_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Address
        studentaddress_label = Label(
            class_frame,
            text="Address:",
            font=("times new  roman", 13, "bold"),
            fg="black",
        )
        studentaddress_label.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        studentaddress_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_address,
            width=16,
            font=("times new  roman", 13, "bold"),
        )
        studentaddress_entry.grid(row=3, column=4, padx=10, pady=5, sticky=W)

        # phone
        studentphone_label = Label(
            class_frame,
            text="Number:",
            font=("times new  roman", 13, "bold"),
            fg="black",
        )
        studentphone_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        studentphone_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_num,
            width=16,
            font=("times new  roman", 13, "bold"),
        )
        studentphone_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Email
        studentemail_label = Label(
            class_frame,
            text="E-mail:",
            font=("times new  roman", 13, "bold"),
            fg="black",
        )
        studentemail_label.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        studentemail_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_email,
            width=16,
            font=("times new  roman", 13, "bold"),
        )
        studentemail_entry.grid(row=4, column=4, padx=5, pady=5, sticky=W)

        ## radio Buttons
        self.var_radio1 = StringVar()

        radiobtn1 = ttk.Radiobutton(
            class_frame,
            variable=self.var_radio1,
            text="Take photo Sample",
            value="Yes",
        )
        radiobtn1.grid(row=5, column=0)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(
            class_frame,
            variable=self.var_radio1,
            text="No photo Sample",
            value="No",
        )
        radiobtn2.grid(row=5, column=1)

        ## Buttons frame
        btn_frame = Frame(class_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=170, width=700, height=90)

        save_btn = Button(
            btn_frame,
            text="SAVE",
            command=self.add_data,
            width=15,
            font=("times new  roman", 13, "bold"),
            fg="black",
            bg="blue",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame,
            text="UPDATE",
            command=self.update_data,
            width=15,
            font=("times new  roman", 13, "bold"),
            fg="black",
            bg="blue",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            text="DELETE",
            command=self.delete_data,
            width=15,
            font=("times new  roman", 13, "bold"),
            fg="black",
            bg="blue",
        )
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(
            btn_frame,
            text="RESET",
            command=self.reset_data,
            width=15,
            font=("times new  roman", 13, "bold"),
            fg="black",
            bg="blue",
        )
        reset_btn.grid(row=0, column=3)

        take_btn = Button(
            btn_frame,
            text="Take A PHOTO",
            command=self.generate_dataset,
            width=15,
            font=("times new  roman", 13, "bold"),
            fg="black",
            bg="blue",
        )
        take_btn.grid(row=1, column=0, pady=10)

        nottake_btn = Button(
            btn_frame,
            text="UPDATE A PHOTO",
            width=15,
            font=("times new  roman", 13, "bold"),
            fg="black",
            bg="blue",
        )
        nottake_btn.grid(row=1, column=1, pady=10)

        ###Search System

        sear_frame = LabelFrame(
            right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("times new  roman", 13, "bold"),
            fg="green",
        )
        sear_frame.place(x=5, y=0, width=550, height=100)

        # search by
        search_label = Label(
            sear_frame,
            text="Search By",
            font=("times new  roman", 16, "bold"),
            fg="white",
            background="red",
        )
        search_label.grid(row=0, column=0, padx=10)

        sear_combo = ttk.Combobox(
            sear_frame,
            font=("times new  roman", 10, "bold"),
            state="readonly",
            width=10,
        )
        sear_combo["values"] = ("Select", "Roll no", "StudentID", "phone no.", "Name")
        sear_combo.current(0)
        sear_combo.grid(row=0, column=1, padx=2, pady=2)

        search_entry = ttk.Entry(
            sear_frame, width=10, font=("times new  roman", 13, "bold")
        )
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(
            sear_frame,
            text="SEARCH",
            width=10,
            font=("times new  roman", 13, "bold"),
            fg="black",
            bg="blue",
        )
        search_btn.grid(row=0, column=3, pady=10)

        showall_btn = Button(
            sear_frame,
            text="SHOW ALL",
            width=10,
            font=("times new  roman", 13, "bold"),
            fg="black",
            bg="blue",
        )
        showall_btn.grid(row=0, column=4, pady=10)

        ##########Table Frame#######

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=120, width=550, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "dep",
                "year",
                "sem",
                "id",
                "name",
                "roll",
                "gender",
                "dob",
                "address",
                "num",
                "email",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll NO")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("num", text="Number")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)

        self.student_table.column("address", width=100)
        self.student_table.column("num", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ###################Function Declartaion######

    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="Localhost",
                    username="root",
                    password="W@2915djkq#",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_address.get(),
                        self.var_num.get(),
                        self.var_email.get(),
                        
                    
                        self.var_radio1.get(),
                    )
                )

                conn.commit()
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details has been added successfully",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"fue to :{str(es)}", parent=self.root)
                
    ##########Fetch Data############
    def fetch_data(self):
        conn = mysql.connector.connect(
                    host="Localhost",
                    username="root",
                    password="W@2915djkq#",
                    database="face_recognizer",
                )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()        
                
    #######get Cursor########
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_std_id.set(data[3]),
        self.var_std_name.set(data[4]),
        self.var_roll.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_address.set(data[8]),
        self.var_num.set(data[9]),
        self.var_email.set(data[10]),
        self.var_radio1.set(data[11])
        
                    
    #######update function##################
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            
        else:
            try:
                Update=messagebox.askyesno("Update","Do You Want to Update this Student",parent=self.root)
                
                conn = mysql.connector.connect(
                host="Localhost",
                username="root",
                password="W@2915djkq#",
                database="face_recognizer",
            )
                my_cursor = conn.cursor()
                my_cursor.execute("Update a student set Dep=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,DOB=%s,Address=%s,num=%s,email=%s,Photosample=%s where std_id=%s",(
                    
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_num.get(),
                    self.var_email.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    
                ))
                
                
                messagebox.showinfo("Success","Student Details Successfully update Completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                
                    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)           
        
    ####delete function########
    def delete_data(self):
        if self.var_std_id.get()==" ":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you Want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                    host="Localhost",
                    username="root",
                    password="W@2915djkq#",
                    database="face_recognizer",
                )
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                
                else:
                    if not delete:
                        return    
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Succesfully deleted student details",parent=self.root)
                                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
    
    
    #####reset button######
    def reset_data(self):
        self.var_dep.set("Select Depaertment")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_num.set("")
        self.var_email.set("")
        self.var_radio1.set("")    
    
    ####################---Generate data set or take Photo Sample -------
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            
        else:
            try:
            
                conn = mysql.connector.connect(
                    host="Localhost",
                    username="root",
                    password="W@2915djkq#",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                
                my_cursor.execute("Select *From Student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update a student set Dep=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,DOB=%s,Address=%s,num=%s,email=%s,Photosample=%s where std_id=%s",(
                        
                        self.var_dep.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_address.get(),
                        self.var_num.get(),
                        self.var_email.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==+1
                        
                    ))
                    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # ------ Load Predifined data on face frontal from opencv--------
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling Factor=1.3   ----Default
                    #Minimum Neighbor=5
                    
                    #-----RECTANGLE-----
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                
                # ---- to OPEN CAMERA -----
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitkey(1)==13 or int(img_id)==100:
                        break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating Data Sets Completed !!!")
                    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                     
                
                    
                
                
                    
            

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root = mainloop()
