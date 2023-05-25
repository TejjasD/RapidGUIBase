import sys
sys.dont_write_bytecode = True
sys.path.append('FleetCore/')

from FleetCore.src.scene.sceneLoader import SceneLoader

class Scene:

    def __init__(self):
        self.graphPath = "FleetCore/asset/scene/sample.json"
        self.sceneLoader = SceneLoader(self.graphPath)
        self.graph = self.sceneLoader.graph

