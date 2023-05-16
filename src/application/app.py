# Built by Tejas Deolasee

from core.assetLoader.assetLoader import AssetLoader
from gui.screen.screenManager import ScreenManager
from gui.tkInter.manager.tkIntermanager import TkInterManager
from eventHandler.eventHandlerCalculator import EventHandlerCalculator
from user.passwordManager.passwordManager import passwordManager 

#########################################################################################

class App():
    
    def __init__(self, name):
        self.assetLoader = AssetLoader(name)
        self.tkInterManager = TkInterManager(self.assetLoader.assetsDictionary['tkInterUI'])
        self.root = self.tkInterManager.createRoot(self.assetLoader.assetsDictionary['root']['window']["Value"])

#########################################################################################
    
    def initContinued(self, eventHandler):
        self.screenManager = ScreenManager(eventHandler, self.assetLoader.assetsDictionary['layout'] , self.tkInterManager, self.root)
        self.passwordManager = passwordManager()
        self.screenNumber = 0
        self.activeScreen = self.screenManager.screensList[self.screenNumber]
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
