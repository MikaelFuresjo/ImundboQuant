import pandas as pd
from typing import Callable, Dict, NewType

TColumnName = NewType("ColumnName", str)
TFeatureLambda = NewType("TFeatureLambda", Callable[[pd.DataFrame, pd.DataFrame], None])
TFeatureLambdasDict = NewType("TFeatureLambdasDict", Dict[TColumnName, TFeatureLambda])
