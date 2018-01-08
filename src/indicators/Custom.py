import numpy as np
import pandas as pd

def miniSharp(data: pd.DataFrame, row: int, period: int):
    """Calculate MiniSharp for selected period of given ticker data DataFrame 
    MiniSharp is similar to Williams%R, RSI and Stochastic, but without upper and lower bounds
    Will use data rows [row:row+period+1]
    """
    _Diff_CpLf = (np.amin(data["Low"][row:row+period+1])-data["Close"][row])/data["Close"][row]
    _Diff_CpHf = (np.amax(data["High"][row:row+period+1])-data["Close"][row])/data["Close"][row]
    _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
    _ABSofDiff_CpLf = abs(_Diff_CpLf)
    _ABSofDiff_CpHf = abs(_Diff_CpHf)
    _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
    _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
    return _KeyValueLong - _KeyValueShort

def pastSharp(data: pd.DataFrame, row: int, period: int):
    """Calculate PastSharp for selected period of given ticker data DataFrame
    PastSharp is similar to Williams%R, RSI and Stochastic, but without upper and lower bounds
    Will use data rows [row-period-1:row+1]
    """
    _Diff_CpLf = (np.amin(data["Low"][row-period-1:row+1])-data["Close"][row])/data["Close"][row]
    _Diff_CpHf = (np.amax(data["High"][row-period-1:row+1])-data["Close"][row])/data["Close"][row]
    _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
    _ABSofDiff_CpLf = abs(_Diff_CpLf)
    _ABSofDiff_CpHf = abs(_Diff_CpHf)
    _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
    _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
    return _KeyValueLong - _KeyValueShort

