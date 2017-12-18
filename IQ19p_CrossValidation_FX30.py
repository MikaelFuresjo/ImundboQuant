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
import numpy as np
import pandas as pd
import time
import random

TrainLocation = r'C:\Users\UserTrader\Documents\ImundboQuant\InstrumentList\IQ19p_FX30\50kFX30sortDate_535ft.xlsx'


trainData = pd.read_excel(TrainLocation)
print(trainData)


#_featureToCheck = "_Date"
#_featureToCheck = "_Diff_CtoL"
#_featureToCheck = "_Diff_CtoH"
#_featureToCheck = "_Low34_L"
#_featureToCheck = "_PastSCH05to34"
#_featureToCheck = "_DiffU34_L3"
_featureToCheck = "_SMA3_C"
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

trainData = trainData.sort(_featureToCheck, ascending=False)
print(trainData)

countX = 0

while (countX < 1000000):
    
    units = 16
    max_feat_Rand = 12
    countX = countX + 1
    time.sleep(1)
    StartTime = time.time()  
    


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
                                '_Diff_CtoL',
                                '_sign5Stoch144',
                                '_PastSCH05to34',
                                '_PastSCH05to13',
                                '_SMA13_C',
                                '_Perc3_H',
                                '_PastSCH08to34',
                                '_DiffD3_C',
                                '_Diff_CtoH',
                                '_PastSCH13to34',
                                '_EvNo60',
                                '_PastSCH08to21',
                                '_Low10_L',
                                '_Low34_L',
                                '_SMA89vs144',
                                '_BBD34',
                                'Diff_RL3_RL13',
                                '_diffStochSign55',
                                '_Diff_CtoC3',
                                '_Low55_L',
                                '_SMA55vs89',
                                '_DiffU3_C',
                                '_Perc34_L20',
                                '_DiffD34_C',
                                'Diff_C_RL5',
                                '_diffStochSign144',
                                '_Diff_CtoO',
                                '_stoch55Level',
                                '_DiffU34_L3',
                                '_BBU13',
                                '_Diff_CtoC6',
                                '_Diff_CtoC1',
                                '_DiffU233_C',
                                '_stoch377',
                                '_EvNo900',
                                '_Perc89_M50',
                                'RL144',
                                '_BBD300',
                                '_STD3sign',
                                '_Perc8_H',
                                'Diff_C_RL3',
                                '_stoch233Level',
                                '_SMA3_C',
                                '_SMA21vs144',
                                '_SMA233vs377',
                                '_Diff_CtoO7',
                                '_Diff_CtoH24',
                                '_Low9_L',
                                '_STD13sign',
                                '_Perc13_H',
                                '_DiffD89_H3',
                                '_Perc377_L',
                                '_DiffU3_L3',
                                '_BBU5',
                                '_SMA13vs144',
                                '_SMA5vs8',
                                '_Perc21_L',
                                '_Diff_CtoH1',
                                '_BBU55',
                                '_stoch233',
                                '_Low8_L',
                                '_DiffU200_C',
                                'Diff_RL8_RL55',
                                '_Low233_L',
                                '_DiffU233_L3',
                                '_Diff_CtoL9',
                                '_DiffD377_H3',
                                'Diff_C_RL13',
                                '_High9_H',
                                '_STD144sign',
                                '_Perc100_L20',
                                'Diff_RL89_RL200',
                                '_PastSCH13to21',
                                '_SMA34vs144',
                                '_STD377_C',
                                '_Perc377_L20',
                                'Diff_RL200_RL233',
                                '_Perc3_H80',
                                '_Perc34_L',
                                'Diff_C_RL89'
                                ],  units))                               
    ####---------------------------------------------------------------------------  
    
        _Horizontxxx = ''.join(random.sample([
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
    
        _Horizont = ''.join(random.sample([
                                        'Tgt_SCH05to08'                                      
                                      ],1))
    
    
   
    
    
        X = np.array(trainData[FEATURES].values) # making a np array from the pd dataset
        y = trainData[_Horizont].values # put in relevant target class
        
      
        _CV = 60 #USE 60 to slit in to seperate 3M periods or 180 to 1M periods
      
        logreg = RandomForestClassifier(n_estimators = n_estimators_Rand,
                                        max_depth = max_depth_Rand,
                                        warm_start='False',
                                        max_features=max_feat_Rand,
                                        min_samples_leaf=min_samples_leaf_Rand,
                                        bootstrap='True',
                                        max_leaf_nodes=max_leaf_nodes_Rand,
                                        min_samples_split=min_samples_split_Rand,
                                        random_state=42,
                                        n_jobs=1)

    except Exception as e:
        print(str(e))
        #pass    
    
    try:        
        from sklearn.model_selection import cross_val_score
        scores = cross_val_score(logreg, X, y, cv=_CV)
        
        _minScore = round(np.amin(scores),6)
        _maxScore = round(np.amax(scores),6)
        _meanScore = round(np.mean(scores),6)
        _stdScore = round(np.std(scores),6)
        _SharpMin = round(_minScore/_stdScore,6)
        _SharpMean = round(_meanScore/_stdScore,6)
        
        EndTime = time.time()
        TotalTime = round((EndTime - StartTime)/60,2)
        
        
        
        print(str(_minScore) + str("   ")+ str(TotalTime))

        _fileNameOfResults = str('IQ19p_')+str(_CV)+str(_featureToCheck)+str('.txt')   # put in path and filename for results       

        appendFile = open(_fileNameOfResults, 'a') # put in path and filename for results
        appendFile.write('\n' + str(_minScore)+

                        str(',Time:,')  +
                        str(TotalTime) + 

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
     
        appendFile.close()
        FEATURES = []
    except Exception as e:
        print(str(e))           
