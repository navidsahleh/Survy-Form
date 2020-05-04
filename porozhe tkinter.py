from tkinter import *
from tkinter import ttk
from tkinter .ttk import *

root=Tk()
s=Style()
s.configure('My.TFrame', background='orange')
root.geometry('600x650+350+10')
frame1=ttk.Frame(root,height=250,width=600,relief=RIDGE,style='My.TFrame')
frame1.place(x=0,y=0)
frame2=ttk.Frame(root,height=400,width=600,relief=RIDGE,style='My.TFrame')
frame2.place(x=0,y=250)
img=PhotoImage(file="E:\\pycharm\\tour_logo.gif")
label1=ttk.Label(frame1,text='Explore our world your way',font=('Arial','14','bold'),background='blue')
label1.place(x=300,y=60)
label2=ttk.Label(frame1,image=img)
label2.place(x=60,y=40)
label3=ttk.Label(frame1,text='we are happy to have you here\n please send us some msg inorder to become better\n and i am very tired please shut up!\nok let us talk about your trip :D'
                 ,justify=CENTER,background='blue')
label3.place(x=290,y=95)

label4=ttk.Label(frame2,text='Name :',background='red')
label4.place(x=30,y=40)
entry1=ttk.Entry(frame2)
entry1.place(x=30,y=60)

label5=ttk.Label(frame2,text='Email :',background='red')
label5.place(x=350,y=40)
entry2=ttk.Entry(frame2)
entry2.place(x=350,y=60)

label6=ttk.Label(frame2,text='Comments :',background='red')
label6.place(x=30,y=115)
text=Text(frame2,width=55,height=10,wrap='word')
text.place(x=30,y=135)

def clear_all():
    text.delete('1.0','end')
    entry1.delete(0,END)
    entry2.delete(0,END)

def show_entry():
    print(entry2.get())
    print(text.get('1.0','end'))
    entry1.delete(0,END)
    entry2.delete(0,END)
    text.delete('1.0','end')
    print('your msg has been submited!!!')

button1=ttk.Button(frame2,text='Submit',command=show_entry)
button1.place(x=30,y=315)

button2=ttk.Button(frame2,text='Clear',command=clear_all)
button2.place(x=400,y=310)

root.mainloop()