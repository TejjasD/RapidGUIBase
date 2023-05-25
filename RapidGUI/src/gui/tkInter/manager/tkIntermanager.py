# Built by Tejas Deolasee

from gui.tkInter.elements.button import Button
from gui.tkInter.elements.label import Label
from gui.tkInter.elements.textBox import TextBox
from gui.tkInter.elements.root import Root
from gui.tkInter.elements.canvas import Canvas
from gui.tkInter.elements.scrollBar import ScrollBar
from gui.tkInter.elements.frame import Frame

#########################################################################################

class TkInterManager():

    def __init__(self, uiAssets):
        self.uiAssets = uiAssets

#########################################################################################

    def createButton(self, base, instanceData, command):
        uiAsset = list(self.uiAssets["button"].iloc[instanceData[9]])
        return Button(instanceData, base, uiAsset, command)
    
#########################################################################################

    def createLabel(self, base, instanceData):
        uiAsset = list(self.uiAssets["label"].iloc[instanceData[9]])
        return Label(instanceData, base, uiAsset)

#########################################################################################

    def createTextBox(self, base, instanceData):
        uiAsset = list(self.uiAssets["textBox"].iloc[instanceData[8]])
        return TextBox(instanceData, base, uiAsset)

#########################################################################################

    def createRoot(self, instanceData):
        return Root(instanceData)

#########################################################################################

    def createCanvas(self, base):
        return Canvas(None, base)
    
#########################################################################################

    def createScrollBar(self, base, command):
        return ScrollBar(None, base, None, command)

#########################################################################################

    def createFrame(self, base):
        return Frame(None, base)

#########################################################################################