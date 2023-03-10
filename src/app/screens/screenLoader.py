# Built by Tejas Deolasee

from app.screens.screen import Screen

import os

#########################################################################################

class ScreenLoader:

    def __init__(self, eventHandler):
        self.screensList = []
        self.eventHandler = eventHandler

        self.loadScreens()

#########################################################################################

    def countNumberOfScreens(self):
        path = "T:\\Python\\FinanceManager\\config\\layout"
        return len(os.listdir(path))

#########################################################################################

    def loadScreens(self):
        numScreens = self.countNumberOfScreens()
        for screenNumber in range(numScreens):
            screenInstance = Screen(screenNumber)
            screenInstance.loadScreen(self.eventHandler)
            self.screensList.append(screenInstance)

#########################################################################################
    
    def buildScreen(self, screenNumber, rootWidth, rootHeight):
        self.screensList[screenNumber].build(rootWidth, rootHeight)

#########################################################################################
