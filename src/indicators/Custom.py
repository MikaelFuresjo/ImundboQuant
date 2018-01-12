import numpy as np
import pandas as pd
from typing import Callable, Dict

from utils.Utils import columnName

def getCustomFeatures() -> Dict[str, Callable[[pd.DataFrame, pd.DataFrame], None]]:
    """Get custom features
       Will add miniSharp and pastSharp
       returns a dictionary of {columnName: lamda (data, feature): feature }
    """

    customFeatures = {}
    r = range(5, 34+1)
    # customFeatures.update([columnName("MiniSharp", i), miniSharp(i)] for i in r)  # Forward-looking
    customFeatures.update([columnName("PastSharp", i), miniSharp(i)] for i in r)

    return customFeatures

def miniSharp(period: int):
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
    return miniSharpLambda

def pastSharp(period: int):
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
    return pastSharpLambda

