# Built by Tejas Deolasee

import tkinter as tk
import math


#########################################################################################

class Button:

    def __init__(self, buttonUIConfigs, buttonInstancedata, command):
        self.buttonUIConfigs = buttonUIConfigs
        self.buttonInstanceData = buttonInstancedata
        self.command = command
        self.id = 0
        self.pos = (0, 0)
        self.row = []
        self.button = None

        self.rowStart = 0
        self.rowSpan = 0
        self.columnStart = 0
        self.columnSpan = 0
        self.structure = 0

        self.implButtonInstanceData()
        self.createButton()
    
    def implButtonInstanceData(self):
        self.id = self.buttonInstanceData[0]
        self.pos = (self.buttonInstanceData[1], self.buttonInstanceData[2])
        self.row = list(self.buttonUIConfigs.iloc[self.buttonInstanceData[9]])

        self.rowStart = int(self.buttonInstanceData[3])-1
        self.rowSpan = int(self.buttonInstanceData[4])-self.rowStart
        self.columnStart = int(self.buttonInstanceData[5])-1
        self.columnSpan = int(self.buttonInstanceData[6])-self.columnStart
        self.sticky = self.buttonInstanceData[7]
        self.structure  = self.buttonInstanceData[10]
        
        if not isinstance(self.sticky, str):
            if math.isnan(self.sticky):
                self.sticky = ""
    
    def createButton(self):
        self.button = tk.Button(bd=self.row[1],
                                bg=self.row[2], 
                                fg=self.row[3], 
                                activebackground=self.row[4], 
                                activeforeground=self.row[5], 
                                font=(self.row[6], self.row[7]), 
                                highlightcolor=self.row[10], 
                                padx=self.row[11], 
                                pady=self.row[12], 
                                relief=self.row[13], 
                                text=self.buttonInstanceData[8], 
                                command=self.command)
        
        self.button.config(width=self.row[8])
        self.button.config(height=self.row[9])


#########################################################################################


class Label:

    def __init__(self, labelUIConfigs, labelInstancedata):
        self.labelUIConfigs = labelUIConfigs
        self.labelInstanceData = labelInstancedata
        self.id = 0
        self.pos = (0, 0)
        self.row = []
        self.label = None

        self.rowStart = 0
        self.rowSpan = 0
        self.columnStart = 0
        self.columnSpan = 0
        self.structure = 0

        self.implLabelInstanceData()
        self.createLabel()
    
    def implLabelInstanceData(self):
        self.id = self.labelInstanceData[0]
        self.pos = (self.labelInstanceData[1], self.labelInstanceData[2])
        self.row = list(self.labelUIConfigs.iloc[self.labelInstanceData[9]])
        
        self.rowStart = int(self.labelInstanceData[3])-1
        self.rowSpan = int(self.labelInstanceData[4])-self.rowStart
        self.columnStart = int(self.labelInstanceData[5])-1
        self.columnSpan = int(self.labelInstanceData[6])-self.columnStart
        self.sticky = self.labelInstanceData[7]
        self.structure  = self.labelInstanceData[10]

        if not isinstance(self.sticky, str):
            if math.isnan(self.sticky):
                self.sticky = ""
    

    def createLabel(self):
        self.label = tk.Label(fg=self.row[1], 
                              bg = self.row[2],
                              font=(self.row[3], self.row[4]), 
                              text=self.labelInstanceData[8])


#########################################################################################


class TextBox:
    
    def __init__(self, textBoxUIConfigs, textBoxInstancedata):
        self.textBoxUIConfigs = textBoxUIConfigs
        self.textBoxInstanceData = textBoxInstancedata
        self.id = 0
        self.pos = (0, 0)
        self.row = []
        self.textBox = None

        self.rowStart = 0
        self.rowSpan = 0
        self.columnStart = 0
        self.columnSpan = 0
        self.structure  = None

        self.impltextBoxInstanceData()
        self.createtextBox()
    
    def impltextBoxInstanceData(self):
        self.id = self.textBoxInstanceData[0]
        self.pos = (self.textBoxInstanceData[1], self.textBoxInstanceData[2])
        self.row = list(self.textBoxUIConfigs.iloc[int(self.textBoxInstanceData[8])])

        self.rowStart = int(self.textBoxInstanceData[3])-1
        self.rowSpan = int(self.textBoxInstanceData[4])-self.rowStart
        self.columnStart = int(self.textBoxInstanceData[5])-1
        self.columnSpan = int(self.textBoxInstanceData[6])-self.columnStart
        self.sticky = self.textBoxInstanceData[7]
        self.structure  = self.textBoxInstanceData[9]

        if not isinstance(self.sticky, str):
            if math.isnan(self.sticky):
                self.sticky = ""
    
    
    def createtextBox(self):
        self.textBox = tk.Entry(bd=self.row[1],
                                bg=self.row[2], 
                                fg=self.row[3],  
                                font=(self.row[4], self.row[5]), 
                                highlightcolor=self.row[6],  
                                relief=self.row[7],
                                width=self.row[8])
        # self.textBox.config(height)

#########################################################################################

class DummyFrame:
    def __init__(self, bgColor, width, height, row, column):
        self.frame = tk.Frame(background=bgColor, width=width, height=height)
        self.row = row
        self.column = column

#########################################################################################

    

       


        

    

