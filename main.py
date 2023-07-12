from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import tkinter
from student import Student
from train  import Train
from face_recog import Face_Recognition
from attendance import Attendance

class face_recoginiton_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recoginiton System")

        # first image
        img = Image.open(r"D:\Face Recoginition Attendance system\Images\campus1.jpg")
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
        img2 = Image.open(r"D:\Face Recoginition Attendance system\Images\erc.jpg")
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
            text="FACE  RECOGNITION  ATTENDANCE  SYSTEM ",
            font=("times new  roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1350, height=45)

        # students Button
        img4 = Image.open(r"D:\Face Recoginition Attendance system\Images\st.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(
            bg_img, image=self.photoimg4, command=self.students_details, cursor="hand2"
        )
        b1.place(x=200, y=75, width=180, height=180)

        b1_1 = Button(
            bg_img,
            text="Students Details",
            command=self.students_details,
            cursor="hand2",
            font=("times new  roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=225, width=180, height=40)

        # Face Detech Button
        img5 = Image.open(r"D:\Face Recoginition Attendance system\Images\face.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,command=self.face_data, cursor="hand2")
        b1.place(x=500, y=75, width=180, height=180)

        b1_1 = Button(
            bg_img,
            text="Face Detector",command=self.face_data,
            cursor="hand2",
            font=("times new  roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=500, y=225, width=180, height=40)

        # Attendance  Button
        img6 = Image.open(r"D:\Face Recoginition Attendance system\Images\scan.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, command=self.attendance_data,cursor="hand2")
        b1.place(x=800, y=70, width=180, height=180)

        b1_1 = Button(
            bg_img,
            text="Attendance",command=self.attendance_data,
            cursor="hand2",
            font=("times new  roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=800, y=225, width=180, height=40)

        # Train Data
        img7 = Image.open(r"D:\Face Recoginition Attendance system\Images\train.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,command=self.train_data, cursor="hand2")
        b1.place(x=200, y=275, width=180, height=180)

        b1_1 = Button(
            bg_img,
            text="Train Data",command=self.train_data,
            cursor="hand2",
            font=("times new  roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=450, width=180, height=40)

        # Photo
        img8 = Image.open(r"D:\Face Recoginition Attendance system\Images\photo1.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,command=self.open_img, cursor="hand2")
        b1.place(x=500, y=275, width=180, height=180)

        b1_1 = Button(
            bg_img,
            text="Photos",
            command=self.open_img,
            cursor="hand2",
            font=("times new  roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=500, y=450, width=180, height=40)

        # Exit
        img9 = Image.open(r"D:\Face Recoginition Attendance system\Images\Exit.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, command=self.iExit,cursor="hand2")
        b1.place(x=800, y=275, width=180, height=180)

        b1_1 = Button(
            bg_img,
            text="Exit",command=self.iExit,
            cursor="hand2",
            font=("times new  roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=800, y=450, width=180, height=40)

    
    def open_img(self):
        os.startfile("data")
        
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are You Sure To Exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    
    
    
        ##########Functiion Buttons########

    def students_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
        
        
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window) 





if __name__ == "__main__":
    root = Tk()
    obj = face_recoginiton_system(root)
    root = mainloop()
