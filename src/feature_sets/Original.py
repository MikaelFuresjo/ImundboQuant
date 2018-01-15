import numpy as np
import pandas as pd
from typing import Callable, Dict

from indicators import Custom, Date, Diff, Rolling

from utils.CustomTypes import TColumnName, TFeatureLambda, TFeatureLambdasDict
from utils.Utils import columnName

def getOriginalFeatureSet() -> TFeatureLambdasDict:
    """Get features from original Python 2.7 code
       NOT COMPLETE YET
       returns TFeatureLambdasDict
    """

    features: TFeatureLambdasDict = {}

    # Date-based
    features.update(Date.getDateFeatures())
    
    
    """Get diff-based features
       Will add lagging diffs CtoX, normally for 0..25
       returns a dictionary of {columnName: lamda (data, feature): feature }
    """
    r = range(0, 25+1)
    [features.update(Diff.CtoH(i)) for i in r]
    [features.update(Diff.CtoL(i)) for i in r]
    [features.update(Diff.CtoO(i)) for i in r]
    r = range(1, 25+1)
    [features.update(Diff.CtoC(i)) for i in r]

    # MiniSharp and PastSharp
    r = range(5, 34+1)
    [features.update(Custom.miniSharp(i)) for i in r] 
    #[features.update(Custom.pastSharp(i)) for i in r]  # Forward-looking

    #featuresToExtract.update(indicators.Rolling.getRollingFeatures())
    #featuresToExtract.update(indicators.Famous.getFamousFeatures())

    return features

