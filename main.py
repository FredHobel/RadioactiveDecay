import random
import numpy as np
import tkinter
from tkinter import messagebox






def decay(count, halflife):


    sample = np.zeros(count)
    remaining = count
    measure = 0
    tick = 0
    percent = []
    
    while remaining > 0:
        #print(sample)
        i = 0
        for i in range(0,count):
            
            if sample[i] == 0:
                measure = random.randint(0,1)

                if measure == 1:
                    remaining = remaining - 1
                    sample[i] = 1
                measure = 0
            if i == count-1:
                tick += 1
                percent.append(remaining/count)


    time = tick*halflife
    return time, percent
    
"""
count = int(input("enter the number of particles to simulate: "))
if count == 0:
    count = 1

halflife = float(input("enter the half life of the particles in seconds: "))
halflife, count = abs(halflife), abs(count)
"""

top = tkinter.Tk()

top.geometry("500x400")

L1 = tkinter.Label(top, text="Number of particles:")
L1.pack( side = tkinter.LEFT)

E1 = tkinter.Entry(top, bd =5)
E1.pack(side = tkinter.LEFT)



E2 = tkinter.Entry(top, bd =5)
E2.pack(side = tkinter.RIGHT)

L2 = tkinter.Label(top, text="Half life in seconds:")
L2.pack( side = tkinter.RIGHT)



def helloCallBack():
    amount = int(E1.get())
    half = float(E2.get())
    ret2 = ""

    if amount < 1 or half <= 0:
        tkinter.messagebox.showinfo("Results","Invalid entry")
    else:
        ret, retlist = decay(amount,half)  
        ret = str(ret)
        for i in range(len(retlist)):
            ret2 += str(retlist[i]) + ', '


        tkinter.messagebox.showinfo("Results","It took " + ret + " seconds for the sample to fully decay. The proportions remaining at each halflife were " + ret2 )

B1 = tkinter.Button(top, text ="Results", command = helloCallBack)
B1.place(x = 250,y = 350)



# Code to add widgets will go here...
top.mainloop()


#print (decay(count, halflife))

