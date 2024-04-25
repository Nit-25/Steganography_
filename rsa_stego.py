from tkinter import *  
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import filedialog
import cv2
import os
import string
import rsa


def encrytion_input():
    global input_msg
    global private_key
    img = box_1_path.get()
    public_key = box_2_path.get()
    input_msg = box_5_path.get("1.0", "end-1c")
    private_key = box_3_path.get()
    result = encrypted(img,public_key,input_msg)
    

def encrypted(img,public_key,input_msg):
    global encrypted_message
    secret_msg = input_msg
    with open(public_key,"rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    encrypted_message = rsa.encrypt(secret_msg.encode(), public_key)
    img = cv2.imread(img)

    n=0
    m=0
    z=0

    for i in range(len(encrypted_message)):
        img[n,m,z]=encrypted_message[i]
        n=n+1
        m=m+1
        z=(z+1)%3

    cv2.imwrite("enc.png",img)

    os.startfile("enc.png")


def decryption_input():
    global encrypted_message
    uprivate_key = box_7_path.get()
    img_destination = box_6_path.get()
    result = decrypted(uprivate_key,img_destination,encrypted_message)


def decrypted(uprivate_key,img_destination,encrypted_message):
    global private_key
    img = cv2.imread(img_destination)
    with open(private_key,"rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    with open(uprivate_key,"rb") as f:
        uprivate_key = rsa.PrivateKey.load_pkcs1(f.read())

    n=0
    m=0
    z=0

    if uprivate_key==private_key:
        msg = []
        for i in range(len(encrypted_message)):
            msg.append(img[n,m,z])
            n=n+1
            m=m+1
            z=(z+1)%3
        msg_bytes = bytes(msg)
        decrypt = rsa.decrypt(msg_bytes,private_key)
        decrypted_message = decrypt.decode()
        box_10.config(text=decrypted_message,bg="pink",fg="black")
    else:
        box_10.config(text="Invalid private key")
        

t1 = Tk() 
t1.title("Steganography 1") 
t1.geometry("900x500+300+200") 
t1.resizable(False,False) 


box_1 = Label(t1,text="Enter file path of image source").pack()
box_1_path = Entry(t1,width=80,justify="center",textvariable=StringVar(),bg="pink",border=0,fg="black")
box_1_path.pack()

box_2 = Label(t1,text="Enter public key").pack()
box_2_path = Entry(t1,width=80,justify="center",textvariable=StringVar(),bg="pink",border=0,fg="black")
box_2_path.pack()

box_3 = Label(t1,text="Enter private key of reciever").pack()
box_3_path = Entry(t1,width=80,justify="center",textvariable=StringVar(),bg="pink",border=0,fg="black")
box_3_path.pack()


box_5 = Label(t1,text="Enter message").pack()
box_5_path = Text(t1,height=18,width=50)
box_5_path.pack()


label_var = StringVar()


Fin_button = Button(t1, text="Proceed", command=encrytion_input, bg='pink', width=10)
Fin_button.place(relx=0.635, rely=0.940)

# Label using StringVar
result_label = Label(t1, textvariable=label_var)
result_label.pack()

t1.mainloop()

t2 = Tk() 
t2.title("Steganography 2") 
t2.geometry("900x500+300+200") 
t2.resizable(False,False)


box_6 = Label(t2,text="Enter name of the file").pack()
box_6_path = Entry(t2,width=80,justify="center",textvariable=StringVar(),bg="pink",border=0,fg="black")
box_6_path.pack()

box_7 = Label(t2,text="Enter private key").pack()
box_7_path = Entry(t2,width=80,justify="center",textvariable=StringVar(),bg="pink",border=0,fg="black")
box_7_path.pack()


box_8 = Label(t2,text="Secret message")
box_8.place(x=405,y=95)

box_image = PhotoImage(file = "C:\\Users\\birad\\OneDrive\\Documents\\stego\\pink_box.png")
box_9 = Label(image=box_image,bg="pink")
box_9.place(x=200,y=120)

box_10=Label(font=("arial",14,"bold"),bg="pink",wraplength=507)
box_10.place(x=200,y=120)

label_var = StringVar()

Fin_button = Button(t2, text="Proceed", command=decryption_input, bg='pink', width=10)
Fin_button.place(relx=0.700, rely=0.940)

# Label using StringVar
result_label = Label(t2, textvariable=label_var)
result_label.pack()




t2.mainloop()
