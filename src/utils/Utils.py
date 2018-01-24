import pandas as pd

from typing import List, NewType
from utils.CustomTypes import TColumnName, TFeatureLambda, TFeatureLambdasDict


def columnName(feature: str, *settings: List[int]) -> TColumnName:
    # Get pandas column name based on feature name and "setting" (normally period shift)
    cn = feature;
    for setting in settings:
        cn = cn + "_{0:02d}".format(setting)
    return cn

def applyFeatures(featuresDictionary: TFeatureLambdasDict, data: pd.DataFrame, features: pd.DataFrame):
    print("Applying", end='')
    for featureName, feature in featuresDictionary.items():
        print(" {},".format(featureName, feature), end='')
        features[featureName] = feature(data, features)
    print()