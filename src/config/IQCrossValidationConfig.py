import os

class IQCrossValidationConfig(object):
    iqConfig = None

    trainingFolderName = None
    trainingFileName = None

    numIterations = None

    def __init__(self, iqConfig):
        self.iqConfig = iqConfig
        self.parseConfig()

    def parseConfig(self):
        c = self.iqConfig.config["crossValidation"]
        self.trainingFolderName = c["training"]["folder"]
        self.trainingFileName = c["training"]["fileName"]

        self.numIterations = c["numIterations"]

    def getTrainingFolder(self):
        return os.path.join(self.iqConfig.root, self.trainingFolderName)

    def getTrainingFilePath(self):
        return os.path.join(self.getTrainingFolder(), self.trainingFileName)


