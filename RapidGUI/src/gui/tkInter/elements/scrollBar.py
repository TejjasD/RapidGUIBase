# Built by Tejas Deolasee

from gui.tkInter.elements.element import Element
import tkinter as tk

#########################################################################################


class ScrollBar (Element):

    def implInstanceData(self):
        self.type = "scrollBar"

#########################################################################################

    def createElement(self):
        self.element = tk.Scrollbar(self.base.element, orient = "vertical", command = self.command.yview)
        self.set = self.element.set

#########################################################################################
    
    def pack(self):
        self.element.pack(side="right", fill="y")

#########################################################################################