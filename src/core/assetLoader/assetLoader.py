# Built by Tejas Deolasee

import sys
sys.path.append("assets/")

import pandas as pd
import os

#########################################################################################

class AssetLoader:
    def __init__(self):
        self.assetsDictionary = {}
        self.readAssets()

#########################################################################################

    def readAssets(self):
        self.readRootAssets()
        self.readTkInterUIAssets()
        self.readLayoutAssets()

#########################################################################################
    
    def readRootAssets(self):
        rootAssetDictionary = {}
        rootAssetDictionary['window'] =  pd.read_csv('assets\\ui\\root\\window\\window.csv')
        self.assetsDictionary['root'] = rootAssetDictionary

#########################################################################################

    def readTkInterUIAssets(self):
        tkInterUIAssetDictionary = {}
        tkInterUIAssetDictionary['button'] = pd.read_csv('assets\\ui\\tkInterElements\\buttonUI.csv')
        tkInterUIAssetDictionary['label'] = pd.read_csv('assets\\ui\\tkInterElements\\labelUI.csv')
        tkInterUIAssetDictionary['textBox'] = pd.read_csv('assets\\ui\\tkInterElements\\textBoxUI.csv')
        self.assetsDictionary['tkInterUI'] = tkInterUIAssetDictionary

#########################################################################################
   
    def readLayoutAssets(self):
        screensAssetDictionary = {}
        path = "assets\\layout"
        numScreens =  len(os.listdir(path))
        for screen in range(numScreens):
            screenAssetDictionary = {}
            fileName = 'assets\layout' + '\screen' + str(screen)+ 'Elements.xlsx'
            screenAssetDictionary['button'] = pd.read_excel(fileName, sheet_name = "Buttons")
            screenAssetDictionary['label'] = pd.read_excel(fileName, sheet_name="Labels")
            screenAssetDictionary['textBox'] = pd.read_excel(fileName, sheet_name="TextBoxes")
            screenAssetDictionary['screen'] = pd.read_excel(fileName, sheet_name='Screen')
            screensAssetDictionary[screen] = screenAssetDictionary
        self.assetsDictionary['layout'] = screensAssetDictionary

#########################################################################################




