import numpy as np
import pandas as pd
from typing import Callable, Dict

from indicators import Custom, Date, Diff, Rolling, WellKnown

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
    
    # Well-known
    features.update(WellKnown.bollingerBands(20, 2))
    features.update(WellKnown.bollingerBands(20, 3))

    features.update(WellKnown.macdOscillator(12, 26, 9))

    features.update(WellKnown.stochasticOscillator(5, 3, 3))
    features.update(WellKnown.stochasticOscillator(10, 10, 5))
    features.update(WellKnown.stochasticOscillator(14, 5, 3)) # Most common
    features.update(WellKnown.stochasticOscillator(30, 10, 10))
    features.update(WellKnown.stochasticOscillator(144, 1, 1))
    
    features.update(WellKnown.rsiOscillator(14))
    
    features.update(WellKnown.atr(14))

    #features.update(WellKnown.parabolicSar()) # Iterative, leading to slow to calculate

    features.update(WellKnown.cci())

    return features

