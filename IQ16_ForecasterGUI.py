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

IMUNDBO QUANT v1.6 (Forecaster GUI-style)
"""

###-----------------------------------------------------------------------------

import sys
from Tkinter import *
import time#
import datetime
import numpy as np#
import pandas as pd#
import dateutil
import os
import csv
import matplotlib.dates as mdates
from matplotlib.dates import strpdate2num
import psutil
from sklearn.externals import joblib  
from sklearn.ensemble import RandomForestClassifier
pd.core.format.header_style = None  # <--- Workaround for header formatting


###-----------------------------------------------------------------------------
def makeForecast(inputList):
    import urllib2#
    import urllib
    import datetime
    import time#
    import os
    import dateutil

###-----------------------------------------------------------------------------
### START part One "DATA COLLECTION" - getting fresch intraday data from YahooFinance API, to work with

    #### Get specified content for the instrument list, from file in Python root dir. 
    yahoo_ticker_list = []
    readThisFile = r'lista_' + inputList +'.txt'
    TickerFile = open(readThisFile)
    fleraTickers = TickerFile.read()
    yahoo_ticker_list = fleraTickers.split('\n')
    TickerFile.close()

    yahoo_RealNames_list = []
    readThisFile = r'lista_' + inputList +'_RealNames.txt'
    TickerFile = open(readThisFile)
    fleraTickers = TickerFile.read()
    yahoo_RealNames_list = fleraTickers.split('\n')
    TickerFile.close()

    #### Get content for the FEATURE list, from file in Python root dir.
    FEATURES = []
    readThisFile = r'FEATURES03.txt'
    featuresFile = open(readThisFile)
    fleraFeatures = featuresFile.read()
    FEATURES = fleraFeatures.split('\n')
    featuresFile.close()
    printToFile = ('DONE: reading instrument and features')####
    LocationToSave = r"loooooooooooooooooooooogFile.txt"
    saveFile = open(LocationToSave,'a')
    saveFile.write(printToFile)

    #### Remove, possible old files in Python root dir.
    for eachTicker in yahoo_ticker_list:
        try:        
            os.remove(r'for'+eachTicker+'_excel.xlsx')
        except Exception as e:
            print(str(e))
    for eachTicker in yahoo_ticker_list:
        try:                     
            os.remove(r'EOD'+eachTicker+'.txt')###
        except Exception as e:
            printToFile = (str(e))
            logFile = open('lo0gFile.txt','a')
            logFile.write("\n"+printToFile)
            logFile.close()


    print('DONE: deleting old files')####
    time.sleep(4)


    #### Parse EOD data for every instrument from finance.yahoo and save it linebyline in a 1st .txt file
    for eachTicker in yahoo_ticker_list:
        try:
            urlToVisit =  'http://chartapi.finance.yahoo.com/instrument/1.0/'+eachTicker+'/chartdata;type=quote;range=2y/csv'
            sourceCode = urllib2.urlopen(urlToVisit).read()
            splitSource = sourceCode.split('\n')
            LocationToSave = r'EOD'+eachTicker+'.txt'

            for eachLine in splitSource:
                splitLine = eachLine.split(',')
                if len(splitLine)==6:
                    if 'values' not in eachLine:
                        saveFile = open(LocationToSave,'a')
                        lineToWrite = eachLine+'\n'
                        saveFile.write(lineToWrite)
            saveFile.close()
            time.sleep(1) ### in respect to yahoo.finance 
        except Exception as e:
            print(str(e))
            #pass
    print('DONE: parsing EOD data and save as EOD_ticker_txt')####


    #### Parse 5min data for every instrument from yahoo AND save in 2nd .txt file for each ticker
    for eachTicker in yahoo_ticker_list:
        try:
            urlToVisit =  'http://chartapi.finance.yahoo.com/instrument/1.0/'+eachTicker+'/chartdata;type=quote;range=40d/csv'
            sourceCode = urllib2.urlopen(urlToVisit).read()
            splitSource = sourceCode.split('\n')
            LocationToSave = r'5min'+eachTicker+'.txt'

            for eachLine in splitSource:
                splitLine = eachLine.split(',')
                if len(splitLine)==6:
                    if 'values' not in eachLine:
                        saveFile = open(LocationToSave,'a')
                        lineToWrite = eachLine+'\n'
                        saveFile.write(lineToWrite)

            saveFile.close()
            time.sleep(1) ### in respect to yahoo.finance 
        except Exception as e:
            print(str(e))
            #pass
    print('DONE: parsing 5min data and save as 5min_ticker_txt')####


    #### Sort out only todays 5min data from 2nd .txt file AND save todays data in a 3rd .txt file for each ticker
    for eachTicker in yahoo_ticker_list:
        try:
            FileLocation = r'5min'+eachTicker+'.txt'
            Unix,Open,High,Low,Close,Volume = np.loadtxt(FileLocation, unpack=True, delimiter=',')
            today = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
            UnixToday = datetime.datetime.fromtimestamp(Unix[-2]).strftime('%Y-%m-%d')
            if today != UnixToday:
                try:                     
                    os.remove(r'EOD'+eachTicker+'.txt')###
                except Exception as e:
                    print(str(e))
            else:
                for x in range(1, 400):#############
                    UnixToday = datetime.datetime.fromtimestamp(Unix[-x]).strftime('%Y-%m-%d')
                    if today == UnixToday:
                        forUnix = Unix[-x]
                        forOpen = Open[-x]
                        forHigh = High[-x]
                        forLow = Low[-x]
                        forClose = Close[-x]
                        LocationToSave = r'todayEOD'+eachTicker+'.txt'
                        saveFile = open(LocationToSave,'a')
                        lineToWrite = str(forUnix)+','+str(forOpen)+','+str(forHigh)+','+str(forLow)+','+str(forClose)+'\n'
                        saveFile.write(lineToWrite)
                        saveFile.close()

        except Exception as e:
            #pass
            print(str(e))
    e = str('DONE: sort out todays 5min data')####
    printToFile = (str(e))
    logFile = open('lo0gFile.txt','a')
    logFile.write(printToFile)
    logFile.close()
    

    #### Read the 3rd .txt file with only todays 5min data AND convert to EOD format to 4th .txt file
    for eachTicker in yahoo_ticker_list:
        try:
            FileLocation = r'todayEOD'+eachTicker+'.txt'
            Unix,Open,High,Low,Close = np.loadtxt(FileLocation, unpack=True, delimiter=',')
            NoLen = len(Unix)

            forUnix = datetime.datetime.fromtimestamp(Unix[-2]).strftime('%Y%m%d')
            forOpen = Open[-2]
            forHigh = np.amax(High[0:NoLen])
            forLow = np.amin(Low[0:NoLen])
            forClose = Close[0]
    #        print(str(forUnix)+str(eachTicker)+str(UnixTodayInLoop))
            LocationToSave = r'EODtoday'+eachTicker+'.txt'
            saveFile = open(LocationToSave,'w')
            lineToWrite = str(forUnix)+','+str(forOpen)+','+str(forHigh)+','+str(forLow)+','+str(forClose)+',1\n'
            saveFile.write(lineToWrite)
            saveFile.close()

        except Exception as e:
            #pass
            print(str(e))
    print('DONE: convert 5min data tot EOD')####    
    printToFile = (str('DONE: convert 5min data tot EOD'))
    logFile = open('lo0gFile.txt','a')
    logFile.write("\n"+printToFile)
    logFile.close()


    #### append todays EOD from 4th .txt file to the list of all EOD data in 1st .txt file
    for eachTicker in yahoo_ticker_list:
        try:
            EODFile = open(r'EODtoday'+eachTicker+'.txt')
            EODline = EODFile.readlines()
            EODtoday = EODline[0]
            EODFile.close()
            LocationToSave = r'EOD'+eachTicker+'.txt'
            saveFile = open(LocationToSave,'a')
            lineToWrite = EODtoday
            saveFile.write(lineToWrite)
            saveFile.close()
        except Exception as e:
            print(str(e))
            #pass

### END part One - getting fresch intraday data to work with
###-----------------------------------------------------------------------------
### START part Two "PREPROCESS" - Load fresh data and create all additional Features AND
### save all data to one .xlsx file for each ticker


    from datetime import datetime       
    for eachTicker in yahoo_ticker_list:
        try:
            FileLocation = r'EOD'+eachTicker+'.txt'
            Date, Open, High, Low, Close, Volume = np.loadtxt(FileLocation, delimiter=',', unpack=True,converters={ 0: mdates.strpdate2num('%Y%m%d')})
            Zeros = [1]*len(Date)
            date = int(Date[-1])
            dt = datetime.fromordinal(date)
            ### create the individual Features
### START calculation of choosen list of FEATURES for the MACHINE LEARNING process ###
            _DayOfYear = float(dt.strftime('%j')) # part with calender based FEATURES
            _DayOfMonth = float(dt.strftime('%d'))
            _DayOfWeek = float(dt.strftime('%w'))
            # part with FEATURES based on % relative from last Close,
            _Diff_CtoH = round((Close[-1]-High[-1])/High[-1],3)  
            _Diff_CtoH1 = round((Close[-1]-High[-2])/High[-2],3)
            _Diff_CtoH2 = round((Close[-1]-High[-3])/High[-3],3)
            _Diff_CtoH3 = round((Close[-1]-High[-4])/High[-4],3)
            _Diff_CtoH4 = round((Close[-1]-High[-5])/High[-5],3)
            _Diff_CtoH5 = round((Close[-1]-High[-6])/High[-6],3)
            _Diff_CtoH6 = round((Close[-1]-High[-7])/High[-7],3)
            _Diff_CtoH7 = round((Close[-1]-High[-8])/High[-8],3)
            _Diff_CtoH8 = round((Close[-1]-High[-9])/High[-9],3)
            _Diff_CtoH9 = round((Close[-1]-High[-10])/High[-10],3)
            _Diff_CtoH10 = round((Close[-1]-High[-11])/High[-11],3)
            _Diff_CtoH11 = round((Close[-1]-High[-12])/High[-12],3)
            _Diff_CtoH12 = round((Close[-1]-High[-13])/High[-13],3)
            _Diff_CtoH13 = round((Close[-1]-High[-14])/High[-14],3)
            _Diff_CtoH14 = round((Close[-1]-High[-15])/High[-15],3)
            _Diff_CtoH15 = round((Close[-1]-High[-16])/High[-16],3)
            _Diff_CtoH16 = round((Close[-1]-High[-17])/High[-17],3)
            _Diff_CtoH17 = round((Close[-1]-High[-18])/High[-18],3)
            _Diff_CtoH18 = round((Close[-1]-High[-19])/High[-19],3)
            _Diff_CtoH19 = round((Close[-1]-High[-20])/High[-20],3)
            _Diff_CtoH20 = round((Close[-1]-High[-21])/High[-21],3)
            _Diff_CtoH21 = round((Close[-1]-High[-22])/High[-22],3)
            _Diff_CtoH22 = round((Close[-1]-High[-23])/High[-23],3)
            _Diff_CtoH23 = round((Close[-1]-High[-24])/High[-24],3)
            _Diff_CtoH24 = round((Close[-1]-High[-25])/High[-25],3)
            _Diff_CtoH25 = round((Close[-1]-High[-26])/High[-26],3)

            _Diff_CtoL = round((Close[-1]-Low[-1])/Low[-1],3)
            _Diff_CtoL1 = round((Close[-1]-Low[-2])/Low[-2],3)
            _Diff_CtoL2 = round((Close[-1]-Low[-3])/Low[-3],3)
            _Diff_CtoL3 = round((Close[-1]-Low[-4])/Low[-4],3)
            _Diff_CtoL4 = round((Close[-1]-Low[-5])/Low[-5],3)
            _Diff_CtoL5 = round((Close[-1]-Low[-6])/Low[-6],3)
            _Diff_CtoL6 = round((Close[-1]-Low[-7])/Low[-7],3)
            _Diff_CtoL7 = round((Close[-1]-Low[-8])/Low[-8],3)
            _Diff_CtoL8 = round((Close[-1]-Low[-9])/Low[-9],3)
            _Diff_CtoL9 = round((Close[-1]-Low[-10])/Low[-10],3)
            _Diff_CtoL10 = round((Close[-1]-Low[-11])/Low[-11],3)
            _Diff_CtoL11 = round((Close[-1]-Low[-12])/Low[-12],3)
            _Diff_CtoL12 = round((Close[-1]-Low[-13])/Low[-13],3)
            _Diff_CtoL13 = round((Close[-1]-Low[-14])/Low[-14],3)
            _Diff_CtoL14 = round((Close[-1]-Low[-15])/Low[-15],3)
            _Diff_CtoL15 = round((Close[-1]-Low[-16])/Low[-16],3)
            _Diff_CtoL16 = round((Close[-1]-Low[-17])/Low[-17],3)
            _Diff_CtoL17 = round((Close[-1]-Low[-18])/Low[-18],3)
            _Diff_CtoL18 = round((Close[-1]-Low[-19])/Low[-19],3)
            _Diff_CtoL19 = round((Close[-1]-Low[-20])/Low[-20],3)
            _Diff_CtoL20 = round((Close[-1]-Low[-21])/Low[-21],3)
            _Diff_CtoL21 = round((Close[-1]-Low[-22])/Low[-22],3)
            _Diff_CtoL22 = round((Close[-1]-Low[-23])/Low[-23],3)
            _Diff_CtoL23 = round((Close[-1]-Low[-24])/Low[-24],3)
            _Diff_CtoL24 = round((Close[-1]-Low[-25])/Low[-25],3)
            _Diff_CtoL25 = round((Close[-1]-Low[-26])/Low[-26],3)

            _Diff_CtoO = round((Close[-1]-Open[-1])/Open[-1],3)
            _Diff_CtoO1 = round((Close[-1]-Open[-2])/Open[-2],3)
            _Diff_CtoO2 = round((Close[-1]-Open[-3])/Open[-3],3)
            _Diff_CtoO3 = round((Close[-1]-Open[-4])/Open[-4],3)
            _Diff_CtoO4 = round((Close[-1]-Open[-5])/Open[-5],3)
            _Diff_CtoO5 = round((Close[-1]-Open[-6])/Open[-6],3)
            _Diff_CtoO6 = round((Close[-1]-Open[-7])/Open[-7],3)
            _Diff_CtoO7 = round((Close[-1]-Open[-8])/Open[-8],3)
            _Diff_CtoO8 = round((Close[-1]-Open[-9])/Open[-9],3)
            _Diff_CtoO9 = round((Close[-1]-Open[-10])/Open[-10],3)

            _Diff_CtoC1 = round((Close[-1]-Close[-1])/Close[-1],3)
            _Diff_CtoC2 = round((Close[-1]-Close[-3])/Close[-3],3)
            _Diff_CtoC3 = round((Close[-1]-Close[-4])/Close[-4],3)
            _Diff_CtoC4 = round((Close[-1]-Close[-5])/Close[-5],3)
            _Diff_CtoC5 = round((Close[-1]-Close[-6])/Close[-6],3)
            _Diff_CtoC6 = round((Close[-1]-Close[-7])/Close[-7],3)
            _Diff_CtoC7 = round((Close[-1]-Close[-8])/Close[-8],3)
            _Diff_CtoC8 = round((Close[-1]-Close[-9])/Close[-9],3)
            _Diff_CtoC9 = round((Close[-1]-Close[-10])/Close[-10],3)
            ### PART with onle basic HLOC data
            _justOpen = Open[-1] 
            _justHigh = High[-1]
            _justLow = Low[-1]
            _justClose = Close[-1]
            ### PART with FEATURES based on % relation Close or Sub-indicator to upper/lower BollingerBand
            _SMA_H3 = float(round(np.sum(High[:-4:-1])/5,2)) # short moving average based on H & L
            _SMA_L3 = float(round(np.sum(Low[:-4:-1])/5,2))  # this two are sub-indicators

            _BBU5 = round(np.sum(Close[:-4:-1])/5,3)+(round(np.std(Close[-4:-1])*2,3)) # Upper BollingerBand
            _BBD5 = round(np.sum(Close[:-4:-1])/5,3)-(round(np.std(Close[-4:-1])*2,3)) # Lower BollingerBand
            _DiffU5_C = round((Close[-1]-_BBU5)/_BBU5,3) 
            _DiffD5_C = round((Close[-1]-_BBD5)/_BBD5,3)

            _BBU13 = round(np.sum(Close[:-12:-1])/13,3)+(round(np.std(Close[:-12:-1])*2,3))
            _BBD13 = round(np.sum(Close[:-12:-1])/13,3)-(round(np.std(Close[:-12:-1])*2,3))
            _DiffU13_L3 = round((_SMA_L3-_BBU13)/_BBU13,3)

            _BBU21 = round(np.sum(Close[:-20:-1])/21,3)+(round(np.std(Close[:-20:-1])*2,3))
            _BBD21 = round(np.sum(Close[:-20:-1])/21,3)-(round(np.std(Close[:-20:-1])*2,3))
            _DiffD21_C = round((Close[-1]-_BBD21)/_BBD21,3)
            _DiffD21_H3 = round((_SMA_H3-_BBD21)/_BBD21,3)  

            _BBU34 = round(np.sum(Close[:-33:-1])/34,3)+(round(np.std(Close[:-33:-1])*2,3))
            _BBD34 = round(np.sum(Close[:-33:-1])/34,3)-(round(np.std(Close[:-33:-1])*2,3))
            _DiffU34_C = round((Close[-1]-_BBU34)/_BBU34,3)
            _DiffD34_H3 = round((_SMA_H3-_BBD34)/_BBD34,3)   

            _BBU55 = round(np.sum(Close[:-54:-1])/55,3)+(round(np.std(Close[:-54:-1])*2,3))
            _BBD55 = round(np.sum(Close[:-54:-1])/55,3)-(round(np.std(Close[:-54:-1])*2,3))
            _DiffU55_L3 = round((_SMA_L3-_BBU55)/_BBU55,3)

            _BBU89 = round(np.sum(Close[:-88:-1])/89,3)+(round(np.std(Close[:-88:-1])*2,3))
            _BBD89 = round(np.sum(Close[:-88:-1])/89,3)-(round(np.std(Close[:-88:-1])*2,3))
            _DiffU89_C = round((Close[-1]-_BBU89)/_BBU89,3)
            _DiffU89_L3 = round((_SMA_L3-_BBU89)/_BBU89,3)

            _BBU144 = round(np.sum(Close[:-143:-1])/144,3)+(round(np.std(Close[:-143:-1])*2,3))
            _BBD144 = round(np.sum(Close[:-143:-1])/144,3)-(round(np.std(Close[:-143:-1])*2,3))
            _DiffU144_L3 = round((_SMA_L3-_BBU144)/_BBU144,3)

            _BBU233 = round(np.sum(Close[:-232:-1])/233,3)+(round(np.std(Close[:-232:-1])*2,3))
            _BBD233 = round(np.sum(Close[:-232:-1])/233,3)-(round(np.std(Close[:-232:-1])*2,3))
            _DiffU233_C = round((Close[-1]-_BBU233)/_BBU233,3)

            _BBU300 = round(np.sum(Close[:299:-1])/300,3)+(round(np.std(Close[:299:-1])*2,3))
            _BBD300 = round(np.sum(Close[:299:-1])/300,3)-(round(np.std(Close[:299:-1])*2,3))
            _DiffU300_C = round((Close[-1]-_BBU300)/_BBU300,3)
            _DiffD300_C = round((Close[-1]-_BBD300)/_BBD300,3)
            ### PART with % relation, Close to Maxium High or Low from varius days in history
            _High3_H = round((Close[-1]-np.amax(High[:-2:-1]))/np.amax(High[:-2:-1]),3)
            _High5_H = round((Close[-1]-np.amax(High[:-4:-1]))/np.amax(High[:-4:-1]),3)
            _High100_H = round((Close[-1]-np.amax(High[:-99:-1]))/np.amax(High[:-99:-1]),3)
            _High377_H = round((Close[-1]-np.amax(High[:-376:-1]))/np.amax(High[:-376:-1]),3)
            _Low3_L = round((Close[-1]-np.amin(Low[:-2:-1]))/np.amin(Low[:-2:-1]),3)
            _Low34_L = round((Close[-1]-np.amin(Low[:-33:-1]))/np.amin(Low[:-33:-1]),3)
            _Low55_L = round((Close[-1]-np.amin(Low[:-54:-1]))/np.amin(Low[:-54:-1]),3)
            _Hi3to5 = round((Close[-1]-np.amax(High[:-4:-2]))/np.amax(High[:-4:-2]),3)
            _Hi5to8 = round((Close[-1]-np.amax(High[:-7:-4]))/np.amax(High[:-7:-4]),3)
            _Hi8to13 = round((Close[-1]-np.amax(High[:-12:-7]))/np.amax(High[:-12:-7]),3)
            _Hi34to55 = round((Close[-1]-np.amax(High[:-54:-33]))/np.amax(High[:-54:-33]),3)
            _Hi233to377 = round((Close[-1]-np.amax(High[:-376:-232]))/np.amax(High[:-376:-232]),3)
            _Lo3to5 = round((Close[-1]-np.amin(Low[:-4:-2]))/np.amin(Low[:-4:-2]),3)
            _Lo233to377 = round((Close[-1]-np.amin(Low[:-376:-232]))/np.amin(Low[:-376:-232]),3)        
            ### PART with simple aritmic Feature
            _EvNo5 = round((Close[-1]-5)/5,2) 
### END calculation of choosen list of FEATURES for the MACHINE LEARNING process ###            

            ### append the individual Features to Pandas Dataframe
            df = pd.DataFrame(columns = FEATURES)
            df = df.append({
                        '_DayOfYear':_DayOfYear,
                        '_DayOfMonth':_DayOfMonth,
                        '_DayOfWeek':_DayOfWeek,
                        '_Diff_CtoH':_Diff_CtoH,
                        '_Diff_CtoH1':_Diff_CtoH1,
                        '_Diff_CtoH2':_Diff_CtoH2,
                        '_Diff_CtoH3':_Diff_CtoH3,
                        '_Diff_CtoH4':_Diff_CtoH4,
                        '_Diff_CtoH5':_Diff_CtoH5,
                        '_Diff_CtoH6':_Diff_CtoH6,
                        '_Diff_CtoH7':_Diff_CtoH7,
                        '_Diff_CtoH8':_Diff_CtoH8,
                        '_Diff_CtoH9':_Diff_CtoH9,
                        '_Diff_CtoH10':_Diff_CtoH10,
                        '_Diff_CtoH11':_Diff_CtoH11,
                        '_Diff_CtoH12':_Diff_CtoH12,
                        '_Diff_CtoH13':_Diff_CtoH13,
                        '_Diff_CtoH14':_Diff_CtoH14,
                        '_Diff_CtoH15':_Diff_CtoH15,
                        '_Diff_CtoH16':_Diff_CtoH16,
                        '_Diff_CtoH17':_Diff_CtoH17,
                        '_Diff_CtoH18':_Diff_CtoH18,
                        '_Diff_CtoH19':_Diff_CtoH19,
                        '_Diff_CtoH20':_Diff_CtoH20,
                        '_Diff_CtoH21':_Diff_CtoH21,
                        '_Diff_CtoH22':_Diff_CtoH22,
                        '_Diff_CtoH23':_Diff_CtoH23,
                        '_Diff_CtoH24':_Diff_CtoH24,
                        '_Diff_CtoH25':_Diff_CtoH25,
                        '_Diff_CtoL':_Diff_CtoL,
                        '_Diff_CtoL1':_Diff_CtoL1,
                        '_Diff_CtoL2':_Diff_CtoL2,
                        '_Diff_CtoL3':_Diff_CtoL3,
                        '_Diff_CtoL4':_Diff_CtoL4,
                        '_Diff_CtoL5':_Diff_CtoL5,
                        '_Diff_CtoL6':_Diff_CtoL6,
                        '_Diff_CtoL7':_Diff_CtoL7,
                        '_Diff_CtoL8':_Diff_CtoL8,
                        '_Diff_CtoL9':_Diff_CtoL9,
                        '_Diff_CtoL10':_Diff_CtoL10,
                        '_Diff_CtoL11':_Diff_CtoL11,
                        '_Diff_CtoL12':_Diff_CtoL12,
                        '_Diff_CtoL13':_Diff_CtoL13,
                        '_Diff_CtoL14':_Diff_CtoL14,
                        '_Diff_CtoL15':_Diff_CtoL15,
                        '_Diff_CtoL16':_Diff_CtoL16,
                        '_Diff_CtoL17':_Diff_CtoL17,
                        '_Diff_CtoL18':_Diff_CtoL18,
                        '_Diff_CtoL19':_Diff_CtoL19,
                        '_Diff_CtoL20':_Diff_CtoL20,
                        '_Diff_CtoL21':_Diff_CtoL21,
                        '_Diff_CtoL22':_Diff_CtoL22,
                        '_Diff_CtoL23':_Diff_CtoL23,
                        '_Diff_CtoL24':_Diff_CtoL24,
                        '_Diff_CtoL25':_Diff_CtoL25,
                        '_Diff_CtoO':_Diff_CtoO,
                        '_Diff_CtoO1':_Diff_CtoO1,
                        '_Diff_CtoO2':_Diff_CtoO2,
                        '_Diff_CtoO3':_Diff_CtoO3,
                        '_Diff_CtoO4':_Diff_CtoO4,
                        '_Diff_CtoO5':_Diff_CtoO5,
                        '_Diff_CtoO6':_Diff_CtoO6,
                        '_Diff_CtoO7':_Diff_CtoO7,
                        '_Diff_CtoO8':_Diff_CtoO8,
                        '_Diff_CtoO9':_Diff_CtoO9,
                        '_Diff_CtoC1':_Diff_CtoC1,
                        '_Diff_CtoC2':_Diff_CtoC2,
                        '_Diff_CtoC3':_Diff_CtoC3,
                        '_Diff_CtoC4':_Diff_CtoC4,
                        '_Diff_CtoC5':_Diff_CtoC5,
                        '_Diff_CtoC6':_Diff_CtoC6,
                        '_Diff_CtoC7':_Diff_CtoC7,
                        '_Diff_CtoC8':_Diff_CtoC8,
                        '_Diff_CtoC9':_Diff_CtoC9,
                        '_justOpen':_justOpen,
                        '_justHigh':_justHigh,
                        '_justLow':_justLow,
                        '_justClose':_justClose,
                        '_DiffU5_C':_DiffU5_C,
                        '_DiffD5_C':_DiffD5_C,
                        '_DiffU13_L3':_DiffU13_L3,
                        '_DiffD21_C':_DiffD21_C,
                        '_DiffD21_H3':_DiffD21_H3,
                        '_DiffU34_C':_DiffU34_C,
                        '_DiffD34_H3':_DiffD34_H3,
                        '_DiffU55_L3':_DiffU55_L3,
                        '_DiffU89_C':_DiffU89_C,
                        '_DiffU89_L3':_DiffU89_L3,
                        '_DiffU144_L3':_DiffU144_L3,
                        '_DiffU233_C':_DiffU233_C,
                        '_DiffU300_C':_DiffU300_C,
                        '_DiffD300_C':_DiffD300_C,
                        '_High3_H':_High3_H,
                        '_High5_H':_High5_H,
                        '_High100_H':_High100_H,
                        '_High377_H':_High377_H,
                        '_Low3_L':_Low3_L,
                        '_Low34_L':_Low34_L,
                        '_Low55_L':_Low55_L,
                        '_Hi3to5':_Hi3to5,
                        '_Hi5to8':_Hi5to8,
                        '_Hi8to13':_Hi8to13,
                        '_Hi34to55':_Hi34to55,
                        '_Hi233to377':_Hi233to377,
                        '_Lo3to5':_Lo3to5,
                        '_Lo233to377':_Lo233to377,
                        '_EvNo5':_EvNo5,
                        }, ignore_index = True)
            ### Write Pandas Datafram to .xlsx file                        
            FileLocation4excel = r'for'+eachTicker+'_excel.xlsx'
            df.to_excel(FileLocation4excel, index=False)
        except Exception as e:
            printToFile = (str(e))
            logFile = open('lo0gFile.txt','a')
            logFile.write(printToFile)
            logFile.close()

### END part Two - Load fresh data and create all additional Features AND
### save all data to one .xlsx file for each ticker
###-----------------------------------------------------------------------------
### START part Three "PREDICTION PROCESS" - Load fresh data from .xlsc file and make Predictions from todays intraday data


    ### Cleaning up unnecessary files
    for eachTicker in yahoo_ticker_list:
        try:
            os.remove(r''+eachTicker+'.txt')###
        except Exception as e:
            print(str(e))
    for eachTicker in yahoo_ticker_list:
        try:
            os.remove(r'EODtoday'+eachTicker+'.txt')###
        except Exception as e:
            print(str(e))
    for eachTicker in yahoo_ticker_list:
        try:                
            os.remove(r'todayEOD'+eachTicker+'.txt')###
        except Exception as e:
            print(str(e))
    for eachTicker in yahoo_ticker_list:
        try:         
            os.remove(r'5min'+eachTicker+'.txt')###        
        except Exception as e:
            print(str(e))    
    ### END Cleaning up unnecessary files

### START part with letting the algo make prediction/Outlook from the fresh data from the .xlsx file
            
    printToFile = (str("Start makeing Forecasts"))
    logFile = open('lo0gFile.txt','a')
    logFile.write("\n" + printToFile)
    logFile.close()

    barChartName = [] #making some empty datalists
    barChartForecast = []         

    Ultimate_df2 = pd.DataFrame(columns = ['[Name]', '[Forecast]']) # creating empty Pandas dataframe

    for eachTicker, eachRealNames in zip(yahoo_ticker_list, yahoo_RealNames_list):
        try:
            global GLBeachName 
            GLBeachName = eachRealNames            
            
            Location = r'for'+eachTicker+'_excel.xlsx'
            data = pd.read_excel(Location)
            X = np.array(data[FEATURES].values) # making a Numpay array from the Pandas dataset
            y1 = data['_justClose'].values # saves the intraday close value 

    ### START loading the saved .pkl files with trained algo information and creating final Prediction/Outlook
    ### Every joblib.load indicates one .pkl file
    ### The file name indicates for how many future days the algo is trained to predict the outcome for (1d = One day)
    ### The first 7 algos calculate on how high the Risk/Reward Ratio was for future move 
    ### the second 7 algos calculate how Big the future move was, using a lot of averageing out to smother the result.
    ### Every trained algo give 5 predictions; StrogSell, Sell, Neutral, Buy and StrongBuy (5cat = five categories)
    ### Every predictions contains a percanage chanse for all of the 5 possible outcomes
    ### Each of the five predictions in % are stored in variable, for every trained algo
            logreg1 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat1d.pkl')
            Value1D = logreg1.predict_proba(X)
            Sell1D = round(Value1D[0][0],4)
            Under1D = round(Value1D[0][1],4)
            Hold1D = round(Value1D[0][2],4)
            Over1D = round(Value1D[0][3],4)
            Buy1D = round(Value1D[0][4],4) 
    
            logreg2 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat2d.pkl')
            Value2D = logreg2.predict_proba(X)
            Sell2D = round(Value2D[0][0],4)
            Under2D = round(Value2D[0][1],4)
            Hold2D = round(Value2D[0][2],4)
            Over2D = round(Value2D[0][3],4)
            Buy2D = round(Value2D[0][4],4)          
    
            logreg3 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat3d.pkl')
            Value3D = logreg3.predict_proba(X)
            Sell3D = round(Value3D[0][0],4)
            Under3D = round(Value3D[0][1],4)
            Hold3D = round(Value3D[0][2],4)
            Over3D = round(Value3D[0][3],4)
            Buy3D = round(Value3D[0][4],4)           
    
            logreg5 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat5d.pkl')
            Value5D = logreg5.predict_proba(X)
            Sell5D = round(Value5D[0][0],4)
            Under5D = round(Value5D[0][1],4)
            Hold5D = round(Value5D[0][2],4)
            Over5D = round(Value5D[0][3],4)
            Buy5D = round(Value5D[0][4],4) 
    
            logreg8 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat8d.pkl')
            Value8D = logreg8.predict_proba(X)
            Sell8D = round(Value8D[0][0],4)
            Under8D = round(Value8D[0][1],4)
            Hold8D = round(Value8D[0][2],4)
            Over8D = round(Value8D[0][3],4)
            Buy8D = round(Value8D[0][4],4) 
    
            logreg13 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat13d.pkl')
            Value13D = logreg13.predict_proba(X)
            Sell13D = round(Value13D[0][0],4)
            Under13D = round(Value13D[0][1],4)
            Hold13D = round(Value13D[0][2],4)
            Over13D = round(Value13D[0][3],4)
            Buy13D = round(Value13D[0][4],4) 
            
            logreg21 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat21d.pkl')
            Value21D = logreg21.predict_proba(X)
            Sell21D = round(Value21D[0][0],4)
            Under21D = round(Value21D[0][1],4)
            Hold21D = round(Value21D[0][2],4)
            Over21D = round(Value21D[0][3],4)
            Buy21D = round(Value21D[0][4],4) 

            ### Part with algos based on calculating how Big the future move was

            roc_logreg1 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat1dROC.pkl')
            roc_Value1D = roc_logreg1.predict_proba(X)
            roc_Sell1D = round(roc_Value1D[0][0],4)
            roc_Under1D = round(roc_Value1D[0][1],4)
            roc_Hold1D = round(roc_Value1D[0][2],4)
            roc_Over1D = round(roc_Value1D[0][3],4)
            roc_Buy1D = round(roc_Value1D[0][4],4) 
    
            roc_logreg2 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat2dROC.pkl')
            roc_Value2D = roc_logreg2.predict_proba(X)
            roc_Sell2D = round(roc_Value2D[0][0],4)
            roc_Under2D = round(roc_Value2D[0][1],4)
            roc_Hold2D = round(roc_Value2D[0][2],4)
            roc_Over2D = round(roc_Value2D[0][3],4)
            roc_Buy2D = round(roc_Value2D[0][4],4)          
    
            roc_logreg3 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat3dROC.pkl')
            roc_Value3D = roc_logreg3.predict_proba(X)
            roc_Sell3D = round(roc_Value3D[0][0],4)
            roc_Under3D = round(roc_Value3D[0][1],4)
            roc_Hold3D = round(roc_Value3D[0][2],4)
            roc_Over3D = round(roc_Value3D[0][3],4)
            roc_Buy3D = round(roc_Value3D[0][4],4)           
    
            roc_logreg5 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat5dROC.pkl')
            roc_Value5D = roc_logreg5.predict_proba(X)
            roc_Sell5D = round(roc_Value5D[0][0],4)
            roc_Under5D = round(roc_Value5D[0][1],4)
            roc_Hold5D = round(roc_Value5D[0][2],4)
            roc_Over5D = round(roc_Value5D[0][3],4)
            roc_Buy5D = round(roc_Value5D[0][4],4) 
    
            roc_logreg8 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat8dROC.pkl')
            roc_Value8D = roc_logreg8.predict_proba(X)
            roc_Sell8D = round(roc_Value8D[0][0],4)
            roc_Under8D = round(roc_Value8D[0][1],4)
            roc_Hold8D = round(roc_Value8D[0][2],4)
            roc_Over8D = round(roc_Value8D[0][3],4)
            roc_Buy8D = round(roc_Value8D[0][4],4) 
    
            roc_logreg13 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat13dROC.pkl')
            roc_Value13D = roc_logreg13.predict_proba(X)
            roc_Sell13D = round(roc_Value13D[0][0],4)
            roc_Under13D = round(roc_Value13D[0][1],4)
            roc_Hold13D = round(roc_Value13D[0][2],4)
            roc_Over13D = round(roc_Value13D[0][3],4)
            roc_Buy13D = round(roc_Value13D[0][4],4) 
            
            roc_logreg21 = joblib.load(r'C:\Users\UserTrader\Documents\_PKLfiles_02\IQ14_5cat21dROC.pkl')
            roc_Value21D = roc_logreg21.predict_proba(X)
            roc_Sell21D = round(roc_Value21D[0][0],4)
            roc_Under21D = round(roc_Value21D[0][1],4)
            roc_Hold21D = round(roc_Value21D[0][2],4)
            roc_Over21D = round(roc_Value21D[0][3],4)
            roc_Buy21D = round(roc_Value21D[0][4],4)

    ### END loading the saved .pkl files with trained algo information

    ### START building own indicators for final prediction values
    
        ### 1st stage, adding all StrongBuy percentage vs all StrongSell percantage
        ### continuing with comparing all Buy percantage vs all Sell percentage
            ### Doing this for the 7 algos based on future Pattern first
            Buy2stdav =  Buy1D+Buy2D+Buy3D+Buy5D+Buy8D+Buy13D+Buy21D
            Sell2stdav = Sell1D+Sell2D+Sell3D+Sell5D+Sell8D+Sell13D+Sell21D
            Over1stdav = Over1D+Over2D+Over3D+Over5D+Over8D+Over13D+Over21D
            Under1stdav = Under1D+Under2D+Under3D+Under5D+Under8D+Under13D+Under21D
            ### 2nd stage, Comparing all positive percentage vs all negative percentage
            BuyVsSell = Buy2stdav-Sell2stdav 
            OverVsUnder = (Over1stdav-Under1stdav)/27.0 ### using divide by 27 to normalise Strong vs Normal Buy/Sell
            preOutlook = BuyVsSell + OverVsUnder
                        
            ### Will only use value if it is high enough, else = 0
            pat_Outlook = float(0.0) 
            if  BuyVsSell > 0.010 and OverVsUnder > 0.010: 
                pat_Outlook = round(preOutlook*100,2)
            elif BuyVsSell < -0.009 and OverVsUnder < -0.009:
                pat_Outlook = round(preOutlook*100,2)
            else:
                pass

            ### Doing this one mote time, for the 7 algos based on future Big move last
            roc_Buy2stdav =  roc_Buy1D+roc_Buy2D+roc_Buy3D+roc_Buy5D+roc_Buy8D+roc_Buy13D+roc_Buy21D
            roc_Sell2stdav = roc_Sell1D+roc_Sell2D+roc_Sell3D+roc_Sell5D+roc_Sell8D+roc_Sell13D+roc_Sell21D
            roc_Over1stdav = roc_Over1D+roc_Over2D+roc_Over3D+roc_Over5D+roc_Over8D+roc_Over13D+roc_Over21D
            roc_Under1stdav = roc_Under1D+roc_Under2D+roc_Under3D+roc_Under5D+roc_Under8D+roc_Under13D+roc_Under21D
            roc_BuyVsSell = roc_Buy2stdav-roc_Sell2stdav
            roc_OverVsUnder = (roc_Over1stdav-roc_Under1stdav)/2.2
            roc_preOutlook = (roc_BuyVsSell + roc_OverVsUnder)/6.1
            roc_Outlook = float(0.0)

            if  roc_BuyVsSell > 0.017 and roc_OverVsUnder > 0.017:  
                roc_Outlook = round(roc_preOutlook*100,2)
            elif roc_BuyVsSell < -0.014 and roc_OverVsUnder < -0.014:
                roc_Outlook = round(roc_preOutlook*100,2)
            else:
                pass
        ### This value is the Final Outlook for the individual Instrument
            Outlook = round(pat_Outlook + (roc_Outlook),2)
            global GLBoutlook             
            GLBoutlook = Outlook
            print(roc_Outlook)
            print(pat_Outlook)
            print(Outlook)             

        ### In some circumstances I put Names to the Outlook values, if the value is not strong enough it gets set to 0
            Trade = '--On Hold--'      
            if roc_Outlook > 0.017 and pat_Outlook > 0.01 and Outlook > 0.04:
                Trade = 'BUY'
            elif roc_Outlook > 0.017 or pat_Outlook > 0.01 and Outlook > 0.04:
                Trade = 'Strong'
            elif roc_Outlook < -0.014 and pat_Outlook < -0.009 and Outlook < -0.009:
                Trade = 'SHORT'
            elif roc_Outlook < -0.014 or pat_Outlook < -0.009 and Outlook < -0.009:
                Trade = 'Weak'                
            else:
                pass                
 
            barChartName.append(GLBeachName)
            barChartForecast.append(GLBoutlook)

            Ultimate_df2 = Ultimate_df2.append({'[Name]':eachRealNames,
                                                '[Forecast]':Outlook,
                                                }, ignore_index = True) 
        
        except Exception as e:
            printToFile = (str(e))
            logFile = open('lo0gFile.txt','a')
            logFile.write("\n" + printToFile)
            logFile.close()

    printToFile = (str("Done makeing Forecasts"))
    logFile = open('lo0gFile.txt','a')
    logFile.write("\n" + printToFile)
    logFile.close()            
    
    ### Saving the results to .xlsx file
    File2Location4excel = r'TEST_DB_excel.xlsx'
    import datetime
    import time#   
    unixTimestamp = int(time.time())
    timestamp = str(datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%Y-%m-%d %H_%M'))
    print(timestamp)
    Ultimate_df = Ultimate_df2.sort('[Forecast]', ascending=False)
    print(Ultimate_df)
    global theList
    theList = Ultimate_df
    time.sleep(3)

### END part with letting the algo make prediction/Outlook from the fresh data from the .xlsx file


### START - Part that create barchart of all predictions in instrument list

    import matplotlib
    matplotlib.style.use('ggplot')
    import matplotlib.pyplot as plt
    import datetime
    import time#   
    unixTimestamp = int(time.time())
    timestamp = str(datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%Y-%m-%d %H_%M'))
    
    pltTitle = str(timestamp + ' CET  predictive algo IQ1.4: ' + inputList)    
    
    Ultimate_df.set_index(["[Name]"],inplace=True)
    Ultimate_df.plot(kind='bar',alpha=0.75, rot=75, title="", legend=False)
    plt.xlabel("")
    fig1 = plt.gcf()
    fig1.set_size_inches(16, 9)
    plt.title(pltTitle,fontsize=26, fontweight='bold', color='#7f7f7f',family='Courier New')
    plt.show()
    plt.draw()
    fig1.savefig(r'C:\Users\UserTrader\Documents\_Image\\'+inputList+'.png', dpi=72)

### END - Part that create barchart of all predictions in instrument list

def myTextNo1():
    skrivutlista = indataNo2.get()
    if skrivutlista == 1:
        lista = str("ASIA")
        makeForecast(lista)
        Txt_list = Text(myGui, height=35, width=40)
        Txt_list.grid(row=5, column=1, rowspan=20, columnspan=3, sticky=NW, padx=10, pady=3)
        Txt_list.insert(END, theList)
        unixTimestamp = int(time.time())
        timestamp = (datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%Y-%m-%d %H:%M'))        
        Txt_TS = Text(myGui, height=1, width=18)
        Txt_TS.grid(row=3, column=2, rowspan=1, columnspan=2, sticky=NW, padx=10, pady=3)
        Txt_TS.insert(END, timestamp)

    elif skrivutlista == 2:
        lista = str("EU")
        makeForecast(lista)
        Txt_list = Text(myGui, height=35, width=40)
        Txt_list.grid(row=5, column=1, rowspan=20, columnspan=3, sticky=NW, padx=10, pady=3)
        Txt_list.insert(END, theList)
        unixTimestamp = int(time.time())
        timestamp = (datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%Y-%m-%d %H:%M'))        
        Txt_TS = Text(myGui, height=1, width=18)
        Txt_TS.grid(row=3, column=2, rowspan=1, columnspan=2, sticky=NW, padx=10, pady=3)
        Txt_TS.insert(END, timestamp)        

    elif skrivutlista == 3:
        lista = str("OMX30")
        makeForecast(lista)        
        Txt_list = Text(myGui, height=35, width=40)
        Txt_list.grid(row=5, column=1, rowspan=20, columnspan=3, sticky=NW, padx=10, pady=3)
        Txt_list.insert(END, theList)
        unixTimestamp = int(time.time())
        timestamp = (datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%Y-%m-%d %H:%M'))        
        Txt_TS = Text(myGui, height=1, width=18)
        Txt_TS.grid(row=3, column=2, rowspan=1, columnspan=2, sticky=NW, padx=10, pady=3)
        Txt_TS.insert(END, timestamp)                

    elif skrivutlista == 4:
        lista = str("USA")
        makeForecast(lista)
        Txt_list = Text(myGui, height=35, width=40)
        Txt_list.grid(row=5, column=1, rowspan=20, columnspan=3, sticky=NW, padx=10, pady=3)
        Txt_list.insert(END, theList)
        unixTimestamp = int(time.time())
        timestamp = (datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%Y-%m-%d %H:%M'))        
        Txt_TS = Text(myGui, height=1, width=18)
        Txt_TS.grid(row=3, column=2, rowspan=1, columnspan=2, sticky=NW, padx=10, pady=3)
        Txt_TS.insert(END, timestamp)                
        
    elif skrivutlista == 5:
        lista = str("DOW30")
        makeForecast(lista)
        Txt_list = Text(myGui, height=35, width=40)
        Txt_list.grid(row=5, column=1, rowspan=20, columnspan=3, sticky=NW, padx=10, pady=3)
        Txt_list.insert(END, theList)
        unixTimestamp = int(time.time())
        timestamp = (datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%Y-%m-%d %H:%M'))        
        Txt_TS = Text(myGui, height=1, width=18)
        Txt_TS.grid(row=3, column=2, rowspan=1, columnspan=2, sticky=NW, padx=10, pady=3)
        Txt_TS.insert(END, timestamp)                
        
    else:
        lista = str("Valuta")
        makeForecast(lista)
        Txt_list = Text(myGui, height=35, width=40)
        Txt_list.grid(row=5, column=1, rowspan=20, columnspan=3, sticky=NW, padx=10, pady=3)
        Txt_list.insert(END, theList)
        unixTimestamp = int(time.time())
        timestamp = (datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%Y-%m-%d %H:%M'))        
        Txt_TS = Text(myGui, height=1, width=18)
        Txt_TS.grid(row=3, column=2, rowspan=1, columnspan=2, sticky=NW, padx=10, pady=3)
        Txt_TS.insert(END, timestamp)                

    
myGui = Tk()
indataNo1 = StringVar() 
indataNo2 = IntVar() 

myGui.geometry("1080x720+150+150")
myGui.title('Imundbo Quant Forecaster  beta-v0.6')

myButton = Button(myGui, text = 'Make forecast', command=myTextNo1)
myButton.grid(row=3, column=1, padx=10, pady=2, sticky=NW)

Txt_info = Text(myGui, height=26, width=70)
Txt_info.grid(row=0, column=5, rowspan=26, padx=3, pady=3, sticky=NW)
Txt_info.insert(END, """Quantitative Analysis Spec.
____________________________________
Language & library: Python & Scikit-learn
Classifier:         Ensemble (Random Tree)
No of Sample Inst.: 192, KibotData 50Stocks&ETFs + All Cont. Fut.
No of Feature:      108, from Pattern Recognition & Volatility
No of labels:       5, diff. outcomes (equally weighted)
No of models:       8 diff time lenghts (equally weighted)
New Data:           Yahoo finance - (EOD + Intraday)
Developer:          Mikael Furesjo (mikael@furesjo.se)
""")


myRadioB_1 = Radiobutton(myGui, text="ASIA-5 (default)", variable=indataNo2, value = 1).grid(row=0, column=1, sticky=NW, padx=10)
myRadioB_1 = Radiobutton(myGui, text="EU-10", variable=indataNo2, value = 2).grid(row=0, column=2, sticky=NW, padx=10)
myRadioB_1 = Radiobutton(myGui, text="OMX30-26", variable=indataNo2, value = 3).grid(row=0, column=3, sticky=NW, padx=10)
myRadioB_1 = Radiobutton(myGui, text="NYSE/CME-13", variable=indataNo2, value = 4).grid(row=1, column=1, sticky=NW, padx=10)
myRadioB_1 = Radiobutton(myGui, text="DOW30-31", variable=indataNo2, value = 5).grid(row=1, column=2, sticky=NW, padx=10)
myRadioB_1 = Radiobutton(myGui, text="Forex-22", variable=indataNo2, value = 6).grid(row=1, column=3, sticky=NW, padx=10)


myGui.mainloop()



