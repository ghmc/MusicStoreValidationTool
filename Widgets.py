from Tkinter import Frame, Label, StringVar, Button, Entry, Canvas
from Tkconstants import TOP,NW , DISABLED, FLAT





def Entry_Widget_Set(rootFrame, color, name, relief, side=TOP, padx=0, pady=15,width=20, callback=None):
    
    class Entry_Widget_Set_C(object):
        
        def __init__(self, rootFrame, color, name, relief, side=side, padx=padx, pady=pady,width=width):
            self.labelFrame = Frame(rootFrame, width=150, height = 0, bg=color,borderwidth=3,relief=relief)
            self.labelFrame.pack(padx=padx, pady=pady,side=side)
            
            
            self.label = Label(self.labelFrame, anchor=NW,  text=name, bg=color,font=("Helvetica", 7))
            self.label.pack(padx=0, pady=0)
            
            self.variable= StringVar() 
            if callback:
                self.variable.trace("w", lambda name, index, mode, sv=self.variable: callback(sv))
            self.entree = Entry(self.labelFrame, textvariable= self.variable, width=width)
            self.entree.pack(side=side, padx=5, pady=4)
            self.entree.config(state=DISABLED)
        
        def __del__(self):
            
            try:del self.entree, self.variable, self.labelFrame
            except:pass
            
    
    inst = Entry_Widget_Set_C(rootFrame, color, name, relief, side=TOP, padx=0, pady=pady,width=width)
    return inst




def Button_set(root, text, method, background, anchor,  width, height , highlightcolor, foreground, side, padx, pady):
    
    btn= Button(root, text=text, background =background, anchor=anchor,  width=width, height = height , highlightcolor=highlightcolor, foreground=foreground, command=method)
    btn.pack(side=side, padx=padx, pady=pady)
    
    return btn






def Set_Led(master, bg, side, big_size=True, borderwidth=0,padx=0,pady=10,relief=FLAT):
    
    class LED(Frame):
        
        def __init__(self, master, bg, side):
            
            Frame.__init__(self, master,width=0, height = 0, borderwidth=borderwidth, relief=relief)
            self.pack(side=side,padx=padx,pady=pady)  
            
            if big_size == True:
                label = Label(self, text="Result",bg="gray78",fg = "black",font=("Helvetica", 10))
                label.pack(side=TOP,padx=0, pady=0)
                
                self.canvas = Canvas(self, height=50, width=50, highlightthickness=0, bg=bg)
                self.canvas.pack(side=TOP,padx=0, pady=0)
            
                self.circle = self.canvas.create_oval(2,48,48,2, fill='grey',dashoffset=1)
            
            elif big_size == False:
                label = Label(self, text="Result",bg="gray78",fg = "black",font=("Helvetica", 10))
                label.pack(side=TOP,padx=0, pady=0)
                
                self.canvas = Canvas(self, height=20, width=20, highlightthickness=0, bg=bg)
                self.canvas.pack(side=TOP,padx=0, pady=0)
            
                self.circle = self.canvas.create_oval(1,18,18,1, fill='grey',dashoffset=1)
            
            else:
                label = Label(self, text="Result",bg="gray78",fg = "black",font=("Helvetica", 10))
                label.pack(side=TOP,padx=0, pady=0)
                
                self.canvas = Canvas(self, height=30, width=30, highlightthickness=0, bg=bg)
                self.canvas.pack(side=TOP,padx=0, pady=0)
            
                self.circle = self.canvas.create_oval(1.5,27,27,1.5, fill='grey',dashoffset=1) 


    led = LED(master, bg = bg, side=side) 
    return led