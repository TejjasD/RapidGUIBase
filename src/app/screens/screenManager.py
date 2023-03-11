# Built by Tejas Deolasee

from app.screens.screen import Screen

#########################################################################################

class ScreenManager:

    def __init__(self, eventHandler, uiConfigs, layoutConfigs, rootWidth, rootHeight):
        self.screensList = []
        self.eventHandler = eventHandler
        self.uiConfigs = uiConfigs
        self.layoutConfigs = layoutConfigs

        self.loadScreens(rootWidth, rootHeight)


#########################################################################################

    def loadScreens(self, rootWidth, rootHeight):
        numScreens = len(self.layoutConfigs)
        for screenNumber in range(numScreens):
            screenInstance = Screen(screenNumber, self.layoutConfigs[screenNumber], self.uiConfigs)
            screenInstance.loadScreen(self.eventHandler, rootWidth, rootHeight)
            self.screensList.append(screenInstance)

#########################################################################################
    
    def buildScreen(self, screenNumber):
        self.screensList[screenNumber].build()

#########################################################################################
