# Built by Tejas Deolasee

from gui.tkInter.Element import Element
import tkinter as tk
import math

#########################################################################################


class Label(Element):
    
    def implInstanceData(self):
        self.type = "label"
        self.id = self.instanceData[0]
        self.pos = (self.instanceData[1], self.instanceData[2])
        self.row = list(self.uiConfigs.iloc[self.instanceData[9]])
        
        self.rowStart = int(self.instanceData[3])-1
        self.rowSpan = int(self.instanceData[4]) - self.rowStart
        self.columnStart = int(self.instanceData[5]) - 1
        self.columnSpan = int(self.instanceData[6])-self.columnStart
        self.sticky = self.instanceData[7]
        self.structure  = self.instanceData[10]

        if not isinstance(self.sticky, str):
            if math.isnan(self.sticky):
                self.sticky = ""
    

    def createElement(self):
        self.element = tk.Label(fg=self.row[1], 
                              bg = self.row[2],
                              font=(self.row[3], self.row[4]), 
                              text=self.instanceData[8])


#########################################################################################