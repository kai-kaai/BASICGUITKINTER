from tkinter import *
import tkinter.messagebox

root = Tk()

root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)

def quitProgram():
    confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรมหรือไม่?")
    if confirm == "yes":
        root.destroy()
    else:
        return

def showName():
    name = (userName.get())
    if name == "":
        tkinter.messagebox.showerror("เตือน","กรุณาใส่ชื่อผู้ใช้งาน")
    else:
        myText.delete(0,END)
        tkinter.messagebox.showinfo("รายละเอียด","ชื่อผู้ใช้งานโปรแกรม = "+name)

userName = StringVar() #ส่วนที่เก็บข้อความใน Entry widget

myText = Entry(root,width=40,font=("Arial",25),textvariable=userName) #ส่วนแสดงผล
myText.pack(padx=5,pady=10)

btnSave = Button(root,text="บันทึก",fg="white",bg="blue",command=showName)
btnSave.pack(ipadx=30,ipady=10)

btnQuit = Button(root,text="ออกจากโปรแกรม",fg="white",bg="red",command=quitProgram)
btnQuit.pack(ipadx=10,ipady=10, pady=10)

root.mainloop()