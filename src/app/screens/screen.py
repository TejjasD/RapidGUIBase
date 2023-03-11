# Built by Tejas Deolasee

from app.tkInter.tkInterElements import *

import random

#########################################################################################

class Screen():


    def __init__(self, screenId, layoutConfigs, uiConfigs):
        self.screenId = screenId
        self.layoutConfigs = layoutConfigs
        self.uiConfigs = uiConfigs
        self.buttonsList = []
        self.labelsList = []
        self.textBoxesList = []
        self.textBoxDict = {}
        self.dummyFrames = []
        
        self.buttonInstanceData = None
        self.labelInstanceData = None
        self.textBoxInstanceData = None
        
        self.mode = "space"
        self.numRows = 0
        self.numColumns = 0
        self.bgColor = None

        self.loadConfigs()
    
#########################################################################################

    def loadConfigs(self):

        self.buttonInstanceData = self.layoutConfigs['button']
        self.labelInstanceData = self.layoutConfigs['label']
        self.textBoxInstanceData = self.layoutConfigs['textBox']

        screenConfigValues = self.layoutConfigs['screen']['Value']
        self.mode = screenConfigValues[0]
        self.numRows = screenConfigValues[1]
        self.numColumns = screenConfigValues[2]
        self.bgColor = screenConfigValues[3]

#########################################################################################

    def loadScreen(self, eventHandler, rootWidth, rootHeight):

        if self.mode == "grid":
            self.loadDummy(rootWidth, rootHeight)
    
        for b in range(self.buttonInstanceData.shape[0]):
            buttonId = self.buttonInstanceData.iloc[b][0]
            buttonInstance = Button(self.uiConfigs['button'], list(self.buttonInstanceData.iloc[b]), getattr(eventHandler, buttonId))
            self.buttonsList.append(buttonInstance)
        
        for l in range(self.labelInstanceData.shape[0]):
            labelInstance = Label(self.uiConfigs['label'], list(self.labelInstanceData.iloc[l]))
            self.labelsList.append(labelInstance)
        
        for t in range(self.textBoxInstanceData.shape[0]):
            textBoxId = self.textBoxInstanceData.iloc[t][0]
            textBoxInstance = TextBox(self.uiConfigs['textBox'], list(self.textBoxInstanceData.iloc[t]))
            self.textBoxesList.append(textBoxInstance)
            self.textBoxDict[textBoxId] = textBoxInstance

#########################################################################################
  
    def build(self):
        if self.mode == 'grid':

            for frame in self.dummyFrames:
                frame.frame.grid(row=frame.row, column=frame.column)

            for button in self.buttonsList:
                button.button.grid()
                button.button.grid(row=button.rowStart, rowspan=button.rowSpan, column=button.columnStart, columnspan=button.columnSpan, sticky=button.sticky)
                button.button.lift()

            for label in self.labelsList:
                label.label.grid(row=label.rowStart, rowspan=label.rowSpan, column=label.columnStart, columnspan=label.columnSpan, sticky=label.sticky)
                label.label.lift()

            for textBox in self.textBoxesList:
                textBox.textBox.grid(row=textBox.rowStart, rowspan=textBox.rowSpan, column=textBox.columnStart, columnspan=textBox.columnSpan, sticky=textBox.sticky)
                textBox.textBox.lift()

        else:
            for button in self.buttonsList:
                button.button.place(x=button.pos[0], y=button.pos[1], width=button.width, height=button.height)

            for label in self.labelsList:
                label.label.place(x=label.pos[0], y=label.pos[1])
            
            for textBox in self.textBoxesList:
                textBox.textBox.place(x=textBox.pos[0], y=textBox.pos[1], width=textBox.width, height=textBox.height)

#########################################################################################

    def loadDummy(self, rootWidth, rootHeight):
        labelWidth = int(rootWidth/self.numColumns)
        labelHeight = int(rootHeight/self.numRows)
        for c in range(self.numColumns):
            for r in range(self.numRows):
                # color  = random.randint(100000, 999999)
                # frame = tk.Frame(background = "#" + str(color), width=labelWidth, height=labelHeight)
                frame = DummyFrame(self.bgColor, labelWidth, labelHeight, r, c)
                self.dummyFrames.append(frame)

#########################################################################################

    def destroy(self):
        for button in self.buttonsList:
            button.button.destroy()
        for label in self.labelsList:
            label.label.destroy()
        for textBox in self.textBoxesList:
            textBox.textBox.destroy()
        for frame in self.dummyFrames:
            frame.frame.destroy()

#########################################################################################
    
    
    
    
