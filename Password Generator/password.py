from tkinter import *
import random

def password():
    n=num_var.get()
    passw=""
    for i in range(n):
        passw+=random.choice('1234567890!@#$%^&*qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    return passw

def displaytex():
    tex.set(password())

def copy():
    root.clipboard_clear()
    root.clipboard_append()
    root.selection_get(selection='CLIPBOARD')
    return "break"

root=Tk()
root.title("Password Generator")
root.geometry("500x400")
root.configure(background="#273b2c")

label1=Label(root,text="Welcome to Password Generator",justify='center',
             bg="#273b2c",fg="white",font=("Helvetica",20,'bold')).place(anchor='center',relx=0.5,rely=0.2)

num_var=IntVar()
entry1=Entry(root,bg="#dee0df",fg="black",justify='left',font=("Helvetica",14),
             textvariable=num_var,borderwidth=1,relief='sunken').place(anchor='center',relx=0.69,rely=0.4)

label2=Label(root,text="Password Length",justify='center',bg="#273b2c",fg="white",
             width=15,height=1,font=("Helvetica",14,'bold')).place(anchor='center',relx=0.28,rely=0.4)

tex=StringVar()
display=Entry(root,bg="#dee0df",justify='left',borderwidth=1,font=("Helvetica",14),relief='sunken',textvariable=tex).place(anchor='center',relx=0.69,rely=0.6)

label3=Label(root,text="Password",justify='center',bg="#273b2c",fg="white",
             width=15,height=1,font=("Helvetica",14,'bold')).place(anchor='center',relx=0.28,rely=0.6)

button1=Button(root,text="Generate",borderwidth=1,relief='raised',width=10,height=2,
               font=("Helvetica",14,'bold'),bg="white",command=displaytex).place(anchor='center',relx=0.5,rely=0.8)

root.mainloop()
