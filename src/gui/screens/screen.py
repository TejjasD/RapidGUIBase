# Built by Tejas Deolasee

from gui.tkInter.elements.button import Button
from gui.tkInter.elements.label import Label
from gui.tkInter.elements.textBox import TextBox
from gui.gridMaker.gridMaker import GridMaker

#########################################################################################

class Screen():


    def __init__(self, screenId, layoutAsstes, uiAssets, rootWidth, rootHeight):
        self.screenId = screenId
        self.layoutAssets = layoutAsstes
        self.uiAssets = uiAssets
        self.rootWidth = rootWidth
        self.rootHeight = rootHeight

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

        self.gridMaker = GridMaker(self.rootWidth, self.rootHeight, self.numRows, self.numColumns)
    
#########################################################################################

    def loadConfigs(self):

        self.buttonInstanceData = self.layoutAssets['button']
        self.labelInstanceData = self.layoutAssets['label']
        self.textBoxInstanceData = self.layoutAssets['textBox']

        screenConfigValues = self.layoutAssets['screen']['Value']
        self.mode = screenConfigValues[0]
        self.numRows = screenConfigValues[1]
        self.numColumns = screenConfigValues[2]
        self.bgColor = screenConfigValues[3]

#########################################################################################

    def loadScreen(self, eventHandler):
    
        for b in range(self.buttonInstanceData.shape[0]):
            buttonId = self.buttonInstanceData.iloc[b][0]
            buttonInstance = Button(self.uiAssets['button'], list(self.buttonInstanceData.iloc[b]), getattr(eventHandler, buttonId))
            self.buttonsList.append(buttonInstance)
        
        for l in range(self.labelInstanceData.shape[0]):
            labelInstance = Label(self.uiAssets['label'], list(self.labelInstanceData.iloc[l]))
            self.labelsList.append(labelInstance)
        
        for t in range(self.textBoxInstanceData.shape[0]):
            textBoxId = self.textBoxInstanceData.iloc[t][0]
            textBoxInstance = TextBox(self.uiAssets['textBox'], list(self.textBoxInstanceData.iloc[t]))
            self.textBoxesList.append(textBoxInstance)
            self.textBoxDict[textBoxId] = textBoxInstance

#########################################################################################
  
    def build(self):
        for button in self.buttonsList:
            button.place(button.pos[0], button.pos[1], button.sticky)

        for label in self.labelsList:
            label.place(label.pos[0], label.pos[1], label.sticky)
        
        for textBox in self.textBoxesList:
            textBox.place(textBox.pos[0], textBox.pos[1], textBox.sticky)

#########################################################################################

    def destroy(self):
        for button in self.buttonsList:
            button.destroy()
        for label in self.labelsList:
            label.destroy()
        for textBox in self.textBoxesList:
            textBox.destroy()

#########################################################################################

    def updateGrid(self):
        if self.mode == "grid":
            for button in self.buttonsList:
                self.gridMaker.positionElement(button)
            for label in self.labelsList:
                self.gridMaker.positionElement(label)
            for textBox in self.textBoxesList:
                self.gridMaker.positionElement(textBox)

#########################################################################################