# Built by Tejas Deolasee

from gui.tkInter.Element import Element
import tkinter as tk
import math

#########################################################################################


class DummyFrame(Element):

    def __init__(self, bgColor, width, height, row, column):
        self.bgColor = bgColor
        self.width = width
        self.height = height
        self.row = row
        self.column = column

#########################################################################################

    def createElement(self):
        self.element = tk.Frame(background = self.bgColor, width =self.width, height =  self.height)

#########################################################################################

    