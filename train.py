from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recoginiton System")
        
        
        
        # Title
        title_lbl = Label(self.root,
        
            text="TRAIN DATA  SET ",
            font=("times new  roman", 40, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1350, height=45)

        
        # first image
        img_top = Image.open(r"D:\Face Recoginition Attendance system\Images\f.jpg")
        img_top = img_top.resize((1300, 280),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1300, height=280)
        
        
        #########Button############
        
        b1_train = Button(
            self.root,
            text="TRAIN DATA",
            command=self.train_classifier,
            cursor="hand2",
            font=("times new  roman", 30, "bold"),
            
            bg="darkblue",
            fg="white",
        )
        b1_train.place(x=0, y=320, width=1350, height=70)
        
        
        
        # #second image
        img_btm = Image.open(r"D:\Face Recoginition Attendance system\Images\f.jpg")
        img_btm = img_btm.resize((1300, 300),Image.Resampling.LANCZOS)
        self.photoimg_btm = ImageTk.PhotoImage(img_btm)

        f_lbl = Label(self.root, image=self.photoimg_btm)
        f_lbl.place(x=0, y=380, width=1300, height=300)
        
        
        
    ###------To Train Data -- LBPH Algorithms---
    def train_classifier(self):
        data_dir=("data") # path has to givenn
        
        # ---------list comprensivee--
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray scale image convert 
            imageNp=np.array(img,'uint8')        ##Grid System convert
            id=int(os.path.split(image)[1].split('.')[1]) 
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        ###-----Train The Classifier ANd SAVE DATA--------
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed!!!")
        
            
               
        
        
    
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root = mainloop()        