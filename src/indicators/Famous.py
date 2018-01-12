import numpy as np
import pandas as pd
from typing import Callable, Dict

from utils.Utils import columnName

def getFamousFeatures() -> Dict[str, Callable[[pd.DataFrame, pd.DataFrame], None]]:
    """Get "famous" indicators
       Bollinger Bands
       MACD
       Stochastics
       Will require relevant SMA, EMA, STD, Max and Min to be computed before
       returns a dictionary of {columnName: lamda (data, feature): feature }
    """

    customFeatures = {}
    customFeatures.update([columnName("BBupper", 20, i), bbUpper(20, i)] for i in [2, 3]) # Sigma = 2, 3
    customFeatures.update([columnName("BBlower", 20, i), bbLower(20, i)] for i in [2, 3]) # Sigma = 2, 3

    return customFeatures

def bbUpper(period: int = 20, sigma: int = 2):
    """Calculate Upper Bollinger Band
    Based on number of standard deviations and period
    Requires SMA(period) and STD(period) to be calculated
    """
    smaName = columnName("SMA", period)
    stdName = columnName("STD", period)
    def bbUpperLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[smaName] + (features[stdName] * sigma)
    return bbUpperLambda

def bbLower(period: int = 20, sigma: int = 2):
    """Calculate Lower Bollinger Band
    Based on number of standard deviations and period
    Requires SMA(period) and STD(period) to be calculated
    """
    smaName = columnName("SMA", period)
    stdName = columnName("STD", period)
    def bbLowerLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[smaName] - (features[stdName] * 2)
    return bbLowerLambda


