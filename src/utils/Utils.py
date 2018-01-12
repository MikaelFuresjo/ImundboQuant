import pandas as pd

from typing import List

def columnName(feature: str, *settings: List[int]):
    # Get pandas column name based on feature name and "setting" (normally period shift)
    cn = feature;
    for setting in settings:
        cn = cn + "_{0:02d}".format(setting)
    return cn

def applyFeatures(featuresDictionary: dict, data: pd.DataFrame, features: pd.DataFrame):
    for featureName, feature in featuresDictionary.items():
        features[featureName] = feature(data, features)