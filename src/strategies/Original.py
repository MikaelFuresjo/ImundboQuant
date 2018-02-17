import numpy as np
import pandas as pd
from typing import Callable, Dict

from indicators import Custom, Date, Diff, Rolling

from utils.CustomTypes import TColumnName, TFeatureLambda, TFeatureLambdasDict
from utils.Utils import columnName

def getStrategy() -> TFeatureLambdasDict:
    """Get same features as original "OldPreProcess.py" script
       NOT COMPLETE
       returns TFeatureLambdasDict
    """

    features: TFeatureLambdasDict = {}

    # Date-based
    features.update(Date.getDateFeatures())
    
    
    # Diff-based features
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


    # Rolling
    [features.update(Rolling.sma(i)) for i in [20, 200]]
    [features.update(Rolling.ema(i)) for i in [9, 10, 12, 26, 50, 200]]
    [features.update(Rolling.std(i)) for i in [20]]
    [features.update(Rolling.max(i)) for i in [3, 5]]
    [features.update(Rolling.min(i)) for i in [3, 5]]

    return features

