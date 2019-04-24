#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Apr  9 10:06:18 2019

@author: nov35102
"""


from tkinter import *
from tkinter import messagebox as msb
from tkinter import filedialog as fld



#otevírání soubor


u
def Otevrit():
    text.delete(1.0,END)
    cesta=fld.askopenfilename(title="Otevřít soubor")
    try:
        soubor=open(cesta,"r")
        for radek in soubor:
            text.insert(END,radek)
        soubor.close()
    except:pass




#uložení
    
def Ulozit():
    sta=fld.askopenfilename(title="Uložit soubor")
    try:
        soubor=open(cesta,"w")
        ret=text.get(1.0,END)
        soubor.write(ret)
        soubor.close()
    except:pass


#konec aplikace
def Konec():
    x=msb.askyesno("Konec ","Konec?")
    if x:
        hlavni.destroy()
 

#velká písmena
def Velka():
    a=text.get(1.0,END)
    a=a.upper()
    text.delete(1.0,END)
    text.insert(1.0,a)
    
    
    
    
    
    
    
    
    
    
    
   
# otevření okna


def OknoNahrad():
    global vstup1
    global vstup2
    global oknoN
    oknoN=Toplevel()
    oknoN.title("Nahrazení znaku")
    t1=Label(oknoN,text="Nahradit znak: ")
    t1.pack(pady=3)
    vstup1=Entry(oknoN)
    vstup1.pack(pady=3)
    t2=Label(oknoN,text="znak:")
    t2.pack(pady=3)
    vstup2=Entry(oknoN)
    vstup2.pack(pady=3)
    akce1=Button(oknoN,text="udělej hned",width=10)
    akce1.pack(pady=3)
    
    
    
    
    
    
    
    
    

hlavni=Tk()

abeceda=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]








text=Text(hlavni,font="Calibry10")
text.pack()

hornimenu=Menu(hlavni)
menusoubor=Menu(hornimenu,tearoff=0)


menusoubor.add_command(label="Otevřít",command=Otevrit)
menusoubor.add_command(label="Uložit",command=Ulozit)


menusoubor.add_separator()







menusoubor.add_command(label="Konec",command=Konec)
hornimenu.add_cascade(label="Soubor",menu=menusoubor)











menuoperace=Menu(hornimenu,tearoff=0)

menuoperace.add_command(label="Velká písmena",command=Velka)

menuoperace.add_command(label="Nahradit znak",command=OknoNahrad)

menuoperace.add_command(label="VYtvořit text")

hornimenu.add_cascade(label="Operace",menu=menuoperace)












hlavni.config(menu=hornimenu)







hlavni.mainloop()