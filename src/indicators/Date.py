import numpy as np
import pandas as pd

def diffCtoH(data: pd.DataFrame, row: int, period: int):
    """Calculate Difference Close to High[-period] for selected period of given ticker data DataFrame 
    Will use data rows [row] and [row-period]
    """
    return (data["Close"][row]-data["High"][row-period])/data["High"][row-period]

def diffCtoL(data: pd.DataFrame, row: int, period: int):
    """Calculate Difference Close to Low[-period] for selected period of given ticker data DataFrame 
    Will use data rows [row] and [row-period]
    """
    return (data["Close"][row]-data["Low"][row-period])/data["Low"][row-period]

def diffCtoO(data: pd.DataFrame, row: int, period: int):
    """Calculate Difference Close to Open[-period] for selected period of given ticker data DataFrame 
    Will use data rows [row] and [row-period]
    """
    return (data["Close"][row]-data["Open"][row-period])/data["Open"][row-period]

def diffCtoC(data: pd.DataFrame, row: int, period: int):
    """Calculate Difference Close to Close[-period] for selected period of given ticker data DataFrame 
    Will use data rows [row] and [row-period]
    """
    return (data["Close"][row]-data["Close"][row-period])/data["Close"][row-period]

