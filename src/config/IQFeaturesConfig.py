import os

# Wrapper for config.json -- DO NOT EDIT
class IQFeaturesConfig(object):
    iqConfig = None

    featuresStrategy = None
    targetsStrategy = None

    featuresOutputFormat = None
    targetsOutputFormat = None
    
    def __init__(self, iqConfig):
        self.iqConfig = iqConfig
        self.parseConfig()

    def parseConfig(self):
        c = self.iqConfig.config["features"]

        self.featuresStrategy = c["featuresStrategy"]
        self.targetsStrategy = c["targetsStrategy"]

        self.featuresOutputFormat = c["featuresOutputFormat"]
        self.targetsOutputFormat = c["targetsOutputFormat"]

