from tkinter import *
screen=Tk()
screen.title("Registration Form")
screen.geometry("400x400")
screen.resizable(False,False)
#label
Label(screen,text="Registration Form",font="ariel 20 bold",bg="red",fg="white").pack(fill="both")

Label(screen,text="Name",font="20").place(x=40,y=75)
Label(screen,text="Age",font="20").place(x=40,y=115)
Label(screen,text="Phone No",font="20").place(x=40,y=155)
Label(screen,text="Email Id",font="20").place(x=40,y=195)
#Entry
name_entry=Entry(screen,font="10")
name_entry.place(x=140,y=75)
age_entry=Entry(screen,font="10")
age_entry.place(x=140,y=115)
phone_entry=Entry(screen,font="10")
phone_entry.place(x=140,y=155)
email_entry=Entry(screen,font="10")
email_entry.place(x=140,y=195)
#Button
Button(screen,text="Register",font="20").place(x=185,y=255)
Button(screen,text="Clear",font="20").place(x=345,y=365)
mainloop()
