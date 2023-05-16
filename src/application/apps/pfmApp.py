# Built by Tejas Deolasee

from application.app import App
from eventHandler.apps.eventHandlerPfm import EventHandlerPfm

#########################################################################################

class PfmApp(App):
    
    def __init__(self):
        self.name = "pfm"
        super().__init__(self.name)
        self.eventHandler = EventHandlerPfm(self)
        super().initContinued(self.eventHandler)

       
#########################################################################################