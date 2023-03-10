# Built by Tejas Deolasee

from tkInter.tkInterElements import *
import pandas as pd
import random

#########################################################################################

class Screen():

    buttonUIConfigs = pd.read_csv('config\\ui\\tkInterElements\\buttonUI.csv')
    labelUIConfigs = pd.read_csv('config\\ui\\tkInterElements\\labelUI.csv')
    textBoxUIConfigs = pd.read_csv('config\\ui\\tkInterElements\\textBoxUI.csv')
    baseLayoutPath = 'config\layout'

    def __init__(self, screenId):
        self.screenId = screenId
        self.buttonsList = []
        self.labelsList = []
        self.textBoxesList = []
        self.textBoxDict = {}
        
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
        fileName = Screen.baseLayoutPath + '\screen' + str(self.screenId)+ 'Elements.xlsx'

        self.buttonInstanceData = pd.read_excel(fileName, sheet_name = "Buttons")
        self.labelInstanceData = pd.read_excel(fileName, sheet_name="Labels")
        self.textBoxInstanceData = pd.read_excel(fileName, sheet_name="TextBoxes")
        screenConfigData = pd.read_excel(fileName, sheet_name='Screen')

        screenCofigValues = screenConfigData['Value']
        self.mode = screenCofigValues[0]
        self.numRows = screenCofigValues[1]
        self.numColumns = screenCofigValues[2]
        self.bgColor = screenCofigValues[3]

#########################################################################################

    def loadScreen(self, eventHandler):
    
        for b in range(self.buttonInstanceData.shape[0]):
            buttonId = self.buttonInstanceData.iloc[b][0]
            buttonInstance = Button(Screen.buttonUIConfigs, list(self.buttonInstanceData.iloc[b]), getattr(eventHandler, buttonId))
            self.buttonsList.append(buttonInstance)
        
        for l in range(self.labelInstanceData.shape[0]):
            labelInstance = Label(Screen.labelUIConfigs, list(self.labelInstanceData.iloc[l]))
            self.labelsList.append(labelInstance)
        
        for t in range(self.textBoxInstanceData.shape[0]):
            textBoxId = self.textBoxInstanceData.iloc[t][0]
            textBoxInstance = TextBox(Screen.textBoxUIConfigs, list(self.textBoxInstanceData.iloc[t]))
            self.textBoxesList.append(textBoxInstance)
            self.textBoxDict[textBoxId] = textBoxInstance

#########################################################################################
  
    def build(self, rootWidth, rootHeight):
        if self.mode == 'grid':
            self.buildDummy(rootWidth, rootHeight)

            for button in self.buttonsList:
                button.button.grid(row=button.rowStart, rowspan=button.rowSpan, column=button.columnStart, columnspan=button.columnSpan)
                button.button.lift()

            for label in self.labelsList:
                label.label.grid(row=label.rowStart, rowspan=label.rowSpan, column=label.columnStart, columnspan=label.columnSpan)
                label.label.lift()

            for textBox in self.textBoxesList:
                textBox.textBox.grid(row=textBox.rowStart, rowspan=textBox.rowSpan, column=textBox.columnStart, columnspan=textBox.columnSpan)
                textBox.textBox.lift()

        else:
            for button in self.buttonsList:
                button.button.place(x=button.pos[0], y=button.pos[1], width=button.width, height=button.height)

            for label in self.labelsList:
                label.label.place(x=label.pos[0], y=label.pos[1])
            
            for textBox in self.textBoxesList:
                textBox.textBox.place(x=textBox.pos[0], y=textBox.pos[1], width=textBox.width, height=textBox.height)

#########################################################################################

    def buildDummy(self, rootWidth, rootHeight):
        labelWidth = int(rootWidth/self.numColumns)
        labelHeight = int(rootHeight/self.numRows)
        for c in range(self.numColumns):
            for r in range(self.numRows):
                color = random.randrange(111111, 999999)
                label = tk.Frame(background=self.bgColor, width=labelWidth, height=labelHeight)
                label.grid(row=r, column=c)

#########################################################################################

    def destroy(self):
        for button in self.buttonsList:
            button.button.destroy()
        for label in self.labelsList:
            label.label.destroy()
        for textBox in self.textBoxesList:
            textBox.textBox.destroy()

#########################################################################################
    
    
    
    
