# Built by Tejas Deolasee

from gui.tkInter.elements.element import Element
import tkinter as tk
import math

#########################################################################################

class TextBox(Element):

    def implInstanceData(self):
        self.type = "textBox"
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
                self.sticky = ""
    
    
    def createElement(self):
        self.element = tk.Entry(bd = self.uiAssets[1],
                                bg = self.uiAssets[2], 
                                fg = self.uiAssets[3],  
                                font = (self.uiAssets[4], self.uiAssets[5]), 
                                highlightcolor = self.uiAssets[6],  
                                relief = self.uiAssets[7],
                                width = self.uiAssets[8])

#########################################################################################

    def get(self):
        return self.element.get()

#########################################################################################