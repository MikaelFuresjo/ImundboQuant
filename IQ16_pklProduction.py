"""
MIT License

Copyright (c) [2016] [Mikael Furesjö]
Software = Python Scripts in the [Imundbo Quant v1.6] series

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

IMUNDBO QUANT v1.6 (.pkl produciton script)
"""


import numpy as np
import pandas as pd
import time

### import FEATURES from .txt file
FEATURES = []
readThisFile = r'C:\Users\UserTrader\Documents\FEATURES03.txt'
featuresFile = open(readThisFile)
fleraFeatures = featuresFile.read()
FEATURES = fleraFeatures.split('\n')
featuresFile.close()

start = time.time()

### import all learning data from .xlsx file
Locatation = r'C:\Users\UserTrader\Documents\IQ14_testmatris_2stdav_5classifiersROC_ALL.xlsx'
data = pd.read_excel(Locatation)
X = np.array(data[FEATURES].values) # making a np array from the pd dataset

### START - Using part from targets who calculate how Big the future move was, Rate of Change (ROC)
######################
y = data['_end1'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat1dROC.pkl')
######################
y = data['_end2'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat2dROC.pkl')
######################
y = data['_end3'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat3dROC.pkl')
######################
y = data['_end5'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat5dROC.pkl')
######################
y = data['_end8'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat8dROC.pkl')
######################
y = data['_end13'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat13dROC.pkl')
######################
y = data['_end21'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat21dROC.pkl')
######################

### END - Using part from targets who calculate how Big the future move was, Rate of Change (ROC)
###------------------------------------------------------
### START - Using part from targets who calculate how high the Risk/Reward Ratio was for future move 

######################
y = data['_TARGET1'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat1d.pkl')
######################
y = data['_TARGET2'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat2d.pkl')
######################
y = data['_TARGET3'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat3d.pkl')
######################
y = data['_TARGET5'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat5d.pkl')
######################
y = data['_TARGET8'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat8d.pkl')
######################
y = data['_TARGET13'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat13d.pkl')
######################
y = data['_TARGET21'].values
from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(n_estimators=198,
                               max_leaf_nodes=365,
                               min_samples_leaf=365,
                               min_samples_split=76,
                               verbose=20,
                               max_depth=52,
                               n_jobs=2)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat21d.pkl')
######################

### END - Using part from targets who calculate how high the Risk/Reward Ratio was for future move 

stop = time.time()
Total = stop-start
print(Total)
