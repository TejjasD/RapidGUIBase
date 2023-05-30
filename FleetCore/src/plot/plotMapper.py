from graph.graphUtils import GraphUtils

class PlotMapper:
    
    def __init__(self, width, height, buffer):
        self.width = width
        self.height = height
        self.bufferX = buffer
        self.bufferY = buffer
    
    def calculateScale(self):
        self.extreamValues = self.graphUtils.getExtreamDistances()
        spanX = self.extreamValues[1] - self.extreamValues[0]
        spanY = self.extreamValues[3] - self.extreamValues[2]
        scaleX = (self.width - 2 * self.bufferX)/spanX
        scaleY = (self.height - 2 * self.bufferY)/spanY
        self.scale = min(scaleX, scaleY)
        if self.scale == scaleX:
            self.bufferY = (self.height - self.scale * spanY)/2
        else:
            self.bufferX = (self.width - self.scale * spanX)/2

    def mapPlot(self, graph):
        self.graph = graph
        self.graphUtils = GraphUtils(self.graph)
        self.calculateScale()
        for node in self.graph.nodes:
            node.x = (node.x - self.extreamValues[0]) * self.scale + self.bufferX
            node.y = (node.y - self.extreamValues[2]) * self.scale + self.bufferY

    def mapPos(self, pos):
        newPosX = (pos[0] - self.extreamValues[0]) * self.scale + self.bufferX
        newPosY = (pos[1] - self.extreamValues[2]) * self.scale + self.bufferY
        return [newPosX, newPosY, 0]




