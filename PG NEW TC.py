from tkinter import *
from random import randint
pg=Tk()
pg.title(" neel's password generator")
pg.geometry("500x500")

def new_rand():
    pw_entry.delete(0,END)

    pw_length=int(my_entry.get())

    my_password =''

    for x in range(pw_length) :
        my_password+=chr(randint(33,126))
    pw_entry.insert(0,my_password)

def clipper() :
    pg.clipboard_clear()

    pg.clipboard_append(pw_entry.get())

my_pw=chr(randint(33,126))


lf=LabelFrame(pg,text="how many charceters")
lf.pack(pady=10)


my_entry=Entry(lf,font=("helvitica",40 ),bd=0,bg="systembuttonface")
my_entry.pack(pady=20,padx=20)


pw_entry=Entry(pg,text="",font=("helvitica",40))
pw_entry.pack(pady=20)


my_frame=Frame(pg)
my_frame.pack()


my_button=Button(my_frame,text="Generate strong password",command= new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button= Button(my_frame,text="copy to clpiboard",command=clipper)
clip_button.grid(row=0,column=1,padx=20)
pg.mainloop()