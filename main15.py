#from floor6 import *
from car15 import *
from tkinter import *
from panel15 import *
import panel15
import math

class interface:
    def __init__(self,master):
        global building
        self.master = master
        self.frame1=Frame(window,width=600,height=800)
        self.frame1.grid(row=0,column=0,sticky=W+N+S)
        self.frame2=Frame(window,width=600,height=800)
        self.frame2.grid(row=0,column=1,sticky=E+N+S)
        
        self.building = Canvas(self.frame1, width = 600, height = 800)
        self.building.grid(sticky=W+N+S+E)

        self.panel = Canvas(self.frame2, width = 520, height = 800)
        self.panel.grid(sticky=W+N+S+E)
       # self.panel.create_rectangle(10,100,500,400,fill="#D3D3D3",outline="#7F7FFF")
        self.panel.create_rectangle(10,420,500,700,fill="white",outline="#7F7FFF")
        #self.make_floors(self.building)
        self.make_elevators(self.building)
        self.draw_panel(self.panel)
        
    def make_elevators(self,canvas):

        self.elevator_list = []
        for i in range(0,4):
            e = car(self,canvas, i)
            self.elevator_list.append(e)
            
    def draw_panel(self, arena):
        self.p = panel(arena,self.elevator_list)
        
    
    #def make_floors(self,canvas):
    #    self.canvas.create_rectangle(115,100,215,700, fill = "#F5B041")
     #   self.canvas.create_rectangle(220,100,320,700, fill = "#F5B041")
      #  self.canvas.create_rectangle(325,100,425,700, fill = "#F5B041")
    #    self.canvas.create_rectangle(430,100,530,700, fill = "#F5B041")
       #     
     #   self.floor_list=[]
      #  for i in range(1,11):
       #     f = Floor(canvas,self,i)
        #    self.floor_list.append(f)
            
    def simulate(self):

        for e in self.elevator_list:
            e.update(self.building)
        self.master.after(40,self.simulate)
        

        
    def floorRequest(self,X,direc):
        if (direc=="up"):
            A=[200]*4
            for e in self.elevator_list:
                if e.ready==1:
                    if e.move_direction=="up" and e.current_floor<=X:
                        A[e.name]=e.current_floor
                    elif e.move_direction=="idle":
                        if(len(e.callQueue)>0):
                            if e.callQueue[0][0]>e.current_floor and e.current_floor>X:
                                A[e.name]=2*max(e.callQueue)[0]-e.current_floor
                            elif e.callQueue[0][0]<e.current_floor and min(e.callQueue)[0]<=X:
                                A[e.name]=e.current_floor+X-min(e.callQueue)[0]
                            else:
                                A[e.name]=e.current_floor
                        else:
                            A[e.name]=e.current_floor
                    elif e.move_direction=="up" and e.current_floor>X:
                        A[e.name]=2*max(e.callQueue)[0]-e.current_floor
                    elif e.move_direction=="down":
                        Y=min(e.callQueue)[0]
                        if Y>X:
                            A[e.name]=e.current_floor
                        else:
                            A[e.name]=e.current_floor-Y+X-Y
            if self.elevator_list[0].ready!=1 and self.elevator_list[1].ready!=1 and self.elevator_list[2].ready!=1 and self.elevator_list[3].ready!=1:
                A[self.elevator_list[0].name]=100
            print(A) 
            mini=abs(X-A[0])
            mini_index=0
            for i in range(0,4):
                A[i]=abs(X-A[i])
                if mini>=A[i]:
                    mini=A[i]
                    mini_index=i
            self.elevator_list[mini_index].addFloor(X,direc)

        elif (direc=="down"):
            A=[200]*4
            for e in self.elevator_list:
                if e.ready==1:
                    if e.move_direction=="down" and e.current_floor>=X:
                        A[e.name]=e.current_floor
                    elif e.move_direction=="idle":
                        if(len(e.callQueue)>0):
                            if e.callQueue[0][0]<e.current_floor and e.current_floor<X:
                                A[e.name]=2*min(e.callQueue)-e.current_floor
                            elif e.callQueue[0][0]>e.current_floor and max(e.callQueue)[0]>=X:
                                A[e.name]=e.current_floor+max(e.callQueue)[0]-X
                            else:
                                A[e.name]=e.current_floor
                        else:
                             A[e.name]=e.current_floor
                    elif e.move_direction=="down" and e.current_floor<X:
                        A[e.name]=2*min(e.callQueue)[0]-e.current_floor
                    elif e.move_direction=="up":
                        Y=max(e.callQueue)[0]
                        if Y<X:
                            A[e.name]=e.current_floor
                        else:
                            A[e.name]=Y-e.current_floor+Y-X 
                if self.elevator_list[0].ready!=1 and self.elevator_list[1].ready!=1 and self.elevator_list[2].ready!=1 and self.elevator_list[3].ready!=1:
                    A[self.elevator_list[0].name]=100      
            print(A)
            mini=abs(X-A[0])
            mini_index=0
            for i in range(0,4):
                A[i]=abs(X-A[i])
                if mini>=A[i]:
                    mini=A[i]
                    mini_index=i
            self.elevator_list[mini_index].addFloor(X,direc)
            
    def update_clock(self):
                now=time.strftime("%H:%M:%S")
                label_time.configure(text=now)
                self.master.update()
                self.master.after(1000,self.update_clock) 
            
        
            
            
        
    
            
        
        
       
        


        
        

window = Tk()
window.title("lift system design")
window.geometry("1200x900")
app = interface(window)
label_time=Label(text="")
app.update_clock()
label_time.grid(sticky=W+S)



app.simulate()

window.mainloop()
