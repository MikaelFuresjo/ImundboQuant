import numpy as np
import pandas as pd
from typing import Callable, Dict

from utils.Utils import columnName


def smaRaw(period: int, column: str = "Close"):
    """Calculate raw simple moving average (SMA)
    Will use data rows [row-period:row]
    """
    def smaRawLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).mean()       # Will return values for early values. min_periods=period-1 changes that
    return {columnName("SMAraw", period): smaRawLambda}

def sma(period: int, column: str = "Close"):
    """Calculate normalized simple moving average (SMA)
    Will use data rows [row-period:row]
    """
    def smaLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).mean()       # Will return values for early values. min_periods=period-1 changes that
    return {columnName("SMA", period): smaLambda}


def emaRaw(period: int, column: str = "Close"):
    """Calculate raw exponential moving average (EMA)
    Will use data rows [row-period:row]
    """
    def emaLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].ewm(span=period,adjust=False).mean()    # Will return values for early values. min_periods=period-1 changes that
    return {columnName("EMAraw", period): emaLambda}

def ema(period: int, column: str = "Close"):
    """Calculate normalized exponential moving average (EMA)
    Will use data rows [row-period:row]
    """
    def emaLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].ewm(span=period,adjust=False).mean()    # Will return values for early values. min_periods=period-1 changes that
    return {columnName("EMA", period): emaLambda}



def varRaw(period: int, column: str = "Close"):
    """Calculate raw rolling variance (second normalized moment)
    Will use data rows [row-period:row]
    """
    def varRawLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).var()         # Will return values for early values. min_periods=period-1 changes that
    return {columnName("VARraw", period): varLambda}

def id(period: int, column: str = "Close"):
    """Calculate Index of Dispersion (ID) = variance / mean = "normalized variance"
    Will use data rows [row-period:row]
    """
    sma = smaRaw(period, column)
    var = varRaw(period, column)

    smaName = list(sma.keys())[0]
    varName = list(var.keys())[0]

    def idLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[varName] / features[smaName];

    features: TFeatureLambdasDict = {}
    features.update(sma)
    features.update(var)
    features.update({
        columnName("ID", period): idLambda
    })

    return features


def stdRaw(period: int, column: str = "Close"):
    """Calculate raw rolling standard deviation
    Will use data rows [row-period:row]
    """
    def stdRawLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).std()         # Will return values for early values. min_periods=period-1 changes that
    return {columnName("STDraw", period): stdRawLambda}

def cv(period: int, column: str = "Close"):
    """Calculate Coefficient of Variation (CV) = std/mean = "normalized standard deviation"
    Will use data rows [row-period:row]
    """
    sma = smaRaw(period, column)
    std = stdRaw(period, column)

    smaName = list(sma.keys())[0]
    stdName = list(std.keys())[0]

    def cvLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[stdName] / features[smaName];

    features: TFeatureLambdasDict = {}
    features.update(sma)
    features.update(std)
    features.update({
        columnName("CV", period): cvLambda
    })

    return features


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

def maxRaw(period: int, column: str = "Close"):
    """Calculate raw rolling max
    Will use data rows [row-period:row]
    """
    def maxRawLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).max()       # Will return values for early values. min_periods=period-1 changes that
    return {columnName("MaxRaw", period): maxRawLambda}

def max(period: int, column: str = "Close"):
    """Calculate normalized max
    Will use data rows [row-period:row]
    """
    maxRaw = maxRaw(period, column)
    maxRawName = list(max.keys())[0]

    def maxLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[maxRawName] / data[column];

    features: TFeatureLambdasDict = {}
    features.update(maxRaw)
    features.update({
        columnName("Max", period): maxLambda
    })

    return features

def minRaw(period: int, column: str = "Close"):
    """Calculate raw rolling min
    Will use data rows [row-period:row]
    """
    def minRawLambda(data: pd.DataFrame, features: pd.DataFrame):
        return data[column].rolling(window=period).min()       # Will return values for early values. min_periods=period-1 changes that
    return {columnName("MinRaw", period): minRawLambda}

def min(period: int, column: str = "Close"):
    """Calculate normalized rolling min
    Will use data rows [row-period:row]
    """
    minRaw = minRaw(period, column)
    minRawName = list(min.keys())[0]

    def minLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[minRawName] / data[column];

    features: TFeatureLambdasDict = {}
    features.update(minRaw)
    features.update({
        columnName("Min", period): minLambda
    })

    return features
