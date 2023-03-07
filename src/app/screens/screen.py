import sys
sys.path.append('src/')
from tkInter.tkInterElements import *

import pandas as pd

class Screen():

    buttonUIConfigs = pd.read_csv('T:\\Python\\FinanceManager\\config\\ui\\tkInterElements\\buttonUI.csv')
    labelUIConfigs = pd.read_csv('T:\\Python\\FinanceManager\\config\\ui\\tkInterElements\\labelUI.csv')
    textBoxUIConfigs = pd.read_csv('T:\\Python\\FinanceManager\\config\\ui\\tkInterElements\\textBoxUI.csv')
    baseLayoutPath = 'T:\\Python\\FinanceManager\\config\layout'

    def __init__(self, screenId):
        self.screenId = screenId
        self.buttonsList = []
        self.labelsList = []
        self.textBoxesList = []
        self.textBoxDict = {}
        

    def loadScreen(self, eventHandler):
        fileName = Screen.baseLayoutPath + '\screen' + str(self.screenId)+ 'Elements.xlsx'

        buttonInstanceData = pd.read_excel(fileName, sheet_name = "Buttons")
        labelInstanceData = pd.read_excel(fileName, sheet_name="Labels")
        textBoxInstanceData = pd.read_excel(fileName, sheet_name="TextBoxes")

        for b in range(buttonInstanceData.shape[0]):
            buttonId = buttonInstanceData.iloc[b][0]
            buttonInstance = Button(Screen.buttonUIConfigs, list(buttonInstanceData.iloc[b]), getattr(eventHandler, buttonId))
            self.buttonsList.append(buttonInstance)
        
        for l in range(labelInstanceData.shape[0]):
            labelInstance = Label(Screen.labelUIConfigs, list(labelInstanceData.iloc[l]))
            self.labelsList.append(labelInstance)
        
        for t in range(textBoxInstanceData.shape[0]):
            textBoxId = textBoxInstanceData.iloc[t][0]
            textBoxInstance = TextBox(Screen.textBoxUIConfigs, list(textBoxInstanceData.iloc[t]))
            self.textBoxesList.append(textBoxInstance)
            self.textBoxDict[textBoxId] = textBoxInstance

    
    def build(self):
        for button in self.buttonsList:
            button.button.place(x=button.pos[0], y=button.pos[1], width=button.width, height=button.height)

        for label in self.labelsList:
            label.label.place(x=label.pos[0], y=label.pos[1])
        
        for textBox in self.textBoxesList:
            textBox.textBox.place(x=textBox.pos[0], y=textBox.pos[1], width=textBox.width, height=textBox.height)


    def destroy(self):
        for button in self.buttonsList:
            button.button.destroy()
        for label in self.labelsList:
            label.label.destroy()
        for textBox in self.textBoxesList:
            textBox.textBox.destroy()
    
    
    
    
