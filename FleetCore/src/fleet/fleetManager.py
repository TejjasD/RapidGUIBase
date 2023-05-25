import sys
sys.dont_write_bytecode = True
sys.path.append('FleetCore/')

from FleetCore.src.scene.scene import Scene

class FleetManager:

    def __init__(self):
        self.scene = Scene()
        self.scenarioManager = None
        self.simulator = None

    def exec(self):
        pass