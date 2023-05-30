
class RobotManager:

    def __init__(self):
        self.robots = []

    def step(self):
        for robot in self.robots:
            robot.step()

    def addRobot(self, robot):
        self.robots.append(robot)
