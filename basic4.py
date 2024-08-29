from tkinter import *
root = Tk()

root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)
root.config(bg="lightblue")

lable1 = Label(root,text="สวัสดี",font=("Arial", 22,"bold"),bg="red",fg="white")
lable1.pack(fill="x", padx=(5,10), pady=(5,10))

lable2 = Label(root,text="Python",font=("Arial", 22,"bold"),bg="blue",fg="white")
lable2.pack(pady=5,ipadx=50,ipady=10)

lable3 = Label(root,text="Tkinter",font=("Arial", 22,"bold"),bg="green",fg="white")
lable3.pack(fill=BOTH,expand=True)

lable4 = Label(root,text="GUI",font=("Arial", 22,"bold"),bg="black",fg="white")
lable4.pack(fill=BOTH,expand=True)

root.mainloop()