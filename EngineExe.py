#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 2


from Tkconstants import NORMAL, DISABLED
import inspect




class Engine(object):
   

    def __init__(self, BGLogs):

        self.BGLogs = BGLogs
        
    def AssertOK(self):    
        current_frame = inspect.currentframe()
        call_frame = inspect.getouterframes(current_frame,2)  
        
        for  i in  inspect.getmembers(self.LedTest):
            if call_frame[1][3]+'_led' == i[0]:
                
                i[1].canvas.itemconfig(i[1].circle, fill="green") 
    
    
    def AssertKO(self):    
        current_frame = inspect.currentframe()
        call_frame = inspect.getouterframes(current_frame,2)  
        
        for  i in  inspect.getmembers(self.LedTest):
            if call_frame[1][3]+'_led' == i[0]:
                
                i[1].canvas.itemconfig(i[1].circle, fill="red")
    
    
    def set_Logs(self, msg):
        
        self.BGLogs.logsvariable.config(state=NORMAL)
        self.BGLogs.logsvariable.get('1.0',"end")
        self.BGLogs.logsvariable.delete('1.0',"end")
        self.BGLogs.logsvariable.insert('1.0',  msg)
        self.BGLogs.logsvariable.config(state=DISABLED)  

          
    def Set_Test_Leds(self, LedTest):
        self.LedTest = LedTest

    
    
    def Set_GenSample_Leds(self, SampleLeds):
        
        self.SampleLeds = SampleLeds
        print inspect.getmembers(self.SampleLeds)
    
        