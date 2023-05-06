# Built by Tejas Deolasee

from gui.tkInter.elements.button import Button
from gui.tkInter.elements.label import Label
from gui.tkInter.elements.textBox import TextBox
from gui.tkInter.elements.dummyFrame import DummyFrame
from gui.structuralizer.structureManager import StructureManager

#########################################################################################

class Screen():


    def __init__(self, screenId, layoutAsstes, uiAssets, rootWidth, rootHeight):
        self.screenId = screenId
        self.layoutAssets = layoutAsstes
        self.uiAssets = uiAssets
        self.rootWidth = rootWidth
        self.rootHeight = rootHeight

        self.structureManager = StructureManager(self.layoutAssets['structure'], self.rootWidth, self.rootHeight)
        self.structureDictionary = self.structureManager.structureDictionary

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

        if self.mode == "grid":
            self.loadDummy()
    
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
        if self.mode == 'grid':

            for frame in self.dummyFrames:
                frame.element.grid(row=frame.row, column=frame.column)

            for button in self.buttonsList:
                button.element.grid()
                button.element.grid(row=button.rowStart, rowspan=button.rowSpan, column=button.columnStart, columnspan=button.columnSpan, sticky=button.sticky)
                button.element.lift()

            for label in self.labelsList:
                label.element.grid(row=label.rowStart, rowspan=label.rowSpan, column=label.columnStart, columnspan=label.columnSpan, sticky=label.sticky)
                label.element.lift()

            for textBox in self.textBoxesList:
                textBox.element.grid(row=textBox.rowStart, rowspan=textBox.rowSpan, column=textBox.columnStart, columnspan=textBox.columnSpan, sticky=textBox.sticky)
                textBox.element.lift()

        else:
            for button in self.buttonsList:
                button.element.place(x=button.pos[0], y=button.pos[1], anchor = button.sticky)

            for label in self.labelsList:
                label.element.place(x=label.pos[0], y=label.pos[1], anchor = label.sticky)
            
            for textBox in self.textBoxesList:
                textBox.element.place(x=textBox.pos[0], y=textBox.pos[1], anchor = textBox.sticky)

#########################################################################################

    def loadDummy(self):
        labelWidth = int(self.rootWidth/self.numColumns)
        labelHeight = int(self.rootHeight/self.numRows)
        for c in range(self.numColumns):
            for r in range(self.numRows):
                # color  = random.randint(100000, 999999)
                # frame = DummyFrame("#"+str(color), labelWidth, labelHeight, r, c)
                frame = DummyFrame(self.bgColor, labelWidth, labelHeight, r, c)
                self.dummyFrames.append(frame)

#########################################################################################

    def destroy(self):
        for button in self.buttonsList:
            button.element.destroy()
        for label in self.labelsList:
            label.element.destroy()
        for textBox in self.textBoxesList:
            textBox.element.destroy()
        for frame in self.dummyFrames:
            frame.element.destroy()

#########################################################################################

    def structuralize(self):
        self.mapStructures()
        self.structureManager.structuralize()
    
#########################################################################################

    def mapStructures(self):
        for button in self.buttonsList:
            self.structureManager.addElement(button)
        for label in self.labelsList:
            self.structureManager.addElement(label)
        for textBox in self.textBoxesList:
            self.structureManager.addElement(textBox)

#########################################################################################