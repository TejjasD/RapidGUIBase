import sys
sys.path.append('src/')
from app.screens.screenLoader import ScreenLoader
from eventHandler.eventHandler import eventHandler
from user.passwordManager.passwordManager import passwordManager 

import tkinter as tk

class Root():
    
    def __init__(self):
        self.root = tk.Tk()
        self.height = 500
        self.width = 1200
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
        self.root.configure(background = '#a8984d')
        self.root.geometry(str(self.width) + "x" + str(self.height))
    
    def build(self):
        self.screenLoader.buildScreen(self.screenNumber)

    def changeScreen(self, newScreenNumber):
        self.screenNumber = newScreenNumber
        self.build()

        
        

        

    


