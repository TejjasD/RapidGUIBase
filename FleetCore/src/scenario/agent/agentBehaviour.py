
class AgentBehaviour:

    def __init__(self, agent):
        self.agent = agent
        self.criticalBattery = 0
        self.batteryDrain = 0.00001
        self.loadingTimeout = 200
        self.unloadingTimeout = 200
    
    def step(self):
        self.agent.battery -= self.batteryDrain
        
        if self.agent.battery >= self.criticalBattery:
            if self.agent.state == "IDLE":
                self.agent.locationManager.pickManager.assignPick(self.agent)
                self.agent.state = "GOING_TO_PICK"
            if self.agent.state == "GOING_TO_PICK":
                if self.agent.localGoal == self.agent.goal:
                    self.agent.state = "REACHED_PICK"
                    self.agent.goal = None
                    self.agent.path = []
                    self.nodesReservedTill = 0
                    self.agent.taskManager.raiseTaskRequest(self.agent)
            if self.agent.state == "REACHED_PICK" and self.agent.task is not None:
                self.agent.state = "LOADING"
                self.loadingCount = 0
            if self.agent.state == "LOADING":
                if self.loadingCount >= self.loadingTimeout:
                    self.agent.state = "TASK_IN_PROGRESS"
                    self.agent.goal = self.agent.task.endLocation
                    self.agent.picked = True
                else:
                    self.loadingCount += 1
            if self.agent.state == "TASK_IN_PROGRESS":
                if self.agent.localGoal == self.agent.goal:
                    self.agent.state = "REACHED_DROP"
                    self.agent.goal = None
                    self.agent.path = []
                    self.nodesReservedTill = 0
            if self.agent.state == "REACHED_DROP":
                self.agent.state = "UNLOADING"
                self.unloadingCount = 0
            if self.agent.state == "UNLOADING":
                if self.unloadingCount >= self.unloadingTimeout:
                    self.agent.state = "IDLE"
                    self.agent.picked = False
                else:
                    self.unloadingCount += 1


            
            
