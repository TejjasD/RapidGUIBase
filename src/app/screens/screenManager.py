# Built by Tejas Deolasee

from app.screens.screen import Screen

#########################################################################################

class ScreenManager:

    def __init__(self, eventHandler, uiConfigs, layoutConfigs, rootWidth, rootHeight):
        self.screensList = []
        self.eventHandler = eventHandler
        self.uiConfigs = uiConfigs
        self.layoutConfigs = layoutConfigs
        self.rootWidth = rootWidth
        self.rootHeight = rootHeight

        self.loadScreens()
        self.structuralizeScreens()


#########################################################################################

    def loadScreens(self):
        numScreens = len(self.layoutConfigs)
        for screenNumber in range(numScreens):
            screenInstance = Screen(screenNumber, self.layoutConfigs[screenNumber], self.uiConfigs, self.rootWidth, self.rootHeight)
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