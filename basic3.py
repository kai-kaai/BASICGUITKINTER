from tkinter import *

root = Tk()

root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)
root.config(bg="lightblue")

#แสดงข้อความ
label1 = Label(root,text="สวัสดี",font=("Arial", 22,"bold"),bg="red",fg="white")
label1.pack()

label2 = Label(root,text="Python",font=("Arial", 22,"bold"),bg="blue",fg="white")
label2.pack()

label3 = Label(root,text="Tkinter",font=("Arial", 22,"bold"),bg="green",fg="white")
label3.pack()

label4 = Label(root,text="GUI",font=("Arial", 22,"bold"),bg="black",fg="white")
label4.pack()
root.mainloop()