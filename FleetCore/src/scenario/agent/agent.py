from scenario.agent.agentBehaviour import AgentBehaviour

class Agent:

    def __init__(self, robot, taskManager, locationManager):
        self.locationManager = locationManager
        self.taskManager = taskManager
        self.robot = robot
        self.pos = robot.pos
        self.battery = robot.battery
        self.id = robot.id
        self.width = 10
        self.height = 15
        self.color =  (0, 0, 139)
        self.state = "IDLE"
        self.agentBehaviour = AgentBehaviour(self)
        self.goal = None
        self.path = []
        self.reservedNodesTill = 0
        self.localGoal = None
        self.speed = 0.01
        self.task = None
        self.picked = False

        self.calculateBoundingBox()
        
    def calculateBoundingBox(self):
        corner1 = (self.pos[0] + self.width/2, self.pos[1] - self.height/2)
        corner2 =  (self.pos[0] + self.width/2, self.pos[1] + self.height/2)
        corner3 = (self.pos[0] - self.width/2, self.pos[1] + self.height/2)
        corner4 =  (self.pos[0] - self.width/2, self.pos[1] - self.height/2)
        self.bounds = [corner1, corner2, corner3, corner4]
    
    def step(self):
        self.agentBehaviour.step()
        self.followPath()
        self.calculateBoundingBox()
    
    def followPath(self):     
        if self.localGoal is not None and len(self.path) != 0:
            currentIndex = self.path.index(self.localGoal)
            if currentIndex <= len(self.path) - 1 and currentIndex < self.reservedNodesTill:
                nextGoal = self.path[currentIndex + 1]
                vector = (nextGoal.x - self.localGoal.x, nextGoal.y - self.localGoal.y)
                self.pos[0] += self.speed * vector[0]
                self.pos[1] += self.speed * vector[1]

                if abs(self.pos[0] - nextGoal.x) < self.speed and abs(self.pos[1] - nextGoal.y) < self.speed:
                    self.localGoal = nextGoal
                    self.pos[0] = nextGoal.x
                    self.pos[1] = nextGoal.y
            


        
        


