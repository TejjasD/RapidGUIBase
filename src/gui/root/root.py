# Built by Tejas Deolasee

from core.assetLoader.assetLoader import AssetLoader
from gui.screens.screenManager import ScreenManager
from eventHandler.eventHandler import eventHandler
from user.passwordManager.passwordManager import passwordManager 

import tkinter as tk

#########################################################################################

class Root():
    
    def __init__(self):
        self.assetLoader = AssetLoader()
        self.widowAssets = self.assetLoader.assetsDictionary['root']['window']
        self.layoutAssets = self.assetLoader.assetsDictionary['layout']
        self.uiAssets = self.assetLoader.assetsDictionary['tkInterUI']

        self.width = self.widowAssets['Value'][0]
        self.height = self.widowAssets['Value'][1]
        
        self.root = tk.Tk()
        self.eventHandler = eventHandler(self)
        self.screenManager = ScreenManager(self.eventHandler, self.uiAssets, self.layoutAssets,  self.width, self.height)
        self.screenNumber = 0
        self.activeScreen = self.screenManager.screensList[self.screenNumber]
        self.passwordManager = passwordManager()

        self.setConfigs()
        self.build()
          
#########################################################################################

    def run(self):
        self.root.mainloop()

#########################################################################################
    
    def setConfigs(self):
        self.root.geometry(str(self.width) + "x" + str(self.height))

#########################################################################################
    
    def build(self):
        self.root.configure(background = self.screenManager.screensList[self.screenNumber].bgColor)
        self.screenManager.buildScreen(self.screenNumber)

#########################################################################################

    def changeScreen(self, newScreenNumber):
        self.screenNumber = newScreenNumber
        self.activeScreen = self.screenManager.screensList[self.screenNumber]
        self.build()

#########################################################################################

        
        

        

    


