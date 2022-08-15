import math
from tkinter import*
import math
from PIL import Image, ImageTk, ImageSequence


class Floor(Frame):
	def __init__(self,name,canvas,app):
	 	Frame.__init__(self)
		self.app =app
		self.name = name
		self.canvas=canvas
		arrow_button1=ImageTk.PhotoImage(Image.open(r"C:\Users\Monster\Desktop\elevator-project\SON\arrowup1.png"))
		arrow_button2=ImageTk.PhotoImage(Image.open(r"C:\Users\Monster\Desktop\elevator-project\SON\arrowdown1.png"))
		if self.name==10:
						
					self.outside_buttons1=Button(canvas,width=20,height=20,text=f"{self.name}",image=arrow_button2,borderwidth=0)
					self.outside_buttons2=Button(canvas,width=20,height=20,text=f"{self.name}",image=arrow_button1,borderwidth=0)
					self.outside_buttons1.place(in_=self.outside_buttons2,rely=2,relx=1.4,anchor=S)
					self.outside_buttons2.place(in_=self.outside_buttons1,rely=-1.2,relx=0)
					self.outside_buttons1.configure(command=lambda:self.onButtonClickDown)
					self.outside_buttons2.configure(command=lambda:self.onButtonClickUp)
		elif self.name!=10:      
					self.outside_buttons1=Button(canvas,width=20,height=20,text=f"{self.name}",image=arrow_button2,borderwidth=0)
					self.outside_buttons2=Button(canvas,width=20,height=20,text=f"{self.name}",image=arrow_button1,borderwidth=0)
					self.outside_buttons1.place(in_=self.outside_buttons2,rely=2,relx=1.6,anchor=S)
					self.outside_buttons2.place(in_=self.outside_buttons1,rely=-1.2,relx=0)
					self.outside_buttons1.configure(command=lambda:self.onButtonClickDown)
					self.outside_buttons2.configure(command=lambda :self.onButtonClickUp)
		self.up_status = "off"
		self.down_status = "off"
		self.elevator_floor_up = []
		self.elevator_floor_down = []
	
	
	 
	def onButtonClickUp(self,event):
		 
		print ("Floor "+str(self.name)+" Up Button "+str(event.x)+" "+str(event.y))
		self.canvas.itemconfigure(self.outside_buttons1,fill="black")
		self.up_status = "on"
		self.app.floor_request(self.name,"up")

	def onButtonClickDown(self,event):
		print ("Floor "+str(self.name)+" Down Button "+str(event.x)+" "+str(event.y))
		self.canvas.itemconfigure(self.outside_buttons2,fill="#CC99CC")
		self.down_status = "on"
		self.app.floor_request(self.name,"down")

	def upButtonTurnOff(self):
		self.canvas.itemconfigure(self.outside_buttons1, fill = "#000")
		self.up_status = "off"

	def downButtonTurnOff(self):
		self.canvas.itemconfigure(self.outside_buttons2, fill = "#000")
		self.down_status = "off"
	
		self.canvas.itemconfigure(self.outside_buttons2, fill = "#000")
		self.down_status = "off"
	
"""window=Tk() 
frame1=Frame(window,width=600,height=800)
frame1.grid(row=0,column=0,sticky=W+N+S)
cv=Canvas(frame1,width=600,height=800)
cv.grid(sticky=W+N+S+E)


frame2=Frame(window,width=600,height=800)
frame2.grid(row=0,column=1,sticky=E+N+S)
canvas=Canvas(frame2,width=520,height=400)
canvas.grid(sticky=N+E+W+S)
for i in range(4):
	a=Floor(canvas,i)

window.mainloop()"""