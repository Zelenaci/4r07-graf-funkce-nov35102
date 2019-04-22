# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 18:14:29 2019
@author: tom11
"""

from tkinter import *
from tkinter import filedialog
import pylab 





class App():
    
    
    
    
    def __init__(self,master):
        self.frame=Frame(master)
        self.frame.grid()
        
        
        
    
        self.selected=IntVar()
        self.selectedmax=StringVar()
        self.selectedmin=StringVar()
        
        
        
        
        
        #okno  výběru
        self.manualFrame = LabelFrame(master, text="Manuálně vytvořit graf")
        self.manualFrame.grid(column=1,row=1)
        
        
        
        
        #vybrání funkce
        
        
        
        Radiobutton(self.manualFrame,text="sin",variable=self.selected, value=0).grid(column=0,row=0)
        Radiobutton(self.manualFrame,text="log",variable=self.selected, value=1).grid(column=0,row=1)
        Radiobutton(self.manualFrame,text="exp",variable=self.selected, value=2).grid(column=0,row=2)
        
        
        
        
        
        
        
        Label(self.manualFrame, text="Od").grid(column=1,row=0)
        Entry(self.manualFrame, textvariable=self.selectedmin,width=5).grid(column=2,row=0)
        
        Label(self.manualFrame, text="Do").grid(column=1,row=1)
        Entry(self.manualFrame, textvariable=self.selectedmax,width=5).grid(column=2,row=1)
        
        
        
        
        #vytvoření grafu 
        Button(self.manualFrame, text="Vykreslit",command=self.Graf).grid(column=1,row=3)
      
        
        
        
        
        
        
        
        #vytvořit podokno
        self.selectedFile=StringVar()
        self.fileFrame = LabelFrame(master,text = "Graf ze souboru",padx=10,pady=10)
        self.fileFrame.grid(column=0,row=1)
        
        
        #výběr souboru
        
        
        Label(self.fileFrame,text="Vložit trasu souboru")
        Entry(self.fileFrame, textvariable=self.selectedFile).grid(sticky=W)
        Button(self.fileFrame, text="Vyberte soubor",command=self.pickfile).grid(column=0,row=1)
        
        Button(self.fileFrame, text="Vykreslit",command=self.SouborGraf).grid(column=0,row=2)
      
        
        
        
        #popis os
        self.axisFrame=LabelFrame(master, text="Popis os",padx=5,pady=5,width=10)
        self.axisFrame.grid(column=0,row=2)
        
        
        
        Label(self.axisFrame,text="Osa X").grid()
        Label(self.axisFrame,text="Osa Y").grid()
        
        
        
        
        
        
        #názvy os
        self.Xaxis=StringVar()
        self.Yaxis=StringVar()
        
        
        
        
        Entry(self.axisFrame, textvariable=self.Xaxis,width=15).grid(column=1,row=0)
        Entry(self.axisFrame, textvariable=self.Yaxis,width=15).grid(column=1,row=1)
        
        
        
        
        
        
        
        
        
        
        
        #vykreslování grafu 2
  
    
    def Graf(self):
        # pole
        x = pylab.linspace(float(self.selectedmin.get()),float(self.selectedmax.get()) ,500)
        
        
        #výběr funkce 
        if self.selected.get()==0:
            y=pylab.sin(x)
            
        elif self.selected.get()==1:
            y=pylab.log10(x)
            
        elif self.selected.get()==2:
            y=pylab.exp(x)
            
        #vykreslení grafu
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
        #načtení souboru
        self.f = open(self.path,"0")


       
        
        
        
        
        
        
        
 
        while True:
            self.line=self.f.readline()
            if self.line=="":
                break
            self.numbers=self.line.split()
            self.x.append(float(self.numbers[1]))
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