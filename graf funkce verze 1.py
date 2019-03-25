# -*- coding: utf-8 -*-
"""
Created on Sat Mar 2 19:44:35 2019

@author: tom11
"""


from tkinter import 
from tkinter import filedialog


import pylab 


class App():
    
    def __init__(self,master):
       
        
        
        self.frame=Frame(master)
        self.frame.grid()


        self.selected=IntVar()
        self.selectedmax=StringVar()
      
        
        
        #okno 
        
        self.manualFrame = LabelFrame(master, text="Manuální graf")
        self.manualFrame.grid(column=1,row=1)
        
        
        #matematické operace
        Radiobutton(self.manualFrame,text="sin",variable=self.selected, value=0).grid(column=0,row=0)
        Radiobutton(self.manualFrame,text="exp",variable=self.selected, value=1).grid(column=0,row=1)
        Radiobutton(self.manualFrame,text="log",variable=self.selected, value=2).grid(column=0,row=2)
        
        
        
        #popsání polí
        
        #OD
        Label(self.manualFrame, text="Začátek").grid(column=1,row=0)
        Entry(self.manualFrame, textvariable=self.selectedmin,width=4).grid(column=2,row=0)
        
        
        #DO
        Label(self.manualFrame, text="Konec").grid(column=1,row=1)
        Entry(self.manualFrame, textvariable=self.selectedmax,width=4).grid(column=2,row=1)
        
        
        
        #vytvoření grafu 
        
        Button(self.manualFrame, text="Vytvoř graf",command=self.Graf).grid(column=1,row=3)
        
     
        #vytvoření podokna grafů se soubory
        self.selectedFile=StringVar(1)
        self.fileFrame = LabelFrame(master,text = "Grafy ze souboru",padx=10,pady=10)
        self.fileFrame.grid(column=1,row=1)
        
        
        
        #vybrat daný soubor
    
        Entry(self.fileFrame, textvariable=self.selectedFile).grid(sticky=)
        Button(self.fileFrame, text="Vyber soubor",command=self.pickfile).grid(column=0,row=1)
        
        Button(self.fileFrame, text="Vytvoř graf",command=self.SouborGraf).grid(column=0,row=2)
        
       
        #okno popisků os
        self.axisFrame=LabelFrame(master, text="Popis osy",padx=10,pady=10,width=15)
        self.axisFrame.grid(column=0,row=2)
        
        Label(self.axisFrame,text="Osa X").grid()
        Label(self.axisFrame,text="Osa Y").grid()
        
        
        
        #pojmenováni osy
        
        
        
        self.Xaxis=StringVar()
        self.Yaxis=StringVar()
        
        Entry(self.axisFrame, textvariable=self.Xaxis,width=15).grid(column=1,row=0)
        Entry(self.axisFrame, textvariable=self.Yaxis,width=15).grid(column=0,row=1)
        
        
        
        #vykreslování grafu z manuálních parametrů
    def Graf(self):
        #vykreslovací pole
        x = pylab.linspace(float(self.selectedmin.get()),float(self.selectedmax.get()) ,500)
       
        
        
        
        if self.selected.get()==0:
            y=pylab.sin(x)
        
        elif self.selected.get()==2:
            y=pylab.exp(x)
            
        elif self.selected.get()==1:
            y=pylab.log10(x)
    
    
        pylab.figure()
        pylab.plot(x,y)
        pylab.xlabel(self.Xaxis.get())
        pylab.ylabel(self.Yaxis.get())
        pylab.grid(True)
        pylab.show()
        
        
        #výběr souboru 
    def pickfile(self):
        self.path=filedialog.askopenfilename(title="Vybrat soubor")
        self.selectedFile.set(self.path)
        
        #graf ze souboru
    def SouborGraf(self):
       
        self.f = open(self.path,"")
   
       
      
        while True:
            self.line=self.f.readline():
                break
            self.numbers=self.line.split()
            self.x.append(float(self.numbers[0]))
            self.y.append(float(self.numbers[1]))
            
        self.f.close()
        pylab.figure()
        pylab.plot(self.x,self.y)
        pylab.xlabel(self.Xaxis.get())
        pylab.ylabel(self.Yaxis.get())
        pylab.grid(True)
        pylab.show()
        
        
root = Tk()
app = App(root)
root.mainloop()