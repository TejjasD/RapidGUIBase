# Built by Tejas Deolasee

from gui.tkInter.elements.button import Button
from gui.tkInter.elements.label import Label
from gui.tkInter.elements.textBox import TextBox
from gui.tkInter.elements.root import Root

#########################################################################################

class TkInterManager():

    def __init__(self, uiAssets):
        self.uiAssets = uiAssets

#########################################################################################

    def createButton(self, instanceData, command):
        uiAsset = list(self.uiAssets["button"].iloc[instanceData[9]])
        return Button(instanceData, uiAsset, command)
    
#########################################################################################

    def createLabel(self, instanceData):
        uiAsset = list(self.uiAssets["label"].iloc[instanceData[9]])
        return Label(instanceData, uiAsset)

#########################################################################################

    def createTextBox(self, instanceData):
        uiAsset = list(self.uiAssets["textBox"].iloc[instanceData[8]])
        return TextBox(instanceData, uiAsset)

#########################################################################################

    def createRoot(self, instanceData):
        return Root(instanceData)

#########################################################################################