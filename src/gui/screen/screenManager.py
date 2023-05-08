# Built by Tejas Deolasee

from gui.screens.screen import Screen

#########################################################################################

class ScreenManager:

    def __init__(self, eventHandler, layoutAssets, tkInterManager, root):
        self.screensList = []
        self.eventHandler = eventHandler
        self.layoutAssets = layoutAssets
        self.root = root
        self.rootWidth = root.width
        self.rootHeight = root.height
        self.tkInterManager = tkInterManager

        self.loadScreens()
        self.updateScreenGrid()


#########################################################################################

    def loadScreens(self):
        numScreens = len(self.layoutAssets)
        for screenNumber in range(numScreens):
            screenInstance = Screen(screenNumber, self.layoutAssets[screenNumber], self.rootWidth, self.rootHeight, self.tkInterManager)
            screenInstance.loadScreen(self.eventHandler)
            self.screensList.append(screenInstance)

#########################################################################################
    
    def buildScreen(self, screenNumber):
        self.screensList[screenNumber].build()

#########################################################################################

    def structuralizeScreens(self):
        for screen in self.screensList:
            screen.structuralize()

#########################################################################################

    def updateScreenGrid(self):
        for screen in self.screensList:
            screen.updateGrid()

#########################################################################################