import numpy as np
import pandas as pd
from typing import Callable, Dict

from indicators import Custom, Date, Diff, Rolling

from utils.CustomTypes import TColumnName, TFeatureLambda, TFeatureLambdasDict
from utils.Utils import columnName

def getStrategy() -> TFeatureLambdasDict:
    """Get average daily gain of +1 to +5 days
       returns TFeatureLambdasDict
    """


    def avgDaily5(column: str = "Close"):
        """Calculate simple moving average (SMA)
        Will use data rows [row-period:row]
        """
        def avgDaily5Lambda(data: pd.DataFrame, features: pd.DataFrame):
            return (
                (data[column].shift(1) - data[column])
              + (data[column].shift(2) - data[column]) / 2.
              + (data[column].shift(3) - data[column]) / 3.
              + (data[column].shift(4) - data[column]) / 4.
              + (data[column].shift(5) - data[column]) / 5.
            ) / 5
        return {columnName("targetAvgDaily5", 5): avgDaily5Lambda}

    features: TFeatureLambdasDict = {}

    features.update(avgDaily5())

    return features

