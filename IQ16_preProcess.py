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

IMUNDBO QUANT v1.6 (Preprocessing script)
"""

import numpy as np
import pandas as pd
import urllib2
import time
import datetime
import os
import csv
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.dates import strpdate2num

#put in your path to the folder of your instrument files
path = r'C:\Users\UserTrader\Documents\StockDataEOD_5save'  


instList = []
instList = os.listdir(path)

print('OK1')
startTime = time.time()

for eachTicker in instList:
    print(eachTicker)
    FileLocation = path + '\\'+ eachTicker
    Date, Open, High, Low, Close, Volume = np.loadtxt(FileLocation, delimiter=',', unpack=True,converters={ 0: mdates.strpdate2num('%m/%d/%Y')})
                     
    Zeros = [1]*len(Date) #making extra data array with "1" for future calculation of MA with linear regression
    noInstList = len(Date) #skip the last 60 days for making space for P/L calculation for at most 34 days
    for x in range(400, noInstList-23): #skip the last 400 days for making space to calculate indicatiors that need 377 past days

### START First part -  calculate on how high the Risk/Reward Ratio is for future move in 1,2,3,5,8,13,21 days 
        try:
            try:            
                _Diff_CpLf = ((Low[x+1])-Close[x])/Close[x]
                _Diff_CpHf = ((High[x+1])-Close[x])/Close[x]
                _CpHf_Less_CpLf = _Diff_CpHf + _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _01KeyValueLong = _CpHf_Less_CpLf/_ABSofDiff_CpLf
                _01KeyValueShort = _CpHf_Less_CpLf/_ABSofDiff_CpHf
            except Exception as e:
                print(str('part1'))
            try:
                _Diff_CpLf = ((Low[x+2])-Close[x])/Close[x]
                _Diff_CpHf = ((High[x+2])-Close[x])/Close[x]
                _CpHf_Less_CpLf = _Diff_CpHf + _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _02KeyValueLong = _CpHf_Less_CpLf/_ABSofDiff_CpLf           
                _02KeyValueShort = _CpHf_Less_CpLf/_ABSofDiff_CpHf
            except Exception as e:
                print(str('part2'))            
            try:
                _Diff_CpLf = ((Low[x+3])-Close[x])/Close[x]
                _Diff_CpHf = ((High[x+3])-Close[x])/Close[x]
                _CpHf_Less_CpLf = _Diff_CpHf + _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _03KeyValueLong = _CpHf_Less_CpLf/_ABSofDiff_CpLf            
                _03KeyValueShort = _CpHf_Less_CpLf/_ABSofDiff_CpHf
            except Exception as e:
                print(str('part3'))            
            
            try:
                _Diff_CpLf = ((Low[x+5])-Close[x])/Close[x]
                _Diff_CpHf = ((High[x+5])-Close[x])/Close[x]
                _CpHf_Less_CpLf = _Diff_CpHf + _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _05KeyValueLong = _CpHf_Less_CpLf/_ABSofDiff_CpLf            
                _05KeyValueShort = _CpHf_Less_CpLf/_ABSofDiff_CpHf
            except Exception as e:
                print(str('part4'))
            try:
                _Diff_CpLf = ((Low[x+8])-Close[x])/Close[x]
                _Diff_CpHf = ((High[x+8])-Close[x])/Close[x]
                _CpHf_Less_CpLf = _Diff_CpHf + _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _08KeyValueLong = _CpHf_Less_CpLf/_ABSofDiff_CpLf            
                _08KeyValueShort = _CpHf_Less_CpLf/_ABSofDiff_CpHf
            except Exception as e:
                print(str('part5'))            
            try:
                _Diff_CpLf = ((Low[x+13])-Close[x])/Close[x]
                _Diff_CpHf = ((High[x+13])-Close[x])/Close[x]
                _CpHf_Less_CpLf = _Diff_CpHf + _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _13KeyValueLong = _CpHf_Less_CpLf/_ABSofDiff_CpLf            
                _13KeyValueShort = _CpHf_Less_CpLf/_ABSofDiff_CpHf
            except Exception as e:
                print(str('part6'))            
            try:                     
                _Diff_CpLf = ((Low[x+21])-Close[x])/Close[x]
                _Diff_CpHf = ((High[x+21])-Close[x])/Close[x]
                _CpHf_Less_CpLf = _Diff_CpHf + _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _21KeyValueLong = _CpHf_Less_CpLf/_ABSofDiff_CpLf            
                _21KeyValueShort = _CpHf_Less_CpLf/_ABSofDiff_CpHf 
            except Exception as e:
                print(str('part7'))    
                
            _TARGET1 = round(_01KeyValueLong + _01KeyValueShort,4)
            _TARGET2 = round(_02KeyValueLong + _02KeyValueShort,4)
            _TARGET3 = round(_03KeyValueLong + _03KeyValueShort,4)
            _TARGET5 = round(_05KeyValueLong + _05KeyValueShort,4)
            _TARGET8 = round(_08KeyValueLong + _08KeyValueShort,4)
            _TARGET13 = round(_13KeyValueLong + _13KeyValueShort,4)
            _TARGET21 = round(_21KeyValueLong + _21KeyValueShort,4)            

### END First part -  calculate on how high the Risk/Reward Ratio is for future move in 1,2,3,5,8,13,21 days

### START Second part - calculate how Big the future move was, using a lot of averageing out to smother the result.             
            try:            
                _Avg_OtoO1 = round((np.average(Open[x+1:x+2])-Close[x])/Close[x],4)
                _Men_OtoO1 = round((np.median(Open[x+1:x+2])-Close[x])/Close[x],4)
                _Avg_HtoH1 = round((np.average(High[x+1:x+2])-Close[x])/Close[x],4)
                _Men_HtoH1 = round((np.median(High[x+1:x+2])-Close[x])/Close[x],4)
                _Avg_LtoL1 = round((np.average(Low[x+1:x+2])-Close[x])/Close[x],4)
                _Men_LtoL1 = round((np.median(Low[x+1:x+2])-Close[x])/Close[x],4)
                _Avg_CtoC1 = round((np.average(Close[x+1:x+2])-Close[x])/Close[x],4)
                _Men_CtoC1 = round((np.median(Close[x+1:x+2])-Close[x])/Close[x],4)      
                _end1 = round((_Avg_OtoO1+_Men_OtoO1+_Avg_HtoH1+_Men_HtoH1+_Avg_LtoL1+_Men_LtoL1+_Avg_CtoC1+_Men_CtoC1)/8,4)
            except Exception as e:
                print(str('part8'))
            try:
                _Avg_OtoO2 = round((np.average(Open[x+1:x+3])-Close[x])/Close[x],4)
                _Men_OtoO2 = round((np.median(Open[x+1:x+3])-Close[x])/Close[x],4)
                _Avg_HtoH2 = round((np.average(High[x+1:x+3])-Close[x])/Close[x],4)
                _Men_HtoH2 = round((np.median(High[x+1:x+3])-Close[x])/Close[x],4)
                _Avg_LtoL2 = round((np.average(Low[x+1:x+3])-Close[x])/Close[x],4)
                _Men_LtoL2 = round((np.median(Low[x+1:x+3])-Close[x])/Close[x],4)
                _Avg_CtoC2 = round((np.average(Close[x+1:x+3])-Close[x])/Close[x],4)
                _Men_CtoC2 = round((np.median(Close[x+1:x+3])-Close[x])/Close[x],4)      
                _end2 = round((_Avg_OtoO2+_Men_OtoO2+_Avg_HtoH2+_Men_HtoH2+_Avg_LtoL2+_Men_LtoL2+_Avg_CtoC2+_Men_CtoC2)/8,4)
            except Exception as e:
                print(str('part9'))            
            try:            
                _Avg_OtoO3 = round((np.average(Open[x+1:x+4])-Close[x])/Close[x],4)
                _Men_OtoO3 = round((np.median(Open[x+1:x+4])-Close[x])/Close[x],4)
                _Avg_HtoH3 = round((np.average(High[x+1:x+4])-Close[x])/Close[x],4)
                _Men_HtoH3 = round((np.median(High[x+1:x+4])-Close[x])/Close[x],4)
                _Avg_LtoL3 = round((np.average(Low[x+1:x+4])-Close[x])/Close[x],4)
                _Men_LtoL3 = round((np.median(Low[x+1:x+4])-Close[x])/Close[x],4)
                _Avg_CtoC3 = round((np.average(Close[x+1:x+4])-Close[x])/Close[x],4)
                _Men_CtoC3 = round((np.median(Close[x+1:x+4])-Close[x])/Close[x],4)      
                _end3 = round((_Avg_OtoO3+_Men_OtoO3+_Avg_HtoH3+_Men_HtoH3+_Avg_LtoL3+_Men_LtoL3+_Avg_CtoC3+_Men_CtoC3)/8,4)
            except Exception as e:
                print(str('part10'))
            try:
                _Avg_OtoO5 = round((np.average(Open[x+1:x+6])-Close[x])/Close[x],4)
                _Men_OtoO5 = round((np.median(Open[x+1:x+6])-Close[x])/Close[x],4)
                _Avg_HtoH5 = round((np.average(High[x+1:x+6])-Close[x])/Close[x],4)
                _Men_HtoH5 = round((np.median(High[x+1:x+6])-Close[x])/Close[x],4)
                _Avg_LtoL5 = round((np.average(Low[x+1:x+6])-Close[x])/Close[x],4)
                _Men_LtoL5 = round((np.median(Low[x+1:x+6])-Close[x])/Close[x],4)
                _Avg_CtoC5 = round((np.average(Close[x+1:x+6])-Close[x])/Close[x],4)
                _Men_CtoC5 = round((np.median(Close[x+1:x+6])-Close[x])/Close[x],4)      
                _end5 = round((_Avg_OtoO5+_Men_OtoO5+_Avg_HtoH5+_Men_HtoH5+_Avg_LtoL5+_Men_LtoL5+_Avg_CtoC5+_Men_CtoC5)/8,4)
            except Exception as e:
                print(str('part11'))
            try:
                _Avg_OtoO8 = round((np.average(Open[x+1:x+9])-Close[x])/Close[x],4)
                _Men_OtoO8 = round((np.median(Open[x+1:x+9])-Close[x])/Close[x],4)
                _Avg_HtoH8 = round((np.average(High[x+1:x+9])-Close[x])/Close[x],4)
                _Men_HtoH8 = round((np.median(High[x+1:x+9])-Close[x])/Close[x],4)
                _Avg_LtoL8 = round((np.average(Low[x+1:x+9])-Close[x])/Close[x],4)
                _Men_LtoL8 = round((np.median(Low[x+1:x+9])-Close[x])/Close[x],4)
                _Avg_CtoC8 = round((np.average(Close[x+1:x+9])-Close[x])/Close[x],4)
                _Men_CtoC8 = round((np.median(Close[x+1:x+9])-Close[x])/Close[x],4)      
                _end8 = round((_Avg_OtoO8+_Men_OtoO8+_Avg_HtoH8+_Men_HtoH8+_Avg_LtoL8+_Men_LtoL8+_Avg_CtoC8+_Men_CtoC8)/8,4)
            except Exception as e:
                print(str('part12'))
            try:
                _Avg_OtoO13 = round((np.average(Open[x+1:x+14])-Close[x])/Close[x],4)
                _Men_OtoO13 = round((np.median(Open[x+1:x+14])-Close[x])/Close[x],4)
                _Avg_HtoH13 = round((np.average(High[x+1:x+14])-Close[x])/Close[x],4)
                _Men_HtoH13 = round((np.median(High[x+1:x+14])-Close[x])/Close[x],4)
                _Avg_LtoL13 = round((np.average(Low[x+1:x+14])-Close[x])/Close[x],4)
                _Men_LtoL13 = round((np.median(Low[x+1:x+14])-Close[x])/Close[x],4)
                _Avg_CtoC13 = round((np.average(Close[x+1:x+14])-Close[x])/Close[x],4)
                _Men_CtoC13 = round((np.median(Close[x+1:x+14])-Close[x])/Close[x],4)      
                _end13 = round((_Avg_OtoO13+_Men_OtoO13+_Avg_HtoH13+_Men_HtoH13+_Avg_LtoL13+_Men_LtoL13+_Avg_CtoC13+_Men_CtoC13)/8,4)
            except Exception as e:
                print(str('part13'))
            try:
                _Avg_OtoO21 = round((np.average(Open[x+1:x+22])-Close[x])/Close[x],4)
                _Men_OtoO21 = round((np.median(Open[x+1:x+22])-Close[x])/Close[x],4)
                _Avg_HtoH21 = round((np.average(High[x+1:x+22])-Close[x])/Close[x],4)
                _Men_HtoH21 = round((np.median(High[x+1:x+22])-Close[x])/Close[x],4)
                _Avg_LtoL21 = round((np.average(Low[x+1:x+22])-Close[x])/Close[x],4)
                _Men_LtoL21 = round((np.median(Low[x+1:x+22])-Close[x])/Close[x],4)
                _Avg_CtoC21 = round((np.average(Close[x+1:x+22])-Close[x])/Close[x],4)
                _Men_CtoC21 = round((np.median(Close[x+1:x+22])-Close[x])/Close[x],4)      
                _end21 = round((_Avg_OtoO21+_Men_OtoO21+_Avg_HtoH21+_Men_HtoH21+_Avg_LtoL21+_Men_LtoL21+_Avg_CtoC21+_Men_CtoC21)/8,4)
            except Exception as e:
                print(str('part14'))
### END Second part - calculate how Big the future move was, using a lot of averageing out to smother the result.   
                
### START calculation of choosen list of FEATURES for the MACHINE LEARNING process ###          
            #Get Date info from .txt file and convet it to string format
            date = int(Date[x])
            dt = datetime.fromordinal(date)
            _DateStamp = str(dt.strftime('%Y-%m-%d'))                
            #part with date related Features                
            _DayOfYear = float(dt.strftime('%j'))
            _DayOfMonth = float(dt.strftime('%d'))
            _DayOfWeek = float(dt.strftime('%w'))
            _DayOfWeek = float(dt.strftime('%w'))
            #part with percentual relations with past price levels 
            _Diff_CtoH = round((Close[x]-High[x])/High[x],3)
            _Diff_CtoH1 = round((Close[x]-High[x-1])/High[x-1],3)
            _Diff_CtoH2 = round((Close[x]-High[x-2])/High[x-2],3)
            _Diff_CtoH3 = round((Close[x]-High[x-3])/High[x-3],3)
            _Diff_CtoH4 = round((Close[x]-High[x-4])/High[x-4],3)
            _Diff_CtoH5 = round((Close[x]-High[x-5])/High[x-5],3)
            _Diff_CtoH6 = round((Close[x]-High[x-6])/High[x-6],3)
            _Diff_CtoH7 = round((Close[x]-High[x-7])/High[x-7],3)
            _Diff_CtoH8 = round((Close[x]-High[x-8])/High[x-8],3)
            _Diff_CtoH9 = round((Close[x]-High[x-9])/High[x-9],3)
            _Diff_CtoH10 = round((Close[x]-High[x-10])/High[x-10],3)
            _Diff_CtoH11 = round((Close[x]-High[x-11])/High[x-11],3)
            _Diff_CtoH12 = round((Close[x]-High[x-12])/High[x-12],3)
            _Diff_CtoH13 = round((Close[x]-High[x-13])/High[x-13],3)
            _Diff_CtoH14 = round((Close[x]-High[x-14])/High[x-14],3)
            _Diff_CtoH15 = round((Close[x]-High[x-15])/High[x-15],3)
            _Diff_CtoH16 = round((Close[x]-High[x-16])/High[x-16],3)
            _Diff_CtoH17 = round((Close[x]-High[x-17])/High[x-17],3)
            _Diff_CtoH18 = round((Close[x]-High[x-18])/High[x-18],3)
            _Diff_CtoH19 = round((Close[x]-High[x-19])/High[x-19],3)
            _Diff_CtoH20 = round((Close[x]-High[x-20])/High[x-20],3)
            _Diff_CtoH21 = round((Close[x]-High[x-21])/High[x-21],3)
            _Diff_CtoH22 = round((Close[x]-High[x-22])/High[x-22],3)
            _Diff_CtoH23 = round((Close[x]-High[x-23])/High[x-23],3)
            _Diff_CtoH24 = round((Close[x]-High[x-24])/High[x-24],3)
            _Diff_CtoH25 = round((Close[x]-High[x-25])/High[x-25],3)

            _Diff_CtoL = round((Close[x]-Low[x])/Low[x],3)
            _Diff_CtoL1 = round((Close[x]-Low[x-1])/Low[x-1],3)
            _Diff_CtoL2 = round((Close[x]-Low[x-2])/Low[x-2],3)
            _Diff_CtoL3 = round((Close[x]-Low[x-3])/Low[x-3],3)
            _Diff_CtoL4 = round((Close[x]-Low[x-4])/Low[x-4],3)
            _Diff_CtoL5 = round((Close[x]-Low[x-5])/Low[x-5],3)
            _Diff_CtoL6 = round((Close[x]-Low[x-6])/Low[x-6],3)
            _Diff_CtoL7 = round((Close[x]-Low[x-7])/Low[x-7],3)
            _Diff_CtoL8 = round((Close[x]-Low[x-8])/Low[x-8],3)
            _Diff_CtoL9 = round((Close[x]-Low[x-9])/Low[x-9],3)
            _Diff_CtoL10 = round((Close[x]-Low[x-10])/Low[x-10],3)
            _Diff_CtoL11 = round((Close[x]-Low[x-11])/Low[x-11],3)
            _Diff_CtoL12 = round((Close[x]-Low[x-12])/Low[x-12],3)
            _Diff_CtoL13 = round((Close[x]-Low[x-13])/Low[x-13],3)
            _Diff_CtoL14 = round((Close[x]-Low[x-14])/Low[x-14],3)
            _Diff_CtoL15 = round((Close[x]-Low[x-15])/Low[x-15],3)
            _Diff_CtoL16 = round((Close[x]-Low[x-16])/Low[x-16],3)
            _Diff_CtoL17 = round((Close[x]-Low[x-17])/Low[x-17],3)
            _Diff_CtoL18 = round((Close[x]-Low[x-18])/Low[x-18],3)
            _Diff_CtoL19 = round((Close[x]-Low[x-19])/Low[x-19],3)
            _Diff_CtoL20 = round((Close[x]-Low[x-20])/Low[x-20],3)
            _Diff_CtoL21 = round((Close[x]-Low[x-21])/Low[x-21],3)
            _Diff_CtoL22 = round((Close[x]-Low[x-22])/Low[x-22],3)
            _Diff_CtoL23 = round((Close[x]-Low[x-23])/Low[x-23],3)
            _Diff_CtoL24 = round((Close[x]-Low[x-24])/Low[x-24],3)
            _Diff_CtoL25 = round((Close[x]-Low[x-25])/Low[x-25],3)

            _Diff_CtoO = round((Close[x]-Open[x])/Open[x],3)
            _Diff_CtoO1 = round((Close[x]-Open[x-1])/Open[x-1],3)
            _Diff_CtoO2 = round((Close[x]-Open[x-2])/Open[x-2],3)
            _Diff_CtoO3 = round((Close[x]-Open[x-3])/Open[x-3],3)
            _Diff_CtoO4 = round((Close[x]-Open[x-4])/Open[x-4],3)
            _Diff_CtoO5 = round((Close[x]-Open[x-5])/Open[x-5],3)
            _Diff_CtoO6 = round((Close[x]-Open[x-6])/Open[x-6],3)
            _Diff_CtoO7 = round((Close[x]-Open[x-7])/Open[x-7],3)
            _Diff_CtoO8 = round((Close[x]-Open[x-8])/Open[x-8],3)
            _Diff_CtoO9 = round((Close[x]-Open[x-9])/Open[x-9],3)


            _Diff_CtoC1 = round((Close[x]-Close[x-1])/Close[x-1],3)
            _Diff_CtoC2 = round((Close[x]-Close[x-2])/Close[x-2],3)
            _Diff_CtoC3 = round((Close[x]-Close[x-3])/Close[x-3],3)
            _Diff_CtoC4 = round((Close[x]-Close[x-4])/Close[x-4],3)
            _Diff_CtoC5 = round((Close[x]-Close[x-5])/Close[x-5],3)
            _Diff_CtoC6 = round((Close[x]-Close[x-6])/Close[x-6],3)
            _Diff_CtoC7 = round((Close[x]-Close[x-7])/Close[x-7],3)
            _Diff_CtoC8 = round((Close[x]-Close[x-8])/Close[x-8],3)
            _Diff_CtoC9 = round((Close[x]-Close[x-9])/Close[x-9],3)

            _justOpen = float(Open[x])
            _justHigh = float(High[x])
            _justLow = float(Low[x])
            _justClose = float(Close[x])
            
            #part with indicator creations based on Standard Deviations/Volatility
            _SMA_H3 = round(np.sum(High[x-4:x+1])/5,2) #sub indicator
            _SMA_L3 = round(np.sum(Low[x-4:x+1])/5,2) #sub indicator
            _BBU5 = round(np.sum(Close[x+1-5:x+1])/5,3)+(round(np.std(Close[x+1-5:x+1])*2,3)) #sub indicator (Bollinger Band)
            _BBD5 = round(np.sum(Close[x+1-5:x+1])/5,3)-(round(np.std(Close[x+1-5:x+1])*2,3)) #sub indicator (Bollinger Band)
            _DiffU5_C = round((Close[x]-_BBU5)/_BBU5,3)
            _DiffD5_C = round((Close[x]-_BBD5)/_BBD5,3)
            _BBU13 = round(np.sum(Close[x+1-13:x+1])/13,3)+(round(np.std(Close[x+1-13:x+1])*2,3)) #sub indicator (Bollinger Band)
            _BBD13 = round(np.sum(Close[x+1-13:x+1])/13,3)-(round(np.std(Close[x+1-13:x+1])*2,3)) #sub indicator (Bollinger Band)
            _DiffU13_L3 = round((_SMA_L3-_BBU13)/_BBU13,3)
            _BBU21 = round(np.sum(Close[x+1-21:x+1])/21,3)+(round(np.std(Close[x+1-21:x+1])*2,3)) #sub indicator (Bollinger Band)
            _BBD21 = round(np.sum(Close[x+1-21:x+1])/21,3)-(round(np.std(Close[x+1-21:x+1])*2,3)) #sub indicator (Bollinger Band)
            _DiffD21_C = round((Close[x]-_BBD21)/_BBD21,3)
            _DiffD21_H3 = round((_SMA_H3-_BBD21)/_BBD21,3)  
            _BBU34 = round(np.sum(Close[x+1-34:x+1])/34,3)+(round(np.std(Close[x+1-34:x+1])*2,3)) #sub indicator (Bollinger Band)
            _BBD34 = round(np.sum(Close[x+1-34:x+1])/34,3)-(round(np.std(Close[x+1-34:x+1])*2,3)) #sub indicator (Bollinger Band)
            _DiffU34_C = round((Close[x]-_BBU34)/_BBU34,3)
            _DiffD34_H3 = round((_SMA_H3-_BBD34)/_BBD34,3)   
            _BBU55 = round(np.sum(Close[x+1-55:x+1])/55,3)+(round(np.std(Close[x+1-55:x+1])*2,3)) #sub indicator (Bollinger Band)
            _BBD55 = round(np.sum(Close[x+1-55:x+1])/55,3)-(round(np.std(Close[x+1-55:x+1])*2,3)) #sub indicator (Bollinger Band)
            _DiffU55_L3 = round((_SMA_L3-_BBU55)/_BBU55,3)
            _BBU89 = round(np.sum(Close[x+1-89:x+1])/89,3)+(round(np.std(Close[x+1-89:x+1])*2,3)) #sub indicator (Bollinger Band)
            _BBD89 = round(np.sum(Close[x+1-89:x+1])/89,3)-(round(np.std(Close[x+1-89:x+1])*2,3)) #sub indicator (Bollinger Band)
            _DiffU89_C = round((Close[x]-_BBU89)/_BBU89,3)
            _DiffU89_L3 = round((_SMA_L3-_BBU89)/_BBU89,3)
            _BBU144 = round(np.sum(Close[x+1-144:x+1])/144,3)+(round(np.std(Close[x+1-144:x+1])*2,3)) #sub indicator (Bollinger Band)
            _BBD144 = round(np.sum(Close[x+1-144:x+1])/144,3)-(round(np.std(Close[x+1-144:x+1])*2,3)) #sub indicator (Bollinger Band)
            _DiffU144_L3 = round((_SMA_L3-_BBU144)/_BBU144,3)
            _BBU233 = round(np.sum(Close[x+1-233:x+1])/233,3)+(round(np.std(Close[x+1-233:x+1])*2,3)) #sub indicator (Bollinger Band)
            _BBD233 = round(np.sum(Close[x+1-233:x+1])/233,3)-(round(np.std(Close[x+1-233:x+1])*2,3)) #sub indicator (Bollinger Band)
            _DiffU233_C = round((Close[x]-_BBU233)/_BBU233,3)
            _BBU300 = round(np.sum(Close[x+1-300:x+1])/300,3)+(round(np.std(Close[x+1-300:x+1])*2,3)) #sub indicator (Bollinger Band)
            _BBD300 = round(np.sum(Close[x+1-300:x+1])/300,3)-(round(np.std(Close[x+1-300:x+1])*2,3)) #sub indicator (Bollinger Band)
            _DiffU300_C = round((Close[x]-_BBU300)/_BBU300,3)
            _DiffD300_C = round((Close[x]-_BBD300)/_BBD300,3)
            
            #part with indicator creations based on Price Action/High & Low values and symbolic numbers            
            _High3_H = round((Close[x]-np.amax(High[x+1-3:x+1]))/np.amax(High[x+1-3:x+1]),3)
            _High5_H = round((Close[x]-np.amax(High[x+1-5:x+1]))/np.amax(High[x+1-5:x+1]),3)
            _High100_H = round((Close[x]-np.amax(High[x+1-100:x+1]))/np.amax(High[x+1-100:x+1]),3)
            _High377_H = round((Close[x]-np.amax(High[x+1-377:x+1]))/np.amax(High[x+1-377:x+1]),3)
            _Low3_L = round((Close[x]-np.amin(Low[x+1-3:x+1]))/np.amin(Low[x+1-3:x+1]),3)
            _Low34_L = round((Close[x]-np.amin(Low[x+1-34:x+1]))/np.amin(Low[x+1-34:x+1]),3)
            _Low55_L = round((Close[x]-np.amin(Low[x+1-55:x+1]))/np.amin(Low[x+1-55:x+1]),3)
            _Hi3to5 = round((Close[x]-np.amax(High[x+1-5:x+1-3]))/np.amax(High[x+1-5:x+1-3]),3)
            _Hi5to8 = round((Close[x]-np.amax(High[x+1-8:x+1-5]))/np.amax(High[x+1-8:x+1-5]),3)
            _Hi8to13 = round((Close[x]-np.amax(High[x+1-13:x+1-8]))/np.amax(High[x+1-13:x+1-8]),3)
            _Hi34to55 = round((Close[x]-np.amax(High[x+1-55:x+1-34]))/np.amax(High[x+1-55:x+1-34]),3)
            _Hi233to377 = round((Close[x]-np.amax(High[x+1-377:x+1-233]))/np.amax(High[x+1-377:x+1-233]),3)
            _Lo3to5 = round((Close[x]-np.amin(Low[x+1-5:x+1-3]))/np.amin(Low[x+1-5:x+1-3]),3)
            _Lo233to377 = round((Close[x]-np.amin(Low[x+1-377:x+1-233]))/np.amin(Low[x+1-377:x+1-233]),3)        
            _EvNo5 = round((Close[x]-5)/5,2)
        
        except Exception as e:
            print(str(e))

### END calculation of choosen list of FEATURES for the MACHINE LEARNING process ###            

### START part where to write every Future value and Feature, day by day and intrument by instrument to .txt file to read csv style. 
        LocationToSave = FileLocation = path + '\\MASSIVE_BS4T_07_ROC.txt'
        saveFile = open(LocationToSave,'a')
        lineToWrite = (
                    str(_justOpen) + ',' +
                    str(_justHigh) + ',' +
                    str(_justLow) + ',' +
                    str(_justClose) + ',' +                        
                    str(eachTicker) + ',' +
                    str(_DateStamp) + ',' +
                    str(_TARGET1) + ',' +
                    str(_TARGET2) + ',' +
                    str(_TARGET3) + ',' +
                    str(_TARGET5) + ',' +
                    str(_TARGET8) + ',' +
                    str(_TARGET13) + ',' +
                    str(_TARGET21) + ',' +
                    str(_end1) + ',' +
                    str(_end2) + ',' +
                    str(_end3) + ',' +
                    str(_end5) + ',' +
                    str(_end8) + ',' +
                    str(_end13) + ',' +
                    str(_end21) + ',' +                    
                    str(_DayOfYear) + ',' +
                    str(_DayOfMonth) + ',' +
                    str(_DayOfWeek) + ',' +
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
                    str(_justOpen) + ',' +
                    str(_justHigh) + ',' +
                    str(_justLow) + ',' +
                    str(_justClose) + ',' +
                    str(_DiffU5_C) + ',' +
                    str(_DiffD5_C) + ',' +
                    str(_DiffU13_L3) + ',' +
                    str(_DiffD21_C) + ',' +
                    str(_DiffD21_H3) + ',' +
                    str(_DiffU34_C) + ',' +
                    str(_DiffD34_H3) + ',' +
                    str(_DiffU55_L3) + ',' +
                    str(_DiffU89_C) + ',' +
                    str(_DiffU89_L3) + ',' +
                    str(_DiffU144_L3) + ',' +
                    str(_DiffU233_C) + ',' +
                    str(_DiffU300_C) + ',' +
                    str(_DiffD300_C) + ',' +
                    str(_High3_H) + ',' +
                    str(_High5_H) + ',' +
                    str(_High100_H) + ',' +
                    str(_High377_H) + ',' +
                    str(_Low3_L) + ',' +
                    str(_Low34_L) + ',' +
                    str(_Low55_L) + ',' +
                    str(_Hi3to5) + ',' +
                    str(_Hi5to8) + ',' +
                    str(_Hi8to13) + ',' +
                    str(_Hi34to55) + ',' +
                    str(_Hi233to377) + ',' +
                    str(_Lo3to5) + ',' +
                    str(_Lo233to377) + ',' +
                    str(_EvNo5) + '\n'
                    )
        
        saveFile.write(lineToWrite)
        saveFile.close() 
### END part where to write every Future value and Feature, day by day and intrument by instrument to .txt file to read csv style. 
        
endTime = time.time()        
totalTime = endTime - startTime
print(totalTime)