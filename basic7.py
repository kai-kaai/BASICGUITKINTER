from tkinter import *
root = Tk()

root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)
root.config(bg="lightblue")

#การสร้างเฟรม
fram1 = Frame(root,bg="pink")
fram2 = LabelFrame(root,text="Frame title")

#แสดงเฟรม
fram1.pack(fill=BOTH,expand=True)
Button(fram1,text="Button 1").pack()
Button(fram1,text="Button 2").pack()
Button(fram1,text="Button 3").pack()
fram2.pack(fill=BOTH,expand=True)
Button(fram2,text="Button 4").grid(row=0,column=0)
Button(fram2,text="Button 5").grid(row=0,column=1)
Button(fram2,text="Button 6").grid(row=0,column=2)
root.mainloop()