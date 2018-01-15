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

IMUNDBO QUANT v1.8 (Preprocessing script)
"""

import csv
from datetime import datetime
import glob
import numpy as np
import pandas as pd
import time
import datetime
import matplotlib.pyplot as plt
import os
import sys
import traceback

from config.IQConfig import IQConfig
import feature_sets.Original
import indicators.Custom
import indicators.Date
import indicators.Diff
import indicators.Famous
import indicators.Rolling
from gui.console import Console
from utils.Utils import columnName, applyFeatures


c = Console(
"""  ___
 |  _ \ _ __ ___ _ __  _ __ ___   ___ ___  ___ ___                         
 | |_) | '__/ _ \ '_ \| '__/ _ \ / __/ _ \/ __/ __|                        
 |  __/| | |  __/ |_) | | | (_) | (_|  __/\__ \__ \                        
 |_|   |_|  \___| .__/|_|  \___/ \___\___||___/___/                        
                |_|                                  

 Preprocess ticker data and extract features to use optimizing machine learning system
 Ticker data should be inside "instrumentsFolder", one csv file per ticker.

 Each file is expected to contain comma-separated values:
 ["Date", "Open", "High", "Low", "Close", "Volume", "OI"]

""")



# Settings are kept in config/config.json
#########################################
#  Example config relevant PreProcess:
#  {
#     "root": "c:\\data",
#     "preProcess": {
#       "folder": "PreProcess",
#       "instrumentsFolder": "PreProcess\\Instrument_FX30",
#       "featuresFile": "MASSIVE_IQ19p_535ft.txt"
#     },
#  }


config = IQConfig()
preProcessPath = config.preProcess.getFolder()
instrumentsPath = config.preProcess.getInstrumentsFolder()

featuresOutputPath = os.path.join(preProcessPath, config.preProcess.featuresFileName)
allInstrumentsFeatures = None

instruments = glob.glob(os.path.join(instrumentsPath, "*.txt"))

fileColumns = ["Date", "Open", "High", "Low", "Close", "Volume", "OI"]


numInstruments = len(instruments)

print ('Reading {0} files with ticker data from {1}...'.format(numInstruments, instrumentsPath))

numCompleted = 0
numFailed = 0


#featuresToExtract = indicators.Date.getDateFeatures()
#featuresToExtract.update(indicators.Diff.getDiffFeatures())
#featuresToExtract.update(indicators.Rolling.getRollingFeatures())
#featuresToExtract.update(indicators.Famous.getFamousFeatures())
featuresToExtract = feature_sets.Original.getOriginalFeatureSet()

featureColumnNames = []
for feature, settings in featuresToExtract.items():
    featureColumnNames.append(feature)

print("Features to calculate: {0}".format(featureColumnNames))



for index, instrument in enumerate(instruments):
    instrumentPath = os.path.join(instrumentsPath, instrument)
    instrumentName = os.path.splitext(instrument)[0]

    print("\nProcessing {0} ({1} / {2})...".format(instrumentName, index+1, numInstruments))

    #{
    #    "date": True,
    #    "dayOfWeek": True,
    #    "dayOfMonth": True,
    #    "dayOfYear": True,
    #    "weekOfYear": True,
    #    "monthOfYear": True,
    #    "time": True,
    #    "hour": True,
    #    "minute": True,
    #
    #    #"diffCtoH": range(0, 25+1),  #Idea: Adding all these four maybe duplicates data unneccessarily?
    #    #"diffCtoL": range(0, 25+1),  #      How about only keeping CtoC and use intraday for the others?
    #    #"diffCtoO": range(0, 25+1),  #      Even simple algos should probably be able to combine?
    #    #"diffCtoC": range(1, 25+1),  #      Maybe intraday move n days ago could be interesting as well...
    #
    #    #"EMA": [12, 26], #MACD
    #    #"SMA": [20], #BB
    #    #"STD": [2, 3], #BB
    #    #https://en.wikipedia.org/wiki/Moment_(mathematics)
    #    #https://iknowfirst.com/technical-indicators
    #}


    try:
        data = pd.read_csv(instrumentPath, parse_dates=['Date'], header=None, index_col="Date", names=fileColumns)
        features = pd.DataFrame(columns = featureColumnNames, index = data.index)
        numRows = len(data)

    except Exception as e:
        numFailed+=1
        print("Error processing {0}. Skipping".format(instrument))
        traceback.print_exc()
        continue

    applyFeatures(featuresToExtract, data, features)

    # Benchmark 1 50s for first 2
    # Benchmark 2 22s for first 7
    features = features[featureColumnNames] #remove any extra

    allInstrumentsFeatures = pd.concat([allInstrumentsFeatures, features], ignore_index = True)
    allInstrumentsFeatures.to_csv(featuresOutputPath, ";")
    print("Saved {0}".format(featuresOutputPath))

    ## plot values, rolling mean and Bollinger Bands
    #ax = data['Close'].plot(title="Bollinger Bands", label=instrumentName, figsize=(80, 60))
    #features[columnName("SMA", 200)].plot(label='SMA(20)', ax=ax)
    #features[columnName("BBupper", 20, 2)].plot(label='upper band', ax=ax)
    #features[columnName("BBlower", 20, 2)].plot(label='lower band', ax=ax)
    #
    ## Add labels 
    #ax.legend(loc='lower left')
    #ax.set_xlabel("Date")
    #ax.set_ylabel("Price")
    #plt.savefig(os.path.join(preProcessPath, instrumentName + ".png"))
    #print ("Saved " + os.path.join(preProcessPath, instrumentName + ".png"))
    
    
    c.timer.print_elapsed("Completed processing of {0}".format(instrumentName))

    numCompleted+=1
### END part where to write every Future value and Feature, day by day and intrument by instrument to .txt file to read csv style. 
        
c.timer.print_elapsed('Completed preprocessing {0} files with ticker data ({1} failed) from {2}'.format(numCompleted, numFailed, instrumentPath))
