# Built by Tejas Deolasee

from gui.gridMaker.gridMaker import GridMaker

#########################################################################################

class Screen():


    def __init__(self, screenId, layoutAsstes, tkInterManager, root):
        self.screenId = screenId
        self.layoutAssets = layoutAsstes
        self.tkInterManager = tkInterManager
        self.root = root
        self.base = self.root

        self.buttonsList = []
        self.labelsList = []
        self.textBoxesList = []
        self.textBoxDict = {}
        self.dynamicElements = []
        
        self.buttonInstanceData = None
        self.labelInstanceData = None
        self.textBoxInstanceData = None
        
        self.isScrollBar = "N"
        self.numRows = 0
        self.numColumns = 0
        self.bgColor = None

        self.loadConfigs()

        self.activeRow = self.numRows
        self.activeColumn = self.numColumns

        self.gridMaker = GridMaker(self, self.root.width, self.root.height, self.numRows, self.numColumns)
    
#########################################################################################

    def loadConfigs(self):

        self.buttonInstanceData = self.layoutAssets['button']
        self.labelInstanceData = self.layoutAssets['label']
        self.textBoxInstanceData = self.layoutAssets['textBox']

        screenConfigValues = self.layoutAssets['screen']['Value']
        self.numRows = screenConfigValues[0]
        self.numColumns = screenConfigValues[1]
        self.bgColor = screenConfigValues[2]
        self.isScrollBar = screenConfigValues[3]

#########################################################################################

    def loadScreen(self, eventHandler):
        
        if self.isScrollBar == "Y":
            self.loadScrollBar()
        
        for b in range(self.buttonInstanceData.shape[0]):
            buttonId = self.buttonInstanceData.iloc[b][0]
            buttonInstance = self.tkInterManager.createButton(self.base, list(self.buttonInstanceData.iloc[b]), getattr(eventHandler, buttonId))
            self.buttonsList.append(buttonInstance)
        
        for l in range(self.labelInstanceData.shape[0]):
            labelInstance = self.tkInterManager.createLabel(self.base, list(self.labelInstanceData.iloc[l]))
            self.labelsList.append(labelInstance)
        
        for t in range(self.textBoxInstanceData.shape[0]):
            textBoxId = self.textBoxInstanceData.iloc[t][0]
            textBoxInstance = self.tkInterManager.createTextBox(self.base, list(self.textBoxInstanceData.iloc[t]))
            self.textBoxesList.append(textBoxInstance)
            self.textBoxDict[textBoxId] = textBoxInstance

#########################################################################################

    def loadScrollBar(self):
        
        self.canvas = self.tkInterManager.createCanvas(self.root) 
        self.scrollBar = self.tkInterManager.createScrollBar(self.root, self.canvas)
        self.canvas.configScrollBar(self.scrollBar)

        self.frame = self.tkInterManager.createFrame(self.canvas)
        self.frame.changeColor(self.bgColor)
        self.canvas.createWindow(self.frame)

        self.base = self.frame

#########################################################################################

    def loadDynamicElements(self):

        for button in self.buttonsList:
            if (button.rowStart is not None):
                if (button.rowStart < 0 or button.columnStart < 0):
                    self.dynamicElements.append(button)

        for label in self.labelsList:
            if (label.rowStart is not None):
                if (label.rowStart < 0 or label.columnStart < 0):
                    self.dynamicElements.append(label)
        
        for textBox in self.textBoxesList:
            if (textBox.rowStart is not None):
                if (textBox.rowStart < 0 or textBox.columnStart < 0):
                    self.dynamicElements.append(textBox)

#########################################################################################      
  
    def build(self):
        self.root.setBgColor(self.bgColor)
        
        if self.isScrollBar == "Y":
            self.canvas.pack()
            self.scrollBar.pack()
        
        for button in self.buttonsList:
            button.place()

        for label in self.labelsList:
            label.place()
        
        for textBox in self.textBoxesList:
            textBox.place()

#########################################################################################

    def destroy(self):
        for button in self.buttonsList:
            button.destroy()
        for label in self.labelsList:
            label.destroy()
        for textBox in self.textBoxesList:
            textBox.destroy()

        if self.isScrollBar == "Y":
            self.canvas.destroy()
            self.scrollBar.destroy()

#########################################################################################

    def updateGrid(self):
        for button in self.buttonsList:
            self.gridMaker.positionElement(button)
        for label in self.labelsList:
            self.gridMaker.positionElement(label)
        for textBox in self.textBoxesList:
            self.gridMaker.positionElement(textBox)

#########################################################################################

    def addRow(self):
        self.activeRow += 1
        self.rePositionDynamicElements()

#########################################################################################

    def addColumn(self):
        self.activeColumn += 1
        self.rePositionDynamicElements()
    
#########################################################################################

    def rePositionDynamicElements(self):
        for element in self.dynamicElements:
            self.gridMaker.positionElement(element)
            element.place()

#########################################################################################

    def resizeAllElements(self, width, height):
        self.gridMaker.updateGrid(width, height)
        self.frame.configure(width, height)
        for button in self.buttonsList:
            self.gridMaker.positionElement(button)
            button.place()
        for label in self.labelsList:
            self.gridMaker.positionElement(label)
            label.place()
        for textBox in self.textBoxesList:
            self.gridMaker.positionElement(textBox)
            textBox.place()

#########################################################################################
