"""
MIT License

Copyright (c) [2016] [Mikael Furesjö]
Software = Python Scripts in the [Imundbo Quant v1.9] series

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

IMUNDBO QUANT v1.9 (.pkl produciton script)
"""
import numpy as np
import pandas as pd
import time
start = time.time()
### import all learning data from .xlsx file


_pklName = 'FX30_IQ19o'
#########################################
_slotNo = '10'
_Horizont = 'Tgt_SCH05to08'
_TrainingInst = 'LH40_535ft'
_NoFeatures = 10
#########################################



# Import specific list of Features from file for each day
FEATURES = []
readThisFile = r'C:\Users\UserTrader\Documents\ImundboQuant\pklFiles\\'+_pklName+'\\'+_pklName+'_Feat_Slot'+_slotNo+'.txt'
featuresFile = open(readThisFile)
fleraFeatures = featuresFile.read()
FEATURES = fleraFeatures.split('\n')
featuresFile.close()

TrainLocation = r'C:\Users\UserTrader\Documents\ImundboQuant\InstrumentList\IQ19n_FX30\all'+_TrainingInst+'.xlsx'
trainData = pd.read_excel(TrainLocation)


X = np.array(trainData[FEATURES].values) # making a np array from the pd dataset
y = trainData[_Horizont].values # put in relevant target class

from sklearn.ensemble import RandomForestClassifier
RFclf = RandomForestClassifier(min_samples_leaf=50,
                               max_features=_NoFeatures, 
                               max_leaf_nodes=10000,
                               min_samples_split=150,                               
                               max_depth=150,                               
                               n_estimators=150,
                               ##
                               random_state=42,
                               n_jobs=1)
RFclf.fit(X,y)
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl
joblib.dump(RFclf, 'C:\Users\UserTrader\Documents\ImundboQuant\pklFiles\\'+_pklName+'\\'+_pklName+'_Slot'+_slotNo+'.pkl')


######################



stop = time.time()
Total = stop-start
print(Total)
