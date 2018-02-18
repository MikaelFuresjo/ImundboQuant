import os

class IQPickleProducerConfig(object):
    iqConfig = None

    folderName = None
    featuresFolderName = None
    featuresPrefix = None
    
    trainingFolderName = None
    trainingFileName = None

    slot = None
    horizon = None
    trainingInst = None
    numFeatures = None

    randomForestConfig = None
    
    def __init__(self, iqConfig):
        self.iqConfig = iqConfig
        self.parseConfig()

    def parseConfig(self):
        c = self.iqConfig.config["pickleProducer"]

        self.folderName = c["folder"]

        self.featuresFolderName = c["features"]["folder"]
        self.featuresPrefix = c["features"]["prefix"]
        
        self.trainingFolderName = c["training"]["folder"]
        self.trainingFileName = c["training"]["fileName"]

        #What are these three settings? (refer to config.json for values)
        self.slot = c["slot"]
        self.horizon = c["horizon"]
        self.trainingInst = c["trainingInst"]  # Not used after specifying training filename explicitly, bad idea?
    
        self.numFeatures = c["numFeatures"]
    

        self.randomForestConfig = c["randomForest"]


    def getFeaturesFolder(self):
        return os.path.join(self.iqConfig.root, self.featuresFolderName)

    def getFeaturesFileName(self):
        return self.featuresPrefix + '_Feat_Slot' + self.slot + '.txt'

    def getFeaturesFilePath(self):
        return os.path.join(self.getFeaturesFolder(), self.getFeaturesFileName())


    def getFolder(self):
        return os.path.join(self.iqConfig.root, self.folderName)

    def getPickleFileName(self):
        return self.featuresPrefix + '_Slot' + self.slot + '.pkl'

    def getPickleFilePath(self):
        return os.path.join(self.getFolder(), self.getPickleFileName())


    def getTrainingFolder(self):
        return os.path.join(self.iqConfig.root, self.trainingFolderName)

    def getTrainingFilePath(self):
        return os.path.join(self.getTrainingFolder(), self.trainingFileName)  # 'all'+_TrainingInst+'.xlsx')
