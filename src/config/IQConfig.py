import json
from config.IQPreProcessConfig import IQPreProcessConfig

class IQConfig(object):
    configFile = None
    config = None

    root = None
    preProcess = None

    def __init__(self, configFile=r"..\config\config.json"):
        self.configFile = configFile
        self.loadConfig()

    def loadConfig(self):
        with open(self.configFile, 'r') as f:
            self.config = json.load(f)
        self.parseConfig()


    def parseConfig(self):
        self.root = self.config["root"]
        self.preProcess = IQPreProcessConfig(self)
