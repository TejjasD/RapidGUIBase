# Built by Tejas Deolasee

from gui.tkInter.elements.element import Element
import tkinter as tk

#########################################################################################


class Frame (Element):

    def implInstanceData(self):
        self.type = "frame"

#########################################################################################

    def createElement(self):
        self.element =  tk.Frame(self.base.element)

#########################################################################################
    