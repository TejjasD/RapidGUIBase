# Built by Tejas Deolasee

import tkinter as tk
import math


#########################################################################################

class Element:

    def __init__(self, uiConfigs, instancedata, command = None):
        self.type = None
        self.uiConfigs = uiConfigs
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
        self.structure = 0

        self.implInstanceData()
        self.createElement()

#########################################################################################
    
    def implInstanceData(self):
        pass

#########################################################################################
    
    def createElement(self):
        pass

#########################################################################################

    

       


        

    

