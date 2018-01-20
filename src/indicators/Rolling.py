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


def var(period: int, column: str = "Close"):
    """Calculate rolling variance (second normalized moment)
    Will use data rows [row-period:row]
    """
    def varLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).var()         # Will return values for early values. min_periods=period-1 changes that
    return {columnName("VAR", period): varLambda}


def std(period: int, column: str = "Close"):
    """Calculate rolling standard deviation
    Will use data rows [row-period:row]
    """
    def stdLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).std()         # Will return values for early values. min_periods=period-1 changes that
    return {columnName("STD", period): stdLambda}

def skew(period: int, column: str = "Close"):
    """Calculate rolling standardized skewness (third normalized moment)
    Will use data rows [row-period:row]
    """
    def skewLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling_skew(window=period)         # Will return values for early values. min_periods=period-1 changes that
    return {columnName("SKEW", period): skewLambda}

def kurt(period: int, column: str = "Close"):
    """Calculate rolling standardized kurtosis (forth normalized moment)
    Will use data rows [row-period:row]
    """
    def kurtLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling_kurt(window=period)         # Will return values for early values. min_periods=period-1 changes that
    return {columnName("KURT", period): kurtLambda}

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

