import numpy as np
import pandas as pd
from typing import Callable, Dict

from indicators import Diff
from indicators import Rolling
from utils.CustomTypes import TFeatureLambdasDict
from utils.Utils import columnName



def bollingerBands(period: int = 20, sigma: int = 2, column: str = "Close") -> TFeatureLambdasDict:
    """Calculate Normalized Bollinger Bands
    Based on number of standard deviations and period
    Will also add SMA(period) and STD(period)
    """

    sma = Rolling.smaRaw(period, column)
    std = Rolling.stdRaw(period, column)

    smaName = list(sma.keys())[0]
    stdName = list(std.keys())[0]

    def bbUpperLambda(data: pd.DataFrame, features: pd.DataFrame):
        return (features[smaName] + (features[stdName] * sigma)) / data[column]

    def bbLowerLambda(data: pd.DataFrame, features: pd.DataFrame):
        return (features[smaName] - (features[stdName] * 2)) / data[column]

    features: TFeatureLambdasDict = {}
    features.update(sma)
    features.update(std)
    features.update({
        columnName("BBupper", period, sigma): bbUpperLambda,
        columnName("BBlower", period, sigma): bbLowerLambda
    })

    return features

#    #https://iknowfirst.com/technical-indicators

def macdOscillator(mediumPeriod: int = 12, longPeriod: int = 26, shortPeriod: int = 9):
    """Calculate Normalized MACD
    MACD Line = mid (often 12day) EMA – long (often 26day) EMA
    Signal Line = short (often 9day) EMA of MACD Line
    The MACD Histogram is the MACD Line – Signal Line
    Will also add needed normalized EMAs
    """

    # Using normalized EMAs will yield a normalized MACD
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
    """Calculate Normalized Stochastic Oscillator
    Calculates %K-fast = 100(Close - Min(period))/(Max(period) - Min(period))   100-factor removed due to normalizing
    %K smooths %K-fast
    %D smooths %K
    Will also add MaxRaw(period) and MinRaw(period)
    """

    max = Rolling.maxRaw(period)
    min = Rolling.minRaw(period)

    maxName = list(max.keys())[0]
    minName = list(min.keys())[0]

    stochKFastName = columnName("Stoch-K-Fast", period)
    stochKName = columnName("Stoch-K", period, smoothKPeriod)
    stochDName = columnName("Stoch-D", period, smoothKPeriod, smoothDPeriod)

    def kFastLambda(data: pd.DataFrame, features: pd.DataFrame):
        return (data[column] - features[minName]) / (features[maxName] - features[minName]) # * 100

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
    """Calculate Normalized RSI Oscillator
    Will also add DiffRaw(Close, Close-1)
    """

    diff = Diff.CtoCRaw(1)

    diffName = list(diff.keys())[0]

    posName = columnName("PosGainRaw", period)
    negName = columnName("NegGainRaw", period)
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
        return 1 - (1.0 / (1.0 + features[rsiRawName]))
        # return 100.0 - (100.0 / (1.0 + features[rsiRawName]))    # Non-normalized RSI


    features: TFeatureLambdasDict = {}
    features.update(diff)
    features.update({
        posName: posGainLambda,
        negName: negGainLambda,
        rsiRawName: rsiRawLambda,
        rsiName: rsiLambda
    })

    return features


#Not used, but kept for reference
def atrRaw(period: int = 14, close: str = "Close", high: str = "High", low: str = "Low") -> TFeatureLambdasDict:
    """Calculate Average True Range
    Based on TR and period
    Will also add TR (True Range)
    """

    trName = columnName("TRraw")
    atrName = columnName("ATRraw")

    def trLambda(data: pd.DataFrame, features: pd.DataFrame):
        closes = data[close]
        highs = data[high]
        lows = data[low]
        closes1 = closes.shift(-1)

        atr1 = highs - lows
        atr2 = (highs - closes1).abs()
        atr3 = (closes1 - lows).abs()
        return np.max([atr1, atr2, atr3], axis=0)

    def atrLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[trName].rolling(window = period).mean()

    features: TFeatureLambdasDict = {
        trName: trLambda,
        atrName: atrLambda
    }

    return features


def atr(period: int = 14, close: str = "Close", high: str = "High", low: str = "Low") -> TFeatureLambdasDict:
    """Calculate Normalized Average True Range
    Based on Normalized TR and period
    Will also add Normalized TR (True Range)
    """

    trName = columnName("TR")
    atrName = columnName("ATR")

    def trLambda(data: pd.DataFrame, features: pd.DataFrame):
        closes = data[close]
        highs = data[high]
        lows = data[low]
        closes1 = closes.shift(-1)

        atr1 = highs - lows
        atr2 = (highs - closes1).abs()
        atr3 = (closes1 - lows).abs()
        return np.max([atr1, atr2, atr3], axis=0) / closes1

    def atrLambda(data: pd.DataFrame, features: pd.DataFrame):
        return features[trName].rolling(window = period).mean()

    features: TFeatureLambdasDict = {
        trName: trLambda,
        atrName: atrLambda
    }

    return features


#Not used, kept for reference
def parabolicSarRaw(af: float = 0.02, amax: float = 0.2, highColumn: str = "High", lowColumn: str = "Low") -> TFeatureLambdasDict:
    """Calculate Parabolic SAR
    "Stop and Reversal"
    Iterative implementation
    """

    psarName = columnName("PSARraw")

    def psarLambda(data: pd.DataFrame, features: pd.DataFrame):
        high = data[highColumn]
        low = data[lowColumn]

        # Starting values
        sig0, xpt0, af0 = True, high[0], af
        sar = [low[0] - (high - low).std()]

        for i in range(1, len(data)):
            sig1, xpt1, af1 = sig0, xpt0, af0

            lmin = min(low[i - 1], low[i])
            lmax = max(high[i - 1], high[i])

            if sig1:
                sig0 = low[i] > sar[-1]
                xpt0 = max(lmax, xpt1)
            else:
                sig0 = high[i] >= sar[-1]
                xpt0 = min(lmin, xpt1)

            if sig0 == sig1:
                sari = sar[-1] + (xpt1 - sar[-1])*af1
                af0 = min(amax, af1 + af)

                if sig0:
                    af0 = af0 if xpt0 > xpt1 else af1
                    sari = min(sari, lmin)
                else:
                    af0 = af0 if xpt0 < xpt1 else af1
                    sari = max(sari, lmax)
            else:
                af0 = af
                sari = xpt0

            sar.append(sari)

        return pd.Series(sar, index=data.index)

    features: TFeatureLambdasDict = {
        psarName: psarLambda
    }

    return features


def parabolicSar(af: float = 0.02, amax: float = 0.2, highColumn: str = "High", lowColumn: str = "Low", normalizeColumn: str = "Close") -> TFeatureLambdasDict:
    """Calculate Normalized Parabolic SAR
    "Stop and Reversal"
    Iterative implementation, normalized simply by latest close
    """

    psarName = columnName("PSAR")

    def psarLambda(data: pd.DataFrame, features: pd.DataFrame):
        high = data[highColumn]
        low = data[lowColumn]

        # Starting values
        sig0, xpt0, af0 = True, high[0], af
        sar = [low[0] - (high - low).std()]

        for i in range(1, len(data)):
            sig1, xpt1, af1 = sig0, xpt0, af0

            lmin = min(low[i - 1], low[i])
            lmax = max(high[i - 1], high[i])

            if sig1:
                sig0 = low[i] > sar[-1]
                xpt0 = max(lmax, xpt1)
            else:
                sig0 = high[i] >= sar[-1]
                xpt0 = min(lmin, xpt1)

            if sig0 == sig1:
                sari = sar[-1] + (xpt1 - sar[-1])*af1
                af0 = min(amax, af1 + af)

                if sig0:
                    af0 = af0 if xpt0 > xpt1 else af1
                    sari = min(sari, lmin)
                else:
                    af0 = af0 if xpt0 < xpt1 else af1
                    sari = max(sari, lmax)
            else:
                af0 = af
                sari = xpt0

            sar.append(sari)

        return pd.Series(sar / data[normalizeColumn], index=data.index)

    features: TFeatureLambdasDict = {
        psarName: psarLambda
    }

    return features


def cci(period: int = 20, c=1.5, closeCol: str = "Close", highCol: str = "High", lowCol: str = "Low"):
    """Calculate CCI (Commodity Channel Index)
    CCI is with default c=0.015 is set so that 70-80% of values fall into the [-100,100] range
    c is therefore set to 1.5 =  cTypical*100 to make 70-80% fall into [-1,1]
    """

    cciName = columnName("CCI", period)

    def cciLambda(data: pd.DataFrame, features: pd.DataFrame):
        priceMean = data[[highCol, lowCol, closeCol]].mean(axis=1)

        priceMeanAverage = priceMean.rolling(window=period).mean()
        meanDeviation = (priceMeanAverage - priceMean).abs().rolling(window=period).mean()
        
        # mdev = moments.rolling_apply(s, n, lambda x: np.fabs(x - x.mean()).mean())

        return (priceMean - priceMeanAverage)/(c * meanDeviation)

    features: TFeatureLambdasDict = {
        cciName: cciLambda
    }

    return features

