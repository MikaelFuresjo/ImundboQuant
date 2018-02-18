import os

# Wrapper for config.json -- DO NOT EDIT
class IQTrainRandomForestRegressorsConfig(object):
    iqConfig = None

    trainingDataOutputFile: str = None

    numIterations: int = None
    randomForestConfig = None
    
    def __init__(self, iqConfig):
        self.iqConfig = iqConfig
        self.parseConfig()

    def parseConfig(self):
        c = self.iqConfig.config["trainRandomForestRegressors"]

        self.trainingDataOutputFile = c["trainingDataOutputFile"]
        
        self.numIterations = c["numIterations"]
        self.randomForestConfig = c["randomForestSettings"]
