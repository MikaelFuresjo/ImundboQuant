import numpy as np
import pandas as pd
from typing import Callable, Dict, NewType, Tuple

from utils.CustomTypes import TColumnName, TFeatureLambda, TFeatureLambdasDict
from utils.Utils import columnName


def miniSharp(period: int) -> TFeatureLambdasDict:
    def miniSharpLambda(data: pd.DataFrame, features: pd.DataFrame):
        """Calculate --- FORWARD LOOKING --- MiniSharp for selected period of given ticker data DataFrame 
        MiniSharp is similar to Williams%R, RSI and Stochastic, but without upper and lower bounds
        Will use data rows [row:row+period+1]
        """
        # shifts to make it forward looking
        _Diff_CpLf = (data["Low"].shift(period+1).rolling(window=period+1).min().shift(-period-1)-data["Close"])/data["Close"]
        _Diff_CpHf = (data["High"].shift(period+1).rolling(window=period+1).max().shift(-period-1)-data["Close"])/data["Close"]
        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
        _ABSofDiff_CpLf = _Diff_CpLf.abs()
        _ABSofDiff_CpHf = _Diff_CpHf.abs()
        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
        return _KeyValueLong - _KeyValueShort
    return {columnName("MiniSharp", period): miniSharpLambda}

def pastSharp(period: int) -> TFeatureLambdasDict:
    """Calculate PastSharp for selected period of given ticker data DataFrame
    PastSharp is similar to Williams%R, RSI and Stochastic, but without upper and lower bounds
    Will use data rows [row-period-1:row+1]
    """
    def pastSharpLambda(data: pd.DataFrame, features: pd.DataFrame):
        """Calculate --- FORWARD LOOKING --- MiniSharp for selected period of given ticker data DataFrame 
        MiniSharp is similar to Williams%R, RSI and Stochastic, but without upper and lower bounds
        Will use data rows [row:row+period+1]
        """
        # shifts to make it forward looking
        _Diff_CpLf = (data["Low"].rolling(window=period+1).min()-data["Close"])/data["Close"]
        _Diff_CpHf = (data["High"].rolling(window=period+1).max()-data["Close"])/data["Close"]
        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
        _ABSofDiff_CpLf = _Diff_CpLf.abs()
        _ABSofDiff_CpHf = _Diff_CpHf.abs()
        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
        return _KeyValueLong - _KeyValueShort
    return {columnName("PastSharp", period): pastSharpLambda}

