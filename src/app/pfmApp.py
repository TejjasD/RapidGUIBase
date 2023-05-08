# Built by Tejas Deolasee

from core.assetLoader.assetLoader import AssetLoader
from gui.screen.screenManager import ScreenManager
from gui.tkInter.manager.tkIntermanager import TkInterManager
from eventHandler.eventHandler import eventHandler
from user.passwordManager.passwordManager import passwordManager 

import tkinter as tk

#########################################################################################

class PfmApp():
    
    def __init__(self):
        self.assetLoader = AssetLoader()
        self.tkInterManager = TkInterManager(self.assetLoader.assetsDictionary['tkInterUI'])
        self.root = self.tkInterManager.createRoot(self.assetLoader.assetsDictionary['root']['window']["Value"])

        self.eventHandler = eventHandler(self)
        self.screenManager = ScreenManager(self.eventHandler, self.assetLoader.assetsDictionary['layout'] , self.tkInterManager, self.root)
        self.screenNumber = 0
        self.activeScreen = self.screenManager.screensList[self.screenNumber]
        self.passwordManager = passwordManager()

        self.build()
          
#########################################################################################

    def run(self):
        self.root.run()

#########################################################################################
    
    def build(self):
        self.screenManager.buildScreen(self.screenNumber)

#########################################################################################

    def changeScreen(self, newScreenNumber):
        self.screenNumber = newScreenNumber
        self.activeScreen = self.screenManager.screensList[self.screenNumber]
        self.build()

#########################################################################################
