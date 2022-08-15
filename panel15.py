import math 
import pygame
import time
from tkinter import*
from tkinter import ttk

class panel(Frame):
    def __init__(self,canvas,elevator_list):
        Frame.__init__(self)
        self.cp_1_x=-20
        self.cp_1_y=-200
     
     
        self.canvas=canvas
        self.combobox_list=[]
        self.cur_var=StringVar()
        self.is_selected=False
        
        for i in range (0, 4):  
            self.combobox_list.append([])
        self.elevator_list=elevator_list
        
        cv1=canvas.create_rectangle(10,100,500,400,fill="#D3D3D3",outline="#7F7FFF")
        display_label=Label(canvas,text="-please choose the floor you want to go",background="#D3D3D3",foreground="#212F3C",font=("Helvetica 15")).place(x=60,y=150)
        
         
    def combobox(self):
        #lift1
        body_1=canvas.create_rectangle(50+self.cp_1_x,200,150+self.cp_1_x,300,fill ="#fff",activefill="#C1E950",outline="#7F7FFF")
        cur_var=StringVar()
        label_car1=Label(canvas,text="CAR1",background="#D3D3D3",font=("Bizon 10 bold"),foreground="#7F7FFF").place(x=60,y=310)
        self.combobox_key1=ttk.Combobox(canvas,textvariable=cur_var,state="normal")
        self.combobox_key1["values"]= [ n for n in range(1,11)]
        self.combobox_key1.current(0)
        self.combobox_key1.bind("<<ComboboxSelected>>",lambda event:self.combobox_selected(1,event))
        self.combobox_key1.place(x=60,y=240,width=40)
        
        #lift2
        body_2=canvas.create_rectangle(160+self.cp_1_x,200,260+self.cp_1_x,300,fill ="#fff",activefill="#C1E950",outline="#7F7FFF")
        cur_var=StringVar()
        label_car2=Label(canvas,text="CAR2",background="#D3D3D3",font=("Bizon 10 bold"),foreground="#7F7FFF").place(x=170,y=310)
        self.combobox_key2=ttk.Combobox(canvas,textvariable=cur_var,state="normal")
        self.combobox_key2["values"]= [ n for n in range(1,11)]
        self.combobox_key2.current(0)
        self.combobox_key2.bind("<<ComboboxSelected>>",lambda event:self.combobox_selected(2,event))
        self.combobox_key2.place(x=170,y=240,width=40)
        
        #lift3
        body_3=canvas.create_rectangle(270+self.cp_1_x,200,370+self.cp_1_x,300,fill ="#fff",activefill="#C1E950",outline="#7F7FFF")
        cur_var=StringVar()
        label_car3=Label(canvas,text="CAR3",background="#D3D3D3",font=("Bizon 10 bold"),foreground="#7F7FFF").place(x=280,y=310)
        self.combobox_key3=ttk.Combobox(canvas,textvariable=cur_var,state="normal")
        self.combobox_key3["values"]= [ n for n in range(1,11)]
        self.combobox_key3.current(0)
        self.combobox_key3.bind("<<ComboboxSelected>>",lambda event:self.combobox_selected(3,event))
        self.combobox_key3.place(x=280,y=240,width=40)
        
        
        #lift4
        body_4=canvas.create_rectangle(380+self.cp_1_x,200,480+self.cp_1_x,300,fill ="#fff",activefill="#C1E950",outline="#7F7FFF")
        cur_var=StringVar()
        label_car4=Label(canvas,text="CAR4",background="#D3D3D3",font=("Bizon 10 bold"),foreground="#7F7FFF").place(x=390,y=310)
        self.combobox_key4=ttk.Combobox(canvas,textvariable=cur_var,state="normal")
        self.combobox_key4["values"]= [ n for n in range(1,11)]
        self.combobox_key4.current(0)
        self.combobox_key4.bind("<<ComboboxSelected>>",lambda event:self.combobox_selected(4,event),self.is_selected)
        self.combobox_key4.place(x=390,y=240,width=40)
        
    def is_selected(self):
        pass
        self.is_selected=True
     
    def combobox_selected(self,no,event):
        combobox_key=event.widget.get()
        print(("lift:" +" "+ str(no))+"   "+ "value:"+"  "+str(combobox_key))
        if no==1:
                self.combobox_key1["state"]="disabled"
                self.elevator_list[no-1].addFloor(combobox_key,"none")
                
                
        elif no==2:
            self.combobox_key2["state"]="disabled"
            self.elevator_list[no-1].addFloor(combobox_key,"none")
        elif no==3:
            self.combobox_key3["state"]="disabled"
            self.elevator_list[no-1].addFloor(combobox_key,"none")
        else:
            self.combobox_key4["state"]="disabled"
            self.elevator_list[no-1].addFloor(combobox_key,"none")
            




            
        
            
            
            
            

                
            
            
        
        
        

        
        
            
        
        
        
        
        
        
"""window=Tk() 
frame1=Frame(window,width=600,height=800)
frame1.grid(row=0,column=0,sticky=W+N+S)
cv=Canvas(frame1,width=600,height=800)
cv.grid(sticky=W+N+S+E)


frame2=Frame(window,width=600,height=800)
frame2.grid(row=0,column=1,sticky=E+N+S)
canvas=Canvas(frame2,width=520,height=400)
canvas.grid(sticky=N+E+W+S)
elev=[1,2,3]
a=panel(canvas,elev)
a.combobox()
window.mainloop()
"""