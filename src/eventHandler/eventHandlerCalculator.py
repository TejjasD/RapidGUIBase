# Built by Tejas Deolasee

from eventHandler.eventHandler import EventHandler
from mathematics.algebra.bodmasOperator import BodMasOperator

#########################################################################################

class EventHandlerCalculator (EventHandler):
        
    def btCalculator0(self):
        screen = self.app.activeScreen
        screen.destroy()
        self.app.changeScreen(1)

#########################################################################################

    def btHistory0(self):
        pass

#########################################################################################

    def bt11(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("1")
        

#########################################################################################

    def bt21(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("2")

#########################################################################################

    def bt31(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("3")

#########################################################################################

    def bt41(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("4")

#########################################################################################

    def bt51(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("5")

#########################################################################################

    def bt61(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("6")

#########################################################################################

    def bt71(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("7")

#########################################################################################

    def bt81(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("8")

#########################################################################################

    def bt91(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("9")

#########################################################################################

    def bt01(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("0")

#########################################################################################

    def btClear1(self):
        self.app.activeScreen.textBoxesList[0].clear()

#########################################################################################

    def btCancel1(self):
        self.app.activeScreen.textBoxesList[0].backSpace()

#########################################################################################

    def btAdd1(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("+")
        

#########################################################################################

    def btSubstract1(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("-")

#########################################################################################

    def btMultiply1(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("x")

#########################################################################################

    def btDivide1(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("/")

#########################################################################################

    def btEqual1(self):
        text = self.app.activeScreen.textBoxesList[0].get()
        bodmasOperator = BodMasOperator(text)
        self.app.activeScreen.textBoxesList[0].insertAtEnd(str(bodmasOperator.answer))

#########################################################################################

    def btBracketOpen1(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd("(")

#########################################################################################


    def btBracketClose1(self):
        self.app.activeScreen.textBoxesList[0].insertAtEnd(")")

#########################################################################################


  