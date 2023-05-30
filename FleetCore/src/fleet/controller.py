from graph.copuledPathPlanner import CoupledPathPlanner

class Controller:

    def __init__(self, scenarioManager, scene):
        self.scenarioManager = scenarioManager
        self.graph = scene.graph
        self.coupledPathPlanner = CoupledPathPlanner(self.graph)
        self.agentManager = self.scenarioManager.agentManager


    def step(self):
        for agent in self.agentManager.agents:
            if agent.goal is not None and agent.path == []:
                agent.path = self.graph.findPath(agent.pos, agent.goal)
                agent.localGoal = agent.path[0]
        self.reserveNodes()
    

    def reserveNodes(self):
        paths = []
        for agent in self.agentManager.agents:
            if len(agent.path) != 0:
                paths.append(agent.path)
        reservedTill = self.coupledPathPlanner.getReservedNodes(paths)

        for i in range(0, len(self.agentManager.agents)):
            self.agentManager.agents[i].reservedNodesTill = reservedTill[i]


            
        
