#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 2

import requests


from EngineExe import Engine

import sys



class TestsDefinition(Engine):
   

        
    
    
    
    def Test1(self):
        """ 1. Check that port is configurable
    
    Initial Condition : Run music store server 0.1.0 executable by opening a shell command line and launch following command:
    music_store_server-0.1.0-windows.exe -p 3000"""
        
   
                 
        myurl = 'http://localhost:3000'
          
       
        
            
        try:
            x  = requests.request('GET', url=myurl )
            
            
            
            self.set_Logs(x.text)
            if x.status_code == 200:
                self.AssertOK() 
            else:
                self.AssertKO()
        
        
        except:
            self.set_Logs("Not able to connect to port 3000")
            self.AssertKO()
        
    
    
    
    
    def Test2(self):
        """2.Check that Storage folder is configurable
Initial Condition:
1. Create a folder "Storage" in <local_adress>/Storage
2. Run music store server 0.1.0  executable by opening a shell command line and launch following command:
music_store_server-0.1.0-windows.exe -p 5555 ./<local_adress>/Storage

3.Put several wav file sample in Storage folder

4.open a web browser and tape following address:  
http://localhost:5555/list"""
        
    
        myurl = 'http://localhost:5555/list'
          
       
        
            
        try:
            x  = requests.request('GET', url=myurl )
            
            self.set_Logs(str(x.status_code)+"\n"+ x.text)
            if x.status_code == 200 and len(x.text.split('.wav\",')) > 1:
                self.AssertOK() 
            else:
                self.AssertKO()
        
        
        except:
            self.set_Logs(str(sys.exc_info()[1])+'\n'+str(sys.exc_info()[1]))
            self.AssertKO()
    
    
    
    
    
    
    
    
    def Test3(self):
        """3-check available routes are available and comprehensive for user
        Initial Condition:
1. Run music store server 0.1.0 executable

2. From Client side, open Chrome and enter web adress: http://localhost:5555/"""
    
        myurl = 'http://localhost:5555/'
          
       
        
            
        try:
            x  = requests.request('GET', url=myurl )
            
            self.set_Logs(str(x.status_code)+"\n"+ x.text)
            if x.status_code == 200 and "POST" in x.text and "GET" in x.text and "DELETE" in x.text:
                self.AssertOK() 
            else:
                self.AssertKO()
        
        
        except:
            self.set_Logs(str(sys.exc_info()[1])+'\n'+str(sys.exc_info()[1]))
            self.AssertKO()
    
    
    
    def Test4(self):
        """4-Check the upload of an high quality audio wav sample
        Initial Condition:
        Generate a high quality wav audio sample with button on left"""
        
        f= open('outputHighQuality.wav'  ,"rb")
        myurl = 'http://localhost:5555/upload'
        header =  { 'content_type': 'audio/wav' }   
        x  = requests.request('POST', url=myurl , data = f , headers=header  ) 
        print (x.text)
        print (x.status_code)
        if x.status_code == 200:
            self.music_id = x.content
            self.set_Logs(x.text)
            self.AssertOK()
            
        else:
            self.set_Logs(x.text)
            self.AssertKO()
    
    
    
    
    
    def Test5(self):
        """5-Check the upload of an low quality audio wav sample
        Initial Condition:
        Generate a low quality wav audio sample with button on left"""
        
        f= open('outputLowQuality.wav'  ,"rb")
        myurl = 'http://localhost:5555/upload'
        header =  { 'content_type': 'audio/wav' }   
        x  = requests.request('POST', url=myurl , data = f , headers=header  ) 
        print (x.text)
        print (x.status_code)
        if x.status_code == 200:
            self.music_id = x.content
            self.set_Logs(x.text)
            self.AssertOK()
            
        else:
            self.set_Logs(x.text)
            self.AssertKO()
        
    def Test6(self):
        """6-Check the upload of an long duration audio wav sample
        Initial Condition:
        Generate a long duration wav audio sample with button on left"""
        
        f= open('outputLongDur.wav'  ,"rb")
        myurl = 'http://localhost:5555/upload'
        header =  { 'content_type': 'audio/wav' }   
        x  = requests.request('POST', url=myurl , data = f , headers=header  ) 
        print (x.text)
        print (x.status_code)
        if x.status_code == 200:
            self.music_id = x.content
            self.set_Logs(x.text)
            self.AssertOK()
            
        else:
            self.set_Logs(x.text)
            self.AssertKO()
        
    def Test7(self):
        """7-Check the return of list of audio wav sample
       Initial Condition: Download a wav audio sample and copy it Storage folder of server"""
            
        myurl = 'http://localhost:5555/list'
        x = requests.request('GET', url=myurl)  
        
        if x.status_code == 200:
            self.set_Logs(x.text)
            self.AssertOK()
            
        else:
            self.set_Logs(x.text)
            self.AssertKO()
    
    
    def Test8(self):
        """8-Check return of statistics of audio sample file from server
        Initial Condition: A sample audio should be already uploaded on server and given ID are provided"""
        try:
            self.music_id
            myurl = 'http://localhost:5555/stats/'+str(self.music_id)
            x  = requests.request('GET', url=myurl)  
            if "Rate" in x.text and "Sample" in x.text:
                self.set_Logs(x.text)
                self.AssertOK()
        except:
            self.set_Logs("Music sample ID is not provided")
            self.AssertKO()
    
    def Test9(self):
        """9-Check delete of audio sample file from server
        Initial Condition: A sample audio should be already uploaded on server and given ID are provided"""
        try:
            self.music_id
            myurl = 'http://localhost:5555/'+str(self.music_id)
            x  = requests.request('DELETE', url=myurl)  
            if x.status_code == 200:
                myurl = 'http://localhost:5555/stats/'+str(self.music_id)
                x  = requests.request('GET', url=myurl) 
                if x.status_code == 400:
                    self.set_Logs("Music ID is deleted")
                    self.AssertOK()
            else:
                self.set_Logs(x.text)
                self.AssertKO()
        
        
        except:
            self.set_Logs("Music sample ID is not provided")
            self.AssertKO()