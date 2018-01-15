import numpy as np
import pandas as pd
from typing import Callable, Dict

from indicators import Diff
from indicators import Rolling
from utils.CustomTypes import TFeatureLambdasDict
from utils.Utils import columnName


def bollingerBands(period: int = 20, sigma: int = 2) -> TFeatureLambdasDict:
    """Calculate Bollinger Bands
    Based on number of standard deviations and period
    Will also add SMA(period) and STD(period)
    """

    sma = Rolling.sma(period)
    std = Rolling.std(period)

    smaName = list(sma.keys())[0]
    stdName = list(std.keys())[0]

    def bbUpperLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[smaName] + (features[stdName] * sigma)

    def bbLowerLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[smaName] - (features[stdName] * 2)

    features: TFeatureLambdasDict = {}
    features.update(sma)
    features.update(std)
    features.update({
        columnName("BBupper", 20, period): bbUpperLambda,
        columnName("BBlower", 20, period): bbLowerLambda
    })

    return features

#    #https://en.wikipedia.org/wiki/Moment_(mathematics)
#    #https://iknowfirst.com/technical-indicators

def macdOscillator(mediumPeriod: int = 12, longPeriod: int = 26, shortPeriod: int = 9):
    """Calculate MACD
    MACD Line = mid (often 12day) EMA – long (often 26day) EMA
    Signal Line = short (often 9day) EMA of MACD Line
    The MACD Histogram is the MACD Line – Signal Line
    Will also add needed EMAs
    """

    emaShort = Rolling.ema(shortPeriod)
    emaMedium = Rolling.ema(mediumPeriod)
    emaLong = Rolling.ema(longPeriod)

    shortName =  list(emaShort.keys())[0]
    mediumName = list(emaMedium.keys())[0]
    longName =   list(emaLong.keys())[0]

    macdLineName = columnName("MACDline", mediumPeriod, longPeriod, shortPeriod)
    macdSignalName = columnName("MACDsignal", mediumPeriod, longPeriod, shortPeriod)
    macdHistogramName = columnName("MACDhistogram", mediumPeriod, longPeriod, shortPeriod)

    def macdLineLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[mediumName] - features[longName]

    def macdSignalLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[macdLineName].ewm(span=shortPeriod, adjust=False).mean()

    def macdHistogramLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[macdLineName] - features[macdSignalName]

    features: TFeatureLambdasDict = {}
    features.update(emaShort)
    features.update(emaMedium)
    features.update(emaLong)
    features.update({
        macdLineName: macdLineLambda,
        macdSignalName: macdSignalLambda,
        macdHistogramName: macdHistogramLambda
    })

    return features


def stochasticOscillator(period: int = 14, smoothKPeriod: int = 5, smoothDPeriod: int = 3, column: str = "Close") -> TFeatureLambdasDict:
    """Calculate Stochastic Oscillator
    Calculates %K-fast = 100(Close - Min(period))/(Max(period) - Min(period))
    %K smooths %K-fast
    %D smooths %K
    Will also add Max(period) and Min(period)
    """

    max = Rolling.max(period)
    min = Rolling.min(period)

    maxName = list(max.keys())[0]
    minName = list(min.keys())[0]

    stochKFastName = columnName("Stoch-K-Fast", period)
    stochKName = columnName("Stoch-K", period, smoothKPeriod)
    stochDName = columnName("Stoch-D", period, smoothKPeriod, smoothDPeriod)

    def kFastLambda(data: pd.DataFrame, features: pd.DataFrame):
        return 100. * (data[column] - features[minName]) / (features[maxName] - features[minName])

    def kLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[stochKFastName].rolling(window=smoothKPeriod).mean()

    def dLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[stochKName].rolling(window=smoothDPeriod).mean()

    features: TFeatureLambdasDict = {}
    features.update(max)
    features.update(min)
    features.update({
        stochKFastName: kFastLambda,
        stochKName: kLambda,
        stochDName: dLambda
    })

    return features


def rsiOscillator(period: int = 14) -> TFeatureLambdasDict:
    """Calculate RSI Oscillator
    Will also add Diff(Close, Close-1)
    """

    diff = Diff.CtoC(1)

    diffName = list(diff.keys())[0]

    posName = columnName("PosGain", period)
    negName = columnName("NegGain", period)
    rsiRawName = columnName("RSIraw", period)
    rsiName = columnName("RSI", period)


    def posGainLambda(data: pd.DataFrame, features: pd.DataFrame):
        d = features[diffName]
        return d.where(d > 0, 0).ewm(span=period, adjust=False).mean()

    def negGainLambda(data: pd.DataFrame, features: pd.DataFrame):
        d = features[diffName]
        return -1*d.where(d < 0, 0).ewm(span=period, adjust=False).mean()

    def rsiRawLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[posName] / features[negName]

    def rsiLambda(data: pd.DataFrame, features: pd.DataFrame):
        return 100.0 - (100.0 / (1.0 + features[rsiRawName]))


    features: TFeatureLambdasDict = {}
    features.update(diff)
    features.update({
        posName: posGainLambda,
        negName: negGainLambda,
        rsiRawName: rsiRawLambda,
        rsiName: rsiLambda
    })

    return features
