from tkinter import *
from tkinter import PhotoImage

import datetime 

clock=Tk()
clock.title('Digital Clock')
clock.geometry('1000x500')
clock.config(bg='black')
#bg= PhotoImage(file = "pngwing.com.png") 

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    min=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')
    day=time.strftime('%a')
    month=time.strftime('%m')
    year=time.strftime('%y')
    
    lab_6.config(text=day)
    lab_7.config(text=month)
    lab_8.config(text=year)

    
    lab_3.config(text=hr)
    lab_4.config(text=min)
    lab_5.config(text=sec)
    lab_3.after(200,date_time)
    
    

lab_1=Label(clock,text='Digital',font=('Harlow Solid Italic',30),fg="cyan",bg="black")
lab_1.place(x=550,y=50,height=50,width=250)

lab_2=Label(clock,text='CLOCK',font=('Sitka Small Semibold',70),fg="cyan",bg="black")
lab_2.place(x=450,y=100,height=90,width=350)

lab_3=Label(clock,text='00',font=('Times New Roman',30),fg="cyan",bg="black")
lab_3.place(x=150,y=280,height=40,width=50)

lab_h=Label(clock,text='hour',font=('Times New Roman',15),fg="cyan",bg="black")
lab_h.place(x=150,y=320,height=40,width=50)

lab_4=Label(clock,text='00',font=('Times New Roman',30),fg="cyan",bg="black")
lab_4.place(x=250,y=280,height=40,width=50)

lab_m=Label(clock,text='min',font=('Times New Roman',15),fg="cyan",bg="black")
lab_m.place(x=250,y=320,height=40,width=50)

lab_5=Label(clock,text='00',font=('Times New Roman',30),fg="cyan",bg="black")
lab_5.place(x=350,y=280,height=40,width=50)

lab_s=Label(clock,text='sec',font=('Times New Roman',15),fg="cyan",bg="black")
lab_s.place(x=350,y=320,height=40,width=50)

lab_6=Label(clock,text="sunday",font=('Times New Roman',30),fg="cyan",bg="black")
lab_6.place(x=500,y=280,height=45,width=150)

lab_d=Label(clock,text='day',font=('Times New Roman',15),fg="cyan",bg="black")
lab_d.place(x=550,y=320,height=40,width=50)

lab_7=Label(clock,text="may",font=('Times New Roman',30),fg="cyan",bg="black")
lab_7.place(x=750,y=280,height=45,width=150)

lab_mo=Label(clock,text='month',font=('Times New Roman',15),fg="cyan",bg="black")
lab_mo.place(x=800,y=325,height=30,width=50)

lab_8=Label(clock,text="2024",font=('Times New Roman',30),fg="cyan",bg="black")
lab_8.place(x=630,y=380,height=45,width=150)

lab_m=Label(clock,text='year',font=('Times New Roman',15),fg="cyan",bg="black")
lab_m.place(x=680,y=420,height=30,width=50)


date_time()


clock.mainloop()
