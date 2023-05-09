# Built by Tejas Deolasee

#########################################################################################

class Element:

    def __init__(self, instancedata = None, base = None, uiAssets = None, command = None):
        self.base = base
        self.type = None
        self.uiAssets = uiAssets
        self.instanceData = instancedata
        self.command = command
        self.element = None

        self.implInstanceData()
        self.createElement()

#########################################################################################
    
    def implInstanceData(self):
        pass

#########################################################################################
    
    def createElement(self):
        pass

#########################################################################################

    def destroy(self):
        self.element.destroy()

#########################################################################################

    def place(self):
        self.element.place(x = self.pos[0], y = self.pos[1], anchor = self.sticky)

#########################################################################################



        

    

