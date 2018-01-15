import numpy as np
import pandas as pd
from typing import Callable, Dict

from utils.Utils import columnName


def sma(period: int, column: str = "Close"):
    """Calculate simple moving average (SMA)
    Will use data rows [row-period:row]
    """
    def smaLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).mean()       # Will return values for early values. min_periods=period-1 changes that
    return {columnName("SMA", period): smaLambda}

def ema(period: int, column: str = "Close"):
    """Calculate exponential moving average (EMA)
    Will use data rows [row-period:row]
    """
    def emaLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].ewm(span=period,adjust=False).mean()    # Will return values for early values. min_periods=period-1 changes that
    return {columnName("EMA", period): emaLambda}


def std(period: int, column: str = "Close"):
    """Calculate rolling standard deviation
    Will use data rows [row-period:row]
    """
    def stdLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).std()         # Will return values for early values. min_periods=period-1 changes that
    return {columnName("STD", period): stdLambda}

def max(period: int, column: str = "Close"):
    """Calculate rolling max
    Will use data rows [row-period:row]
    """
    def maxLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).max()       # Will return values for early values. min_periods=period-1 changes that
    return {columnName("Max", period): maxLambda}

def min(period: int, column: str = "Close"):
    """Calculate rolling min
    Will use data rows [row-period:row]
    """
    def minLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).min()       # Will return values for early values. min_periods=period-1 changes that
    return {columnName("Min", period): minLambda}

