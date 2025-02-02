class AttendanceManager(tk.Tk):
	def __init__(self,*args,**kwargs):
		tk.Tk. __init__(self,*args,**kwargs)
		container=tk.Frame(self)
		
		container.pack(side="top",fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
		
		self.frames=dict() 	
		for F in (StartPage,NewRecord,ManageAttendance,DeleteRecord,EditRecord,AddSubjects,TodayData):
			frame=F(container,self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		
		self.show_frame(StartPage)
	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()
