# Built by Tejas Deolasee

import tkinter as tk
import math


#########################################################################################

class Element:

    def __init__(self, uiAssets, instancedata, command = None):
        self.type = None
        self.uiAssets = uiAssets
        self.instanceData = instancedata
        self.command = command
        self.id = 0
        self.pos = (0, 0)
        self.row = []
        self.element = None
        self.width = None
        self.height = None

        self.rowStart = 0
        self.rowSpan = 0
        self.columnStart = 0
        self.columnSpan = 0
        self.sticky = "center"

        self.implInstanceData()
        self.createElement()

#########################################################################################
    
    def implInstanceData(self):
        pass

#########################################################################################
    
    def createElement(self):
        pass

#########################################################################################

    def destroy(self):
        self.element.destroy()

#########################################################################################

    def place(self, x, y, sticky):
        self.element.place(x = x, y = y, anchor = sticky)

#########################################################################################

    def get(self):
        return self.element.get()
    
#########################################################################################

       


        

    

