# Built by Tejas Deolasee

import sys
sys.dont_write_bytecode = True
sys.path.append('src/')
from gui.tkInter.manager.tkIntermanager import TkInterManager
from core.assetLoader.assetLoader import AssetLoader
from gui.gridMaker.gridMakerFree import GridMakerFree

class CanvasTest:

    def __init__(self):
        pass

#########################################################################################

    def adjustElements(self, event):
        if event.widget == self.root.element:
            width = event.width
            height = event.height
            print(width, height)
            self.gridMaker.updateGrid(width, height)
            self.gridMaker.positionElement(self.tempButton)
            self.tempButton.place()

#########################################################################################

    def tempButton(self):
        print("Pressed")

#########################################################################################

    def impl(self):
        assetLoader = AssetLoader("pfm")
        self.tkInterManager = TkInterManager(assetLoader.assetsDictionary['tkInterUI'])
        self.root = self.tkInterManager.createRoot(assetLoader.assetsDictionary['root']['window']["Value"])
        self.root.element.bind("<Configure>", self.adjustElements)

        self.gridMaker = GridMakerFree(self.root.width, self.root.height, 1, 1)
        self.buttonInstancedata = ["TempButton", self.root.width/2, self.root.height/2, 0 , 0, 0, 0, "center", "Press", 3]
        self.tempButton = self.tkInterManager.createButton(self.root, self.buttonInstancedata, getattr(self, "tempButton"))
        self.gridMaker.positionElement(self.tempButton)
        self.tempButton.place()
        self.root.run()

######################################################################################### 

testObject = CanvasTest()
testObject.impl()

#########################################################################################

