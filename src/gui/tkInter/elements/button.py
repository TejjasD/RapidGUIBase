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

        if not math.isnan(self.instanceData[3]):
            self.rowStart = int(self.instanceData[3]) 
            self.rowSpan = int(self.instanceData[4]) - self.rowStart + 1
            self.columnStart = int(self.instanceData[5]) 
            self.columnSpan = int(self.instanceData[6]) - self.columnStart + 1
        else:
            self.rowStart = None
            self.rowSpan = None
            self.columnStart = None
            self.columnSpan = None
    
        self.sticky = self.instanceData[7]

        
        if not isinstance(self.sticky, str):
            if math.isnan(self.sticky):
                self.sticky = "center"
    
    def createElement(self):
        self.element = tk.Button(self.base.element,
                                bd = self.uiAssets[1],
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