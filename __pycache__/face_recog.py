from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recoginiton System")
        
        
        # Title
        title_lbl = Label(self.root,
        
            text="FACE RECOGNITION ",
            font=("times new  roman", 40, "bold"),
            bg="white",
            fg="green",
        )
        title_lbl.place(x=0, y=0, width=1350, height=45)
        
        # first image
        img_top = Image.open(r"D:\\Face Recoginition Attendance system\\Images\\dector1.jpg")
        img_top = img_top.resize((650, 650),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=650, height=650)
        
        # second image
        img_bttm = Image.open(r"D:\\Face Recoginition Attendance system\\Images\\dector22.jpg")
        img_bttm = img_bttm.resize((650, 650),Image.Resampling.LANCZOS)
        self.photoimg_bttm = ImageTk.PhotoImage(img_bttm)

        f_lbl = Label(self.root, image=self.photoimg_bttm)
        f_lbl.place(x=640, y=45, width=650, height=650)
        
        #########Button############
        
        b1_train = Button(
            self.root,
            text="Face Recognition",
            command=self.face_reg,
            cursor="hand2",
            font=("times new  roman", 20, "bold"),
            
            bg="red",
            fg="white",
        )
        b1_train.place(x=470, y=450, width=300, height=50)

        
        
    ######------Face recongnition-------
    def face_reg(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                #---------- to show data we fetches from Databases---------
                conn = mysql.connector.connect(
                    host="Localhost",
                    username="root",
                    password="W@2915djkq#",
                    database="face_recognizer",
                )
                
                
                
                
                my_cursor = conn.cursor()
                
                my_cursor.execute("Select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n=
                
                my_cursor.execute("Select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                
                my_cursor.execute("Select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                
                
                
                
            
                
                
                if confidence>77:
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                    
                coord=[x,y,w,h]
                
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cp=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cp.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cp.release()
            
        cv2.destroyAllWindows()
                
            
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root = mainloop() 
