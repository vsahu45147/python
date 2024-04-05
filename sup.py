from turtle import *
import os
import time
import pickle
setup(width=1500,height=1500,startx=0,starty=0)
bgcolor('pink')
up()
goto(-245,200)
write("GAME OVER",False,align='left',font=("Domestic Manners",62,"bold"))
goto(-245,100)
redplace=pickle.load(open("Places/redplace.dat","rb"))
greenplace=pickle.load(open("Places/greenplace.dat","rb"))
yellowplace=pickle.load(open("Places/yellowplace.dat","rb"))
blueplace=pickle.load(open("Places/blueplace.dat","rb"))
maxplace=pickle.load(open("Misc/maxplace.dat","rb"))

def place_1():
    global redplace,greenplace,yellowplace,blueplace,maxplace
    if(redplace==1):
        write(" Red won 1st Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(greenplace==1):
        write(" Green won 1st Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(yellowplace==1):
        write(" Yellow won 1st Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(blueplace==1):
        write(" Blue won 1st Place",False,align='left',font=("Domestic Manners",32,"bold"))



def place_2():
    global redplace,greenplace,yellowplace,blueplace,maxplace
    goto(-245,0)
    if(redplace==2):
        write(" Red won 2nd Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(greenplace==2):
        write(" Green won 2nd Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(yellowplace==2):
        write(" Yellow won 2nd Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(blueplace==2):
        write(" Blue won 2nd Place",False,align='left',font=("Domestic Manners",32,"bold"))


def place_3():
    global redplace,greenplace,yellowplace,blueplace,maxplace
    goto(-245,-100)
    if(redplace==3):
        write(" Red won 3rd Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(greenplace==3):
        write(" Green won 3rd Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(yellowplace==3):
        write(" Yellow won 3rd Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(blueplace==3):
        write(" Blue won 3rd Place",False,align='left',font=("Domestic Manners",32,"bold"))



def place_4():
    global redplace,greenplace,yellowplace,blueplace,maxplace
    goto(-245,-200)
    if(redplace==0):
        write(" Red won 4th Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(greenplace==0):
        write(" Green won 4th Place",False,align='left',font=("Domestic Manners",32,"bold"))    
    elif(yellowplace==0):
        write(" Yellow won 4th Place",False,align='left',font=("Domestic Manners",32,"bold"))
    elif(blueplace==0):
        write(" Blue won 4th Place",False,align='left',font=("Domestic Manners",32,"bold"))

place_1()
place_2()
if(maxplace==3):
    place_3()
if(maxplace==4):
    place_3()
    place_4()

goto(-300,-300)
write(" Press  Enter  To  Continue",False,align='left',font=("Domestic Manners",32,"bold"))
def Enter():
    bye()
    os.system("python3 main.py")
onkey(Enter,"Return")
listen()

mainloop()
done()