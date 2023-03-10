from app.screens.screenLoader import ScreenLoader
from eventHandler.eventHandler import eventHandler
from user.passwordManager.passwordManager import passwordManager 

import tkinter as tk
import pandas as pd

class Root():
    
    def __init__(self):
        self.widowConfigs = pd.read_csv('config\\ui\\root\\window\\window.csv')
        self.width = self.widowConfigs['Value'][0]
        self.height = self.widowConfigs['Value'][1]

        self.root = tk.Tk()
        self.numScreens = 1
        self.eventHandler = eventHandler(self)
        self.screenLoader = ScreenLoader(self.eventHandler)
        self.screenNumber = 0
        self.passwordManager = passwordManager()

        self.setConfigs()
        self.build()
        
    def run(self):
        self.root.mainloop()
    
    def setConfigs(self):
        self.root.geometry(str(self.width) + "x" + str(self.height))
    
    def build(self):
        self.root.configure(background = self.screenLoader.screensList[self.screenNumber].bgColor)
        self.screenLoader.buildScreen(self.screenNumber, self.width, self.height)

    def changeScreen(self, newScreenNumber):
        self.screenNumber = newScreenNumber
        self.build()

        
        

        

    


