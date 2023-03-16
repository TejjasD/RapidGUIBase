# Built by Tejas Deolasee

import sys
sys.path.append("config/")

import pandas as pd
import os

#########################################################################################

class configManager:
    def __init__(self):
        self.configDictionary = {}
        self.readConfigs()

#########################################################################################

    def readConfigs(self):
        self.readRootConfigs()
        self.readTkInterUIConfigs()
        self.readLayoutConfigs()

#########################################################################################
    
    def readRootConfigs(self):
        rootConfigDictionary = {}
        rootConfigDictionary['window'] =  pd.read_csv('config\\ui\\root\\window\\window.csv')
        self.configDictionary['root'] = rootConfigDictionary

#########################################################################################

    def readTkInterUIConfigs(self):
        tkInterUIconfigsDictionary = {}
        tkInterUIconfigsDictionary['button'] = pd.read_csv('config\\ui\\tkInterElements\\buttonUI.csv')
        tkInterUIconfigsDictionary['label'] = pd.read_csv('config\\ui\\tkInterElements\\labelUI.csv')
        tkInterUIconfigsDictionary['textBox'] = pd.read_csv('config\\ui\\tkInterElements\\textBoxUI.csv')
        self.configDictionary['tkInterUI'] = tkInterUIconfigsDictionary

#########################################################################################
   
    def readLayoutConfigs(self):
        screensConfigDictionary = {}
        path = "config\\layout"
        numScreens =  len(os.listdir(path))
        for screen in range(numScreens):
            screenConfigDictionary = {}
            fileName = 'config\layout' + '\screen' + str(screen)+ 'Elements.xlsx'
            screenConfigDictionary['button'] = pd.read_excel(fileName, sheet_name = "Buttons")
            screenConfigDictionary['label'] = pd.read_excel(fileName, sheet_name="Labels")
            screenConfigDictionary['textBox'] = pd.read_excel(fileName, sheet_name="TextBoxes")
            screenConfigDictionary['screen'] = pd.read_excel(fileName, sheet_name='Screen')
            screenConfigDictionary['structure']  =pd.read_excel(fileName, sheet_name="Structures")
            screensConfigDictionary[screen] = screenConfigDictionary
        self.configDictionary['layout'] = screensConfigDictionary

#########################################################################################




