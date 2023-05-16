# Built by Tejas Deolasee

from gui.tkInter.elements.element import Element
import tkinter as tk

#########################################################################################


class Root (Element):

    def implInstanceData(self):
        self.width = self.instanceData[0]
        self.height = self.instanceData[1]
        self.type = "root"

#########################################################################################

    def createElement(self):
        self.element = tk.Tk()
        self.element.geometry(str(self.width) + "x" + str(self.height))
        
#########################################################################################

    def setBgColor(self, bgColor):
        self.element.configure(background = bgColor)

#########################################################################################

    def run(self):
        self.element.mainloop()

#########################################################################################