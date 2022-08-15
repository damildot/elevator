
import numpy as np
class car(object):

	def __init__(self,building,canvas,name):
		self.canvas=canvas
		self.width = 120
		self.height = 60
		self.seperation = 160 
		self.startx = 100
		self.starty = 100
		self.velo = 5
		self.velo2= 1
		self.color= "#2E4053"
		self.building=building
		self.name = name
		canvas.create_rectangle(100,100,580,800,fill="",outline="#ff0000")
		self.body = canvas.create_rectangle(self.startx+(self.name*self.seperation),self.starty+535,self.startx+self.width+(self.name*self.seperation),self.starty+self.height+535,fill=self.color)
		self.x = canvas.coords(self.body)[0]
		self.y = canvas.coords(self.body)[1]
		self.dest = "None"
		self.left = canvas.create_rectangle(self.startx+(self.name*self.seperation)+self.width/2,self.y,self.startx+(self.name*self.seperation)+self.width/2,self.y+self.height,fill="#FE8")
		self.right = canvas.create_rectangle(self.startx+(self.name*self.seperation)+self.width/2,self.y,self.startx+(self.name*self.seperation)+self.width/2,self.y+self.height,fill="#FE8")
		self.floor_list = []
		for i in range(0,10):
			self.floor_list.append(False)
		self.callQueue = []
		self.dest = None
		self.gate_status = 0
		self.move_direction = "idle"
		self.open_status = 0
		self.status = "idle"
		self.current_floor = 0
		self.vel = 0
		self.people=0
		self.ready=1
  
	def sorted_queue(self,callQueue):
		q_len= len(callQueue)
		callQueue =np.sort(callQueue)
		current=self.current_floor
		if self.move_direction=="up":
			for i in range (0,q_len):
				if callQueue[i][0]>current:
					above_dest=list(callQueue[i])
		
		elif self.move_direction=="down":
			for i in range (0,q_len):
				if callQueue[i][0]<current:
					below_dest=list(callQueue[i])
     
		above_dest=sorted(above_dest,reverse=True)
		below_dest=sorted(below_dest,reverse=False)
		self.callQueue=above_dest+below_dest
  
	def addFloor(self,floor,dir):
		if [floor,dir] not in self.callQueue:
			if ((([floor,"up"] not in self.callQueue) or ([floor,"down"] not in self.callQueue))  and dir=="none"):
				self.callQueue.append([floor,dir])
			elif dir=="up" or dir=="down":				
				self.callQueue.append([floor,dir])
				if [floor,"none"] in self.callQueue:
					self.callQueue.remove([floor,"none"])
     

		self.sorted_queue(self.callQueue)
		print ("call queue "+ str(self.name+1)+" "+ str(self.callQueue))
  
	def update(self,canvas):
		if self.status == "idle":
			self.checkQueue()

		elif self.status == "moving":
			self.checkQueue()
			self.checkDestination()
			self.moveElevator(canvas)

		elif self.status == "opening":
			self.openGate(canvas)

		elif self.status == "open":
			self.keepGateOpen()

		elif self.status == "closing" and self.ready==1:
			self.closeGate(canvas)

		elif self.status == "closing" and (self.ready==2 or self.ready==3):
			self.openGate(canvas)
   
		canvas.update()
  
	def checkQueue(self):

		if not(len(self.callQueue)==0):
			self.dest = self.callQueue[0][0]
			if self.status == "idle":
				if self.current_floor < self.dest:
					self.vel = -self.velo
				elif self.current_floor > self.dest:
					self.vel = self.velo
				else:
					self.vel = 0

			self.status = "moving"

	def checkDestination(self):
		if not(len(self.callQueue)==0):
			self.dest = self.callQueue[0][0]
		self.sorted_queue(self.callQueue)
		self.current_floor = float(10-(self.y))
		if self.dest == self.current_floor:
			if self.callQueue[0][1]=="up":
				self.building.floor_list[self.dest].upButtonTurnOff()
				self.building.floor_list[self.dest].elevator_floor_up = None
			elif self.callQueue[0][1]=="down":
				self.building.floor_list[self.dest].downButtonTurnOff()
				self.building.floor_list[self.dest].elevator_floor_down = None


			panel = self.building.p
			if self.dest==0:
				panel.canvas.itemconfig(panel.button_list[self.name][9], fill="#A9A9A9")
				panel.flag_list[self.name][9] = False
			else:
				panel.canvas.itemconfig(panel.button_list[self.name][int(self.dest)-1], fill="#A9A9A9")
				panel.flag_list[self.name][int(self.dest)-1] = False

			
			self.callQueue.remove(self.callQueue[0])


			self.status = "opening"
			self.vel = 0

	def openGate(self,canvas):
		if self.gate_status == 20:
			self.status = "open"
		else:
			self.gate_status += 1
			canvas.coords(self.left,self.x+self.width/2,self.y,self.x-self.gate_status+self.width/2,self.y+self.height)
			canvas.coords(self.right,self.x+self.width/2,self.y,self.x+self.gate_status+self.width/2,self.y+self.height)

	def keepGateOpen(self):
		if self.open_status >= 40 and self.ready==1:
			self.status = "closing"
			self.open_status = 0

		else:
			self.open_status += 2

	def closeGate(self,canvas):
		if self.gate_status == 0 :
			self.status = "idle"

		else:
			self.gate_status -= 1
			canvas.coords(self.left,self.x-self.gate_status+self.width/2,self.y,self.x+self.width/2,self.y+self.height)
			canvas.coords(self.right,self.x+self.width/2+self.gate_status,self.y,self.x+self.width/2,self.y+self.height)

	

	def moveElevator(self,canvas):
		if self.vel>0:
			self.move_direction = "down"
		elif self.vel<0:
			self.move_direction = "up"
		else:
			self.move_direction = "idle"

		canvas.move(self.body,0,self.vel)
		canvas.move(self.left,0,self.vel)
		canvas.move(self.right,0,self.vel)
		self.x = canvas.coords(self.body)[0]
		self.y = canvas.coords(self.body)[1]




     
		
	
  
  

  
  
  
  
  
  
  
  
		
		
"""window=Tk() 
frame1=Frame(window,width=600,height=800)
frame1.grid(row=0,column=0,sticky=W+N+S)
cv=Canvas(frame1,width=600,height=800)
cv.grid(sticky=W+N+S+E)
for i in range(4):
	car(frame1, cv, i)
window.mainloop()
"""