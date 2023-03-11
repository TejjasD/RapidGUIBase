# Built by Tejas Deolasee

from app.tkInter.tkInterElements import *

#########################################################################################

class eventHandler:

    def __init__(self, root):
        self.root = root

#########################################################################################
        
    def btLogin0(self):
        screen = self.root.screenManager.screensList[self.root.screenNumber]
        loginId = screen.textBoxDict['tbUserId0'].textBox.get()
        password = screen.textBoxDict['tbPassword0'].textBox.get()
        if self.root.passwordManager.authenticateUser(loginId, password):
            screen.destroy()
            self.root.changeScreen(1)

#########################################################################################

    def btSignUp0(self):
        print("Signed Up")

#########################################################################################

    def btAddMonth1(self):
        self.root.screenManager.screensList[self.root.screenNumber].destroy()
        self.root.changeScreen(2)

#########################################################################################

    def btInvestments2(self):
        pass

#########################################################################################
    
    def btCash2(self):
        pass

#########################################################################################
    
    def btLiabilities2(self):
        pass

#########################################################################################

    def btAddField2(self):
       pass
        
    
#########################################################################################
