from scenario.agent.agent import Agent

class AgentManager:

    def __init__(self, robotManager, locationManager, taskManager, plotMapper, graph):
        self.robotManager = robotManager
        self.taskManager = taskManager
        self.locationManager = locationManager
        self.graph = graph
        self.plotMapper = plotMapper
        self.agents = []
        self.adjustAgents()
        self.connectAgents()

    def adjustAgents(self):
        pass
        # for robot in self.robotManager.robots:
            # newPos = self.plotMapper.mapPos(robot.pos)
            # robot.pos = newPos
            # node = self.graph.graphUtils.getNearestNode(robot.pos)
            # robot.pos = node.pos

    def connectAgents(self):
        for robot in self.robotManager.robots:
            agent = Agent(robot, self.taskManager, self.locationManager)
            self.agents.append(agent)
        
    def step(self):
        for agent in self.agents:
            agent.step()