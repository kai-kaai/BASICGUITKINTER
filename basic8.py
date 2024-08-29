from tkinter import *
root = Tk()

root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)

def showName():
    name = (userName.get())
    print(name)
    myText.delete(0,END)

userName = StringVar() #ส่วนที่เก็บข้อความใน Entry widget

myText = Entry(root,width=40,font=("Arial",25),textvariable=userName) #ส่วนแสดงผล
myText.pack(padx=5,pady=10)

btnSave = Button(root,text="บันทึก",fg="white",bg="blue",command=showName)
btnSave.pack(ipadx=30,ipady=10)

root.mainloop()