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

import numpy as np
import pandas as pd
import time
import datetime
import os
import csv
from datetime import datetime
import sys
from matplotlib.dates import date2num

from config.IQConfig import IQConfig
from gui.console import Console

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

instruments = os.listdir(instrumentsPath)
numInstruments = len(instruments)

print ('Reading {0} files with ticker data from {1}...'.format(numInstruments, instrumentsPath))

_justOpen = 0.0
_justHigh = 0.0
_justLow = 0.0
_justClose = 0.0
instrument = 0.0
_DateStamp = 0.0
_Return01 = 0.0
Tgt_SCH05to08 = 0.0
Tgt_SCH05to13 = 0.0
Tgt_SCH05to21 = 0.0
Tgt_SCH05to34 = 0.0
Tgt_SCH08to13 = 0.0
Tgt_SCH08to21 = 0.0
Tgt_SCH08to34 = 0.0
Tgt_SCH13to21 = 0.0
Tgt_SCH13to34 = 0.0
Tgt_SCH21to34 = 0.0
_Diff_CtoH14 = 0.0
_Diff_CtoL20 = 0.0
_Perc21_H = 0.0
_Perc21_H80 = 0.0
_EvNo5000 = 0.0
_SMA89vs377 = 0.0
_SMA_L3 = 0.0
_Diff_CtoH5 = 0.0
_Low8_L = 0.0
_Perc8_M50 = 0.0
_diffStochSign34 = 0.0
_SMA8_C = 0.0
_DiffD100_H3 = 0.0
_SMA3vs8 = 0.0
Diff_RL8_RL21 = 0.0
_SMA13_C = 0.0
_Perc200_H = 0.0
_Perc21_L = 0.0
_Diff_CtoC8 = 0.0
_BBU200 = 0.0
_Perc8_H80 = 0.0
_EvNo1000 = 0.0
_DiffU8_C = 0.0
_Perc5_H = 0.0
_Perc89_H = 0.0
_EvNo300 = 0.0
_Diff_CtoH19 = 0.0
_Perc233_H80 = 0.0
_BBU377 = 0.0
_DiffD89_C = 0.0
_Diff_CtoH8 = 0.0
_DiffD34_C = 0.0
_Diff_CtoH17 = 0.0
_diffStochSign377 = 0.0
_Perc55_M50 = 0.0
Diff_RL5_RL21 = 0.0
_SMA34_C = 0.0
_diffStochSign100 = 0.0
_STD21sign = 0.0
_stoch377Level = 0.0
_diffStochSign21 = 0.0
_diffStochSign55 = 0.0
_Diff_CtoH21 = 0.0
_Perc3_M50 = 0.0
_Diff_CtoH6 = 0.0
_Diff_CtoL9 = 0.0
_BBU300 = 0.0
_STD377vsSign = 0.0
_diffStochSign8 = 0.0
_stoch300Level = 0.0
_Diff_CtoH2 = 0.0
_Perc5_M50 = 0.0
_Low89_L = 0.0
_SMA3vs34 = 0.0


numCompleted = 0
numFailed = 0

for index, instrument in enumerate(instruments):
    instrumentPath = os.path.join(instrumentsPath, instrument)
    instrumentName = os.path.splitext(instrument)[0]
    #Date, Open, High, Low, Close, Volume, OI = np.loadtxt(instrumentPath, delimiter=',', unpack=True,converters={ 0: bytespdate2num('%Y-%m-%d')})
    
    print("\nProcessing {0} ({1} / {2})...".format(instrumentName, index+1, numInstruments))


    try:
        data = pd.read_csv(instrumentPath, parse_dates=['Date'], header=None, names=["Date", "Open", "High", "Low", "Close", "Volume", "OI"])
        Date, Open, High, Low, Close, Volume, OI = data.values.T
        #Date = date2num(Date) #Todo: Remove this and keep native Datetime
    except Exception as e:
        numFailed+=1
        print("Error processing {0}: {1}. Skipping".format(instrument, e))
        continue

    Zeros = [1]*len(Date) #making extra data array with "1" for future calculation of MA with linear regression
    numDates = len(Date) 
    
    print("Iterating {0} rows, using range [400:-35]".format(numDates))

    # skip the last 35 days for making space for P/L calculation for at most 34 days
    # skip the last 400 days for making space to calculate indicatiors that need 377 past days
    for x in range(400, numDates-35): 

        
### START First part -  calculate on how high the Risk/Reward Ratio is for future move in 1,2,3,5,8,13,21 days 
        try:
            # Without splitting columns (... = data.values.T above) we could iterate actual rows in the pandas dataframe and use for example row["Date"] instead
            dt = Date[x]
            _DateStamp = dt.strftime('%Y-%m-%d')
            _dateYear = float(dt.year) #Why float?
            _dateMonthOfYear = float(dt.month) #Why float?
        
            if _dateYear > 1966 and (_dateMonthOfYear >0 or _dateMonthOfYear >0 or _dateMonthOfYear >0 ):
                try:            
                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+6])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+6])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_05 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass
                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+7])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+7])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_06 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass


                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+8])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+8])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_07 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+9])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+9])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_08 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+10])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+10])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_09 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+11])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+11])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_10 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+12])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+12])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_11 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+13])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+13])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_12 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass
    
                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+14])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+14])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_13 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+15])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+15])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_14 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+16])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+16])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_15 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+17])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+17])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_16 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+18])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+18])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_17 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+19])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+19])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_18 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+20])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+20])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_19 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+21])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+21])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_20 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass
    
                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+22])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+22])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_21 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+23])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+23])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_22 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+24])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+24])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_23 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+25])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+25])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_24 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+26])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+26])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_25 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+27])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+27])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_26 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+28])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+28])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_27 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+29])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+29])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_28 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+30])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+30])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_29 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+31])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+31])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_30 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+32])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+32])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_31 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+33])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+33])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_32 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+34])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+34])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_33 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass
    
                    try:            
                        _Diff_CpLf = (np.amin(Low[x:x+35])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x:x+35])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _MiniSharp_34 = np.round(_KeyValueLong - _KeyValueShort,6)
     
                    except Exception as e:
                        pass


                    _MiniSCH05to08 = (
                                        _MiniSharp_05 +
                                        _MiniSharp_06 +
                                        _MiniSharp_07 +
                                        _MiniSharp_08
                                        )/4

                    _MiniSCH05to13 = (
                                        _MiniSharp_05 +
                                        _MiniSharp_06 +
                                        _MiniSharp_07 +
                                        _MiniSharp_08 +
                                        _MiniSharp_09 +
                                        _MiniSharp_10 +
                                        _MiniSharp_11 +
                                        _MiniSharp_12 +
                                        _MiniSharp_13
                                        )/9

                    _MiniSCH05to21 = (
                                        _MiniSharp_05 +
                                        _MiniSharp_06 +
                                        _MiniSharp_07 +
                                        _MiniSharp_08 +
                                        _MiniSharp_09 +
                                        _MiniSharp_10 +
                                        _MiniSharp_11 +
                                        _MiniSharp_12 +
                                        _MiniSharp_13 +
                                        _MiniSharp_14 +
                                        _MiniSharp_15 +
                                        _MiniSharp_16 +
                                        _MiniSharp_17 +
                                        _MiniSharp_18 +
                                        _MiniSharp_19 +
                                        _MiniSharp_20 +
                                        _MiniSharp_21
                                        )/17

                    _MiniSCH05to34 = (
                                        _MiniSharp_05 +
                                        _MiniSharp_06 +
                                        _MiniSharp_07 +
                                        _MiniSharp_08 +
                                        _MiniSharp_09 +
                                        _MiniSharp_10 +
                                        _MiniSharp_11 +
                                        _MiniSharp_12 +
                                        _MiniSharp_13 +
                                        _MiniSharp_14 +
                                        _MiniSharp_15 +
                                        _MiniSharp_16 +
                                        _MiniSharp_17 +
                                        _MiniSharp_18 +
                                        _MiniSharp_19 +
                                        _MiniSharp_20 +
                                        _MiniSharp_21 +
                                        _MiniSharp_22 +
                                        _MiniSharp_23 +
                                        _MiniSharp_24 +
                                        _MiniSharp_25 +
                                        _MiniSharp_26 +
                                        _MiniSharp_27 +
                                        _MiniSharp_28 +
                                        _MiniSharp_29 +
                                        _MiniSharp_30 +
                                        _MiniSharp_31 +
                                        _MiniSharp_32 +
                                        _MiniSharp_33 +
                                        _MiniSharp_34
                                        )/30

                    _MiniSCH08to13 = (
                                        _MiniSharp_08 +
                                        _MiniSharp_09 +
                                        _MiniSharp_10 +
                                        _MiniSharp_11 +
                                        _MiniSharp_12 +
                                        _MiniSharp_13
                                        )/6


                    _MiniSCH08to21 = (
                                        _MiniSharp_08 +
                                        _MiniSharp_09 +
                                        _MiniSharp_10 +
                                        _MiniSharp_11 +
                                        _MiniSharp_12 +
                                        _MiniSharp_13 +
                                        _MiniSharp_14 +
                                        _MiniSharp_15 +
                                        _MiniSharp_16 +
                                        _MiniSharp_17 +
                                        _MiniSharp_18 +
                                        _MiniSharp_19 +
                                        _MiniSharp_20 +
                                        _MiniSharp_21
                                        )/14


                    _MiniSCH08to34 = (
                                        _MiniSharp_08 +
                                        _MiniSharp_09 +
                                        _MiniSharp_10 +
                                        _MiniSharp_11 +
                                        _MiniSharp_12 +
                                        _MiniSharp_13 +
                                        _MiniSharp_14 +
                                        _MiniSharp_15 +
                                        _MiniSharp_16 +
                                        _MiniSharp_17 +
                                        _MiniSharp_18 +
                                        _MiniSharp_19 +
                                        _MiniSharp_20 +
                                        _MiniSharp_21 +
                                        _MiniSharp_22 +
                                        _MiniSharp_23 +
                                        _MiniSharp_24 +
                                        _MiniSharp_25 +
                                        _MiniSharp_26 +
                                        _MiniSharp_27 +
                                        _MiniSharp_28 +
                                        _MiniSharp_29 +
                                        _MiniSharp_30 +
                                        _MiniSharp_31 +
                                        _MiniSharp_32 +
                                        _MiniSharp_33 +
                                        _MiniSharp_34
                                        )/27

                    _MiniSCH13to21 = (
                                        _MiniSharp_13 +
                                        _MiniSharp_14 +
                                        _MiniSharp_15 +
                                        _MiniSharp_16 +
                                        _MiniSharp_17 +
                                        _MiniSharp_18 +
                                        _MiniSharp_19 +
                                        _MiniSharp_20 +
                                        _MiniSharp_21
                                        )/9


                    _MiniSCH13to34 = (
                                        _MiniSharp_13 +
                                        _MiniSharp_14 +
                                        _MiniSharp_15 +
                                        _MiniSharp_16 +
                                        _MiniSharp_17 +
                                        _MiniSharp_18 +
                                        _MiniSharp_19 +
                                        _MiniSharp_20 +
                                        _MiniSharp_21 +
                                        _MiniSharp_22 +
                                        _MiniSharp_23 +
                                        _MiniSharp_24 +
                                        _MiniSharp_25 +
                                        _MiniSharp_26 +
                                        _MiniSharp_27 +
                                        _MiniSharp_28 +
                                        _MiniSharp_29 +
                                        _MiniSharp_30 +
                                        _MiniSharp_31 +
                                        _MiniSharp_32 +
                                        _MiniSharp_33 +
                                        _MiniSharp_34
                                        )/22

                    _MiniSCH21to34 = (
                                        _MiniSharp_21 +
                                        _MiniSharp_22 +
                                        _MiniSharp_23 +
                                        _MiniSharp_24 +
                                        _MiniSharp_25 +
                                        _MiniSharp_26 +
                                        _MiniSharp_27 +
                                        _MiniSharp_28 +
                                        _MiniSharp_29 +
                                        _MiniSharp_30 +
                                        _MiniSharp_31 +
                                        _MiniSharp_32 +
                                        _MiniSharp_33 +
                                        _MiniSharp_34
                                        )/14
                                    
        ####################################################

                    SCH_Dxxp5 = 0.7851
                    SCH_Dxxn5 = -0.7787
                    SCH_Dxxp4 = 0.6403
                    SCH_Dxxn4 = -0.6315
                    SCH_Dxxp3 = 0.4821
                    SCH_Dxxn3 = -0.4707
                    SCH_Dxxp2 = 0.3042
                    SCH_Dxxn2 = -0.2913
                    SCH_Dxxp1 = 0.1081
                    SCH_Dxxn1 = -0.0950

    
                    if _MiniSCH05to08 >  SCH_Dxxp5:###
                        Tgt_SCH05to08 = 5
                    elif _MiniSCH05to08 < SCH_Dxxn5:
                        Tgt_SCH05to08 = -5
                    elif _MiniSCH05to08 > SCH_Dxxp4:###
                        Tgt_SCH05to08 = 4
                    elif _MiniSCH05to08 < SCH_Dxxn4:
                        Tgt_SCH05to08 = -4
                    elif _MiniSCH05to08 > SCH_Dxxp3:###
                        Tgt_SCH05to08 = 3
                    elif _MiniSCH05to08 < SCH_Dxxn3:
                        Tgt_SCH05to08 = -3
                    elif _MiniSCH05to08 > SCH_Dxxp2:###
                        Tgt_SCH05to08 = 2
                    elif _MiniSCH05to08 < SCH_Dxxn2:
                        Tgt_SCH05to08 = -2       
                    elif _MiniSCH05to08 > SCH_Dxxp1:###
                        Tgt_SCH05to08 = 1
                    elif _MiniSCH05to08 < SCH_Dxxn1:
                        Tgt_SCH05to08 = -1                      
                    else:
                        Tgt_SCH05to08 = 0


                    if _MiniSCH05to13 >  SCH_Dxxp5:###
                        Tgt_SCH05to13 = 5
                    elif _MiniSCH05to13 < SCH_Dxxn5:
                        Tgt_SCH05to13 = -5
                    elif _MiniSCH05to13 > SCH_Dxxp4:###
                        Tgt_SCH05to13 = 4
                    elif _MiniSCH05to13 < SCH_Dxxn4:
                        Tgt_SCH05to13 = -4
                    elif _MiniSCH05to13 > SCH_Dxxp3:###
                        Tgt_SCH05to13 = 3
                    elif _MiniSCH05to13 < SCH_Dxxn3:
                        Tgt_SCH05to13 = -3
                    elif _MiniSCH05to13 > SCH_Dxxp2:###
                        Tgt_SCH05to13 = 2
                    elif _MiniSCH05to13 < SCH_Dxxn2:
                        Tgt_SCH05to13 = -2       
                    elif _MiniSCH05to13 > SCH_Dxxp1:###
                        Tgt_SCH05to13 = 1
                    elif _MiniSCH05to13 < SCH_Dxxn1:
                        Tgt_SCH05to13 = -1                      
                    else:
                        Tgt_SCH05to13 = 0

                    if _MiniSCH05to21 >  SCH_Dxxp5:###
                        Tgt_SCH05to21 = 5
                    elif _MiniSCH05to21 < SCH_Dxxn5:
                        Tgt_SCH05to21 = -5
                    elif _MiniSCH05to21 > SCH_Dxxp4:###
                        Tgt_SCH05to21 = 4
                    elif _MiniSCH05to21 < SCH_Dxxn4:
                        Tgt_SCH05to21 = -4
                    elif _MiniSCH05to21 > SCH_Dxxp3:###
                        Tgt_SCH05to21 = 3
                    elif _MiniSCH05to21 < SCH_Dxxn3:
                        Tgt_SCH05to21 = -3
                    elif _MiniSCH05to21 > SCH_Dxxp2:###
                        Tgt_SCH05to21 = 2
                    elif _MiniSCH05to21 < SCH_Dxxn2:
                        Tgt_SCH05to21 = -2       
                    elif _MiniSCH05to21 > SCH_Dxxp1:###
                        Tgt_SCH05to21 = 1
                    elif _MiniSCH05to21 < SCH_Dxxn1:
                        Tgt_SCH05to21 = -1                      
                    else:
                        Tgt_SCH05to21 = 0

                    if _MiniSCH05to34 >  SCH_Dxxp5:###
                        Tgt_SCH05to34 = 5
                    elif _MiniSCH05to34 < SCH_Dxxn5:
                        Tgt_SCH05to34 = -5
                    elif _MiniSCH05to34 > SCH_Dxxp4:###
                        Tgt_SCH05to34 = 4
                    elif _MiniSCH05to34 < SCH_Dxxn4:
                        Tgt_SCH05to34 = -4
                    elif _MiniSCH05to34 > SCH_Dxxp3:###
                        Tgt_SCH05to34 = 3
                    elif _MiniSCH05to34 < SCH_Dxxn3:
                        Tgt_SCH05to34 = -3
                    elif _MiniSCH05to34 > SCH_Dxxp2:###
                        Tgt_SCH05to34 = 2
                    elif _MiniSCH05to34 < SCH_Dxxn2:
                        Tgt_SCH05to34 = -2       
                    elif _MiniSCH05to34 > SCH_Dxxp1:###
                        Tgt_SCH05to34 = 1
                    elif _MiniSCH05to34 < SCH_Dxxn1:
                        Tgt_SCH05to34 = -1                      
                    else:
                        Tgt_SCH05to34 = 0

                    if _MiniSCH08to13 >  SCH_Dxxp5:###
                        Tgt_SCH08to13 = 5
                    elif _MiniSCH08to13 < SCH_Dxxn5:
                        Tgt_SCH08to13 = -5
                    elif _MiniSCH08to13 > SCH_Dxxp4:###
                        Tgt_SCH08to13 = 4
                    elif _MiniSCH08to13 < SCH_Dxxn4:
                        Tgt_SCH08to13 = -4
                    elif _MiniSCH08to13 > SCH_Dxxp3:###
                        Tgt_SCH08to13 = 3
                    elif _MiniSCH08to13 < SCH_Dxxn3:
                        Tgt_SCH08to13 = -3
                    elif _MiniSCH08to13 > SCH_Dxxp2:###
                        Tgt_SCH08to13 = 2
                    elif _MiniSCH08to13 < SCH_Dxxn2:
                        Tgt_SCH08to13 = -2       
                    elif _MiniSCH08to13 > SCH_Dxxp1:###
                        Tgt_SCH08to13 = 1
                    elif _MiniSCH08to13 < SCH_Dxxn1:
                        Tgt_SCH08to13 = -1                      
                    else:
                        Tgt_SCH08to13 = 0

                    if _MiniSCH08to21 >  SCH_Dxxp5:###
                        Tgt_SCH08to21 = 5
                    elif _MiniSCH08to21 < SCH_Dxxn5:
                        Tgt_SCH08to21 = -5
                    elif _MiniSCH08to21 > SCH_Dxxp4:###
                        Tgt_SCH08to21 = 4
                    elif _MiniSCH08to21 < SCH_Dxxn4:
                        Tgt_SCH08to21 = -4
                    elif _MiniSCH08to21 > SCH_Dxxp3:###
                        Tgt_SCH08to21 = 3
                    elif _MiniSCH08to21 < SCH_Dxxn3:
                        Tgt_SCH08to21 = -3
                    elif _MiniSCH08to21 > SCH_Dxxp2:###
                        Tgt_SCH08to21 = 2
                    elif _MiniSCH08to21 < SCH_Dxxn2:
                        Tgt_SCH08to21 = -2       
                    elif _MiniSCH08to21 > SCH_Dxxp1:###
                        Tgt_SCH08to21 = 1
                    elif _MiniSCH08to21 < SCH_Dxxn1:
                        Tgt_SCH08to21 = -1                      
                    else:
                        Tgt_SCH08to21 = 0

                    if _MiniSCH08to34 >  SCH_Dxxp5:###
                        Tgt_SCH08to34 = 5
                    elif _MiniSCH08to34 < SCH_Dxxn5:
                        Tgt_SCH08to34 = -5
                    elif _MiniSCH08to34 > SCH_Dxxp4:###
                        Tgt_SCH08to34 = 4
                    elif _MiniSCH08to34 < SCH_Dxxn4:
                        Tgt_SCH08to34 = -4
                    elif _MiniSCH08to34 > SCH_Dxxp3:###
                        Tgt_SCH08to34 = 3
                    elif _MiniSCH08to34 < SCH_Dxxn3:
                        Tgt_SCH08to34 = -3
                    elif _MiniSCH08to34 > SCH_Dxxp2:###
                        Tgt_SCH08to34 = 2
                    elif _MiniSCH08to34 < SCH_Dxxn2:
                        Tgt_SCH08to34 = -2       
                    elif _MiniSCH08to34 > SCH_Dxxp1:###
                        Tgt_SCH08to34 = 1
                    elif _MiniSCH08to34 < SCH_Dxxn1:
                        Tgt_SCH08to34 = -1                      
                    else:
                        Tgt_SCH08to34 = 0

                    if _MiniSCH13to21 >  SCH_Dxxp5:###
                        Tgt_SCH13to21 = 5
                    elif _MiniSCH13to21 < SCH_Dxxn5:
                        Tgt_SCH13to21 = -5
                    elif _MiniSCH13to21 > SCH_Dxxp4:###
                        Tgt_SCH13to21 = 4
                    elif _MiniSCH13to21 < SCH_Dxxn4:
                        Tgt_SCH13to21 = -4
                    elif _MiniSCH13to21 > SCH_Dxxp3:###
                        Tgt_SCH13to21 = 3
                    elif _MiniSCH13to21 < SCH_Dxxn3:
                        Tgt_SCH13to21 = -3
                    elif _MiniSCH13to21 > SCH_Dxxp2:###
                        Tgt_SCH13to21 = 2
                    elif _MiniSCH13to21 < SCH_Dxxn2:
                        Tgt_SCH13to21 = -2       
                    elif _MiniSCH13to21 > SCH_Dxxp1:###
                        Tgt_SCH13to21 = 1
                    elif _MiniSCH13to21 < SCH_Dxxn1:
                        Tgt_SCH13to21 = -1                      
                    else:
                        Tgt_SCH13to21 = 0

                    if _MiniSCH13to34 >  SCH_Dxxp5:###
                        Tgt_SCH13to34 = 5
                    elif _MiniSCH13to34 < SCH_Dxxn5:
                        Tgt_SCH13to34 = -5
                    elif _MiniSCH13to34 > SCH_Dxxp4:###
                        Tgt_SCH13to34 = 4
                    elif _MiniSCH13to34 < SCH_Dxxn4:
                        Tgt_SCH13to34 = -4
                    elif _MiniSCH13to34 > SCH_Dxxp3:###
                        Tgt_SCH13to34 = 3
                    elif _MiniSCH13to34 < SCH_Dxxn3:
                        Tgt_SCH13to34 = -3
                    elif _MiniSCH13to34 > SCH_Dxxp2:###
                        Tgt_SCH13to34 = 2
                    elif _MiniSCH13to34 < SCH_Dxxn2:
                        Tgt_SCH13to34 = -2       
                    elif _MiniSCH13to34 > SCH_Dxxp1:###
                        Tgt_SCH13to34 = 1
                    elif _MiniSCH13to34 < SCH_Dxxn1:
                        Tgt_SCH13to34 = -1                      
                    else:
                        Tgt_SCH13to34 = 0

                    if _MiniSCH21to34 >  SCH_Dxxp5:###
                        Tgt_SCH21to34 = 5
                    elif _MiniSCH21to34 < SCH_Dxxn5:
                        Tgt_SCH21to34 = -5
                    elif _MiniSCH21to34 > SCH_Dxxp4:###
                        Tgt_SCH21to34 = 4
                    elif _MiniSCH21to34 < SCH_Dxxn4:
                        Tgt_SCH21to34 = -4
                    elif _MiniSCH21to34 > SCH_Dxxp3:###
                        Tgt_SCH21to34 = 3
                    elif _MiniSCH21to34 < SCH_Dxxn3:
                        Tgt_SCH21to34 = -3
                    elif _MiniSCH21to34 > SCH_Dxxp2:###
                        Tgt_SCH21to34 = 2
                    elif _MiniSCH21to34 < SCH_Dxxn2:
                        Tgt_SCH21to34 = -2       
                    elif _MiniSCH21to34 > SCH_Dxxp1:###
                        Tgt_SCH21to34 = 1
                    elif _MiniSCH21to34 < SCH_Dxxn1:
                        Tgt_SCH21to34 = -1                      
                    else:
                        Tgt_SCH21to34 = 0                    
        ########################################################3
    
        ### END Second part - calculate how Big the future move was, using a lot of averageing out to smother the result.   
                    
        ### START calculation of choosen list of FEATURES for the MACHINE LEARNING process ###          
                    #Get Date info from .txt file and convet it to string format
    
                    _justOpen = float(Open[x])
                    _justHigh = float(High[x])
                    _justLow = float(Low[x])
                    _justClose = float(Close[x])

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-6:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-6:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_05 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass
                    try:            
                        _Diff_CpLf = (np.amin(Low[x-7:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-7:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_06 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass


                    try:            
                        _Diff_CpLf = (np.amin(Low[x-8:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-8:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_07 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-9:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-9:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_08 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-10:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-10:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_09 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-11:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-11:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_10 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-12:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-12:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_11 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-13:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-13:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_12 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass
    
                    try:            
                        _Diff_CpLf = (np.amin(Low[x-14:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-14:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_13 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-15:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-15:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_14 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-16:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-16:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_15 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-17:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-17:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_16 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-18:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-18:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_17 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-19:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-19:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_18 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-20:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-20:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_19 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-21:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-21:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_20 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass
    
                    try:            
                        _Diff_CpLf = (np.amin(Low[x-22:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-22:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_21 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-23:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-23:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_22 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-24:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-24:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_23 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-25:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-25:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_24 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-26:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-26:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_25 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-27:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-27:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_26 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-28:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-28:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_27 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-29:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-29:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_28 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-30:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-30:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_29 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-31:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-31:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_30 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-32:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-32:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_31 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-33:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-33:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_32 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass

                    try:            
                        _Diff_CpLf = (np.amin(Low[x-34:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-34:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_33 = np.round(_KeyValueLong - _KeyValueShort,6)
                    except Exception as e:
                        pass
    
                    try:            
                        _Diff_CpLf = (np.amin(Low[x-35:x+1])-Close[x])/Close[x]
                        _Diff_CpHf = (np.amax(High[x-35:x+1])-Close[x])/Close[x]
                        _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                        _ABSofDiff_CpLf = abs(_Diff_CpLf)
                        _ABSofDiff_CpHf = abs(_Diff_CpHf)
                        _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                        _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                        _PastSharp_34 = np.round(_KeyValueLong - _KeyValueShort,6)
     
                    except Exception as e:
                        pass


                    _PastSCH05to08 = (
                                        _PastSharp_05 +
                                        _PastSharp_06 +
                                        _PastSharp_07 +
                                        _PastSharp_08
                                        )/4

                    _PastSCH05to13 = (
                                        _PastSharp_05 +
                                        _PastSharp_06 +
                                        _PastSharp_07 +
                                        _PastSharp_08 +
                                        _PastSharp_09 +
                                        _PastSharp_10 +
                                        _PastSharp_11 +
                                        _PastSharp_12 +
                                        _PastSharp_13
                                        )/9

                    _PastSCH05to21 = (
                                        _PastSharp_05 +
                                        _PastSharp_06 +
                                        _PastSharp_07 +
                                        _PastSharp_08 +
                                        _PastSharp_09 +
                                        _PastSharp_10 +
                                        _PastSharp_11 +
                                        _PastSharp_12 +
                                        _PastSharp_13 +
                                        _PastSharp_14 +
                                        _PastSharp_15 +
                                        _PastSharp_16 +
                                        _PastSharp_17 +
                                        _PastSharp_18 +
                                        _PastSharp_19 +
                                        _PastSharp_20 +
                                        _PastSharp_21
                                        )/17

                    _PastSCH05to34 = (
                                        _PastSharp_05 +
                                        _PastSharp_06 +
                                        _PastSharp_07 +
                                        _PastSharp_08 +
                                        _PastSharp_09 +
                                        _PastSharp_10 +
                                        _PastSharp_11 +
                                        _PastSharp_12 +
                                        _PastSharp_13 +
                                        _PastSharp_14 +
                                        _PastSharp_15 +
                                        _PastSharp_16 +
                                        _PastSharp_17 +
                                        _PastSharp_18 +
                                        _PastSharp_19 +
                                        _PastSharp_20 +
                                        _PastSharp_21 +
                                        _PastSharp_22 +
                                        _PastSharp_23 +
                                        _PastSharp_24 +
                                        _PastSharp_25 +
                                        _PastSharp_26 +
                                        _PastSharp_27 +
                                        _PastSharp_28 +
                                        _PastSharp_29 +
                                        _PastSharp_30 +
                                        _PastSharp_31 +
                                        _PastSharp_32 +
                                        _PastSharp_33 +
                                        _PastSharp_34
                                        )/30

                    _PastSCH08to13 = (
                                        _PastSharp_08 +
                                        _PastSharp_09 +
                                        _PastSharp_10 +
                                        _PastSharp_11 +
                                        _PastSharp_12 +
                                        _PastSharp_13
                                        )/6


                    _PastSCH08to21 = (
                                        _PastSharp_08 +
                                        _PastSharp_09 +
                                        _PastSharp_10 +
                                        _PastSharp_11 +
                                        _PastSharp_12 +
                                        _PastSharp_13 +
                                        _PastSharp_14 +
                                        _PastSharp_15 +
                                        _PastSharp_16 +
                                        _PastSharp_17 +
                                        _PastSharp_18 +
                                        _PastSharp_19 +
                                        _PastSharp_20 +
                                        _PastSharp_21
                                        )/14


                    _PastSCH08to34 = (
                                        _PastSharp_08 +
                                        _PastSharp_09 +
                                        _PastSharp_10 +
                                        _PastSharp_11 +
                                        _PastSharp_12 +
                                        _PastSharp_13 +
                                        _PastSharp_14 +
                                        _PastSharp_15 +
                                        _PastSharp_16 +
                                        _PastSharp_17 +
                                        _PastSharp_18 +
                                        _PastSharp_19 +
                                        _PastSharp_20 +
                                        _PastSharp_21 +
                                        _PastSharp_22 +
                                        _PastSharp_23 +
                                        _PastSharp_24 +
                                        _PastSharp_25 +
                                        _PastSharp_26 +
                                        _PastSharp_27 +
                                        _PastSharp_28 +
                                        _PastSharp_29 +
                                        _PastSharp_30 +
                                        _PastSharp_31 +
                                        _PastSharp_32 +
                                        _PastSharp_33 +
                                        _PastSharp_34
                                        )/27

                    _PastSCH13to21 = (
                                        _PastSharp_13 +
                                        _PastSharp_14 +
                                        _PastSharp_15 +
                                        _PastSharp_16 +
                                        _PastSharp_17 +
                                        _PastSharp_18 +
                                        _PastSharp_19 +
                                        _PastSharp_20 +
                                        _PastSharp_21
                                        )/9


                    _PastSCH13to34 = (
                                        _PastSharp_13 +
                                        _PastSharp_14 +
                                        _PastSharp_15 +
                                        _PastSharp_16 +
                                        _PastSharp_17 +
                                        _PastSharp_18 +
                                        _PastSharp_19 +
                                        _PastSharp_20 +
                                        _PastSharp_21 +
                                        _PastSharp_22 +
                                        _PastSharp_23 +
                                        _PastSharp_24 +
                                        _PastSharp_25 +
                                        _PastSharp_26 +
                                        _PastSharp_27 +
                                        _PastSharp_28 +
                                        _PastSharp_29 +
                                        _PastSharp_30 +
                                        _PastSharp_31 +
                                        _PastSharp_32 +
                                        _PastSharp_33 +
                                        _PastSharp_34
                                        )/22

                    _PastSCH21to34 = (
                                        _PastSharp_21 +
                                        _PastSharp_22 +
                                        _PastSharp_23 +
                                        _PastSharp_24 +
                                        _PastSharp_25 +
                                        _PastSharp_26 +
                                        _PastSharp_27 +
                                        _PastSharp_28 +
                                        _PastSharp_29 +
                                        _PastSharp_30 +
                                        _PastSharp_31 +
                                        _PastSharp_32 +
                                        _PastSharp_33 +
                                        _PastSharp_34
                                        )/14

                   
                    #part with date related Features
                    _Diff_CtoH = np.round((Close[x]-High[x])/High[x],3)
                    _Diff_CtoH1 = np.round((Close[x]-High[x-1])/High[x-1],3)
                    _Diff_CtoH2 = np.round((Close[x]-High[x-2])/High[x-2],3)
                    _Diff_CtoH3 = np.round((Close[x]-High[x-3])/High[x-3],3)
                    _Diff_CtoH4 = np.round((Close[x]-High[x-4])/High[x-4],3)
                    _Diff_CtoH5 = np.round((Close[x]-High[x-5])/High[x-5],3)
                    _Diff_CtoH6 = np.round((Close[x]-High[x-6])/High[x-6],3)
                    _Diff_CtoH7 = np.round((Close[x]-High[x-7])/High[x-7],3)
                    _Diff_CtoH8 = np.round((Close[x]-High[x-8])/High[x-8],3)
                    _Diff_CtoH9 = np.round((Close[x]-High[x-9])/High[x-9],3)
                    _Diff_CtoH10 = np.round((Close[x]-High[x-10])/High[x-10],3)
                    _Diff_CtoH11 = np.round((Close[x]-High[x-11])/High[x-11],3)
                    _Diff_CtoH12 = np.round((Close[x]-High[x-12])/High[x-12],3)
                    _Diff_CtoH13 = np.round((Close[x]-High[x-13])/High[x-13],3)
                    _Diff_CtoH14 = np.round((Close[x]-High[x-14])/High[x-14],3)
                    _Diff_CtoH15 = np.round((Close[x]-High[x-15])/High[x-15],3)
                    _Diff_CtoH16 = np.round((Close[x]-High[x-16])/High[x-16],3)
                    _Diff_CtoH17 = np.round((Close[x]-High[x-17])/High[x-17],3)
                    _Diff_CtoH18 = np.round((Close[x]-High[x-18])/High[x-18],3)
                    _Diff_CtoH19 = np.round((Close[x]-High[x-19])/High[x-19],3)
                    _Diff_CtoH20 = np.round((Close[x]-High[x-20])/High[x-20],3)
                    _Diff_CtoH21 = np.round((Close[x]-High[x-21])/High[x-21],3)
                    _Diff_CtoH22 = np.round((Close[x]-High[x-22])/High[x-22],3)
                    _Diff_CtoH23 = np.round((Close[x]-High[x-23])/High[x-23],3)
                    _Diff_CtoH24 = np.round((Close[x]-High[x-24])/High[x-24],3)
                    _Diff_CtoH25 = np.round((Close[x]-High[x-25])/High[x-25],3)
                    _Diff_CtoL = np.round((Close[x]-Low[x])/Low[x],3)
                    _Diff_CtoL1 = np.round((Close[x]-Low[x-1])/Low[x-1],3)
                    _Diff_CtoL2 = np.round((Close[x]-Low[x-2])/Low[x-2],3)
                    _Diff_CtoL3 = np.round((Close[x]-Low[x-3])/Low[x-3],3)
                    _Diff_CtoL4 = np.round((Close[x]-Low[x-4])/Low[x-4],3)
                    _Diff_CtoL5 = np.round((Close[x]-Low[x-5])/Low[x-5],3)
                    _Diff_CtoL6 = np.round((Close[x]-Low[x-6])/Low[x-6],3)
                    _Diff_CtoL7 = np.round((Close[x]-Low[x-7])/Low[x-7],3)
                    _Diff_CtoL8 = np.round((Close[x]-Low[x-8])/Low[x-8],3)
                    _Diff_CtoL9 = np.round((Close[x]-Low[x-9])/Low[x-9],3)
                    _Diff_CtoL10 = np.round((Close[x]-Low[x-10])/Low[x-10],3)
                    _Diff_CtoL11 = np.round((Close[x]-Low[x-11])/Low[x-11],3)
                    _Diff_CtoL12 = np.round((Close[x]-Low[x-12])/Low[x-12],3)
                    _Diff_CtoL13 = np.round((Close[x]-Low[x-13])/Low[x-13],3)
                    _Diff_CtoL14 = np.round((Close[x]-Low[x-14])/Low[x-14],3)
                    _Diff_CtoL15 = np.round((Close[x]-Low[x-15])/Low[x-15],3)
                    _Diff_CtoL16 = np.round((Close[x]-Low[x-16])/Low[x-16],3)
                    _Diff_CtoL17 = np.round((Close[x]-Low[x-17])/Low[x-17],3)
                    _Diff_CtoL18 = np.round((Close[x]-Low[x-18])/Low[x-18],3)
                    _Diff_CtoL19 = np.round((Close[x]-Low[x-19])/Low[x-19],3)
                    _Diff_CtoL20 = np.round((Close[x]-Low[x-20])/Low[x-20],3)
                    _Diff_CtoL21 = np.round((Close[x]-Low[x-21])/Low[x-21],3)
                    _Diff_CtoL22 = np.round((Close[x]-Low[x-22])/Low[x-22],3)
                    _Diff_CtoL23 = np.round((Close[x]-Low[x-23])/Low[x-23],3)
                    _Diff_CtoL24 = np.round((Close[x]-Low[x-24])/Low[x-24],3)
                    _Diff_CtoL25 = np.round((Close[x]-Low[x-25])/Low[x-25],3)
    
                    _Diff_CtoO = np.round((Close[x]-Open[x])/Open[x],3)
                    _Diff_CtoO1 = np.round((Close[x]-Open[x-1])/Open[x-1],3)
                    _Diff_CtoO2 = np.round((Close[x]-Open[x-2])/Open[x-2],3)
                    _Diff_CtoO3 = np.round((Close[x]-Open[x-3])/Open[x-3],3)
                    _Diff_CtoO4 = np.round((Close[x]-Open[x-4])/Open[x-4],3)
                    _Diff_CtoO5 = np.round((Close[x]-Open[x-5])/Open[x-5],3)
                    _Diff_CtoO6 = np.round((Close[x]-Open[x-6])/Open[x-6],3)
                    _Diff_CtoO7 = np.round((Close[x]-Open[x-7])/Open[x-7],3)
                    _Diff_CtoO8 = np.round((Close[x]-Open[x-8])/Open[x-8],3)
                    _Diff_CtoO9 = np.round((Close[x]-Open[x-9])/Open[x-9],3)
    
    
                    _Diff_CtoC1 = np.round((Close[x]-Close[x-1])/Close[x-1],3)
                    _Diff_CtoC2 = np.round((Close[x]-Close[x-2])/Close[x-2],3)
                    _Diff_CtoC3 = np.round((Close[x]-Close[x-3])/Close[x-3],3)
                    _Diff_CtoC4 = np.round((Close[x]-Close[x-4])/Close[x-4],3)
                    _Diff_CtoC5 = np.round((Close[x]-Close[x-5])/Close[x-5],3)
                    _Diff_CtoC6 = np.round((Close[x]-Close[x-6])/Close[x-6],3)
                    _Diff_CtoC7 = np.round((Close[x]-Close[x-7])/Close[x-7],3)
                    _Diff_CtoC8 = np.round((Close[x]-Close[x-8])/Close[x-8],3)
                    _Diff_CtoC9 = np.round((Close[x]-Close[x-9])/Close[x-9],3)            
    
                    _SMA_H3 = np.round(np.sum(High[x-4:x+1])/5,4)
                    _SMA_L3 = np.round(np.sum(Low[x-4:x+1])/5,4)
                
                    _BBU3 = np.round(np.sum(Close[x+1-3:x+1])/3,3)+(round(np.std(Close[x+1-3:x+1])*2,3))
                    _BBD3 = np.round(np.sum(Close[x+1-3:x+1])/3,3)-(round(np.std(Close[x+1-3:x+1])*2,3))
                    _DiffU3_C = np.round((Close[x]-_BBU3)/_BBU3,3)
                    _DiffU3_L3 = np.round((_SMA_L3-_BBU3)/_BBU3,3)
                    _DiffD3_C = np.round((Close[x]-_BBD3)/_BBD3,3)
                    _DiffD3_H3 = np.round((_SMA_H3-_BBD3)/_BBD3,3)   
    
                    _BBU5 = np.round(np.sum(Close[x+1-5:x+1])/5,3)+(round(np.std(Close[x+1-5:x+1])*2,3))
                    _BBD5 = np.round(np.sum(Close[x+1-5:x+1])/5,3)-(round(np.std(Close[x+1-5:x+1])*2,3))
                    _DiffU5_C = np.round((Close[x]-_BBU5)/_BBU5,3)
                    _DiffU5_L3 = np.round((_SMA_L3-_BBU5)/_BBU5,3)
                    _DiffD5_C = np.round((Close[x]-_BBD5)/_BBD5,3)
                    _DiffD5_H3 = np.round((_SMA_H3-_BBD5)/_BBD5,3)  
    
                    _BBU8 = np.round(np.sum(Close[x+1-8:x+1])/8,3)+(round(np.std(Close[x+1-8:x+1])*2,3))
                    _BBD8 = np.round(np.sum(Close[x+1-8:x+1])/8,3)-(round(np.std(Close[x+1-8:x+1])*2,3))
                    _DiffU8_C = np.round((Close[x]-_BBU8)/_BBU8,3)
                    _DiffU8_L3 = np.round((_SMA_L3-_BBU8)/_BBU8,3)
                    _DiffD8_C = np.round((Close[x]-_BBD8)/_BBD8,3)
                    _DiffD8_H3 = np.round((_SMA_H3-_BBD8)/_BBD8,3)     
    
                    _BBU13 = np.round(np.sum(Close[x+1-13:x+1])/13,3)+(round(np.std(Close[x+1-13:x+1])*2,3))
                    _BBD13 = np.round(np.sum(Close[x+1-13:x+1])/13,3)-(round(np.std(Close[x+1-13:x+1])*2,3))
                    _DiffU13_C = np.round((Close[x]-_BBU13)/_BBU13,3)
                    _DiffU13_L3 = np.round((_SMA_L3-_BBU13)/_BBU13,3)
                    _DiffD13_C = np.round((Close[x]-_BBD13)/_BBD13,3)
                    _DiffD13_H3 = np.round((_SMA_H3-_BBD13)/_BBD13,3)     
    
                    _BBU21 = np.round(np.sum(Close[x+1-21:x+1])/21,3)+(round(np.std(Close[x+1-21:x+1])*2,3))
                    _BBD21 = np.round(np.sum(Close[x+1-21:x+1])/21,3)-(round(np.std(Close[x+1-21:x+1])*2,3))
                    _DiffU21_C = np.round((Close[x]-_BBU21)/_BBU21,3)
                    _DiffU21_L3 = np.round((_SMA_L3-_BBU21)/_BBU21,3)
                    _DiffD21_C = np.round((Close[x]-_BBD21)/_BBD21,3)
                    _DiffD21_H3 = np.round((_SMA_H3-_BBD21)/_BBD21,3)  
    
                    _BBU34 = np.round(np.sum(Close[x+1-34:x+1])/34,3)+(round(np.std(Close[x+1-34:x+1])*2,3))
                    _BBD34 = np.round(np.sum(Close[x+1-34:x+1])/34,3)-(round(np.std(Close[x+1-34:x+1])*2,3))
                    _DiffU34_C = np.round((Close[x]-_BBU34)/_BBU34,3)
                    _DiffU34_L3 = np.round((_SMA_L3-_BBU34)/_BBU34,3)
                    _DiffD34_C = np.round((Close[x]-_BBD34)/_BBD34,3)
                    _DiffD34_H3 = np.round((_SMA_H3-_BBD34)/_BBD34,3)   
    
                    _BBU55 = np.round(np.sum(Close[x+1-55:x+1])/55,3)+(round(np.std(Close[x+1-55:x+1])*2,3))
                    _BBD55 = np.round(np.sum(Close[x+1-55:x+1])/55,3)-(round(np.std(Close[x+1-55:x+1])*2,3))
                    _DiffU55_C = np.round((Close[x]-_BBU55)/_BBU55,3)
                    _DiffU55_L3 = np.round((_SMA_L3-_BBU55)/_BBU55,3)
                    _DiffD55_C = np.round((Close[x]-_BBD55)/_BBD55,3)
                    _DiffD55_H3 = np.round((_SMA_H3-_BBD55)/_BBD55,3)  
    
                    _BBU89 = np.round(np.sum(Close[x+1-89:x+1])/89,3)+(round(np.std(Close[x+1-89:x+1])*2,3))
                    _BBD89 = np.round(np.sum(Close[x+1-89:x+1])/89,3)-(round(np.std(Close[x+1-89:x+1])*2,3))
                    _DiffU89_C = np.round((Close[x]-_BBU89)/_BBU89,3)
                    _DiffU89_L3 = np.round((_SMA_L3-_BBU89)/_BBU89,3)
                    _DiffD89_C = np.round((Close[x]-_BBD89)/_BBD89,3)
                    _DiffD89_H3 = np.round((_SMA_H3-_BBD89)/_BBD89,3)    
    
                    _BBU100 = np.round(np.sum(Close[x+1-100:x+1])/100,3)+(round(np.std(Close[x+1-100:x+1])*2,3))
                    _BBD100 = np.round(np.sum(Close[x+1-100:x+1])/100,3)-(round(np.std(Close[x+1-100:x+1])*2,3))
                    _DiffU100_C = np.round((Close[x]-_BBU100)/_BBU100,3)
                    _DiffU100_L3 = np.round((_SMA_L3-_BBU100)/_BBU100,3)
                    _DiffD100_C = np.round((Close[x]-_BBD100)/_BBD100,3)
                    _DiffD100_H3 = np.round((_SMA_H3-_BBD100)/_BBD100,3) 
    
                    _BBU144 = np.round(np.sum(Close[x+1-144:x+1])/144,3)+(round(np.std(Close[x+1-144:x+1])*2,3))
                    _BBD144 = np.round(np.sum(Close[x+1-144:x+1])/144,3)-(round(np.std(Close[x+1-144:x+1])*2,3))
                    _DiffU144_C = np.round((Close[x]-_BBU144)/_BBU144,3)
                    _DiffU144_L3 = np.round((_SMA_L3-_BBU144)/_BBU144,3)
                    _DiffD144_C = np.round((Close[x]-_BBD144)/_BBD144,3)
                    _DiffD144_H3 = np.round((_SMA_H3-_BBD144)/_BBD144,3)  
    
                    _BBU200 = np.round(np.sum(Close[x+1-200:x+1])/200,3)+(round(np.std(Close[x+1-200:x+1])*2,3))
                    _BBD200 = np.round(np.sum(Close[x+1-200:x+1])/200,3)-(round(np.std(Close[x+1-200:x+1])*2,3))
                    _DiffU200_C = np.round((Close[x]-_BBU200)/_BBU200,3)
                    _DiffU200_L3 = np.round((_SMA_L3-_BBU200)/_BBU200,3)
                    _DiffD200_C = np.round((Close[x]-_BBD200)/_BBD200,3)
                    _DiffD200_H3 = np.round((_SMA_H3-_BBD200)/_BBD200,3)    
    
                    _BBU233 = np.round(np.sum(Close[x+1-233:x+1])/233,3)+(round(np.std(Close[x+1-233:x+1])*2,3))
                    _BBD233 = np.round(np.sum(Close[x+1-233:x+1])/233,3)-(round(np.std(Close[x+1-233:x+1])*2,3))
                    _DiffU233_C = np.round((Close[x]-_BBU233)/_BBU233,3)
                    _DiffU233_L3 = np.round((_SMA_L3-_BBU233)/_BBU233,3)
                    _DiffD233_C = np.round((Close[x]-_BBD233)/_BBD233,3)
                    _DiffD233_H3 = np.round((_SMA_H3-_BBD233)/_BBD233,3) 
    
                    _BBU300 = np.round(np.sum(Close[x+1-300:x+1])/300,3)+(round(np.std(Close[x+1-300:x+1])*2,3))
                    _BBD300 = np.round(np.sum(Close[x+1-300:x+1])/300,3)-(round(np.std(Close[x+1-300:x+1])*2,3))
                    _DiffU300_C = np.round((Close[x]-_BBU300)/_BBU300,3)
                    _DiffU300_L3 = np.round((_SMA_L3-_BBU300)/_BBU300,3)
                    _DiffD300_C = np.round((Close[x]-_BBD300)/_BBD300,3)
                    _DiffD300_H3 = np.round((_SMA_H3-_BBD300)/_BBD300,3)  
    
                    _BBU377 = np.round(np.sum(Close[x+1-377:x+1])/377,3)+(round(np.std(Close[x+1-377:x+1])*2,3))
                    _BBD377 = np.round(np.sum(Close[x+1-377:x+1])/377,3)-(round(np.std(Close[x+1-377:x+1])*2,3))
                    _DiffU377_C = np.round((Close[x]-_BBU377)/_BBU377,3)
                    _DiffU377_L3 = np.round((_SMA_L3-_BBU377)/_BBU377,3)
                    _DiffD377_C = np.round((Close[x]-_BBD377)/_BBD377,3)
                    _DiffD377_H3 = np.round((_SMA_H3-_BBD377)/_BBD377,3) 
    
                    # Repeated from start of loop
                    _dateDayOfYear = float(dt.strftime('%j'))
                    _dateWeekOfYear = float(dt.strftime('%W'))
                    _dateMonthOfYear = float(dt.strftime('%m'))
                    _dateDayOfMonth = float(dt.strftime('%d'))
                    _dateDayOfWeek = float(dt.strftime('%w'))
    
                    _EvNo5 = np.round((Close[x]-5)/5,3)
                    _EvNo10 = np.round((Close[x]-10)/10,3)
                    _EvNo20 = np.round((Close[x]-20)/20,3)
                    _EvNo30 = np.round((Close[x]-30)/30,3)
                    _EvNo40 = np.round((Close[x]-40)/40,3)
                    _EvNo50 = np.round((Close[x]-50)/50,3)
                    _EvNo60 = np.round((Close[x]-60)/60,3)
                    _EvNo70 = np.round((Close[x]-70)/70,3)
                    _EvNo80 = np.round((Close[x]-80)/80,3)
                    _EvNo90 = np.round((Close[x]-90)/90,3)
                    _EvNo100 = np.round((Close[x]-100)/100,3)
                    _EvNo200 = np.round((Close[x]-200)/200,3)
                    _EvNo300 = np.round((Close[x]-300)/300,3)
                    _EvNo400 = np.round((Close[x]-400)/400,3)
                    _EvNo500 = np.round((Close[x]-500)/500,3)
                    _EvNo600 = np.round((Close[x]-600)/600,3)
                    _EvNo700 = np.round((Close[x]-700)/700,3)
                    _EvNo800 = np.round((Close[x]-800)/800,3)
                    _EvNo900 = np.round((Close[x]-900)/900,3)
                    _EvNo1000 = np.round((Close[x]-1000)/1000,3)
                    _EvNo2000 = np.round((Close[x]-2000)/2000,3)
                    _EvNo3000 = np.round((Close[x]-3000)/3000,3)
                    _EvNo4000 = np.round((Close[x]-4000)/4000,3)
                    _EvNo5000 = np.round((Close[x]-5000)/5000,3)
                    _EvNo10000 = np.round((Close[x]-1000)/1000,3)
    
                    _Perc3_H = np.round((Close[x]-np.percentile(High[x-3:x+1],95))/np.percentile(High[x-3:x+1],95),3)
                    _Perc5_H = np.round((Close[x]-np.percentile(High[x-5:x+1],95))/np.percentile(High[x-5:x+1],95),3)
                    _Perc8_H = np.round((Close[x]-np.percentile(High[x-8:x+1],95))/np.percentile(High[x-8:x+1],95),3)
                    _Perc13_H = np.round((Close[x]-np.percentile(High[x-13:x+1],95))/np.percentile(High[x-13:x+1],95),3)        
                    _Perc21_H = np.round((Close[x]-np.percentile(High[x-21:x+1],95))/np.percentile(High[x-21:x+1],95),3)
                    _Perc34_H = np.round((Close[x]-np.percentile(High[x-34:x+1],95))/np.percentile(High[x-34:x+1],95),3)
                    _Perc55_H = np.round((Close[x]-np.percentile(High[x-55:x+1],95))/np.percentile(High[x-55:x+1],95),3)
                    _Perc89_H = np.round((Close[x]-np.percentile(High[x-89:x+1],95))/np.percentile(High[x-89:x+1],95),3)
                    _Perc100_H = np.round((Close[x]-np.percentile(High[x-100:x+1],95))/np.percentile(High[x-100:x+1],95),3)
                    _Perc144_H = np.round((Close[x]-np.percentile(High[x-144:x+1],95))/np.percentile(High[x-144:x+1],95),3)
                    _Perc200_H = np.round((Close[x]-np.percentile(High[x-200:x+1],95))/np.percentile(High[x-200:x+1],95),3)
                    _Perc233_H = np.round((Close[x]-np.percentile(High[x-233:x+1],95))/np.percentile(High[x-233:x+1],95),3)
                    _Perc377_H = np.round((Close[x]-np.percentile(High[x-377:x+1],95))/np.percentile(High[x-377:x+1],95),3)
    
                    _Perc3_L = np.round((Close[x]-np.percentile(Low[x-3:x+1],5))/np.percentile(Low[x-3:x+1],5),3)
                    _Perc5_L = np.round((Close[x]-np.percentile(Low[x-5:x+1],5))/np.percentile(Low[x-5:x+1],5),3)
                    _Perc8_L = np.round((Close[x]-np.percentile(Low[x-8:x+1],5))/np.percentile(Low[x-8:x+1],5),3)
                    _Perc13_L = np.round((Close[x]-np.percentile(Low[x-13:x+1],5))/np.percentile(Low[x-13:x+1],5),3)
                    _Perc21_L = np.round((Close[x]-np.percentile(Low[x-21:x+1],5))/np.percentile(Low[x-21:x+1],5),3)
                    _Perc34_L = np.round((Close[x]-np.percentile(Low[x-34:x+1],5))/np.percentile(Low[x-34:x+1],5),3)
                    _Perc55_L = np.round((Close[x]-np.percentile(Low[x-55:x+1],5))/np.percentile(Low[x-55:x+1],5),3)
                    _Perc89_L = np.round((Close[x]-np.percentile(Low[x-89:x+1],5))/np.percentile(Low[x-89:x+1],5),3)
                    _Perc100_L = np.round((Close[x]-np.percentile(Low[x-100:x+1],5))/np.percentile(Low[x-100:x+1],5),3)
                    _Perc144_L = np.round((Close[x]-np.percentile(Low[x-144:x+1],5))/np.percentile(Low[x-144:x+1],5),3)
                    _Perc200_L = np.round((Close[x]-np.percentile(Low[x-200:x+1],5))/np.percentile(Low[x-200:x+1],5),3)
                    _Perc233_L = np.round((Close[x]-np.percentile(Low[x-233:x+1],5))/np.percentile(Low[x-233:x+1],5),3)
                    _Perc377_L = np.round((Close[x]-np.percentile(Low[x-377:x+1],5))/np.percentile(Low[x-377:x+1],5),3)
    
                    _Perc3_H80 = np.round((Close[x]-np.percentile(High[x-3:x+1],80))/np.percentile(High[x-3:x+1],80),3)        
                    _Perc5_H80 = np.round((Close[x]-np.percentile(High[x-5:x+1],80))/np.percentile(High[x-5:x+1],80),3)
                    _Perc8_H80 = np.round((Close[x]-np.percentile(High[x-8:x+1],80))/np.percentile(High[x-8:x+1],80),3)
                    _Perc13_H80 = np.round((Close[x]-np.percentile(High[x-13:x+1],80))/np.percentile(High[x-13:x+1],80),3)        
                    _Perc21_H80 = np.round((Close[x]-np.percentile(High[x-21:x+1],80))/np.percentile(High[x-21:x+1],80),3)
                    _Perc34_H80 = np.round((Close[x]-np.percentile(High[x-34:x+1],80))/np.percentile(High[x-34:x+1],80),3)
                    _Perc55_H80 = np.round((Close[x]-np.percentile(High[x-55:x+1],80))/np.percentile(High[x-55:x+1],80),3)
                    _Perc89_H80 = np.round((Close[x]-np.percentile(High[x-89:x+1],80))/np.percentile(High[x-89:x+1],80),3)
                    _Perc100_H80 = np.round((Close[x]-np.percentile(High[x-100:x+1],80))/np.percentile(High[x-100:x+1],80),3)
                    _Perc144_H80 = np.round((Close[x]-np.percentile(High[x-144:x+1],80))/np.percentile(High[x-144:x+1],80),3)
                    _Perc200_H80 = np.round((Close[x]-np.percentile(High[x-200:x+1],80))/np.percentile(High[x-200:x+1],80),3)
                    _Perc233_H80 = np.round((Close[x]-np.percentile(High[x-233:x+1],80))/np.percentile(High[x-233:x+1],80),3)
                    _Perc377_H80 = np.round((Close[x]-np.percentile(High[x-377:x+1],80))/np.percentile(High[x-377:x+1],80),3)
    
                    _Perc3_L20 = np.round((Close[x]-np.percentile(Low[x-3:x+1],20))/np.percentile(Low[x-3:x+1],20),3)
                    _Perc5_L20 = np.round((Close[x]-np.percentile(Low[x-5:x+1],20))/np.percentile(Low[x-5:x+1],20),3)
                    _Perc8_L20 = np.round((Close[x]-np.percentile(Low[x-8:x+1],20))/np.percentile(Low[x-8:x+1],20),3)
                    _Perc13_L20 = np.round((Close[x]-np.percentile(Low[x-13:x+1],20))/np.percentile(Low[x-13:x+1],20),3)
                    _Perc21_L20 = np.round((Close[x]-np.percentile(Low[x-21:x+1],20))/np.percentile(Low[x-21:x+1],20),3)
                    _Perc34_L20 = np.round((Close[x]-np.percentile(Low[x-34:x+1],20))/np.percentile(Low[x-34:x+1],20),3)
                    _Perc55_L20 = np.round((Close[x]-np.percentile(Low[x-55:x+1],20))/np.percentile(Low[x-55:x+1],20),3)
                    _Perc89_L20 = np.round((Close[x]-np.percentile(Low[x-89:x+1],20))/np.percentile(Low[x-89:x+1],20),3)
                    _Perc100_L20 = np.round((Close[x]-np.percentile(Low[x-100:x+1],20))/np.percentile(Low[x-100:x+1],20),3)
                    _Perc144_L20 = np.round((Close[x]-np.percentile(Low[x-144:x+1],20))/np.percentile(Low[x-144:x+1],20),3)
                    _Perc200_L20 = np.round((Close[x]-np.percentile(Low[x-200:x+1],20))/np.percentile(Low[x-200:x+1],20),3)
                    _Perc233_L20 = np.round((Close[x]-np.percentile(Low[x-233:x+1],20))/np.percentile(Low[x-233:x+1],20),3)
                    _Perc377_L20 = np.round((Close[x]-np.percentile(Low[x-377:x+1],20))/np.percentile(Low[x-377:x+1],20),3)
    
                    _Perc3_M50 = np.round((Close[x]-np.percentile(High[x-3:x+1],50))/np.percentile(High[x-3:x+1],50),3)        
                    _Perc5_M50 = np.round((Close[x]-np.percentile(High[x-5:x+1],50))/np.percentile(High[x-5:x+1],50),3)
                    _Perc8_M50 = np.round((Close[x]-np.percentile(High[x-8:x+1],50))/np.percentile(High[x-8:x+1],50),3)
                    _Perc13_M50 = np.round((Close[x]-np.percentile(High[x-13:x+1],50))/np.percentile(High[x-13:x+1],50),3)        
                    _Perc21_M50 = np.round((Close[x]-np.percentile(High[x-21:x+1],50))/np.percentile(High[x-21:x+1],50),3)
                    _Perc34_M50 = np.round((Close[x]-np.percentile(High[x-34:x+1],50))/np.percentile(High[x-34:x+1],50),3)
                    _Perc55_M50 = np.round((Close[x]-np.percentile(High[x-55:x+1],50))/np.percentile(High[x-55:x+1],50),3)
                    _Perc89_M50 = np.round((Close[x]-np.percentile(High[x-89:x+1],50))/np.percentile(High[x-89:x+1],50),3)
                    _Perc100_M50 = np.round((Close[x]-np.percentile(High[x-100:x+1],50))/np.percentile(High[x-100:x+1],50),3)
                    _Perc144_M50 = np.round((Close[x]-np.percentile(High[x-144:x+1],50))/np.percentile(High[x-144:x+1],50),3)
                    _Perc200_M50 = np.round((Close[x]-np.percentile(High[x-200:x+1],50))/np.percentile(High[x-200:x+1],50),3)
                    _Perc233_M50 = np.round((Close[x]-np.percentile(High[x-233:x+1],50))/np.percentile(High[x-233:x+1],50),3)
                    _Perc377_M50 = np.round((Close[x]-np.percentile(High[x-377:x+1],50))/np.percentile(High[x-377:x+1],50),3)
    
                    RL3 = np.round(np.polyfit(Zeros[x-3:x+1], Close[x-3:x+1], 0),3)[0]
                    RL5 = np.round(np.polyfit(Zeros[x-5:x+1], Close[x-5:x+1], 0),3)[0]
                    RL8 = np.round(np.polyfit(Zeros[x-8:x+1], Close[x-8:x+1], 0),3)[0]
                    RL13 = np.round(np.polyfit(Zeros[x-13:x+1], Close[x-13:x+1], 0),3)[0]
                    RL21 = np.round(np.polyfit(Zeros[x-21:x+1], Close[x-21:x+1], 0),3)[0]
                    RL34 = np.round(np.polyfit(Zeros[x-34:x+1], Close[x-34:x+1], 0),3)[0]
                    RL55 = np.round(np.polyfit(Zeros[x-55:x+1], Close[x-55:x+1], 0),3)[0]
                    RL89 = np.round(np.polyfit(Zeros[x-89:x+1], Close[x-89:x+1], 0),3)[0]
                    RL100 = np.round(np.polyfit(Zeros[x-100:x+1], Close[x-100:x+1], 0),3)[0]
                    RL144 = np.round(np.polyfit(Zeros[x-144:x+1], Close[x-144:x+1], 0),3)[0]
                    RL200 = np.round(np.polyfit(Zeros[x-200:x+1], Close[x-200:x+1], 0),3)[0]
                    RL233 = np.round(np.polyfit(Zeros[x-233:x+1], Close[x-233:x+1], 0),3)[0]
                    RL377 = np.round(np.polyfit(Zeros[x-377:x+1], Close[x-377:x+1], 0),3)[0]
    
                    Diff_C_RL3 = np.round((Close[x]-RL3)/RL3,3)
                    Diff_C_RL5 = np.round((Close[x]-RL5)/RL5,3)
                    Diff_C_RL8 = np.round((Close[x]-RL8)/RL8,3)
                    Diff_C_RL13 = np.round((Close[x]-RL13)/RL13,3)
                    Diff_C_RL21 = np.round((Close[x]-RL21)/RL21,3)
                    Diff_C_RL34 = np.round((Close[x]-RL34)/RL34,3)
                    Diff_C_RL55 = np.round((Close[x]-RL55)/RL55,3)
                    Diff_C_RL89 = np.round((Close[x]-RL89)/RL89,3)
                    Diff_C_RL100 = np.round((Close[x]-RL100)/RL100,3)
                    Diff_C_RL144 = np.round((Close[x]-RL144)/RL144,3)
                    Diff_C_RL200 = np.round((Close[x]-RL200)/RL200,3)
                    Diff_C_RL233 = np.round((Close[x]-RL233)/RL233,3)
                    Diff_C_RL377 = np.round((Close[x]-RL377)/RL377,3)
    
                    Diff_RL3_RL5 = np.round((RL3-RL5)/RL5,3)
                    Diff_RL3_RL8 = np.round((RL3-RL8)/RL8,3)
                    Diff_RL3_RL13 = np.round((RL3-RL13)/RL13,3)
                    Diff_RL3_RL21 = np.round((RL3-RL21)/RL21,3)
                    Diff_RL3_RL34 = np.round((RL3-RL34)/RL34,3)
    
                    Diff_RL5_RL8 = np.round((RL5-RL8)/RL8,3)
                    Diff_RL5_RL13 = np.round((RL5-RL13)/RL13,3)
                    Diff_RL5_RL21 = np.round((RL5-RL21)/RL21,3)
                    Diff_RL5_RL34 = np.round((RL5-RL34)/RL34,3)
                    Diff_RL5_RL55 = np.round((RL5-RL55)/RL55,3)
    
                    Diff_RL8_RL13 = np.round((RL8-RL13)/RL13,3)
                    Diff_RL8_RL21 = np.round((RL8-RL21)/RL21,3)
                    Diff_RL8_RL34 = np.round((RL8-RL34)/RL34,3)
                    Diff_RL8_RL55 = np.round((RL8-RL55)/RL55,3)
                    Diff_RL8_RL89 = np.round((RL8-RL89)/RL89,3)
    
                    Diff_RL13_RL21 = np.round((RL13-RL21)/RL21,3)
                    Diff_RL13_RL34 = np.round((RL13-RL34)/RL34,3)
                    Diff_RL13_RL55 = np.round((RL13-RL55)/RL55,3)
                    Diff_RL13_RL139 = np.round((RL13-RL89)/RL89,3)
                    Diff_RL13_RL100 = np.round((RL13-RL100)/RL100,3)
    
                    Diff_RL21_RL34 = np.round((RL21-RL34)/RL34,3)
                    Diff_RL21_RL55 = np.round((RL21-RL55)/RL55,3)
                    Diff_RL21_RL89 = np.round((RL21-RL89)/RL89,3)
                    Diff_RL21_RL100 = np.round((RL21-RL100)/RL100,3)
                    Diff_RL21_RL144 = np.round((RL21-RL144)/RL144,3)
    
                    Diff_RL34_RL55 = np.round((RL34-RL55)/RL55,3)
                    Diff_RL34_RL89 = np.round((RL34-RL89)/RL89,3)
                    Diff_RL34_RL100 = np.round((RL34-RL100)/RL100,3)
                    Diff_RL34_RL144 = np.round((RL34-RL144)/RL144,3)
                    Diff_RL34_RL200 = np.round((RL34-RL200)/RL200,3)
    
                    Diff_RL55_RL89 = np.round((RL55-RL89)/RL89,3)
                    Diff_RL55_RL100 = np.round((RL55-RL100)/RL100,3)
                    Diff_RL55_RL144 = np.round((RL55-RL144)/RL144,3)
                    Diff_RL55_RL200 = np.round((RL55-RL200)/RL200,3)
                    Diff_RL55_RL233 = np.round((RL55-RL233)/RL233,3)
    
                    Diff_RL89_RL100 = np.round((RL89-RL100)/RL100,3)
                    Diff_RL89_RL144 = np.round((RL89-RL144)/RL144,3)
                    Diff_RL89_RL200 = np.round((RL89-RL200)/RL200,3)
                    Diff_RL89_RL233 = np.round((RL89-RL233)/RL233,3)
                    Diff_RL89_RL377 = np.round((RL89-RL377)/RL377,3)
    
                    Diff_RL100_RL144 = np.round((RL100-RL144)/RL144,3)
                    Diff_RL100_RL200 = np.round((RL100-RL200)/RL200,3)
                    Diff_RL100_RL233 = np.round((RL100-RL233)/RL233,3)
                    Diff_RL100_RL377 = np.round((RL100-RL377)/RL377,3)
    
                    Diff_RL144_RL200 = np.round((RL144-RL200)/RL200,3)
                    Diff_RL144_RL233 = np.round((RL144-RL233)/RL233,3)
                    Diff_RL144_RL377 = np.round((RL144-RL377)/RL377,3)
    
                    Diff_RL200_RL233 = np.round((RL200-RL233)/RL233,3)
                    Diff_RL200_RL377 = np.round((RL200-RL377)/RL377,3)
    
                    Diff_RL233_RL377 = np.round((RL233-RL377)/RL377,3)
                
                
                    _SMA3_C = np.round((Close[x]-(np.sum(Close[x-3:x+1])/3))/(np.sum(Close[x-3:x+1])/3),3)
                    _SMA5_C = np.round((Close[x]-(np.sum(Close[x-5:x+1])/5))/(np.sum(Close[x-5:x+1])/5),3)
                    _SMA8_C = np.round((Close[x]-(np.sum(Close[x-8:x+1])/8))/(np.sum(Close[x-8:x+1])/8),3)
                    _SMA13_C = np.round((Close[x]-(np.sum(Close[x-13:x+1])/13))/(np.sum(Close[x-13:x+1])/13),3)
                    _SMA21_C = np.round((Close[x]-(np.sum(Close[x-21:x+1])/21))/(np.sum(Close[x-21:x+1])/21),3)
                    _SMA34_C = np.round((Close[x]-(np.sum(Close[x-34:x+1])/34))/(np.sum(Close[x-34:x+1])/34),3)
                    _SMA55_C = np.round((Close[x]-(np.sum(Close[x-55:x+1])/55))/(np.sum(Close[x-55:x+1])/55),3)
                    _SMA89_C = np.round((Close[x]-(np.sum(Close[x-89:x+1])/89))/(np.sum(Close[x-89:x+1])/89),3)
                    _SMA144_C = np.round((Close[x]-(np.sum(Close[x-144:x+1])/144))/(np.sum(Close[x-144:x+1])/144),3)
                    _SMA233_C = np.round((Close[x]-(np.sum(Close[x-233:x+1])/233))/(np.sum(Close[x-233:x+1])/233),3)
                    _SMA377_C = np.round((Close[x]-(np.sum(Close[x-377:x+1])/377))/(np.sum(Close[x-377:x+1])/377),3)
                    _SMA100_C = np.round((Close[x]-(np.sum(Close[x-100:x+1])/100))/(np.sum(Close[x-100:x+1])/100),3)
                    _SMA200_C = np.round((Close[x]-(np.sum(Close[x-200:x+1])/200))/(np.sum(Close[x-200:x+1])/200),3)
                    _SMA300_C = np.round((Close[x]-(np.sum(Close[x-300:x+1])/300))/(np.sum(Close[x-300:x+1])/300),3)
                
                    _SMA3vs5 = np.round((_SMA3_C-_SMA5_C)/_SMA5_C,3)
                    _SMA3vs8 = np.round((_SMA3_C-_SMA8_C)/_SMA8_C,3)
                    _SMA3vs13 = np.round((_SMA3_C-_SMA13_C)/_SMA13_C,3)
                    _SMA3vs21 = np.round((_SMA3_C-_SMA21_C)/_SMA21_C,3)
                    _SMA3vs34 = np.round((_SMA3_C-_SMA34_C)/_SMA34_C,3)
                    _SMA5vs8 = np.round((_SMA5_C-_SMA8_C)/_SMA8_C,3)
                    _SMA5vs13 = np.round((_SMA5_C-_SMA13_C)/_SMA13_C,3)
                    _SMA5vs21 = np.round((_SMA5_C-_SMA21_C)/_SMA21_C,3)
                    _SMA5vs34 = np.round((_SMA5_C-_SMA34_C)/_SMA34_C,3)
                    _SMA5vs55 = np.round((_SMA5_C-_SMA55_C)/_SMA55_C,3)
                    _SMA8vs13 = np.round((_SMA8_C-_SMA13_C)/_SMA13_C,3)
                    _SMA8vs21 = np.round((_SMA8_C-_SMA21_C)/_SMA21_C,3)
                    _SMA8vs34 = np.round((_SMA8_C-_SMA34_C)/_SMA34_C,3)
                    _SMA8vs55 = np.round((_SMA8_C-_SMA55_C)/_SMA55_C,3)
                    _SMA8vs89 = np.round((_SMA8_C-_SMA89_C)/_SMA89_C,3)
                    _SMA13vs21 = np.round((_SMA13_C-_SMA21_C)/_SMA21_C,3)
                    _SMA13vs34 = np.round((_SMA13_C-_SMA34_C)/_SMA34_C,3)
                    _SMA13vs55 = np.round((_SMA13_C-_SMA55_C)/_SMA55_C,3)
                    _SMA13vs89 = np.round((_SMA13_C-_SMA89_C)/_SMA89_C,3)
                    _SMA13vs144 = np.round((_SMA13_C-_SMA144_C)/_SMA144_C,3)
                    _SMA21vs34 = np.round((_SMA21_C-_SMA34_C)/_SMA34_C,3)
                    _SMA21vs55 = np.round((_SMA21_C-_SMA55_C)/_SMA55_C,3)
                    _SMA21vs89 = np.round((_SMA21_C-_SMA89_C)/_SMA89_C,3)
                    _SMA21vs144 = np.round((_SMA21_C-_SMA144_C)/_SMA144_C,3)
                    _SMA21vs233 = np.round((_SMA21_C-_SMA233_C)/_SMA233_C,3)
                    _SMA34vs55 = np.round((_SMA34_C-_SMA55_C)/_SMA55_C,3)
                    _SMA34vs89 = np.round((_SMA34_C-_SMA89_C)/_SMA89_C,3)
                    _SMA34vs144 = np.round((_SMA34_C-_SMA144_C)/_SMA144_C,3)
                    _SMA34vs233 = np.round((_SMA34_C-_SMA233_C)/_SMA233_C,3)
                    _SMA34vs377 = np.round((_SMA34_C-_SMA377_C)/_SMA377_C,3)
                    _SMA55vs89 = np.round((_SMA55_C-_SMA89_C)/_SMA89_C,3)
                    _SMA55vs144 = np.round((_SMA55_C-_SMA144_C)/_SMA144_C,3)
                    _SMA55vs233 = np.round((_SMA55_C-_SMA233_C)/_SMA233_C,3)
                    _SMA55vs377 = np.round((_SMA55_C-_SMA377_C)/_SMA377_C,3)
                    _SMA89vs144 = np.round((_SMA89_C-_SMA144_C)/_SMA144_C,3)
                    _SMA89vs233 = np.round((_SMA89_C-_SMA233_C)/_SMA233_C,3)
                    _SMA89vs377 = np.round((_SMA89_C-_SMA377_C)/_SMA377_C,3)
                    _SMA144vs233 = np.round((_SMA144_C-_SMA233_C)/_SMA233_C,3)
                    _SMA144vs377 = np.round((_SMA144_C-_SMA377_C)/_SMA377_C,3)
                    _SMA233vs377 = np.round((_SMA233_C-_SMA377_C)/_SMA377_C,3)            

                    _STD3_C = np.round(np.std(Close[x-3:x+1])/Close[x],3)
                    _STD3_C1m = np.round(np.std(Close[x-4:x])/Close[x-1],3)        
                    _STD3_C2m = np.round(np.std(Close[x-5:x-1])/Close[x-2],3)        
                    _STD3_C3m = np.round(np.std(Close[x-6:x-2])/Close[x-3],3)
                    _STD3_C4m = np.round(np.std(Close[x-7:x-3])/Close[x-4],3)        
                    _STD3sign = np.round((_STD3_C + _STD3_C1m + _STD3_C2m + _STD3_C3m + _STD3_C4m)/5,3)
                    _STD3vsSign = np.round((_STD3_C-_STD3sign)/_STD3sign,3)
    
                    _STD5_C = np.round(np.std(Close[x-5:x+1])/Close[x],3)
                    _STD5_C1m = np.round(np.std(Close[x-6:x])/Close[x-1],3)        
                    _STD5_C2m = np.round(np.std(Close[x-7:x-1])/Close[x-2],3)        
                    _STD5_C3m = np.round(np.std(Close[x-8:x-2])/Close[x-3],3)
                    _STD5_C4m = np.round(np.std(Close[x-9:x-3])/Close[x-4],3)        
                    _STD5sign = np.round((_STD5_C + _STD5_C1m + _STD5_C2m + _STD5_C3m + _STD5_C4m)/5,3)
                    _STD5vsSign = np.round((_STD5_C-_STD5sign)/_STD5sign,3)
    
                    _STD8_C = np.round(np.std(Close[x-8:x+1])/Close[x],3)
                    _STD8_C1m = np.round(np.std(Close[x-9:x])/Close[x-1],3)        
                    _STD8_C2m = np.round(np.std(Close[x-10:x-1])/Close[x-2],3)        
                    _STD8_C3m = np.round(np.std(Close[x-11:x-2])/Close[x-3],3)
                    _STD8_C4m = np.round(np.std(Close[x-12:x-3])/Close[x-4],3)        
                    _STD8sign = np.round((_STD8_C + _STD8_C1m + _STD8_C2m + _STD8_C3m + _STD8_C4m)/5,3)
                    _STD8vsSign = np.round((_STD8_C-_STD8sign)/_STD8sign,3)
                
                    _STD13_C = np.round(np.std(Close[x-13:x+1])/Close[x],3)
                    _STD13_C1m = np.round(np.std(Close[x-14:x])/Close[x-1],3)        
                    _STD13_C2m = np.round(np.std(Close[x-15:x-1])/Close[x-2],3)        
                    _STD13_C3m = np.round(np.std(Close[x-16:x-2])/Close[x-3],3)
                    _STD13_C4m = np.round(np.std(Close[x-17:x-3])/Close[x-4],3)        
                    _STD13sign = np.round((_STD13_C + _STD13_C1m + _STD13_C2m + _STD13_C3m + _STD13_C4m)/5,3)
                    _STD13vsSign = np.round((_STD13_C-_STD13sign)/_STD13sign,3)        
    
                    _STD21_C = np.round(np.std(Close[x-21:x+1])/Close[x],3)
                    _STD21_C1m = np.round(np.std(Close[x-22:x])/Close[x-1],3)        
                    _STD21_C2m = np.round(np.std(Close[x-23:x-1])/Close[x-2],3)        
                    _STD21_C3m = np.round(np.std(Close[x-24:x-2])/Close[x-3],3)
                    _STD21_C4m = np.round(np.std(Close[x-25:x-3])/Close[x-4],3)        
                    _STD21sign = np.round((_STD21_C + _STD21_C1m + _STD21_C2m + _STD21_C3m + _STD21_C4m)/5,3)
                    _STD21vsSign = np.round((_STD21_C-_STD21sign)/_STD21sign,3)
            
                    _STD34_C = np.round(np.std(Close[x-34:x+1])/Close[x],3)
                    _STD34_C1m = np.round(np.std(Close[x-35:x])/Close[x-1],3)        
                    _STD34_C2m = np.round(np.std(Close[x-36:x-1])/Close[x-2],3)        
                    _STD34_C3m = np.round(np.std(Close[x-37:x-2])/Close[x-3],3)
                    _STD34_C4m = np.round(np.std(Close[x-38:x-3])/Close[x-4],3)        
                    _STD34sign = np.round((_STD34_C + _STD34_C1m + _STD34_C2m + _STD34_C3m + _STD34_C4m)/5,3)
                    _STD34vsSign = np.round((_STD34_C-_STD34sign)/_STD34sign,3)
            
                    _STD55_C = np.round(np.std(Close[x-55:x+1])/Close[x],3)
                    _STD55_C1m = np.round(np.std(Close[x-56:x])/Close[x-1],3)        
                    _STD55_C2m = np.round(np.std(Close[x-57:x-1])/Close[x-2],3)        
                    _STD55_C3m = np.round(np.std(Close[x-58:x-2])/Close[x-3],3)
                    _STD55_C4m = np.round(np.std(Close[x-59:x-3])/Close[x-4],3)        
                    _STD55sign = np.round((_STD55_C + _STD55_C1m + _STD55_C2m + _STD55_C3m + _STD55_C4m)/5,3)
                    _STD55vsSign = np.round((_STD55_C-_STD55sign)/_STD55sign,3)        
            
                    _STD89_C = np.round(np.std(Close[x-89:x+1])/Close[x],3)
                    _STD89_C1m = np.round(np.std(Close[x-90:x])/Close[x-1],3)        
                    _STD89_C2m = np.round(np.std(Close[x-91:x-1])/Close[x-2],3)        
                    _STD89_C3m = np.round(np.std(Close[x-92:x-2])/Close[x-3],3)
                    _STD89_C4m = np.round(np.std(Close[x-93:x-3])/Close[x-4],3)        
                    _STD89sign = np.round((_STD89_C + _STD89_C1m + _STD89_C2m + _STD89_C3m + _STD89_C4m)/5,3)
                    _STD89vsSign = np.round((_STD89_C-_STD89sign)/_STD89sign,3)
    
                    _STD144_C = np.round(np.std(Close[x-144:x+1])/Close[x],3)
                    _STD144_C1m = np.round(np.std(Close[x-145:x])/Close[x-1],3)        
                    _STD144_C2m = np.round(np.std(Close[x-146:x-1])/Close[x-2],3)        
                    _STD144_C3m = np.round(np.std(Close[x-147:x-2])/Close[x-3],3)
                    _STD144_C4m = np.round(np.std(Close[x-148:x-3])/Close[x-4],3)        
                    _STD144sign = np.round((_STD144_C + _STD144_C1m + _STD144_C2m + _STD144_C3m + _STD144_C4m)/5,3)
                    _STD144vsSign = np.round((_STD144_C-_STD144sign)/_STD144sign,3)
    
                    _STD233_C = np.round(np.std(Close[x-233:x+1])/Close[x],3)
                    _STD233_C1m = np.round(np.std(Close[x-234:x])/Close[x-1],3)        
                    _STD233_C2m = np.round(np.std(Close[x-235:x-1])/Close[x-2],3)        
                    _STD233_C3m = np.round(np.std(Close[x-236:x-2])/Close[x-3],3)
                    _STD233_C4m = np.round(np.std(Close[x-237:x-3])/Close[x-4],3)        
                    _STD233sign = np.round((_STD233_C + _STD233_C1m + _STD233_C2m + _STD233_C3m + _STD233_C4m)/5,3)
                    _STD233vsSign = np.round((_STD233_C-_STD233sign)/_STD233sign,3)            
    
                    _STD377_C = np.round(np.std(Close[x-377:x+1])/Close[x],3)
                    _STD377_C1m = np.round(np.std(Close[x-378:x])/Close[x-1],3)        
                    _STD377_C2m = np.round(np.std(Close[x-379:x-1])/Close[x-2],3)        
                    _STD377_C3m = np.round(np.std(Close[x-380:x-2])/Close[x-3],3)
                    _STD377_C4m = np.round(np.std(Close[x-381:x-3])/Close[x-4],3)        
                    _STD377sign = np.round((_STD377_C + _STD377_C1m + _STD377_C2m + _STD377_C3m + _STD377_C4m)/5,3)
                    _STD377vsSign = np.round((_STD377_C-_STD377sign)/_STD377sign,3)      
                
                    _STD100_C = np.round(np.std(Close[x-100:x+1])/Close[x],3)
                    _STD100_C1m = np.round(np.std(Close[x-101:x])/Close[x-1],3)        
                    _STD100_C2m = np.round(np.std(Close[x-102:x-1])/Close[x-2],3)        
                    _STD100_C3m = np.round(np.std(Close[x-103:x-2])/Close[x-3],3)
                    _STD100_C4m = np.round(np.std(Close[x-104:x-3])/Close[x-4],3)        
                    _STD100sign = np.round((_STD100_C + _STD100_C1m + _STD100_C2m + _STD100_C3m + _STD100_C4m)/5,3)
                    _STD100vsSign = np.round((_STD100_C-_STD100sign)/_STD100sign,3)            
                
                    _STD200_C = np.round(np.std(Close[x-200:x+1])/Close[x],3)
                    _STD200_C1m = np.round(np.std(Close[x-201:x])/Close[x-1],3)        
                    _STD200_C2m = np.round(np.std(Close[x-202:x-1])/Close[x-2],3)        
                    _STD200_C3m = np.round(np.std(Close[x-203:x-2])/Close[x-3],3)
                    _STD200_C4m = np.round(np.std(Close[x-204:x-3])/Close[x-4],3)        
                    _STD200sign = np.round((_STD200_C + _STD200_C1m + _STD200_C2m + _STD200_C3m + _STD200_C4m)/5,3)
                    _STD200vsSign = np.round((_STD200_C-_STD200sign)/_STD200sign,3)
    
                    _STD300_C = np.round(np.std(Close[x-300:x+1])/Close[x],3)
                    _STD300_C1m = np.round(np.std(Close[x-301:x])/Close[x-1],3)        
                    _STD300_C2m = np.round(np.std(Close[x-302:x-1])/Close[x-2],3)        
                    _STD300_C3m = np.round(np.std(Close[x-303:x-2])/Close[x-3],3)
                    _STD300_C4m = np.round(np.std(Close[x-304:x-3])/Close[x-4],3)        
                    _STD300sign = np.round((_STD300_C + _STD300_C1m + _STD300_C2m + _STD300_C3m + _STD300_C4m)/5,3)
                    _STD300vsSign = np.round((_STD300_C-_STD300sign)/_STD300sign,3)            

                    _stoch5 = np.round((Close[x]-np.amin(Low[x-5:x+1]))/(np.amax(High[x-5:x+1])-np.amin(Low[x-5:x+1]))*100,3)
                    _stoch5m1 = np.round((Close[x-1]-np.amin(Low[x-6:x]))/(np.amax(High[x-6:x])-np.amin(Low[x-6:x]))*100,3)
                    _stoch5m2 = np.round((Close[x-2]-np.amin(Low[x-7:x-1]))/(np.amax(High[x-7:x-1])-np.amin(Low[x-7:x-1]))*100,3)
                    _stoch5m3 = np.round((Close[x-3]-np.amin(Low[x-8:x-2]))/(np.amax(High[x-8:x-2])-np.amin(Low[x-8:x-2]))*100,3)
                    _stoch5m4 = np.round((Close[x-4]-np.amin(Low[x-9:x-3]))/(np.amax(High[x-9:x-3])-np.amin(Low[x-9:x-3]))*100,3)
                    _sign5Stoch5 = np.round((_stoch5+_stoch5m1+_stoch5m2+_stoch5m3+_stoch5m4)/5,3)
                    _diffStochSign5 = np.round((_stoch5-_sign5Stoch5)/_sign5Stoch5,2)
                    if _stoch5 > 80:
                        _stoch5Level = 1.0  
                    elif _stoch5 < 20:
                        _stoch5Level = -1.0
                    else:
                        _stoch5Level = 0.0 
                    
                    _stoch14 = np.round((Close[x]-np.amin(Low[x-14:x+1]))/(np.amax(High[x-14:x+1])-np.amin(Low[x-14:x+1]))*100,3)
                    _stoch8 = np.round((Close[x]-np.amin(Low[x-8:x+1]))/(np.amax(High[x-8:x+1])-np.amin(Low[x-8:x+1]))*100,3)
                    _stoch8m1 = np.round((Close[x-1]-np.amin(Low[x-9:x]))/(np.amax(High[x-9:x])-np.amin(Low[x-9:x]))*100,3)
                    _stoch8m2 = np.round((Close[x-2]-np.amin(Low[x-10:x-1]))/(np.amax(High[x-10:x-1])-np.amin(Low[x-10:x-1]))*100,3)
                    _stoch8m3 = np.round((Close[x-3]-np.amin(Low[x-11:x-2]))/(np.amax(High[x-11:x-2])-np.amin(Low[x-11:x-2]))*100,3)
                    _stoch8m4 = np.round((Close[x-4]-np.amin(Low[x-12:x-3]))/(np.amax(High[x-12:x-3])-np.amin(Low[x-12:x-3]))*100,3)
                    _sign5Stoch8 = np.round((_stoch8+_stoch8m1+_stoch8m2+_stoch8m3+_stoch8m4)/5,3)
                    _diffStochSign8 = np.round((_stoch14-_sign5Stoch8)/_sign5Stoch8,2)
                    if _stoch8 > 80:
                        _stoch8Level = 1.0  
                    elif _stoch8 < 20:
                        _stoch8Level = -1.0
                    else:
                        _stoch8Level = 0.0 
    
    
                    _stoch14m1 = np.round((Close[x-1]-np.amin(Low[x-15:x]))/(np.amax(High[x-14:x+1])-np.amin(Low[x-14:x+1]))*100,3)
                    _stoch14m2 = np.round((Close[x-2]-np.amin(Low[x-16:x-1]))/(np.amax(High[x-14:x+1])-np.amin(Low[x-14:x+1]))*100,3)
                    _stoch14m3 = np.round((Close[x-3]-np.amin(Low[x-17:x-2]))/(np.amax(High[x-14:x+1])-np.amin(Low[x-14:x+1]))*100,3)
                    _stoch14m4 = np.round((Close[x-4]-np.amin(Low[x-18:x-3]))/(np.amax(High[x-14:x+1])-np.amin(Low[x-14:x+1]))*100,3)
                    _sign5Stoch8 = np.round((_stoch14+_stoch14m1+_stoch14m2+_stoch14m3+_stoch14m4)/5,1)
                    _diffStochSign14 = np.round((_stoch14-_sign5Stoch8)/_sign5Stoch8,3)
                    if _stoch14 > 80:
                        _stoch14Level = 1.0  
                    elif _stoch14 < 20:
                        _stoch14Level = -1.0
                    else:
                        _stoch14Level = 0.0 
    
                    _stoch21 = np.round((Close[x]-np.amin(Low[x-21:x+1]))/(np.amax(High[x-21:x+1])-np.amin(Low[x-21:x+1]))*100,3)
                    _stoch21m1 = np.round((Close[x-1]-np.amin(Low[x-22:x]))/(np.amax(High[x-22:x])-np.amin(Low[x-22:x]))*100,3)
                    _stoch21m2 = np.round((Close[x-2]-np.amin(Low[x-23:x-1]))/(np.amax(High[x-23:x-1])-np.amin(Low[x-23:x-1]))*100,3)
                    _stoch21m3 = np.round((Close[x-3]-np.amin(Low[x-24:x-2]))/(np.amax(High[x-24:x-2])-np.amin(Low[x-24:x-2]))*100,3)
                    _stoch21m4 = np.round((Close[x-4]-np.amin(Low[x-25:x-3]))/(np.amax(High[x-25:x-3])-np.amin(Low[x-25:x-3]))*100,3)
                    _sign5Stoch21 = np.round((_stoch21+_stoch21m1+_stoch21m2+_stoch21m3+_stoch21m4)/5,3)
                    _diffStochSign21 = np.round((_stoch21-_sign5Stoch21)/_sign5Stoch21,2)
                    if _stoch21 > 80:
                        _stoch21Level = 1.0  
                    elif _stoch21 < 20:
                        _stoch21Level = -1.0
                    else:
                        _stoch21Level = 0.0 
    
                    _stoch34 = np.round((Close[x]-np.amin(Low[x-34:x+1]))/(np.amax(High[x-34:x+1])-np.amin(Low[x-34:x+1]))*100,3)
                    _stoch34m1 = np.round((Close[x-1]-np.amin(Low[x-35:x]))/(np.amax(High[x-35:x])-np.amin(Low[x-35:x]))*100,3)
                    _stoch34m2 = np.round((Close[x-2]-np.amin(Low[x-36:x-1]))/(np.amax(High[x-36:x-1])-np.amin(Low[x-36:x-1]))*100,3)
                    _stoch34m3 = np.round((Close[x-3]-np.amin(Low[x-37:x-2]))/(np.amax(High[x-37:x-2])-np.amin(Low[x-37:x-2]))*100,3)
                    _stoch34m4 = np.round((Close[x-4]-np.amin(Low[x-38:x-3]))/(np.amax(High[x-38:x-3])-np.amin(Low[x-38:x-3]))*100,3)
                    _sign5Stoch34 = np.round((_stoch34+_stoch34m1+_stoch34m2+_stoch34m3+_stoch34m4)/5,3)
                    _diffStochSign34 = np.round((_stoch34-_sign5Stoch34)/_sign5Stoch34,2)
                    if _stoch34 > 80:
                        _stoch34Level = 1.0  
                    elif _stoch34 < 20:
                        _stoch34Level = -1.0
                    else:
                        _stoch34Level = 0.0 
    
                    _stoch55 = np.round((Close[x]-np.amin(Low[x-55:x+1]))/(np.amax(High[x-55:x+1])-np.amin(Low[x-55:x+1]))*100,3)
                    _stoch55m1 = np.round((Close[x-1]-np.amin(Low[x-56:x]))/(np.amax(High[x-56:x])-np.amin(Low[x-56:x]))*100,3)
                    _stoch55m2 = np.round((Close[x-2]-np.amin(Low[x-57:x-1]))/(np.amax(High[x-57:x-1])-np.amin(Low[x-57:x-1]))*100,3)
                    _stoch55m3 = np.round((Close[x-3]-np.amin(Low[x-58:x-2]))/(np.amax(High[x-58:x-2])-np.amin(Low[x-58:x-2]))*100,3)
                    _stoch55m4 = np.round((Close[x-4]-np.amin(Low[x-59:x-3]))/(np.amax(High[x-59:x-3])-np.amin(Low[x-59:x-3]))*100,3)
                    _sign5Stoch55 = np.round((_stoch55+_stoch55m1+_stoch55m2+_stoch55m3+_stoch55m4)/5,3)
                    _diffStochSign55 = np.round((_stoch55-_sign5Stoch55)/_sign5Stoch55,2)
                    if _stoch55 > 80:
                        _stoch55Level = 1.0  
                    elif _stoch55 < 20:
                        _stoch55Level = -1.0
                    else:
                        _stoch55Level = 0.0 
    
                    _stoch89 = np.round((Close[x]-np.amin(Low[x-89:x+1]))/(np.amax(High[x-89:x+1])-np.amin(Low[x-89:x+1]))*100,3)
                    _stoch89m1 = np.round((Close[x-1]-np.amin(Low[x-90:x]))/(np.amax(High[x-90:x])-np.amin(Low[x-90:x]))*100,3)
                    _stoch89m2 = np.round((Close[x-2]-np.amin(Low[x-91:x-1]))/(np.amax(High[x-91:x-1])-np.amin(Low[x-91:x-1]))*100,3)
                    _stoch89m3 = np.round((Close[x-3]-np.amin(Low[x-92:x-2]))/(np.amax(High[x-92:x-2])-np.amin(Low[x-92:x-2]))*100,3)
                    _stoch89m4 = np.round((Close[x-4]-np.amin(Low[x-93:x-3]))/(np.amax(High[x-93:x-3])-np.amin(Low[x-93:x-3]))*100,3)
                    _sign5Stoch89 = np.round((_stoch89+_stoch89m1+_stoch89m2+_stoch89m3+_stoch89m4)/5,3)
                    _diffStochSign89 = np.round((_stoch89-_sign5Stoch89)/_sign5Stoch89,2)
                    if _stoch89 > 80:
                        _stoch89Level = 1.0  
                    elif _stoch89 < 20:
                        _stoch89Level = -1.0
                    else:
                        _stoch89Level = 0.0 
    
                    _stoch144 = np.round((Close[x]-np.amin(Low[x-144:x+1]))/(np.amax(High[x-144:x+1])-np.amin(Low[x-144:x+1]))*100,3)
                    _stoch144m1 = np.round((Close[x-1]-np.amin(Low[x-145:x]))/(np.amax(High[x-145:x])-np.amin(Low[x-145:x]))*100,3)
                    _stoch144m2 = np.round((Close[x-2]-np.amin(Low[x-146:x-1]))/(np.amax(High[x-146:x-1])-np.amin(Low[x-146:x-1]))*100,3)
                    _stoch144m3 = np.round((Close[x-3]-np.amin(Low[x-147:x-2]))/(np.amax(High[x-147:x-2])-np.amin(Low[x-147:x-2]))*100,3)
                    _stoch144m4 = np.round((Close[x-4]-np.amin(Low[x-148:x-3]))/(np.amax(High[x-148:x-3])-np.amin(Low[x-148:x-3]))*100,3)
                    _sign5Stoch144 = np.round((_stoch144+_stoch144m1+_stoch144m2+_stoch144m3+_stoch144m4)/5,3)
                    _diffStochSign144 = np.round((_stoch144-_sign5Stoch144)/_sign5Stoch144,2)
                    if _stoch144 > 80:
                        _stoch144Level = 1.0  
                    elif _stoch144 < 20:
                        _stoch144Level = -1.0
                    else:
                        _stoch144Level = 0.0 
    
                    _stoch233 = np.round((Close[x]-np.amin(Low[x-233:x+1]))/(np.amax(High[x-233:x+1])-np.amin(Low[x-233:x+1]))*100,3)
                    _stoch233m1 = np.round((Close[x-1]-np.amin(Low[x-234:x]))/(np.amax(High[x-234:x])-np.amin(Low[x-234:x]))*100,3)
                    _stoch233m2 = np.round((Close[x-2]-np.amin(Low[x-235:x-1]))/(np.amax(High[x-235:x-1])-np.amin(Low[x-235:x-1]))*100,3)
                    _stoch233m3 = np.round((Close[x-3]-np.amin(Low[x-236:x-2]))/(np.amax(High[x-236:x-2])-np.amin(Low[x-236:x-2]))*100,3)
                    _stoch233m4 = np.round((Close[x-4]-np.amin(Low[x-237:x-3]))/(np.amax(High[x-237:x-3])-np.amin(Low[x-237:x-3]))*100,3)
                    _sign5Stoch233 = np.round((_stoch233+_stoch233m1+_stoch233m2+_stoch233m3+_stoch233m4)/5,3)
                    _diffStochSign233 = np.round((_stoch233-_sign5Stoch233)/_sign5Stoch233,2)
                    if _stoch233 > 80:
                        _stoch233Level = 1.0  
                    elif _stoch233 < 20:
                        _stoch233Level = -1.0
                    else:
                        _stoch233Level = 0.0 
    
                    _stoch377 = np.round((Close[x]-np.amin(Low[x-377:x+1]))/(np.amax(High[x-377:x+1])-np.amin(Low[x-377:x+1]))*100,3)
                    _stoch377m1 = np.round((Close[x-1]-np.amin(Low[x-378:x]))/(np.amax(High[x-378:x])-np.amin(Low[x-378:x]))*100,3)
                    _stoch377m2 = np.round((Close[x-2]-np.amin(Low[x-379:x-1]))/(np.amax(High[x-379:x-1])-np.amin(Low[x-379:x-1]))*100,3)
                    _stoch377m3 = np.round((Close[x-3]-np.amin(Low[x-380:x-2]))/(np.amax(High[x-380:x-2])-np.amin(Low[x-380:x-2]))*100,3)
                    _stoch377m4 = np.round((Close[x-4]-np.amin(Low[x-381:x-3]))/(np.amax(High[x-381:x-3])-np.amin(Low[x-381:x-3]))*100,3)
                    _sign5Stoch377 = np.round((_stoch377+_stoch377m1+_stoch377m2+_stoch377m3+_stoch377m4)/5,3)
                    _diffStochSign377 = np.round((_stoch377-_sign5Stoch377)/_sign5Stoch377,2)
                    if _stoch377 > 80:
                        _stoch377Level = 1.0  
                    elif _stoch377 < 20:
                        _stoch377Level = -1.0
                    else:
                        _stoch377Level = 0.0 
    
                    _stoch100 = np.round((Close[x]-np.amin(Low[x-100:x+1]))/(np.amax(High[x-100:x+1])-np.amin(Low[x-100:x+1]))*100,3)
                    _stoch100m1 = np.round((Close[x-1]-np.amin(Low[x-101:x]))/(np.amax(High[x-101:x])-np.amin(Low[x-101:x]))*100,3)
                    _stoch100m2 = np.round((Close[x-2]-np.amin(Low[x-102:x-1]))/(np.amax(High[x-102:x-1])-np.amin(Low[x-102:x-1]))*100,3)
                    _stoch100m3 = np.round((Close[x-3]-np.amin(Low[x-103:x-2]))/(np.amax(High[x-103:x-2])-np.amin(Low[x-103:x-2]))*100,3)
                    _stoch100m4 = np.round((Close[x-4]-np.amin(Low[x-104:x-3]))/(np.amax(High[x-104:x-3])-np.amin(Low[x-104:x-3]))*100,3)
                    _sign5Stoch100 = np.round((_stoch100+_stoch100m1+_stoch100m2+_stoch100m3+_stoch100m4)/5,3)
                    _diffStochSign100 = np.round((_stoch100-_sign5Stoch100)/_sign5Stoch100,2)        
                    if _stoch100 > 80:
                        _stoch100Level = 1.0  
                    elif _stoch100 < 20:
                        _stoch100Level = -1.0
                    else:
                        _stoch100Level = 0.0 
    
                    _stoch200 = np.round((Close[x]-np.amin(Low[x-200:x+1]))/(np.amax(High[x-200:x+1])-np.amin(Low[x-200:x+1]))*100,3)
                    _stoch200m1 = np.round((Close[x-1]-np.amin(Low[x-201:x]))/(np.amax(High[x-201:x])-np.amin(Low[x-201:x]))*100,3)
                    _stoch200m2 = np.round((Close[x-2]-np.amin(Low[x-202:x-1]))/(np.amax(High[x-202:x-1])-np.amin(Low[x-202:x-1]))*100,3)
                    _stoch200m3 = np.round((Close[x-3]-np.amin(Low[x-203:x-2]))/(np.amax(High[x-203:x-2])-np.amin(Low[x-203:x-2]))*100,3)
                    _stoch200m4 = np.round((Close[x-4]-np.amin(Low[x-204:x-3]))/(np.amax(High[x-204:x-3])-np.amin(Low[x-204:x-3]))*100,3)
                    _sign5Stoch200 = np.round((_stoch200+_stoch200m1+_stoch200m2+_stoch200m3+_stoch200m4)/5,3)
                    _diffStochSign200 = np.round((_stoch200-_sign5Stoch200)/_sign5Stoch200,2)
                    if _stoch200 > 80:
                        _stoch200Level = 1.0  
                    elif _stoch200 < 20:
                        _stoch200Level = -1.0
                    else:
                        _stoch200Level = 0.0 
    
                    _stoch300 = np.round((Close[x]-np.amin(Low[x-300:x+1]))/(np.amax(High[x-300:x+1])-np.amin(Low[x-300:x+1]))*100,3)
                    _stoch300m1 = np.round((Close[x-1]-np.amin(Low[x-301:x]))/(np.amax(High[x-301:x])-np.amin(Low[x-301:x]))*100,3)
                    _stoch300m2 = np.round((Close[x-2]-np.amin(Low[x-302:x-1]))/(np.amax(High[x-302:x-1])-np.amin(Low[x-302:x-1]))*100,3)
                    _stoch300m3 = np.round((Close[x-3]-np.amin(Low[x-303:x-2]))/(np.amax(High[x-303:x-2])-np.amin(Low[x-303:x-2]))*100,3)
                    _stoch300m4 = np.round((Close[x-4]-np.amin(Low[x-304:x-3]))/(np.amax(High[x-304:x-3])-np.amin(Low[x-304:x-3]))*100,3)
                    _sign5Stoch300 = np.round((_stoch300+_stoch300m1+_stoch300m2+_stoch300m3+_stoch300m4)/5,3)
                    _diffStochSign300 = np.round((_stoch300-_sign5Stoch300)/_sign5Stoch300,2)
                    if _stoch300 > 80:
                        _stoch300Level = 1.0  
                    elif _stoch300 < 20:
                        _stoch300Level = -1.0
                    else:
                        _stoch300Level = 0.0 
                
                    _Low3_L = np.round((Close[x]-np.amin(Low[x+1-3:x+1]))/np.amin(Low[x+1-3:x+1]),3)
                    _Low4_L = np.round((Close[x]-np.amin(Low[x+1-4:x+1]))/np.amin(Low[x+1-4:x+1]),3)
                    _Low5_L = np.round((Close[x]-np.amin(Low[x+1-5:x+1]))/np.amin(Low[x+1-5:x+1]),3)
                    _Low6_L = np.round((Close[x]-np.amin(Low[x+1-6:x+1]))/np.amin(Low[x+1-6:x+1]),3)            
                    _Low7_L = np.round((Close[x]-np.amin(Low[x+1-7:x+1]))/np.amin(Low[x+1-7:x+1]),3)   
                    _Low8_L = np.round((Close[x]-np.amin(Low[x+1-8:x+1]))/np.amin(Low[x+1-8:x+1]),3)   
                    _Low9_L = np.round((Close[x]-np.amin(Low[x+1-9:x+1]))/np.amin(Low[x+1-9:x+1]),3)   
                    _Low10_L = np.round((Close[x]-np.amin(Low[x+1-10:x+1]))/np.amin(Low[x+1-10:x+1]),3)   
                    _Low11_L = np.round((Close[x]-np.amin(Low[x+1-11:x+1]))/np.amin(Low[x+1-11:x+1]),3)   
                    _Low12_L = np.round((Close[x]-np.amin(Low[x+1-12:x+1]))/np.amin(Low[x+1-12:x+1]),3)   
                    _Low13_L = np.round((Close[x]-np.amin(Low[x+1-13:x+1]))/np.amin(Low[x+1-13:x+1]),3)   
                    _Low14_L = np.round((Close[x]-np.amin(Low[x+1-14:x+1]))/np.amin(Low[x+1-14:x+1]),3)   
                    _Low15_L = np.round((Close[x]-np.amin(Low[x+1-15:x+1]))/np.amin(Low[x+1-15:x+1]),3)   
                    _Low17_L = np.round((Close[x]-np.amin(Low[x+1-17:x+1]))/np.amin(Low[x+1-17:x+1]),3)   
                    _Low19_L = np.round((Close[x]-np.amin(Low[x+1-19:x+1]))/np.amin(Low[x+1-19:x+1]),3)   
                    _Low21_L = np.round((Close[x]-np.amin(Low[x+1-21:x+1]))/np.amin(Low[x+1-21:x+1]),3)   
                    _Low23_L = np.round((Close[x]-np.amin(Low[x+1-23:x+1]))/np.amin(Low[x+1-23:x+1]),3)   
                    _Low25_L = np.round((Close[x]-np.amin(Low[x+1-25:x+1]))/np.amin(Low[x+1-25:x+1]),3)   
                    _Low34_L = np.round((Close[x]-np.amin(Low[x+1-34:x+1]))/np.amin(Low[x+1-34:x+1]),3)   
                    _Low55_L = np.round((Close[x]-np.amin(Low[x+1-55:x+1]))/np.amin(Low[x+1-55:x+1]),3)   
                    _Low89_L = np.round((Close[x]-np.amin(Low[x+1-89:x+1]))/np.amin(Low[x+1-89:x+1]),3)   
                    _Low144_L = np.round((Close[x]-np.amin(Low[x+1-144:x+1]))/np.amin(Low[x+1-144:x+1]),3)   
                    _Low233_L = np.round((Close[x]-np.amin(Low[x+1-233:x+1]))/np.amin(Low[x+1-233:x+1]),3)   
                    _Low377_L = np.round((Close[x]-np.amin(Low[x+1-377:x+1]))/np.amin(Low[x+1-377:x+1]),3)   
    
                    _High3_H = np.round((Close[x]-np.amax(High[x+1-3:x+1]))/np.amax(High[x+1-3:x+1]),3)
                    _High4_H = np.round((Close[x]-np.amax(High[x+1-4:x+1]))/np.amax(High[x+1-4:x+1]),3)
                    _High5_H = np.round((Close[x]-np.amax(High[x+1-5:x+1]))/np.amax(High[x+1-5:x+1]),3)
                    _High6_H = np.round((Close[x]-np.amax(High[x+1-6:x+1]))/np.amax(High[x+1-6:x+1]),3)
                    _High7_H = np.round((Close[x]-np.amax(High[x+1-7:x+1]))/np.amax(High[x+1-7:x+1]),3)   
                    _High8_H = np.round((Close[x]-np.amax(High[x+1-8:x+1]))/np.amax(High[x+1-8:x+1]),3)   
                    _High9_H = np.round((Close[x]-np.amax(High[x+1-9:x+1]))/np.amax(High[x+1-9:x+1]),3)   
                    _High10_H = np.round((Close[x]-np.amax(High[x+1-10:x+1]))/np.amax(High[x+1-10:x+1]),3)   
                    _High11_H = np.round((Close[x]-np.amax(High[x+1-11:x+1]))/np.amax(High[x+1-11:x+1]),3)   
                    _High12_H = np.round((Close[x]-np.amax(High[x+1-12:x+1]))/np.amax(High[x+1-12:x+1]),3)   
                    _High13_H = np.round((Close[x]-np.amax(High[x+1-13:x+1]))/np.amax(High[x+1-13:x+1]),3)   
                    _High14_H = np.round((Close[x]-np.amax(High[x+1-14:x+1]))/np.amax(High[x+1-14:x+1]),3)   
                    _High15_H = np.round((Close[x]-np.amax(High[x+1-15:x+1]))/np.amax(High[x+1-15:x+1]),3)   
                    _High17_H = np.round((Close[x]-np.amax(High[x+1-17:x+1]))/np.amax(High[x+1-17:x+1]),3)   
                    _High19_H = np.round((Close[x]-np.amax(High[x+1-19:x+1]))/np.amax(High[x+1-19:x+1]),3)   
                    _High21_H = np.round((Close[x]-np.amax(High[x+1-21:x+1]))/np.amax(High[x+1-21:x+1]),3)   
                    _High23_H = np.round((Close[x]-np.amax(High[x+1-23:x+1]))/np.amax(High[x+1-23:x+1]),3)   
                    _High25_H = np.round((Close[x]-np.amax(High[x+1-25:x+1]))/np.amax(High[x+1-25:x+1]),3)   
                    _High34_H = np.round((Close[x]-np.amax(High[x+1-34:x+1]))/np.amax(High[x+1-34:x+1]),3)   
                    _High55_H = np.round((Close[x]-np.amax(High[x+1-55:x+1]))/np.amax(High[x+1-55:x+1]),3)   
                    _High89_H = np.round((Close[x]-np.amax(High[x+1-89:x+1]))/np.amax(High[x+1-89:x+1]),3)   
                    _High144_H = np.round((Close[x]-np.amax(High[x+1-144:x+1]))/np.amax(High[x+1-144:x+1]),3)   
                    _High233_H = np.round((Close[x]-np.amax(High[x+1-233:x+1]))/np.amax(High[x+1-233:x+1]),3)   
                    _High377_H = np.round((Close[x]-np.amax(High[x+1-377:x+1]))/np.amax(High[x+1-377:x+1]),3)

                    _Return01 = np.round((Close[x+1]-Close[x])/Close[x],4)
                    _Return02 = np.round((Close[x+2]-Close[x])/Close[x],4)
                    _Return03 = np.round((Close[x+3]-Close[x])/Close[x],4)
                    _Return04 = np.round((Close[x+4]-Close[x])/Close[x],4)
                    _Return05 = np.round((Close[x+5]-Close[x])/Close[x],4)
                    _Return08 = np.round((Close[x+8]-Close[x])/Close[x],4)
                    _Return13 = np.round((Close[x+13]-Close[x])/Close[x],4)
                    _Return21 = np.round((Close[x+21]-Close[x])/Close[x],4)
                    _Return34 = np.round((Close[x+34]-Close[x])/Close[x],4)

                except Exception as e:
                    print("ERROR: " + str(e))
            
                ### END calculation of choosen list of FEATURES for the MACHINE LEARNING process ###            
            
                ### START part where to write every Future value and Feature, day by day and intrument by instrument to .txt file to read csv style. 
                LocationToSave = os.path.join(preProcessPath, config.preProcess.featuresFileName)
                saveFile = open(LocationToSave,'a')
                lineToWrite = (
                            str(_justOpen) + ',' +
                            str(_justHigh) + ',' +
                            str(_justLow) + ',' +
                            str(_justClose) + ',' +                        
                            str(instrument) + ',' +
                            str(_DateStamp) + ',' +
                            str(_Return01) + ',' +
                            str(Tgt_SCH05to08) + ',' +
                            str(Tgt_SCH05to13) + ',' +
                            str(Tgt_SCH05to21) + ',' +
                            str(Tgt_SCH05to34) + ',' +
                            str(Tgt_SCH08to13) + ',' +
                            str(Tgt_SCH08to21) + ',' +
                            str(Tgt_SCH08to34) + ',' +
                            str(Tgt_SCH13to21) + ',' +
                            str(Tgt_SCH13to34) + ',' +
                            str(Tgt_SCH21to34) + ',' +
                            str(_PastSCH05to08) + ',' +
                            str(_PastSCH05to13) + ',' +
                            str(_PastSCH05to21) + ',' +
                            str(_PastSCH05to34) + ',' +
                            str(_PastSCH08to13) + ',' +
                            str(_PastSCH08to21) + ',' +
                            str(_PastSCH08to34) + ',' +
                            str(_PastSCH13to21) + ',' +
                            str(_PastSCH13to34) + ',' +
                            str(_PastSCH21to34) + ',' +
                            str(_Diff_CtoH) + ',' +
                            str(_Diff_CtoH1) + ',' +
                            str(_Diff_CtoH2) + ',' +
                            str(_Diff_CtoH3) + ',' +
                            str(_Diff_CtoH4) + ',' +
                            str(_Diff_CtoH5) + ',' +
                            str(_Diff_CtoH6) + ',' +
                            str(_Diff_CtoH7) + ',' +
                            str(_Diff_CtoH8) + ',' +
                            str(_Diff_CtoH9) + ',' +
                            str(_Diff_CtoH10) + ',' +
                            str(_Diff_CtoH11) + ',' +
                            str(_Diff_CtoH12) + ',' +
                            str(_Diff_CtoH13) + ',' +
                            str(_Diff_CtoH14) + ',' +
                            str(_Diff_CtoH15) + ',' +
                            str(_Diff_CtoH16) + ',' +
                            str(_Diff_CtoH17) + ',' +
                            str(_Diff_CtoH18) + ',' +
                            str(_Diff_CtoH19) + ',' +
                            str(_Diff_CtoH20) + ',' +
                            str(_Diff_CtoH21) + ',' +
                            str(_Diff_CtoH22) + ',' +
                            str(_Diff_CtoH23) + ',' +
                            str(_Diff_CtoH24) + ',' +
                            str(_Diff_CtoH25) + ',' +
                            str(_Diff_CtoL) + ',' +
                            str(_Diff_CtoL1) + ',' +
                            str(_Diff_CtoL2) + ',' +
                            str(_Diff_CtoL3) + ',' +
                            str(_Diff_CtoL4) + ',' +
                            str(_Diff_CtoL5) + ',' +
                            str(_Diff_CtoL6) + ',' +
                            str(_Diff_CtoL7) + ',' +
                            str(_Diff_CtoL8) + ',' +
                            str(_Diff_CtoL9) + ',' +
                            str(_Diff_CtoL10) + ',' +
                            str(_Diff_CtoL11) + ',' +
                            str(_Diff_CtoL12) + ',' +
                            str(_Diff_CtoL13) + ',' +
                            str(_Diff_CtoL14) + ',' +
                            str(_Diff_CtoL15) + ',' +
                            str(_Diff_CtoL16) + ',' +
                            str(_Diff_CtoL17) + ',' +
                            str(_Diff_CtoL18) + ',' +
                            str(_Diff_CtoL19) + ',' +
                            str(_Diff_CtoL20) + ',' +
                            str(_Diff_CtoL21) + ',' +
                            str(_Diff_CtoL22) + ',' +
                            str(_Diff_CtoL23) + ',' +
                            str(_Diff_CtoL24) + ',' +
                            str(_Diff_CtoL25) + ',' +
                            str(_Diff_CtoO) + ',' +
                            str(_Diff_CtoO1) + ',' +
                            str(_Diff_CtoO2) + ',' +
                            str(_Diff_CtoO3) + ',' +
                            str(_Diff_CtoO4) + ',' +
                            str(_Diff_CtoO5) + ',' +
                            str(_Diff_CtoO6) + ',' +
                            str(_Diff_CtoO7) + ',' +
                            str(_Diff_CtoO8) + ',' +
                            str(_Diff_CtoO9) + ',' +
                            str(_Diff_CtoC1) + ',' +
                            str(_Diff_CtoC2) + ',' +
                            str(_Diff_CtoC3) + ',' +
                            str(_Diff_CtoC4) + ',' +
                            str(_Diff_CtoC5) + ',' +
                            str(_Diff_CtoC6) + ',' +
                            str(_Diff_CtoC7) + ',' +
                            str(_Diff_CtoC8) + ',' +
                            str(_Diff_CtoC9) + ',' +
                            str(_SMA_H3) + ',' +
                            str(_SMA_L3) + ',' +
                            str(_BBU3) + ',' +
                            str(_BBD3) + ',' +
                            str(_DiffU3_C) + ',' +
                            str(_DiffU3_L3) + ',' +
                            str(_DiffD3_C) + ',' +
                            str(_DiffD3_H3) + ',' +
                            str(_BBU5) + ',' +
                            str(_BBD5) + ',' +
                            str(_DiffU5_C) + ',' +
                            str(_DiffU5_L3) + ',' +
                            str(_DiffD5_C) + ',' +
                            str(_DiffD5_H3) + ',' +
                            str(_BBU8) + ',' +
                            str(_BBD8) + ',' +
                            str(_DiffU8_C) + ',' +
                            str(_DiffU8_L3) + ',' +
                            str(_DiffD8_C) + ',' +
                            str(_DiffD8_H3) + ',' +
                            str(_BBU13) + ',' +
                            str(_BBD13) + ',' +
                            str(_DiffU13_C) + ',' +
                            str(_DiffU13_L3) + ',' +
                            str(_DiffD13_C) + ',' +
                            str(_DiffD13_H3) + ',' +
                            str(_BBU21) + ',' +
                            str(_BBD21) + ',' +
                            str(_DiffU21_C) + ',' +
                            str(_DiffU21_L3) + ',' +
                            str(_DiffD21_C) + ',' +
                            str(_DiffD21_H3) + ',' +
                            str(_BBU34) + ',' +
                            str(_BBD34) + ',' +
                            str(_DiffU34_C) + ',' +
                            str(_DiffU34_L3) + ',' +
                            str(_DiffD34_C) + ',' +
                            str(_DiffD34_H3) + ',' +
                            str(_BBU55) + ',' +
                            str(_BBD55) + ',' +
                            str(_DiffU55_C) + ',' +
                            str(_DiffU55_L3) + ',' +
                            str(_DiffD55_C) + ',' +
                            str(_DiffD55_H3) + ',' +
                            str(_BBU89) + ',' +
                            str(_BBD89) + ',' +
                            str(_DiffU89_C) + ',' +
                            str(_DiffU89_L3) + ',' +
                            str(_DiffD89_C) + ',' +
                            str(_DiffD89_H3) + ',' +
                            str(_BBU100) + ',' +
                            str(_BBD100) + ',' +
                            str(_DiffU100_C) + ',' +
                            str(_DiffU100_L3) + ',' +
                            str(_DiffD100_C) + ',' +
                            str(_DiffD100_H3) + ',' +
                            str(_BBU144) + ',' +
                            str(_BBD144) + ',' +
                            str(_DiffU144_C) + ',' +
                            str(_DiffU144_L3) + ',' +
                            str(_DiffD144_C) + ',' +
                            str(_DiffD144_H3) + ',' +
                            str(_BBU200) + ',' +
                            str(_BBD200) + ',' +
                            str(_DiffU200_C) + ',' +
                            str(_DiffU200_L3) + ',' +
                            str(_DiffD200_C) + ',' +
                            str(_DiffD200_H3) + ',' +
                            str(_BBU233) + ',' +
                            str(_BBD233) + ',' +
                            str(_DiffU233_C) + ',' +
                            str(_DiffU233_L3) + ',' +
                            str(_DiffD233_C) + ',' +
                            str(_DiffD233_H3) + ',' +
                            str(_BBU300) + ',' +
                            str(_BBD300) + ',' +
                            str(_DiffU300_C) + ',' +
                            str(_DiffU300_L3) + ',' +
                            str(_DiffD300_C) + ',' +
                            str(_DiffD300_H3) + ',' +
                            str(_BBU377) + ',' +
                            str(_BBD377) + ',' +
                            str(_DiffU377_C) + ',' +
                            str(_DiffU377_L3) + ',' +
                            str(_DiffD377_C) + ',' +
                            str(_DiffD377_H3) + ',' +
                            str(_dateDayOfYear) + ',' +
                            str(_dateWeekOfYear) + ',' +
                            str(_dateMonthOfYear) + ',' +
                            str(_dateDayOfMonth) + ',' +
                            str(_dateDayOfWeek) + ',' +
                            str(_EvNo5) + ',' +
                            str(_EvNo10) + ',' +
                            str(_EvNo20) + ',' +
                            str(_EvNo30) + ',' +
                            str(_EvNo40) + ',' +
                            str(_EvNo50) + ',' +
                            str(_EvNo60) + ',' +
                            str(_EvNo70) + ',' +
                            str(_EvNo80) + ',' +
                            str(_EvNo90) + ',' +
                            str(_EvNo100) + ',' +
                            str(_EvNo200) + ',' +
                            str(_EvNo300) + ',' +
                            str(_EvNo400) + ',' +
                            str(_EvNo500) + ',' +
                            str(_EvNo600) + ',' +
                            str(_EvNo700) + ',' +
                            str(_EvNo800) + ',' +
                            str(_EvNo900) + ',' +
                            str(_EvNo1000) + ',' +
                            str(_EvNo2000) + ',' +
                            str(_EvNo3000) + ',' +
                            str(_EvNo4000) + ',' +
                            str(_EvNo5000) + ',' +
                            str(_EvNo10000) + ',' +
                            str(_Perc3_H) + ',' +
                            str(_Perc5_H) + ',' +
                            str(_Perc8_H) + ',' +
                            str(_Perc13_H) + ',' +
                            str(_Perc21_H) + ',' +
                            str(_Perc34_H) + ',' +
                            str(_Perc55_H) + ',' +
                            str(_Perc89_H) + ',' +
                            str(_Perc100_H) + ',' +
                            str(_Perc144_H) + ',' +
                            str(_Perc200_H) + ',' +
                            str(_Perc233_H) + ',' +
                            str(_Perc377_H) + ',' +
                            str(_Perc3_L) + ',' +
                            str(_Perc5_L) + ',' +
                            str(_Perc8_L) + ',' +
                            str(_Perc13_L) + ',' +
                            str(_Perc21_L) + ',' +
                            str(_Perc34_L) + ',' +
                            str(_Perc55_L) + ',' +
                            str(_Perc89_L) + ',' +
                            str(_Perc100_L) + ',' +
                            str(_Perc144_L) + ',' +
                            str(_Perc200_L) + ',' +
                            str(_Perc233_L) + ',' +
                            str(_Perc377_L) + ',' +
                            str(_Perc3_H80) + ',' +
                            str(_Perc5_H80) + ',' +
                            str(_Perc8_H80) + ',' +
                            str(_Perc13_H80) + ',' +
                            str(_Perc21_H80) + ',' +
                            str(_Perc34_H80) + ',' +
                            str(_Perc55_H80) + ',' +
                            str(_Perc89_H80) + ',' +
                            str(_Perc100_H80) + ',' +
                            str(_Perc144_H80) + ',' +
                            str(_Perc200_H80) + ',' +
                            str(_Perc233_H80) + ',' +
                            str(_Perc377_H80) + ',' +
                            str(_Perc3_L20) + ',' +
                            str(_Perc5_L20) + ',' +
                            str(_Perc8_L20) + ',' +
                            str(_Perc13_L20) + ',' +
                            str(_Perc21_L20) + ',' +
                            str(_Perc34_L20) + ',' +
                            str(_Perc55_L20) + ',' +
                            str(_Perc89_L20) + ',' +
                            str(_Perc100_L20) + ',' +
                            str(_Perc144_L20) + ',' +
                            str(_Perc200_L20) + ',' +
                            str(_Perc233_L20) + ',' +
                            str(_Perc377_L20) + ',' +
                            str(_Perc3_M50) + ',' +
                            str(_Perc5_M50) + ',' +
                            str(_Perc8_M50) + ',' +
                            str(_Perc13_M50) + ',' +
                            str(_Perc21_M50) + ',' +
                            str(_Perc34_M50) + ',' +
                            str(_Perc55_M50) + ',' +
                            str(_Perc89_M50) + ',' +
                            str(_Perc100_M50) + ',' +
                            str(_Perc144_M50) + ',' +
                            str(_Perc200_M50) + ',' +
                            str(_Perc233_M50) + ',' +
                            str(_Perc377_M50) + ',' +
                            str(RL3) + ',' +
                            str(RL5) + ',' +
                            str(RL8) + ',' +
                            str(RL13) + ',' +
                            str(RL21) + ',' +
                            str(RL34) + ',' +
                            str(RL55) + ',' +
                            str(RL89) + ',' +
                            str(RL100) + ',' +
                            str(RL144) + ',' +
                            str(RL200) + ',' +
                            str(RL233) + ',' +
                            str(RL377) + ',' +
                            str(Diff_C_RL3) + ',' +
                            str(Diff_C_RL5) + ',' +
                            str(Diff_C_RL8) + ',' +
                            str(Diff_C_RL13) + ',' +
                            str(Diff_C_RL21) + ',' +
                            str(Diff_C_RL34) + ',' +
                            str(Diff_C_RL55) + ',' +
                            str(Diff_C_RL89) + ',' +
                            str(Diff_C_RL100) + ',' +
                            str(Diff_C_RL144) + ',' +
                            str(Diff_C_RL200) + ',' +
                            str(Diff_C_RL233) + ',' +
                            str(Diff_C_RL377) + ',' +
                            str(Diff_RL3_RL5) + ',' +
                            str(Diff_RL3_RL8) + ',' +
                            str(Diff_RL3_RL13) + ',' +
                            str(Diff_RL3_RL21) + ',' +
                            str(Diff_RL3_RL34) + ',' +
                            str(Diff_RL5_RL8) + ',' +
                            str(Diff_RL5_RL13) + ',' +
                            str(Diff_RL5_RL21) + ',' +
                            str(Diff_RL5_RL34) + ',' +
                            str(Diff_RL5_RL55) + ',' +
                            str(Diff_RL8_RL13) + ',' +
                            str(Diff_RL8_RL21) + ',' +
                            str(Diff_RL8_RL34) + ',' +
                            str(Diff_RL8_RL55) + ',' +
                            str(Diff_RL8_RL89) + ',' +
                            str(Diff_RL13_RL21) + ',' +
                            str(Diff_RL13_RL34) + ',' +
                            str(Diff_RL13_RL55) + ',' +
                            str(Diff_RL13_RL139) + ',' +
                            str(Diff_RL13_RL100) + ',' +
                            str(Diff_RL21_RL34) + ',' +
                            str(Diff_RL21_RL55) + ',' +
                            str(Diff_RL21_RL89) + ',' +
                            str(Diff_RL21_RL100) + ',' +
                            str(Diff_RL21_RL144) + ',' +
                            str(Diff_RL34_RL55) + ',' +
                            str(Diff_RL34_RL89) + ',' +
                            str(Diff_RL34_RL100) + ',' +
                            str(Diff_RL34_RL144) + ',' +
                            str(Diff_RL34_RL200) + ',' +
                            str(Diff_RL55_RL89) + ',' +
                            str(Diff_RL55_RL100) + ',' +
                            str(Diff_RL55_RL144) + ',' +
                            str(Diff_RL55_RL200) + ',' +
                            str(Diff_RL55_RL233) + ',' +
                            str(Diff_RL89_RL100) + ',' +
                            str(Diff_RL89_RL144) + ',' +
                            str(Diff_RL89_RL200) + ',' +
                            str(Diff_RL89_RL233) + ',' +
                            str(Diff_RL89_RL377) + ',' +
                            str(Diff_RL100_RL144) + ',' +
                            str(Diff_RL100_RL200) + ',' +
                            str(Diff_RL100_RL233) + ',' +
                            str(Diff_RL100_RL377) + ',' +
                            str(Diff_RL144_RL200) + ',' +
                            str(Diff_RL144_RL233) + ',' +
                            str(Diff_RL144_RL377) + ',' +
                            str(Diff_RL200_RL233) + ',' +
                            str(Diff_RL200_RL377) + ',' +
                            str(Diff_RL233_RL377) + ',' +
                            str(_SMA3_C) + ',' +
                            str(_SMA5_C) + ',' +
                            str(_SMA8_C) + ',' +
                            str(_SMA13_C) + ',' +
                            str(_SMA21_C) + ',' +
                            str(_SMA34_C) + ',' +
                            str(_SMA55_C) + ',' +
                            str(_SMA89_C) + ',' +
                            str(_SMA144_C) + ',' +
                            str(_SMA233_C) + ',' +
                            str(_SMA377_C) + ',' +
                            str(_SMA100_C) + ',' +
                            str(_SMA200_C) + ',' +
                            str(_SMA300_C) + ',' +
                            str(_SMA3vs5) + ',' +
                            str(_SMA3vs8) + ',' +
                            str(_SMA3vs13) + ',' +
                            str(_SMA3vs21) + ',' +
                            str(_SMA3vs34) + ',' +
                            str(_SMA5vs8) + ',' +
                            str(_SMA5vs13) + ',' +
                            str(_SMA5vs21) + ',' +
                            str(_SMA5vs34) + ',' +
                            str(_SMA5vs55) + ',' +
                            str(_SMA8vs13) + ',' +
                            str(_SMA8vs21) + ',' +
                            str(_SMA8vs34) + ',' +
                            str(_SMA8vs55) + ',' +
                            str(_SMA8vs89) + ',' +
                            str(_SMA13vs21) + ',' +
                            str(_SMA13vs34) + ',' +
                            str(_SMA13vs55) + ',' +
                            str(_SMA13vs89) + ',' +
                            str(_SMA13vs144) + ',' +
                            str(_SMA21vs34) + ',' +
                            str(_SMA21vs55) + ',' +
                            str(_SMA21vs89) + ',' +
                            str(_SMA21vs144) + ',' +
                            str(_SMA21vs233) + ',' +
                            str(_SMA34vs55) + ',' +
                            str(_SMA34vs89) + ',' +
                            str(_SMA34vs144) + ',' +
                            str(_SMA34vs233) + ',' +
                            str(_SMA34vs377) + ',' +
                            str(_SMA55vs89) + ',' +
                            str(_SMA55vs144) + ',' +
                            str(_SMA55vs233) + ',' +
                            str(_SMA55vs377) + ',' +
                            str(_SMA89vs144) + ',' +
                            str(_SMA89vs233) + ',' +
                            str(_SMA89vs377) + ',' +
                            str(_SMA144vs233) + ',' +
                            str(_SMA144vs377) + ',' +
                            str(_SMA233vs377) + ',' +
                            str(_STD3_C) + ',' +
                            str(_STD3sign) + ',' +
                            str(_STD3vsSign) + ',' +
                            str(_STD5_C) + ',' +
                            str(_STD5sign) + ',' +
                            str(_STD5vsSign) + ',' +
                            str(_STD8_C) + ',' +
                            str(_STD8sign) + ',' +
                            str(_STD8vsSign) + ',' +
                            str(_STD13_C) + ',' +
                            str(_STD13sign) + ',' +
                            str(_STD13vsSign) + ',' +
                            str(_STD21_C) + ',' +
                            str(_STD21sign) + ',' +
                            str(_STD21vsSign) + ',' +
                            str(_STD34_C) + ',' +
                            str(_STD34sign) + ',' +
                            str(_STD34vsSign) + ',' +
                            str(_STD55_C) + ',' +
                            str(_STD55sign) + ',' +
                            str(_STD55vsSign) + ',' +
                            str(_STD89_C) + ',' +
                            str(_STD89sign) + ',' +
                            str(_STD89vsSign) + ',' +
                            str(_STD144_C) + ',' +
                            str(_STD144sign) + ',' +
                            str(_STD144vsSign) + ',' +
                            str(_STD233_C) + ',' +
                            str(_STD233sign) + ',' +
                            str(_STD233vsSign) + ',' +
                            str(_STD377_C) + ',' +
                            str(_STD377sign) + ',' +
                            str(_STD377vsSign) + ',' +
                            str(_STD100_C) + ',' +
                            str(_STD100sign) + ',' +
                            str(_STD100vsSign) + ',' +
                            str(_STD200_C) + ',' +
                            str(_STD200sign) + ',' +
                            str(_STD200vsSign) + ',' +
                            str(_STD300_C) + ',' +
                            str(_STD300sign) + ',' +
                            str(_STD300vsSign) + ',' +
                            str(_stoch5) + ',' +
                            str(_sign5Stoch5) + ',' +
                            str(_diffStochSign5) + ',' +
                            str(_stoch5Level) + ',' +
                            str(_stoch14) + ',' +
                            str(_stoch8) + ',' +
                            str(_sign5Stoch8) + ',' +
                            str(_diffStochSign8) + ',' +
                            str(_stoch8Level) + ',' +
                            str(_stoch14) + ',' +
                            str(_sign5Stoch8) + ',' +
                            str(_diffStochSign14) + ',' +
                            str(_stoch14Level) + ',' +
                            str(_stoch21) + ',' +
                            str(_sign5Stoch21) + ',' +
                            str(_diffStochSign21) + ',' +
                            str(_stoch21Level) + ',' +
                            str(_stoch34) + ',' +
                            str(_sign5Stoch34) + ',' +
                            str(_diffStochSign34) + ',' +
                            str(_stoch34Level) + ',' +
                            str(_stoch55) + ',' +
                            str(_sign5Stoch55) + ',' +
                            str(_diffStochSign55) + ',' +
                            str(_stoch55Level) + ',' +
                            str(_stoch89) + ',' +
                            str(_sign5Stoch89) + ',' +
                            str(_diffStochSign89) + ',' +
                            str(_stoch89Level) + ',' +
                            str(_stoch144) + ',' +
                            str(_sign5Stoch144) + ',' +
                            str(_diffStochSign144) + ',' +
                            str(_stoch144Level) + ',' +
                            str(_stoch233) + ',' +
                            str(_sign5Stoch233) + ',' +
                            str(_diffStochSign233) + ',' +
                            str(_stoch233Level) + ',' +
                            str(_stoch377) + ',' +
                            str(_sign5Stoch377) + ',' +
                            str(_diffStochSign377) + ',' +
                            str(_stoch377Level) + ',' +
                            str(_stoch100) + ',' +
                            str(_sign5Stoch100) + ',' +
                            str(_diffStochSign100) + ',' +
                            str(_stoch100Level) + ',' +
                            str(_stoch200) + ',' +
                            str(_sign5Stoch200) + ',' +
                            str(_diffStochSign200) + ',' +
                            str(_stoch200Level) + ',' +
                            str(_stoch300) + ',' +
                            str(_sign5Stoch300) + ',' +
                            str(_diffStochSign300) + ',' +
                            str(_stoch300Level) + ',' +
                            str(_Low3_L) + ',' +
                            str(_Low4_L) + ',' +
                            str(_Low5_L) + ',' +
                            str(_Low6_L) + ',' +
                            str(_Low7_L) + ',' +
                            str(_Low8_L) + ',' +
                            str(_Low9_L) + ',' +
                            str(_Low10_L) + ',' +
                            str(_Low11_L) + ',' +
                            str(_Low12_L) + ',' +
                            str(_Low13_L) + ',' +
                            str(_Low14_L) + ',' +
                            str(_Low15_L) + ',' +
                            str(_Low17_L) + ',' +
                            str(_Low19_L) + ',' +
                            str(_Low21_L) + ',' +
                            str(_Low23_L) + ',' +
                            str(_Low25_L) + ',' +
                            str(_Low34_L) + ',' +
                            str(_Low55_L) + ',' +
                            str(_Low89_L) + ',' +
                            str(_Low144_L) + ',' +
                            str(_Low233_L) + ',' +
                            str(_Low377_L) + ',' +
                            str(_High3_H) + ',' +
                            str(_High4_H) + ',' +
                            str(_High5_H) + ',' +
                            str(_High6_H) + ',' +
                            str(_High7_H) + ',' +
                            str(_High8_H) + ',' +
                            str(_High9_H) + ',' +
                            str(_High10_H) + ',' +
                            str(_High11_H) + ',' +
                            str(_High12_H) + ',' +
                            str(_High13_H) + ',' +
                            str(_High14_H) + ',' +
                            str(_High15_H) + ',' +
                            str(_High17_H) + ',' +
                            str(_High19_H) + ',' +
                            str(_High21_H) + ',' +
                            str(_High23_H) + ',' +
                            str(_High25_H) + ',' +
                            str(_High34_H) + ',' +
                            str(_High55_H) + ',' +
                            str(_High89_H) + ',' +
                            str(_High144_H) + ',' +
                            str(_High233_H) + ',' +
                            str(_High377_H) + '\n'     
                            )
            
                saveFile.write(lineToWrite)
                saveFile.close() 
            else:
                print("Skipped {0}".format(x))
        except Exception as e:
            print("ERROR: " + str(e))
    print("Appended lines of features to {}".format(LocationToSave))
    c.timer.print_elapsed("Completed processing of {0}".format(instrumentName))

    numCompleted+=1
### END part where to write every Future value and Feature, day by day and intrument by instrument to .txt file to read csv style. 
        
c.timer.print_elapsed('Completed preprocessing {0} files with ticker data ({1} failed) from {2}'.format(numCompleted, numFailed, instrumentPath))
