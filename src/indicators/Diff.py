import numpy as np
import pandas as pd
from typing import Callable, Dict

from utils.CustomTypes import TColumnName, TFeatureLambda, TFeatureLambdasDict
from utils.Utils import columnName

def getDiffFeatures() -> Dict[str, Callable[[pd.DataFrame, pd.DataFrame], None]]:
    """Get diff-based features
       Will add lagging diffs CtoX, normally for 0..25
       returns a dictionary of {columnName: lamda (data, feature): feature }
    """

    diffFeatures = {}

    
    return diffFeatures


def diffGeneric(colFrom: str, colTo: str, period: int) -> Callable[[pd.DataFrame, pd.DataFrame], None]:
    def diffGenericLambda(data: pd.DataFrame, features: pd.DataFrame):
        shiftedTo = data[columnName(colTo + "-", period)] = data[colTo].shift(-period)
        return (data[colFrom]-shiftedTo)/shiftedTo
    return diffGenericLambda


def CtoH(period: int) -> TFeatureLambdasDict:
    """Calculate Difference Close to High[-period] 
    Will use data rows [row] and [row-period]
    """
    return {columnName("diffCtoH", period): diffGeneric("Close", "High", period)}


def CtoL(period: int) -> TFeatureLambdasDict:
    """Calculate Difference Close to Low[-period]
    Will use data rows [row] and [row-period]
    """
    return {columnName("diffCtoL", period): diffGeneric("Close", "Low", period)}


def CtoO(period: int) -> TFeatureLambdasDict:
    """Calculate Difference Close to Open[-period]
    Will use data rows [row] and [row-period]
    """
    return {columnName("diffCtoO", period): diffGeneric("Close", "Open", period)}


def CtoC(period: int) -> TFeatureLambdasDict:
    """Calculate Difference Close to Close[-period]
    Will use data rows [row] and [row-period]
    """
    return {columnName("diffCtoH", period): diffGeneric("Close", "Close", period)}


