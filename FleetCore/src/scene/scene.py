
from scene.sceneLoader import SceneLoader

class Scene:

    def __init__(self, plotMapper):
        self.plotMapper = plotMapper
        self.graphPath = "FleetCore/asset/scene/jhajjar4Full.json"
        self.sceneLoader = SceneLoader(self.plotMapper, self.graphPath)
        self.graph = self.sceneLoader.graph

    

