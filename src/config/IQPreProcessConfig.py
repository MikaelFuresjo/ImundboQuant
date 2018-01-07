import os

class IQPreProcessConfig(object):
    iqConfig = None

    folderName = None
    instrumentsFolderName = None
    
    featuresFileName = None

    def __init__(self, iqConfig):
        self.iqConfig = iqConfig
        self.parseConfig()

    def parseConfig(self):
        c = self.iqConfig.config["preProcess"]
        self.folderName = c["folder"]
        self.instrumentsFolderName = c["instrumentsFolder"]
        self.featuresFileName = c["featuresFile"]


    def getFolder(self):
        return os.path.join(self.iqConfig.root, self.folderName)

    def getInstrumentsFolder(self):
        return os.path.join(self.iqConfig.root, self.instrumentsFolderName)

