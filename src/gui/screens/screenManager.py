# Built by Tejas Deolasee

from gui.screens.screen import Screen

#########################################################################################

class ScreenManager:

    def __init__(self, eventHandler, uiAssets, layoutAssets, rootWidth, rootHeight):
        self.screensList = []
        self.eventHandler = eventHandler
        self.uiAssets = uiAssets
        self.layoutAssets = layoutAssets
        self.rootWidth = rootWidth
        self.rootHeight = rootHeight

        self.loadScreens()
        self.structuralizeScreens()


#########################################################################################

    def loadScreens(self):
        numScreens = len(self.layoutAssets)
        for screenNumber in range(numScreens):
            screenInstance = Screen(screenNumber, self.layoutAssets[screenNumber], self.uiAssets, self.rootWidth, self.rootHeight)
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