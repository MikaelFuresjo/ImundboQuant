import os

# Wrapper for config.json -- DO NOT EDIT
class IQInputConfig(object):
    iqConfig = None

    instrumentsGlob = None
    
    columns = None

    def __init__(self, iqConfig):
        self.iqConfig = iqConfig
        self.parseConfig()

    def parseConfig(self):
        c = self.iqConfig.config["input"]
        self.instrumentsGlob = c["instrumentsGlob"]
        self.columns = c["columns"]

