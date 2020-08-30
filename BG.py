from Tkinter import Frame, Label, Text
from Tkconstants import TOP, GROOVE, RIGHT, LEFT,  NW,CENTER, NORMAL, DISABLED
from Widgets import Button_set,  Set_Led
import inspect
from FuncTestDefinition import TestsDefinition
import GenerateHighQualityWavFile
import GenerateLowQualityWavFile
import GenerateLongDurationWavFile







class BG_C(Frame):
	
	def __init__(self,master ):
		
		Frame.__init__(self, master,width=0, height = 0, borderwidth=0,  background= "gray92",relief=GROOVE)
		self.pack(side=LEFT, anchor=NW)
		
		
		
		self.Logs = Logs_C(master=self,   side=RIGHT)
		self.Tests = TestsDefinition(self.Logs)
		
		
		
		self.LT = List_Of_Tests(master=self ,log =self.Logs, Tests=self.Tests,  side=RIGHT )
		self.Tests.Set_Test_Leds(self.LT)
		
		
		
		sampleHightQ = GenerateHighQualityWavFile.Gen()
		sampleLowQ = GenerateLowQualityWavFile.Gen()
		sampleLongD = GenerateLongDurationWavFile.Gen()
		
		self.Gen_Samples = Generate_Audio_Samples(master=self , log = self.Logs, sampleHightQ=sampleHightQ, sampleLowQ=sampleLowQ, sampleLongD=sampleLongD,  side=RIGHT)
				
		sampleHightQ.Set_led_widget(self.Gen_Samples)
		sampleLowQ.Set_led_widget(self.Gen_Samples)
		sampleLongD.Set_led_widget(self.Gen_Samples)



class Generate_Audio_Samples(Frame):
	
	def __init__(self,master, log, sampleHightQ , sampleLowQ , sampleLongD , side,):
		
		
		Frame.__init__(self, master,width=0, height = 0, borderwidth=2,  background= "gray92",relief=GROOVE)
		self.pack(side=side,padx=0, anchor=NW)
		
		label = Label(self, text="Generate Audio Samples",bg="gray78" , relief=GROOVE, fg = "black",font=("Helvetica", 14))
		label.pack(side=TOP,padx=10, pady=50)		
		
		
		self.Gen_lowquality_audio = Create_Test(self, text="Generate a low quality wav audio sample", method= sampleLowQ.Generate, log=log)
		
		self.Gen_highquality_audio = Create_Test(self, text="Generate a high quality wav audio sample", method=sampleHightQ.Generate, log=log)
		
		self.Gen_longdurationquality_audio = Create_Test(self, text="Generate a long duration wav audio sample", method=sampleLongD.Generate, log=log)
		
		

class Logs_C(Frame):
		
	def __init__(self,master,side):

		
		Frame.__init__(self, master,width=0, height = 0, borderwidth=2,  background= "gray92",relief=GROOVE)
		self.pack(side=side, anchor=NW)
		
		
		label = Label(self, text="Logs",bg="gray78",fg = "black",font=("Helvetica", 14))
		label.pack(side=TOP,padx=147.49, pady=2)
		
		
		
		self.logsvariable = Text(self,  bg="white", height= 60, width=50, font=("Silkscreen", 8),  wrap='word')
		self.logsvariable.pack(side=TOP, padx=2, pady=5)
		
	
		
class List_Of_Tests(Frame):
	
	def __init__(self,master, log, Tests, side ):
		
		
		Frame.__init__(self, master,width=0, height = 0, borderwidth=2,  background= "gray92",relief=GROOVE)
		self.pack(side=side,padx=0, anchor=NW)
		
		label = Label(self, text="List Of Tests",bg="gray78",fg = "black",font=("Helvetica", 14))
		label.pack(side=TOP,padx=20, pady=20)
		
		list_of_tests = inspect.getmembers(Tests)
		
		for i in (list_of_tests):
			if "Test" == i[0][0:4] and i[1].__doc__:
				test = Create_Test(self, text="Execute Test : "+i[1].__doc__ , method=i[1], log=log, background="gray78", anchor=CENTER, width=0, height=0, highlightcolor="black", foreground="black", side=TOP, padx=20, pady=5)
				
				setattr(self, i[0]+"_btn", test.get_button())
				setattr(self, i[0]+"_led", test.get_led())
				setattr(self, i[0]+"_desc", i[1].__doc__)
			


class Create_Test(Frame):
		
	def __init__(self,master,text="", method=None, log=None, background="gray78", anchor=CENTER, width=0, height=0, highlightcolor="black", foreground="black", side=TOP, padx=0, pady=0):
		
		Frame.__init__(self, master,width=0, height = 0, borderwidth=2,  background= "gray92",relief=GROOVE)
		self.pack(side=side, anchor=NW)	
		
		
		def bind_func(event):
			log.logsvariable.config(state=NORMAL)
			log.logsvariable.get('1.0',"end")
			log.logsvariable.delete('1.0',"end")
			log.logsvariable.insert('1.0',  text)
			log.logsvariable.config(state=DISABLED)
		
		
		self.btn = Button_set(self, text=text.split('\n')[0],method=method, background=background, anchor=anchor, width=width, height=height, highlightcolor=highlightcolor, foreground=foreground, side=LEFT, padx=10, pady=0)
		
		self.btn.bind("<Enter>", bind_func)
		
		self.led = Set_Led(self, bg= "gray78", side=LEFT, big_size=False, borderwidth=2 )
	
	
	
	
	
	
	def get_button(self):
	
		return self.btn 
	
	def get_led(self):
		return  self.led