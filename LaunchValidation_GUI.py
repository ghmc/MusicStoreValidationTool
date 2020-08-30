#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 2
'''
Created on 18 juil. 2018

@author: bbenmakh
'''


from BG import BG_C
from Tkinter import Tk










  
  



root = Tk()
    
root.wm_title("MusicStore validation version 0.1.0") #Makes the title that will appear in the top left
# root.overrideredirect(False)
root.geometry("1200x750")

#root.geometry("1700x900")

root.config(background = "#FFFFFF") #sets background color to white
#list of tests


BG_C(master=root) # background feature to be launched at startup




root.mainloop()
     
    