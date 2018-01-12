import numpy as np
import pandas as pd
from typing import Callable, Dict

from utils.Utils import columnName

def getRollingFeatures() -> Dict[str, Callable[[pd.DataFrame, pd.DataFrame], None]]:
    """Get rolling features
       Will add SMA, EMA, STD
       SMA 20 and 200 due to Bollinger Bands (20, 2) and common usage
       EMA 9, 12, 26 due to MACD, 10, 50, 200 due to common
       STD 20 (used in BB)
       Max  3, 5  (used in stochastics)
       Min  3, 5  (used in stochastics)
       returns a dictionary of {columnName: lamda (data, feature): feature }
    """

    customFeatures = {}
    customFeatures.update([columnName("SMA", i), sma(i)] for i in [20, 200])
    customFeatures.update([columnName("EMA", i), ema(i)] for i in [9, 10, 12, 26, 50, 200])
    customFeatures.update([columnName("STD", i), std(i)] for i in [20])
    customFeatures.update([columnName("Max", i), max(i)] for i in [3, 5])
    customFeatures.update([columnName("Min", i), min(i)] for i in [3, 5])

    return customFeatures

def sma(period: int, column: str = "Close"):
    """Calculate simple moving average (SMA)
    Will use data rows [row-period:row]
    """
    def smaLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).mean()       # Will return values for early values. min_periods=period-1 changes that
    return smaLambda

def ema(period: int, column: str = "Close"):
    """Calculate exponential moving average (EMA)
    Will use data rows [row-period:row]
    """
    def emaLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].ewm(span=200,adjust=False).mean()    # Will return values for early values. min_periods=period-1 changes that
    return emaLambda


def std(period: int, column: str = "Close"):
    """Calculate rolling standard deviation
    Will use data rows [row-period:row]
    """
    def stdLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).std()         # Will return values for early values. min_periods=period-1 changes that
    return stdLambda

def max(period: int, column: str = "Close"):
    """Calculate rolling max
    Will use data rows [row-period:row]
    """
    def maxLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).max()       # Will return values for early values. min_periods=period-1 changes that
    return maxLambda

def min(period: int, column: str = "Close"):
    """Calculate rolling min
    Will use data rows [row-period:row]
    """
    def minLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).min()       # Will return values for early values. min_periods=period-1 changes that
    return minLambda

