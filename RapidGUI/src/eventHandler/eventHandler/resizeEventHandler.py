# Built by Tejas Deolasee

#########################################################################################

class ResizeEventHandler:

    def __init__(self, eventHandler):
        self.eventHandler = eventHandler
        self.newHight = 0
        self.newWidth = 0
        self.reziseInvokeCount = 0

#########################################################################################

    def resizeEventTrigger(self, event):
        if event.widget == self.eventHandler.root.element:
            self.newWidth = event.width
            self.newHight = event.height
            self.resizeAllElements()

#########################################################################################

    def resizeAllElements(self):
        if (self.reziseInvokeCount != 0):
            self.eventHandler.app.activeScreen.resizeAllElements(self.newWidth, self.newHight)
        else:
            self.reziseInvokeCount += 1

#########################################################################################