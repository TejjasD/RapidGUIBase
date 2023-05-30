from wcs.wcsManager import WcsManager


class TaskManager:

    def __init__(self, scene):
        self.wcsManager = WcsManager(scene.graph)

    def raiseTaskRequest(self, agent):
        task = self.wcsManager.createTask(agent)
        agent.task = task
        print("Task Assigned to Agent")

