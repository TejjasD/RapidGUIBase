# Built by Tejas Deolasee

from gui.tkInter.Element import Element
import tkinter as tk
import math


#########################################################################################

class Button(Element):
    
    def implInstanceData(self):
        self.type = "button"
        self.id = self.instanceData[0]
        self.pos = (self.instanceData[1], self.instanceData[2])
        self.row = list(self.uiAssets.iloc[self.instanceData[9]])

        self.rowStart = int(self.instanceData[3]) - 1
        self.rowSpan = int(self.instanceData[4]) - self.rowStart
        self.columnStart = int(self.instanceData[5]) - 1
        self.columnSpan = int(self.instanceData[6]) - self.columnStart
        self.sticky = self.instanceData[7]

        self.width = self.row[8]
        self.height = self.row[9]
        
        if not isinstance(self.sticky, str):
            if math.isnan(self.sticky):
                self.sticky = ""
    
    def createElement(self):
        self.element = tk.Button(bd=self.row[1],
                                bg=self.row[2], 
                                fg=self.row[3], 
                                activebackground=self.row[4], 
                                activeforeground=self.row[5], 
                                font=(self.row[6], self.row[7]), 
                                highlightcolor=self.row[10], 
                                padx=self.row[11], 
                                pady=self.row[12], 
                                relief=self.row[13], 
                                text=self.instanceData[8], 
                                command=self.command)
        
        self.element.config(width=self.width)
        self.element.config(height=self.height)


#########################################################################################