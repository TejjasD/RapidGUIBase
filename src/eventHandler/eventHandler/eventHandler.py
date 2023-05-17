# Built by Tejas Deolasee

from eventHandler.eventHandler.resizeEventHandler import ResizeEventHandler

#########################################################################################

class EventHandler:

    def __init__(self, app):
        self.app = app
        self.root = self.app.root
        self.resizeEventHandler = ResizeEventHandler(self)
        self.tempLabels = []
        self.tempButtons = []
        self.tempTextBoxes = []

#########################################################################################
        
  