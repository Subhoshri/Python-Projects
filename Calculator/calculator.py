#Making a GUI Calculator using Tkinter Module of Python
from tkinter import *
import math
import tkinter.messagebox

#making functions for performing calculations        
def button_click(char):
    global calc_operator
    calc_operator += str(char)            
    text_input.set(calc_operator)

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)

def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

def button_equal():
    global calc_operator
    if 'log10' in calc_operator or 'log' in calc_operator or 'sin' in calc_operator or 'tan' in calc_operator or 'cos' in calc_operator:
        temp_op=str(eval('math.'+calc_operator))
    else:
        temp_op = str(eval(calc_operator)) 
    text_input.set(temp_op)
    calc_operator = temp_op

def squareroot():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

#Trigonometric functions
def sin():
    global calc_operator
    result = 'sin('
    calc_operator = result
    text_input.set(result)

def cos():
    global calc_operator
    result = 'cos('
    calc_operator = result
    text_input.set(result)

def tan():
    global calc_operator
    result = 'tan('
    calc_operator = result
    text_input.set(result)

def asin():
    global calc_operator
    result = str(math.asin(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def acos():
    global calc_operator
    result = str(math.acos(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def atan():
    global calc_operator
    result = str(math.atan(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)    

def degrees():
    global calc_operator
    result = str(math.degrees(float(calc_operator)))
    calc_operator=result
    text_input.set(result)

def log10():
    global calc_operator
    result = 'log10('
    calc_operator = result
    text_input.set(result)

def ln():
    global calc_operator
    result='log('
    result = str(math.log(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def tenspow():
    global calc_operator
    result = str(10**float(calc_operator))
    calc_operator = result
    text_input.set(result)

def square():
    global calc_operator
    result = str((float(calc_operator))**2)
    calc_operator = result
    text_input.set(result)

def ex():
    global calc_operator
    result = str(math.exp(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def pi():
    global calc_operator
    result = calc_operator+str(math.pi)
    calc_operator = result
    text_input.set(result)

def e():
    global calc_operator
    result = calc_operator+str(math.exp(1))
    calc_operator = result
    text_input.set(result)

def power():
    global calc_operator
    result = calc_operator+"**"
    calc_operator = result
    text_input.set(result)

def mod():
    global calc_operator
    result = calc_operator+"%"
    calc_operator = result
    text_input.set(result)


#GUI Interface
root=Tk()
root.title("Scientific Calculator")
root.geometry("580x470+600+90")
root.resizable(height=False,width=False)
root.configure(background='#363440')

calc=Frame(root,background="#404E9B").grid() 

calc_operator=""
text_input=StringVar()
txtdisplay=Entry(calc, font=("Helvetica",20,'bold'), bg="#D4E2E3", fg="black",
                 bd=30, width=28, justify="right", textvariable=text_input).grid(row=0,column=0,columnspan=5,pady=1)

#Standard Calculator Buttons
#Numeric 
btnone= Button(calc, text="1", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("1")).grid(row=3, column=0, pady=1)
btntwo= Button(calc, text="2", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("2")).grid(row=3, column=1, pady=1)
btnthree= Button(calc, text="3", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("3")).grid(row=3, column=2, pady=1)
btnfour= Button(calc, text="4", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("4")).grid(row=2, column=0, pady=1)
btnfive= Button(calc, text="5", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("5")).grid(row=2, column=1, pady=1)
btnsix= Button(calc, text="6", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("6")).grid(row=2, column=2, pady=1)
btnseven= Button(calc, text="7", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("7")).grid(row=1, column=0, pady=1)
btneight= Button(calc, text="8", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("8")).grid(row=1, column=1, pady=1)
btnnine= Button(calc, text="9", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("9")).grid(row=1, column=2, pady=1)

#Row 1
btnClear = Button(calc, text="DEL",
                  width=6, height=2, bg='#363440', fg="white",
                  font=('Helvetica', 20, 'bold'), bd=4,
                  activebackground="#1A1A57", activeforeground="white",
                  command=button_delete).grid(row=1, column=3, pady=1)

btnAllClear= Button(calc, text=chr(65)+chr(67),
                     width=6, height=2, bg='#363440', fg="white",
                     font=('Helvetica', 20, 'bold'), bd=4,
                     activebackground="#1A1A57", activeforeground="white",
                     command=button_clear_all).grid(row=1, column=4, pady=1)

#Row 2
btnadd= Button(calc, text="+", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("+")).grid(row=2, column=3, pady=1)

btnsub= Button(calc, text="-", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("-")).grid(row=2, column=4, pady=1)

#Row 3
btnmulti= Button(calc, text="x", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("*")).grid(row=3, column=3, pady=1)

btndivide= Button(calc, text="÷", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("/")).grid(row=3, column=4, pady=1)

#Row 4
btnzero= Button(calc, text="0", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("0")).grid(row=4, column=0, pady=1)

btndot= Button(calc, text=".", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click(".")).grid(row=4, column=1, pady=1)

btnlbrac= Button(calc, text="(", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click("(")).grid(row=4, column=2, pady=1)

btnrbrac= Button(calc, text=")", width=6, height=2, 
               bg="#E3E1E4", fg="black", activebackground="#1A1A57", activeforeground="white",
               font=("Helvetica", 20, 'bold'), bd=4, 
               command= lambda:button_click(")")).grid(row=4, column=3, pady=1)

btnequal= Button(calc, text="=", width=6, height=2, 
                 bg="#E3E1E4", fg="black", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=button_equal).grid(row=4, column=4, pady=1)

#Scientific Calculator Buttons
#Row 1
btnpi= Button(calc, text="π", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=pi).grid(row=1, column=5, pady=1)

btnsin= Button(calc, text="sin", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=sin).grid(row=1, column=6, pady=1)

btncos= Button(calc, text="cos", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=cos).grid(row=1, column=7, pady=1)

btntan= Button(calc, text="tan", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=tan).grid(row=1, column=8, pady=1)

btnlog10= Button(calc, text="log\u2081\u2080", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=log10).grid(row=1, column=9, pady=1)

#Row 2
btne= Button(calc, text="e", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=e).grid(row=2, column=5, pady=1)

btnasin= Button(calc, text="sin\u207B\u00B9", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=asin).grid(row=2, column=6, pady=1)

btnacos= Button(calc, text="cos\u207B\u00B9", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=acos).grid(row=2, column=7, pady=1)

btnatan= Button(calc, text="tan\u207B\u00B9", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=atan).grid(row=2, column=8, pady=1)

btnloge= Button(calc, text="ln", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=ln).grid(row=2, column=9, pady=1)

#Row 3
btnpercent= Button(calc, text="%", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=percent).grid(row=3, column=5, pady=1)

btnmod= Button(calc, text="MOD", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=mod).grid(row=3, column=6, pady=1)

btndeg= Button(calc, text="deg", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=degrees).grid(row=3, column=7, pady=1)

btnsqroot= Button(calc, text="\u221A", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=squareroot).grid(row=3, column=8, pady=1)

btnsigns = Button(calc, text='\u00B1', width=6, height=2,
               bg="#6972A9", fg="white", font =('Helvetica', 20, 'bold'),
               activebackground="#1A1A57", activeforeground="white",
               bd=4, command=sign_change).grid(row=3, column=9, pady=1)

#Row 4
btnfac= Button(calc, text="x!", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=fact_func).grid(row=4, column=5, pady=1)

btntenspow= Button(calc, text="10\u02E3", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=tenspow).grid(row=4, column=6, pady=1)

btnsquare= Button(calc, text="x\u00B2", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=square).grid(row=4, column=7, pady=1)

btnpower= Button(calc, text="x**y", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=power).grid(row=4, column=8, pady=1)

btnex= Button(calc, text="e\u02E3", width=6, height=2, 
                 bg="#6972A9", fg="white", font=('Helvetica', 20, 'bold'), 
                 activebackground="#1A1A57", activeforeground="white",
                 bd=4, command=ex).grid(row=4, column=9, pady=1)


lblDisplay = Label(calc, text = "Scientific Calculator",
                   font=('Helvetica',30,'bold'),
                   bg='black', fg='white', justify="left")
 
lblDisplay.grid(row=0, column= 5, columnspan=4)
 
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator",
                                        "Do you want to exit?")
    if iExit>0:
        root.destroy()
        return
 
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("1165x470+0+0")
 
 
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("580x470+0+0")
 
menubar = Menu(calc)
 
# MenuBar 1 :
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)
 
# MenuBar 2 :
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")
 
root.config(menu=menubar)
 
root.mainloop()
