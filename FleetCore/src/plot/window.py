import pygame

from plot.plotMapper import PlotMapper

class Window:

    def __init__(self, fleet):
        self.height = 900
        self.width = 1800
        self.initWindow()
        self.fleet = fleet
        self.running = True
        self.graph = self.fleet.scene.graph
        self.agentManager = self.fleet.scenarioManager.agentManager
        self.buffer = 10
    
    def initWindow(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fleet Core")
        self.backgroundColor = (255, 190, 190)  

    def exec(self):
        while self.running:
            self.fleet.step()
            self.plotElements()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill(self.backgroundColor)
        pygame.quit()
    
    def plotElements(self):
        self.plotGraph()
        self.plotAgents()
        pygame.display.update()

    def plotGraph(self):
        self.plotNodes()
        self.plotEdges()
    
    def plotNodes(self):
        for node in self.graph.nodes:
            pygame.draw.circle(self.window, node.color, (node.x, node.y), node.radius)

    def plotEdges(self):
        for edge in self.graph.edges:
            pygame.draw.polygon(self.window, edge.color, edge.bounds) 
    
    def plotAgents(self):
        for agent in self.agentManager.agents:
            pygame.draw.polygon(self.window, agent.color, agent.bounds) 
            if agent.picked:
                pygame.draw.circle(self.window, (255, 0, 0), (agent.pos[0], agent.pos[1]), agent.width/2)


