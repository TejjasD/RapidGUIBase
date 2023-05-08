# Built by Tejas Deolasee

#########################################################################################

class Element:

    def __init__(self, instancedata, uiAssets = None, command = None):
        self.type = None
        self.uiAssets = uiAssets
        self.instanceData = instancedata
        self.command = command
        self.id = 0
        self.pos = (0, 0)
        self.element = None
        self.width = None
        self.height = None

        self.rowStart = 0
        self.rowSpan = 0
        self.columnStart = 0
        self.columnSpan = 0
        self.sticky = "center"

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

    def place(self, x, y, sticky):
        self.element.place(x = x, y = y, anchor = sticky)

#########################################################################################

    def get(self):
        if self.type == "textBox": 
            return self.element.get()
        else:
            print("--------------------------------------------------------Get Method Called on Wrong Element----------------------------------------------------------------")
            return
    
#########################################################################################

    def run(self):
        if self.type == "root":
            self.element.mainloop()
        else:
            print("--------------------------------------------------------Get Method Called on Wrong Element----------------------------------------------------------------")
            return
    
#########################################################################################



        

    

