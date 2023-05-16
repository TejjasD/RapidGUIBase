# Built by Tejas Deolasee

from application.app import App
from eventHandler.eventHandlerCalculator import EventHandlerCalculator

#########################################################################################

class CalculatorApp(App):
    
    def __init__(self):
        self.name = "calculator"
        super().__init__(self.name)
        self.eventHandler = EventHandlerCalculator(self)
        super().initContinued(self.eventHandler)
          
#########################################################################################
