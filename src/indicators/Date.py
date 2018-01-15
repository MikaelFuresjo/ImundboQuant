import numpy as np
import pandas as pd
from typing import Callable, Dict

from utils.CustomTypes import TColumnName, TFeatureLambda, TFeatureLambdasDict
from utils.Utils import columnName


def getDateFeatures() -> TFeatureLambdasDict:
    """Get date-based features
       returns a dictionary of {columnName: lamda (data, feature): feature }
    """

    return {
        "Date": lambda data, features: data.index.date,
        "Date": lambda data, features: data.index.date,
        "DayOfWeek": lambda data, features: data.index.dayofweek,
        "DayOfMonth": lambda data, features: data.index.day,
        "DayOfYear": lambda data, features: data.index.dayofyear,
        "WeekOfYear": lambda data, features: data.index.weekofyear,
        "MonthOfYear": lambda data, features: data.index.month
    }

def getTimeFeatures() -> TFeatureLambdasDict:
    """Get time-based features
       returns a dictionary of {columnName: lamda (data, feature): feature }
    """

    return {
        "Time": lambda data, features: data.index.time,
        "Hour": lambda data, features: data.index.hour,
        "Minute": lambda data, features: data.index.minute
    }
