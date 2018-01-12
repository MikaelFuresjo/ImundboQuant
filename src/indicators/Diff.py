import numpy as np
import pandas as pd
from typing import Callable, Dict

from utils.Utils import columnName

def getDiffFeatures() -> Dict[str, Callable[[pd.DataFrame, pd.DataFrame], None]]:
    """Get diff-based features
       Will add lagging diffs CtoX, normally for 0..25
       returns a dictionary of {columnName: lamda (data, feature): feature }
    """

    diffFeatures = {}

    r = range(0, 25+1)
    diffFeatures.update([columnName("diffCtoH", i), CtoH(i)] for i in r)
    diffFeatures.update([columnName("diffCtoL", i), CtoL(i)] for i in r)
    diffFeatures.update([columnName("diffCtoO", i), CtoO(i)] for i in r)
    r = range(1, 25+1)
    diffFeatures.update([columnName("diffCtoC", i), CtoC(i)] for i in r)
    
    return diffFeatures


def diffGeneric(colFrom: str, colTo: str, period: int) -> Callable[[pd.DataFrame, pd.DataFrame], None]:
    def diffGenericLambda(data: pd.DataFrame, features: pd.DataFrame):
        shiftedTo = data[columnName(colTo + "-", period)] = data[colTo].shift(-period)
        return (data[colFrom]-shiftedTo)/shiftedTo
    return diffGenericLambda


def CtoH(period: int) -> np.array:
    """Calculate Difference Close to High[-period] 
    Will use data rows [row] and [row-period]
    """
    return diffGeneric("Close", "High", period)


def CtoL(period: int) -> np.array:
    """Calculate Difference Close to Low[-period]
    Will use data rows [row] and [row-period]
    """
    return diffGeneric("Close", "Low", period)


def CtoO(period: int):
    """Calculate Difference Close to Open[-period]
    Will use data rows [row] and [row-period]
    """
    return diffGeneric("Close", "Open", period)


def CtoC(period: int):
    """Calculate Difference Close to Close[-period]
    Will use data rows [row] and [row-period]
    """
    return diffGeneric("Close", "Close", period)


