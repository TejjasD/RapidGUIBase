# Built by Tejas Deolasee

#########################################################################################

class eventHandler:

    def __init__(self, root):
        self.root = root

#########################################################################################
        
    def btLogin(self):
        print("Login Pressed")
        loginId = self.root.screenLoader.screensList[self.root.screenNumber].textBoxDict['tbUserId'].textBox.get()
        password = self.root.screenLoader.screensList[self.root.screenNumber].textBoxDict['tbPassword'].textBox.get()
        if self.root.passwordManager.authenticateUser(loginId, password):
            self.root.screenLoader.screensList[self.root.screenNumber].destroy()
            self.root.changeScreen(1)

#########################################################################################

    def btSignUp(self):
        print("Signed Up")

#########################################################################################

    def btAddMonth(self):
        self.root.screenLoader.screensList[self.root.screenNumber].destroy()
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
