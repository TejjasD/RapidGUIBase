# Built by Tejas Deolasee

from core.configManager.configManager import configManager
from app.screens.screenManager import ScreenManager
from eventHandler.eventHandler import eventHandler
from user.passwordManager.passwordManager import passwordManager 

import tkinter as tk

#########################################################################################

class Root():
    
    def __init__(self):
        self.configManager = configManager()
        self.widowConfigs = self.configManager.configDictionary['root']['window']
        self.layoutConfigs = self.configManager.configDictionary['layout']
        self.uiConfigs = self.configManager.configDictionary['tkInterUI']

        self.width = self.widowConfigs['Value'][0]
        self.height = self.widowConfigs['Value'][1]
        
        self.root = tk.Tk()
        self.numScreens = 1
        self.eventHandler = eventHandler(self)
        self.screenManager = ScreenManager(self.eventHandler, self.uiConfigs, self.layoutConfigs,  self.width, self.height)
        self.screenNumber = 0
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
        self.build()

#########################################################################################

        
        

        

    


