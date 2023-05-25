# Built by Tejas Deolasee

from gui.screen.screen import Screen

#########################################################################################

class ScreenManager:

    def __init__(self, eventHandler, layoutAssets, tkInterManager, root):
        self.screensList = []
        self.eventHandler = eventHandler
        self.layoutAssets = layoutAssets
        self.root = root
        self.tkInterManager = tkInterManager

        self.loadScreens()
        self.updateScreenGrid()


#########################################################################################

    def loadScreens(self):
        numScreens = len(self.layoutAssets)
        for screenNumber in range(numScreens):
            screenInstance = Screen(screenNumber, self.layoutAssets[screenNumber], self.tkInterManager, self.root)
            screenInstance.loadScreen(self.eventHandler)
            screenInstance.loadDynamicElements()
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