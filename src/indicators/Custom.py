import numpy as np
import pandas as pd

def miniSharp(data: pd.DataFrame, row: int, period: int):
    """Calculate miniSharp for selected period of given series 
    MiniSharp is similar to Williams%R, RSI and Stochastic, but without upper and lower bounds
    """
    _Diff_CpLf = (np.amin(data["Low"][row:row+period+1])-data["Close"][row])/data["Close"][row]
    _Diff_CpHf = (np.amax(data["High"][row:row+period+1])-data["Close"][row])/data["Close"][row]
    _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
    _ABSofDiff_CpLf = abs(_Diff_CpLf)
    _ABSofDiff_CpHf = abs(_Diff_CpHf)
    _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
    _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
    return _KeyValueLong - _KeyValueShort
