from tkinter import *

root = Tk()
root.title("I have no idea what I am doing")
root.geometry("600x500")
root.config(bg="lavender")

label1 = Label(root,text="Name: ",bg="lavender", fg="purple")
label1.place(relx=0.3,rely=0.3,anchor=CENTER)
entry1= Entry(root, bg="orchid3", fg="white")
entry1.place(relx=0.5,rely=0.3,anchor=CENTER)

label2 = Label(root,text="Password: ",bg="lavender", fg="purple")
label2.place(relx=0.28,rely=0.4,anchor=CENTER)
entry2= Entry(root, bg="orchid3", fg="white")
entry2.place(relx=0.5,rely=0.4,anchor=CENTER)

label3 = Label(root,text="Captcha: ",bg="lavender", fg="purple")
label3.place(relx=0.2835,rely=0.5,anchor=CENTER)
entry3= Entry(root, bg="orchid3", fg="white")
entry3.place(relx=0.5,rely=0.5,anchor=CENTER)

rlabel1 = Label(root,text="",bg="lavender", fg="purple")
rlabel1.place(relx=0.5,rely=0.6,anchor=CENTER)

rlabel2 = Label(root,text="",bg="lavender", fg="purple")
rlabel2.place(relx=0.5,rely=0.7,anchor=CENTER)

rlabel3 = Label(root,text="",bg="lavender", fg="purple")
rlabel3.place(relx=0.5,rely=0.8,anchor=CENTER)

class userdb:
    def __init__(self, name, pas, cap):
        self._username = name
        self._password = pas
        self._captcha = cap
    def showuser(self):
        rlabel1["text"]="Name: " + self._username
        rlabel2["text"]="Password: " + self._password
        rlabel3["text"]="Captcha: " + self._captcha
    def addUser(self):
        global larry
        names = str(entry1.get())
        self._username=names
        passw = str(entry2.get())
        self._password=passw
        caps = str(entry3.get())
        self._captcha=caps
        print("added")

larry=userdb("larry","1234","c")        
btn1=Button(root,command=larry.addUser(),text="Add User")
btn1.place(relx=0.4,rely=0.2,anchor=CENTER)

btn2=Button(root,command=larry.showuser(),text="Show User")
btn2.place(relx=0.6,rely=0.2,anchor=CENTER)

root.mainloop()