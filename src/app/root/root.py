# Built by Tejas Deolasee

from core.configManager.configManager import configManager
from app.screens.screenLoader import ScreenLoader
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
        self.screenLoader = ScreenLoader(self.eventHandler, self.uiConfigs, self.layoutConfigs)
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
        self.root.configure(background = self.screenLoader.screensList[self.screenNumber].bgColor)
        self.screenLoader.buildScreen(self.screenNumber, self.width, self.height)

#########################################################################################

    def changeScreen(self, newScreenNumber):
        self.screenNumber = newScreenNumber
        self.build()

#########################################################################################

        
        

        

    


