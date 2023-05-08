# Built by Tejas Deolasee

#########################################################################################

class eventHandler:

    def __init__(self, app):
        self.app = app
        self.tempLabels = []
        self.tempButtons = []
        self.tempTextBoxes = []
        self.btAddField2Lock = False

#########################################################################################
        
    def btLogin0(self):
        screen = self.app.screenManager.screensList[self.app.screenNumber]
        loginId = screen.textBoxDict['tbUserId0'].get()
        password = screen.textBoxDict['tbPassword0'].get()
        if self.app.passwordManager.authenticateUser(loginId, password):
            screen.destroy()
            self.app.changeScreen(1)

#########################################################################################

    def btSignUp0(self):
        print("Signed Up")

#########################################################################################

    def btAddMonth1(self):
        self.app.screenManager.screensList[self.app.screenNumber].destroy()
        self.app.changeScreen(2)

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
            labelData = self.app.activeScreen.labelInstanceData
            labelList = self.app.activeScreen.labelsList
            
            maxRow = 0
            for label in labelList:
                if label.columnStart == 7:
                    if label.rowStart > maxRow:
                        maxRow = label.rowStart

            textBoxinstanceData = ["tbFieldName2", 0, 0, maxRow + 1, maxRow + 1, 9, 10, "w", 0]
            labelInstanceData = ["lbFieldName2", 0, 0, maxRow + 1, maxRow + 1, 7, 8, "e", "Enter Field Name :", 5]
            fieldNameTextbox = self.app.tkInterManager.createTextBox(textBoxinstanceData)  
            fieldNameLabel = self.app.tkInterManager.createLabel(labelInstanceData)

            self.app.activeScreen.gridMaker.positionElement(fieldNameTextbox)
            self.app.activeScreen.gridMaker.positionElement(fieldNameLabel)
            fieldNameTextbox.place(fieldNameTextbox.pos[0], fieldNameTextbox.pos[1], fieldNameTextbox.sticky)
            fieldNameLabel.place(fieldNameLabel.pos[0], fieldNameLabel.pos[1], fieldNameLabel.sticky)

            buttonInstancedata = ["btConfirmField2", 0, 0, maxRow + 1, maxRow + 1, 11, 12, "center", "Confirm Field", 3]
            confirmFieldButton = self.app.tkInterManager.createButton(buttonInstancedata, getattr(self, "btConfirmField2"))
            self.app.activeScreen.gridMaker.positionElement(confirmFieldButton)
            confirmFieldButton.place(confirmFieldButton.pos[0], confirmFieldButton.pos[1], confirmFieldButton.sticky)

            self.tempLabels.append(fieldNameLabel)
            self.tempButtons.append(confirmFieldButton)
            self.tempTextBoxes.append(fieldNameTextbox)

            self.btAddField2Lock = True
    
#########################################################################################

    def btConfirmField2(self):
        fieldName = self.tempTextBoxes[0].get() + " :"

        if fieldName != " :":     
            rowStart = self.tempLabels[0].rowStart 
            rowEnd = rowStart + self.tempLabels[0].rowSpan - 1

            textBoxinstanceData = ["tbNewField2", 0, 0, rowStart, rowEnd, 9, 10, "w", 0]
            labelInstanceData = ["lbNewField2", 0, 0, rowStart, rowEnd, 7, 8, "e", fieldName, 3]
            fieldNameTextbox = self.app.tkInterManager.createTextBox(textBoxinstanceData)  
            fieldNameLabel = self.app.tkInterManager.createLabel(labelInstanceData)

            self.app.activeScreen.gridMaker.positionElement(fieldNameTextbox)
            self.app.activeScreen.gridMaker.positionElement(fieldNameLabel)
            fieldNameTextbox.place(fieldNameTextbox.pos[0], fieldNameTextbox.pos[1], fieldNameTextbox.sticky)
            fieldNameLabel.place(fieldNameLabel.pos[0], fieldNameLabel.pos[1], fieldNameLabel.sticky)

            self.app.activeScreen.labelsList.append(fieldNameLabel)
            self.app.activeScreen.textBoxesList.append(fieldNameTextbox)
            self.app.activeScreen.addRow()

        self.tempTextBoxes[0].destroy()
        self.tempButtons[0].destroy()
        self.tempLabels[0].destroy()

        self.tempLabels = []
        self.tempButtons = []
        self.tempTextBoxes = []

        self.btAddField2Lock = False

#########################################################################################