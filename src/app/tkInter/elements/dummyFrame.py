# Built by Tejas Deolasee

from app.tkInter.Element import Element
import tkinter as tk
import math

#########################################################################################


class DummyFrame(Element):
    
    def __init__(self, bgColor, width, height, row, column):
        self.element = tk.Frame(background=bgColor, width=width, height=height)
        self.row = row
        self.column = column

#########################################################################################

    