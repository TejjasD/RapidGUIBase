# Built by Tejas Deolasee

from gui.tkInter.elements.button import Button
from gui.tkInter.elements.textBox import TextBox
from gui.tkInter.elements.label import Label

#########################################################################################

class eventHandler:

    def __init__(self, root):
        self.root = root
        self.tempLabels = []
        self.tempButtons = []
        self.tempTextBoxes = []
        self.btAddField2Lock = False

#########################################################################################
        
    def btLogin0(self):
        screen = self.root.screenManager.screensList[self.root.screenNumber]
        loginId = screen.textBoxDict['tbUserId0'].get()
        password = screen.textBoxDict['tbPassword0'].get()
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

        if  not self.btAddField2Lock:
            labelData = self.root.activeScreen.labelInstanceData
            
            maxRow = 0
            for i in range(len(labelData['columnStart'])):
                if labelData["columnStart"][i] == 8:
                    if labelData["rowStart"][i] > maxRow:
                        maxRow = labelData["rowStart"][i]

            textBoxinstanceData = ["tbFieldName2", 0, 0, maxRow + 1, maxRow + 1, 10, 11, "w", 0]
            labelInstanceData = ["lbFieldName2", 0, 0, maxRow + 1, maxRow + 1, 8, 9, "e", "Enter Field Name :", 5]
            fieldNameTextbox = TextBox(self.root.activeScreen.uiAssets['textBox'], textBoxinstanceData)  
            fieldNameLabel = Label(self.root.activeScreen.uiAssets['label'], labelInstanceData)

            self.root.activeScreen.gridMaker.positionElement(fieldNameTextbox)
            self.root.activeScreen.gridMaker.positionElement(fieldNameLabel)
            fieldNameTextbox.place(fieldNameTextbox.pos[0], fieldNameTextbox.pos[1], fieldNameTextbox.sticky)
            fieldNameLabel.place(fieldNameLabel.pos[0], fieldNameLabel.pos[1], fieldNameLabel.sticky)

            buttonInstancedata = ["btConfirmField2", 0, 0, maxRow + 1, maxRow + 1, 12, 13, "center", "Confirm Field", 3]
            confirmFieldButton = Button(self.root.activeScreen.uiAssets["button"], buttonInstancedata, getattr(self, "btConfirmField2"))
            self.root.activeScreen.gridMaker.positionElement(confirmFieldButton)
            confirmFieldButton.place(confirmFieldButton.pos[0], confirmFieldButton.pos[1], confirmFieldButton.sticky)

            self.tempLabels.append(fieldNameLabel)
            self.tempButtons.append(confirmFieldButton)
            self.tempTextBoxes.append(fieldNameTextbox)

            self.btAddField2Lock = True
    
#########################################################################################

    def btConfirmField2(self):
        fieldName = self.tempTextBoxes[0].get()

        if fieldName != "":     
            rowStart = self.tempLabels[0].rowStart 
            rowEnd = rowStart + self.tempLabels[0].rowSpan - 1

            textBoxinstanceData = ["tbNewField2", 0, 0, rowStart + 1, rowEnd + 1, 10, 11, "w", 0]
            labelInstanceData = ["lbNewField2", 0, 0, rowStart + 1, rowEnd + 1, 8, 9, "e", fieldName, 3]
            fieldNameTextbox = TextBox(self.root.activeScreen.uiAssets['textBox'], textBoxinstanceData)  
            fieldNameLabel = Label(self.root.activeScreen.uiAssets['label'], labelInstanceData)

            self.root.activeScreen.gridMaker.positionElement(fieldNameTextbox)
            self.root.activeScreen.gridMaker.positionElement(fieldNameLabel)
            fieldNameTextbox.place(fieldNameTextbox.pos[0], fieldNameTextbox.pos[1], fieldNameTextbox.sticky)
            fieldNameLabel.place(fieldNameLabel.pos[0], fieldNameLabel.pos[1], fieldNameLabel.sticky)

        self.tempTextBoxes[0].destroy()
        self.tempButtons[0].destroy()
        self.tempLabels[0].destroy()

        self.tempLabels = []
        self.tempButtons = []
        self.tempTextBoxes = []

        self.btAddField2Lock = False

#########################################################################################