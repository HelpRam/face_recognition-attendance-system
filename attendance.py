
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recoginiton System")
        
        
        # Title
        title_lbl = Label(
            self.root,
            text="ATTENDANCE MANAGEMENT SYSTEM ",
            font=("times new  roman", 40, "bold"),
            bg="darkgreen",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1350, height=45)
        
        
        # main frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1480, height=600)
        
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Students Attendance Detail",
            font=("times new  roman", 28, "bold"),
            fg="black",
        )
        left_frame.place(x=5, y=0, width=1240, height=690)
        
        
        b1_train = Button(
            left_frame,
            text="Import CSV",
            command=self.importCsv,
            cursor="hand2",
            font=("times new  roman", 20, "bold"),
            bg="blue",
            fg="white",
        )
        b1_train.place(x=400, y=-4, width=300, height=50)
        ##----SCROLL BAR-------------------------------
        
        
        
        table_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=50, width=1210, height=480)
        

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            column=(
                "id",
                "roll",
                "name",
                "department",
                "time",
                "date",
                "attendance"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="ROLL")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        
        
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
       

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        
        ########__------------Fetch DATA--------------
        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    
    def importCsv(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(("CSV File","*.csv"),("Al1 File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
            
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root = mainloop()