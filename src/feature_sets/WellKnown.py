import numpy as np
import pandas as pd
from typing import Callable, Dict

from indicators import Custom, Date, Diff, Rolling, WellKnown

from utils.CustomTypes import TColumnName, TFeatureLambda, TFeatureLambdasDict
from utils.Utils import columnName

def getWellKnownFeatureSet() -> TFeatureLambdasDict:
    """Get same features as original "OldPreProcess.py" script
       NOT COMPLETE
       returns TFeatureLambdasDict
    """

    features: TFeatureLambdasDict = {}

    # Date-based
    features.update(Date.getDateFeatures())
    
    # Well-known
    features.update(WellKnown.bollingerBands(20, 2))
    features.update(WellKnown.bollingerBands(20, 3))

    features.update(WellKnown.macdOscillator(12, 26, 9))

    features.update(WellKnown.stochasticOscillator(14, 5, 3))
    
    features.update(WellKnown.rsiOscillator(14))
    

    return features

