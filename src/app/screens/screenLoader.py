# Built by Tejas Deolasee

from app.screens.screen import Screen

#########################################################################################

class ScreenLoader:

    def __init__(self, eventHandler, uiConfigs, layoutConfigs):
        self.screensList = []
        self.eventHandler = eventHandler
        self.uiConfigs = uiConfigs
        self.layoutConfigs = layoutConfigs

        self.loadScreens()


#########################################################################################

    def loadScreens(self):
        numScreens = len(self.layoutConfigs)
        for screenNumber in range(numScreens):
            screenInstance = Screen(screenNumber, self.layoutConfigs[screenNumber], self.uiConfigs)
            screenInstance.loadScreen(self.eventHandler)
            self.screensList.append(screenInstance)

#########################################################################################
    
    def buildScreen(self, screenNumber, rootWidth, rootHeight):
        self.screensList[screenNumber].build(rootWidth, rootHeight)

#########################################################################################
