# Built by Tejas Deolasee

from gui.tkInter.elements.element import Element
import tkinter as tk
import math


#########################################################################################

class Button(Element):
    
    def implInstanceData(self):
        self.type = "button"
        self.id = self.instanceData[0]
        self.pos = (self.instanceData[1], self.instanceData[2])
        self.rowStart = int(self.instanceData[3]) - 1
        self.rowSpan = int(self.instanceData[4]) - self.rowStart
        self.columnStart = int(self.instanceData[5]) - 1
        self.columnSpan = int(self.instanceData[6]) - self.columnStart
        self.sticky = self.instanceData[7]

        
        if not isinstance(self.sticky, str):
            if math.isnan(self.sticky):
                self.sticky = ""
    
    def createElement(self):
        self.element = tk.Button(bd = self.uiAssets[1],
                                bg = self.uiAssets[2], 
                                fg = self.uiAssets[3], 
                                activebackground = self.uiAssets[4], 
                                activeforeground = self.uiAssets[5], 
                                font = (self.uiAssets[6], self.uiAssets[7]), 
                                highlightcolor = self.uiAssets[10], 
                                padx = self.uiAssets[11], 
                                pady = self.uiAssets[12], 
                                relief = self.uiAssets[13], 
                                text = self.instanceData[8], 
                                command = self.command)
        
        self.element.config(width = self.uiAssets[8])
        self.element.config(height = self.uiAssets[9])


#########################################################################################