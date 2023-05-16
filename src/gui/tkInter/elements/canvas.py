# Built by Tejas Deolasee

from gui.tkInter.elements.element import Element
import tkinter as tk

#########################################################################################


class Canvas (Element):

    def implInstanceData(self):
        self.type = "canvas"

#########################################################################################

    def createElement(self):
        self.element = tk.Canvas(self.base.element)
        self.yview = self.element.yview

#########################################################################################

    def configScrollBar(self, scrollbar):
        self.element.config(yscrollcommand = scrollbar.set)
        self.element.bind('<Configure>', lambda e: self.element.configure(scrollregion= self.element.bbox("all")))

#########################################################################################

    def createWindow(self, window, pos = (0, 0), anchor = "nw"):
        self.element.create_window(pos, window = window.element, anchor = anchor)

#########################################################################################

    def pack(self):
        self.element.pack(side = "left", fill = "both", expand = 1)

#########################################################################################