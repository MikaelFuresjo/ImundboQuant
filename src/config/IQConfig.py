import json
from config.IQCrossValidationConfig import IQCrossValidationConfig
from config.IQInputConfig import IQInputConfig
from config.IQFeaturesConfig import IQFeaturesConfig
from config.IQTrainRandomForestRegressorsConfig import IQTrainRandomForestRegressorsConfig
from config.IQPickleProducerConfig import IQPickleProducerConfig

# Wrapper for config.json -- DO NOT EDIT
class IQConfig(object):
    configFile = None
    config = None

    root: str = None
    input: IQInputConfig = None
    features: IQFeaturesConfig = None
    trainRandomForestRegressors: IQTrainRandomForestRegressorsConfig = None
    pickleProducer: IQPickleProducerConfig = None

    def __init__(self, configFile=r"..\config\config.json"):
        self.configFile = configFile
        self.loadConfig()

    def loadConfig(self):
        with open(self.configFile, 'r') as f:
            self.config = json.load(f)
        self.parseConfig()


    def parseConfig(self):
        self.root = self.config["root"]
        self.input = IQInputConfig(self)
        self.features = IQFeaturesConfig(self)
        self.trainRandomForestRegressors = IQTrainRandomForestRegressorsConfig(self)
        self.pickleProducer = IQPickleProducerConfig(self)
