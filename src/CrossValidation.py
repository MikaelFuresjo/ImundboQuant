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

IMUNDBO QUANT v1.9 (Gridsearch script)
"""
from sklearn.ensemble import RandomForestClassifier
import os
import numpy as np
import pandas as pd
import time
import random
import traceback

from config.IQConfig import IQConfig
from gui.console import Console
from metrics.Timer import Timer

c = Console(
"""   ____                                _ _     _       _   _               
  / ___|_ __ ___  ___ ___  __   ____ _| (_) __| | __ _| |_(_) ___  _ __    
 | |   | '__/ _ \/ __/ __| \ \ / / _` | | |/ _` |/ _` | __| |/ _ \| '_ \   
 | |___| | | (_) \__ \__ \  \ V / (_| | | | (_| | (_| | |_| | (_) | | | |  
  \____|_|  \___/|___/___/   \_/ \__,_|_|_|\__,_|\__,_|\__|_|\___/|_| |_|  
""")


config = IQConfig()


TrainLocation = config.crossValidation.getTrainingFilePath()



fileSize = os.path.getsize(TrainLocation) / 1024. / 1024.

print ('Reading {0:.2f}MB of training data from {1}...'.format(fileSize, TrainLocation))


trainData = pd.read_excel(TrainLocation, parse_dates=['_DateStamp'])


print("Dropping rows containing, Inf, -Inf, and NaN...")
trainData.replace([np.inf, -np.inf], np.nan)
trainData.dropNA()

# ============ REMOVE ALL BUT 1000 ROWS TO SPEED UP TESTING
#newNumRows = 10000
#print("REMOVING ALL BUT {} ROWS (from {}) FOR TRAINING!".format(newNumRows, len(trainData)))
#trainData = trainData.head(newNumRows)
# ==== END REMOVE =====

#print(trainData)

c.timer.print_elapsed("Reading of training data complete")

#print ("\nData types of columns (should normally show floats, ints and one date column only):")
#print(trainData.dtypes)

_featureToCheck = "Slump"
#_featureToCheck = "_Date"
#_featureToCheck = "_Diff_CtoL"
#_featureToCheck = "_Diff_CtoH"
#_featureToCheck = "_Low34_L"
#_featureToCheck = "_PastSCH05to34"
#_featureToCheck = "_DiffU34_L3"
#_featureToCheck = "_SMA3_C"
#_featureToCheck = "_SMA89vs144"
#_featureToCheck = "_DiffD34_C"
#_featureToCheck = "_Diff_CtoO"
#_featureToCheck = "_Diff_CtoC3"
#_featureToCheck = "_PastSCH13to34"
#_featureToCheck = "_SMA13_C"
#_featureToCheck = "_Low55_L"
#_featureToCheck = "_Low10_L"
#_featureToCheck = "_sign5Stoch144"
#_featureToCheck = "_PastSCH05to13"
#_featureToCheck = "_diffStochSign144"
#_featureToCheck = "_SMA55vs89"
#_featureToCheck = "_DiffD3_C"
#_featureToCheck = "Diff_RL3_RL13"

_CV = 3 #USE 60 to slit in to seperate 3M periods or 180 to 1M periods
_fileNameOfResults = os.path.join(config.crossValidation.getTrainingFolder(), 'IQ19p_' + str(_CV) + _featureToCheck + '.txt')   # put in path and filename for results       


print("Sorting training data by {0}...".format(_featureToCheck))
trainData = trainData.sort_values(by=[_featureToCheck], ascending=False)
#print(trainData)

c.timer.print_elapsed("Sorting complete")

numIterations = config.crossValidation.numIterations

for countX in range(1, numIterations+1):
    iterationTimer = Timer()

    print("\n\nStarting iteration {0} / {1}".format(countX, numIterations))

    #units = 16
    #max_feat_Rand = 12

    time.sleep(1)
    


####---------------------------------------------------------------------------   
#### This part optimized 2016-10-10
    try: 
        units = random.randrange(17,25,1)
        #unitsHalf = units/2
        min_samples_leaf_Rand = 50 #random.randrange(20, 200, 1)# [100],
        
        #_delare2 = 0.5
        _delare1 = random.randrange(618, 850, 1)
        _delare2 = round(_delare1/1000.0001,8)
        max_feat_Rand = int(round(units * _delare2,0))
        max_leaf_nodes_Rand = 10000 #random.randrange(10000, 12000, 1)# [10000 rätt],
        min_samples_split_Rand = 150 #random.randrange(30, 300, 1)# [150 rätt],
        max_depth_Rand = 50 #random.randrange(30, 300, 1)#[150 rätt]    
        n_estimators_Rand = 50 #random.randrange(100, 250, 1)# [150 rätt]
 
    
        FEATURES = (random.sample([
                                '_STD377_C',
                                '_Diff_CtoL',
                                '_SMA89vs144',
                                '_sign5Stoch144',
                                '_SMA13vs144',
                                '_Diff_CtoC6',
                                '_Low233_L',
                                '_Diff_CtoC1',
                                '_Diff_CtoH',
                                '_PastSCH05to13',
                                '_BBU13',
                                '_DiffU34_L3',
                                '_diffStochSign144',
                                '_stoch55Level',
                                '_SMA21vs144',
                                '_Diff_CtoL9',
                                '_STD13sign',
                                '_DiffU233_L3',
                                '_PastSCH08to21',
                                '_Perc100_L20',
                                '_BBD300',
                                'Diff_RL13_RL100',
                                '_DiffD34_C',
                                '_SMA13_C',
                                '_EvNo60',
                                '_stoch377',
                                '_Perc34_L20',
                                '_stoch233Level',
                                '_Perc3_H80',
                                '_PastSCH13to21',
                                'Diff_C_RL5',
                                '_DiffU3_C',
                                'Diff_RL89_RL200',
                                '_Perc3_H',
                                'Diff_RL89_RL100',
                                '_Diff_CtoH6',
                                '_PastSCH05to34',
                                '_Low9_L',
                                '_DiffD377_H3',
                                'Diff_C_RL3',
                                '_Perc8_H',
                                '_Perc34_L',
                                '_Perc13_H',
                                '_High9_H',
                                '_Perc233_M50',
                                'Diff_RL8_RL55',
                                '_stoch21Level',
                                '_SMA34vs144',
                                'Diff_C_RL89',
                                '_Low55_L',
                                '_stoch377Level',
                                'Diff_C_RL13',
                                'Diff_RL3_RL13',
                                '_BBU55',
                                '_STD8_C',
                                '_High6_H',
                                '_Perc100_H80',
                                '_diffStochSign55',
                                '_High17_H',
                                'Diff_RL200_RL233',
                                '_STD100sign',
                                '_Perc21_L',
                                '_Diff_CtoO',
                                'RL144',
                                '_PastSCH08to34',
                                '_Diff_CtoH24',
                                '_SMA5vs8',
                                '_SMA3_C',
                                '_stoch233',
                                '_SMA21_C',
                                '_EvNo900',
                                '_STD3sign',
                                '_DiffU21_L3',
                                '_Low8_L',
                                '_Low89_L',
                                '_Diff_CtoO7',
                                '_Perc200_M50',
                                '_SMA233vs377',
                                '_Perc377_L20',
                                '_BBD34',
                                '_DiffU200_C',
                                '_DiffD3_C',
                                '_STD144sign',
                                '_Diff_CtoH20',
                                '_DiffD21_H3',
                                '_Low10_L',
                                '_BBU5',
                                'Diff_RL55_RL200',
                                '_High7_H',
                                '_Perc89_M50',
                                '_BBU34',
                                'Diff_RL89_RL144',
                                '_STD5sign',
                                '_PastSCH13to34',
                                '_Diff_CtoH1',
                                '_Perc377_L',
                                '_Diff_CtoL11',
                                'Diff_RL3_RL5',
                                'Diff_C_RL8',
                                '_SMA55vs89',
                                'Diff_RL200_RL377',
                                '_SMA3vs5',
                                '_Low13_L',
                                '_High12_H',
                                '_BBU300',
                                '_DiffU3_L3',
                                '_Low34_L',
                                '_High21_H',
                                '_diffStochSign300',
                                '_stoch8',
                                '_stoch200Level',
                                '_DiffU300_C',
                                '_DiffD89_H3',
                                '_Low15_L',
                                '_EvNo3000',
                                '_BBD3',
                                'RL233',
                                '_DiffD5_C',
                                '_SMA55vs233',
                                '_diffStochSign200',
                                'RL5',
                                'Diff_RL5_RL34',
                                '_STD200sign',
                                '_SMA5vs21',
                                '_Perc8_M50',
                                '_Diff_CtoL5',
                                '_Diff_CtoC3',
                                'Diff_RL55_RL144',
                                '_diffStochSign8',
                                '_Perc100_H',
                                'Diff_RL100_RL200',
                                'Diff_RL5_RL21',
                                '_STD55vsSign',
                                '_Perc3_L',
                                '_DiffD89_C',
                                '_STD5vsSign',
                                '_STD300_C',
                                'Diff_C_RL233',
                                '_DiffD144_H3',
                                '_STD21vsSign',
                                '_SMA3vs8',
                                '_Perc55_M50',
                                'RL13',
                                '_Perc55_H'
                                ],  units))                               
    ####---------------------------------------------------------------------------  
    
        _Horizont = ''.join(random.sample([
                                        'Tgt_SCH05to08',
                                        'Tgt_SCH05to13',
                                        'Tgt_SCH05to21',
                                        'Tgt_SCH05to34',
                                        'Tgt_SCH08to13',
                                        'Tgt_SCH08to21',
                                        'Tgt_SCH08to34',
                                        'Tgt_SCH13to21',
                                        'Tgt_SCH13to34',
                                        'Tgt_SCH21to34'
                                      ],1))
    
        _Horizontxxx = ''.join(random.sample([
                                        'Tgt_SCH05to08'                                      
                                      ],1))
    
    
   
    
    
        X = np.array(trainData[FEATURES].values) # making a np array from the pd dataset
        y = trainData[_Horizont].values # put in relevant target class
        
      
      
        logreg = RandomForestClassifier(n_estimators = n_estimators_Rand,
                                        max_depth = max_depth_Rand,
                                        warm_start='False',
                                        max_features=max_feat_Rand,
                                        min_samples_leaf=min_samples_leaf_Rand,
                                        bootstrap='True',
                                        max_leaf_nodes=max_leaf_nodes_Rand,
                                        min_samples_split=min_samples_split_Rand,
                                        random_state=42,
                                        n_jobs=-1)

    except Exception as e:
        print("Error setting up initial RandomForestClassifier")
        traceback.print_exc()

        #pass    
    
    try:        
        from sklearn.model_selection import cross_val_score
        scores = cross_val_score(logreg, X, y, cv=_CV)
        
        #print(scores)

        _minScore = round(np.amin(scores),6)
        _maxScore = round(np.amax(scores),6)
        _meanScore = round(np.mean(scores),6)
        _stdScore = round(np.std(scores),6)
        _SharpMin = round(_minScore/_stdScore,6)
        _SharpMean = round(_meanScore/_stdScore,6)
        
        
        c.timer.print_elapsed("Min score {0}".format(_minScore))


        appendFile = open(_fileNameOfResults, 'a') # put in path and filename for results
        appendFile.write('\n' + str(_minScore)+

                        str(',Time:,')  +
                        str(iterationTimer.elapsed()) + 

                        str(',CV:,')  +
                        str(_CV) + 
                        
                        str(',Sort:,')  +
                        str(_featureToCheck) + 
                        
                        str(',_maxScore:,')  +
                        str(_maxScore) +    

                        str(',_meanScore:,')  +
                        str(_meanScore) +    

                        str(',_stdScore:,')  +
                        str(_stdScore) +    

                        str(',_SharpMin:,')  +
                        str(_SharpMin) +                            

                        str(',_SharpMean:,')  +
                        str(_SharpMean) +    

                        str(',_Target:,')  +
                        str(_Horizont) +    
    
                        str(',No Features:,')  +
                        str(units) +
                        str(',Min Leaf:,')  +
                        str(min_samples_leaf_Rand) +   
                        str(',Max Feat:,')  +
                        str(max_feat_Rand ) +    
                        str(',Leafs Nodes:,')  +
                        str(max_leaf_nodes_Rand) +
                        str(',Sample Split:,')  +
                        str(min_samples_split_Rand) +
                        str(',Depth of the tree:,')  +
                        str(max_depth_Rand) +
                        str(',No of trees:,') + 
                        str(n_estimators_Rand) +                     
                        str(',Features: ,') + 
                        str(FEATURES))
     
        print("Appended row to {0}".format(_fileNameOfResults))
        appendFile.close()
        FEATURES = []
    except Exception as e:
        print("Error during iteration {0}".format(countX))
        traceback.print_exc()

    iterationTimer.print_elapsed("Completed iteration {0}".format(countX), False)

    c.timer.print_elapsed("Total elapsed")

print("\n\n =================================")
c.timer.print_elapsed("\n\nCompleted processing after {0} iterations".format(numIterations))

print("Min score:     {0:.4f}".format(_minScore))
print("CV:            {0:.4f}".format(_CV))
print("Sort:          {0}".format(_featureToCheck))
print("Max score:     {0:.4f}".format(_meanScore))
print("Std score:     {0:.4f}".format(_stdScore))
print("Sharp min:     {0:.4f}".format(_SharpMin))
print("Sharp mean:    {0:.4f}".format(_SharpMean))
print("Num feats:     {0}".format(units))
print("Min leaf:      {0}".format(min_samples_leaf_Rand))
print("Max feat:      {0}".format(max_feat_Rand))
print("Leaf nodes:    {0}".format(max_leaf_nodes_Rand))
print("Depth of tree: {0}".format(max_depth_Rand))
print("Num trees:     {0}".format(n_estimators_Rand))
