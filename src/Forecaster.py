import pandas as pd
import numpy as np
from datetime import datetime
import dateutil
import datetime
import time#
import os
import sys

from gui.console import Console


def makeForecast(inputList):
    try:
        c = Console(None, False, False)
        print("Starting iteration timeline...")

        ##################### CHANGE PATH TO THE DIRECTORY YOU USE ON YOUR COMPUTER ##############
        #importantPath = 'C:\Users\UserTrader\Documents\ImundboQuant\pklFiles\FX30_IQ19p'
        importantPath = r'c:\Documents\ImundboQuant'
        ##################### CHANGE PATH TO THE DIRECTORY USED BY YOUR MetaTrader4 (MT4) PLATFORM ON YOUR COMPUTER ########
        ##################### FROM MT4, FIND THE DIRECTORY UNDER "FILES" => "OPEN DATA FOLDER"  ########        
        #MetaStockCSVfile = 'C:\Users\UserTrader\AppData\Roaming\MetaQuotes\Terminal\C142B020C05FAD9EEC4BE1375F709241\MQL4\Files\orderdata' ## IG Markets
        #MetaStockPath = 'C:\Users\UserTrader\AppData\Roaming\MetaQuotes\Terminal\C142B020C05FAD9EEC4BE1375F709241\MQL4\Files\Research'
        MetaStockCSVfile = r'c:\Users\victo\AppData\Roaming\MetaQuotes\Terminal\53264E01B18B63DA7BC348929475A97C\MQL4\Files\orderdata'
        MetaStockPath = r'c:\Users\victo\AppData\Roaming\MetaQuotes\Terminal\53264E01B18B63DA7BC348929475A97C\MQL4\Files\Research'

        ########################################################################

        FeatFiles = '\\FX30_IQ19p_Feat_Slot'
        pklFiles = '\\FX30_IQ19p_Slot'      
        
        yahoo_ticker_list = []
        readThisFile = r''+importantPath+'\lista_' + inputList +'.txt'
        TickerFile = open(readThisFile)
        fleraTickers = TickerFile.read()
        yahoo_ticker_list = fleraTickers.split('\n')
        TickerFile.close()
    
        yahoo_RealNames_list = []
        readThisFile = r''+importantPath+'\lista_' + inputList +'_RealNames.txt'
        TickerFile = open(readThisFile)
        fleraTickers = TickerFile.read()
        yahoo_RealNames_list = fleraTickers.split('\n')
        TickerFile.close()
    
        c.timer.print_elapsed("Processing {0} tickers with {1} realnames".format(len(yahoo_ticker_list), len(yahoo_RealNames_list)))

        #### Get content for the FEATURE list, from file in Python root dir.
        print("Getting features based on {0} files...".format(FeatFiles))

        FEATURES_IQ19 = []
        readThisFile = r''+importantPath+FeatFiles+'ALL.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES_IQ19 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES01 = []
        readThisFile = r''+importantPath+FeatFiles+'01.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES01 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES02 = []
        readThisFile = r''+importantPath+FeatFiles+'02.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES02 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES03 = []
        readThisFile = r''+importantPath+FeatFiles+'03.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES03 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES04 = []
        readThisFile = r''+importantPath+FeatFiles+'04.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES04 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES05 = []
        readThisFile = r''+importantPath+FeatFiles+'05.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES05 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES06 = []
        readThisFile = r''+importantPath+FeatFiles+'06.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES06 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES07 = []
        readThisFile = r''+importantPath+FeatFiles+'07.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES07 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES08 = []
        readThisFile = r''+importantPath+FeatFiles+'08.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES08 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES09 = []
        readThisFile = r''+importantPath+FeatFiles+'09.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES09 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES10 = []
        readThisFile = r''+importantPath+FeatFiles+'10.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES10 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES11 = []
        readThisFile = r''+importantPath+FeatFiles+'11.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES11 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES12 = []
        readThisFile = r''+importantPath+FeatFiles+'12.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES12 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES13 = []
        readThisFile = r''+importantPath+FeatFiles+'13.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES13 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES14 = []
        readThisFile = r''+importantPath+FeatFiles+'14.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES14 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES15 = []
        readThisFile = r''+importantPath+FeatFiles+'15.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES15 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES16 = []
        readThisFile = r''+importantPath+FeatFiles+'16.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES16 = fleraFeatures.split('\n')
        featuresFile.close()        
        
        FEATURES17 = []
        readThisFile = r''+importantPath+FeatFiles+'17.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES17 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES18 = []
        readThisFile = r''+importantPath+FeatFiles+'18.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES18 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES19 = []
        readThisFile = r''+importantPath+FeatFiles+'19.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES19 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES20 = []
        readThisFile = r''+importantPath+FeatFiles+'20.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES20 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES21 = []
        readThisFile = r''+importantPath+FeatFiles+'21.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES21 = fleraFeatures.split('\n')
        featuresFile.close()        
        
        FEATURES22 = []
        readThisFile = r''+importantPath+FeatFiles+'22.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES22 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES23 = []
        readThisFile = r''+importantPath+FeatFiles+'23.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES23 = fleraFeatures.split('\n')
        featuresFile.close()        
        
        FEATURES24 = []
        readThisFile = r''+importantPath+FeatFiles+'24.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES24 = fleraFeatures.split('\n')
        featuresFile.close()        
        
        FEATURES25 = []
        readThisFile = r''+importantPath+FeatFiles+'25.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES25 = fleraFeatures.split('\n')
        featuresFile.close()        
        
        FEATURES26 = []
        readThisFile = r''+importantPath+FeatFiles+'26.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES26 = fleraFeatures.split('\n')
        featuresFile.close()        
        
        FEATURES27 = []
        readThisFile = r''+importantPath+FeatFiles+'27.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES27 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES28 = []
        readThisFile = r''+importantPath+FeatFiles+'28.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES28 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES29 = []
        readThisFile = r''+importantPath+FeatFiles+'29.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES29 = fleraFeatures.split('\n')
        featuresFile.close()
        
        FEATURES30 = []
        readThisFile = r''+importantPath+FeatFiles+'30.txt'
        featuresFile = open(readThisFile)
        fleraFeatures = featuresFile.read()
        FEATURES30 = fleraFeatures.split('\n')
        featuresFile.close()        

        c.timer.print_elapsed("Finished getting features".format(FeatFiles))

    except Exception as e:
        print(str(e))    
        pass
    
    try:    
        print("\n\n============\n")

        for eachTicker in yahoo_ticker_list:
            FileLocation = r''+MetaStockPath+"\\"+eachTicker+'.txt'
            print("\nOpening ticker {0}...".format(eachTicker))
            Unix, Open, High, Low, Close = np.loadtxt(FileLocation, delimiter=',', unpack=True)
            print("Loaded {0}, computing features...".format(eachTicker))

            _dateDayOfYear = float(datetime.datetime.fromtimestamp(Unix[-1]).strftime('%j'))
            _dateWeekOfYear = float(datetime.datetime.fromtimestamp(Unix[-1]).strftime('%W'))
            _dateMonthOfYear = float(datetime.datetime.fromtimestamp(Unix[-1]).strftime('%m'))
            _dateDayOfMonth = float(datetime.datetime.fromtimestamp(Unix[-1]).strftime('%d'))
            _dateDayOfWeek = float(datetime.datetime.fromtimestamp(Unix[-1]).strftime('%w'))
            
            try:            
                _Diff_CpLf = (np.amin(Low[-1-6:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-6:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_05 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass
            try:            
                _Diff_CpLf = (np.amin(Low[-1-7:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-7:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_06 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass


            try:            
                _Diff_CpLf = (np.amin(Low[-1-8:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-8:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_07 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-9:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-9:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_08 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-10:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-10:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_09 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-11:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-11:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_10 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-12:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-12:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_11 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-13:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-13:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_12 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-14:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-14:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_13 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-15:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-15:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_14 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-16:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-16:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_15 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-17:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-17:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_16 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-18:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-18:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_17 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-19:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-19:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_18 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-20:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-20:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_19 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-21:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-21:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_20 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-22:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-22:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_21 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-23:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-23:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_22 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-24:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-24:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_23 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-25:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-25:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_24 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-26:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-26:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_25 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-27:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-27:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_26 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-28:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-28:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_27 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-29:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-29:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_28 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-30:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-30:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_29 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-31:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-31:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_30 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-32:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-32:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_31 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-33:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-33:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_32 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-34:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-34:-1])-Close[-1])/Close[-1]
                _CpHf_Less_CpLf = _Diff_CpHf - _Diff_CpLf
                _ABSofDiff_CpLf = abs(_Diff_CpLf)
                _ABSofDiff_CpHf = abs(_Diff_CpHf)
                _KeyValueLong = _ABSofDiff_CpHf/_CpHf_Less_CpLf
                _KeyValueShort = _ABSofDiff_CpLf/_CpHf_Less_CpLf
                _PastSharp_33 = np.round(_KeyValueLong - _KeyValueShort,6)
            except Exception as e:
                pass

            try:            
                _Diff_CpLf = (np.amin(Low[-1-35:-1])-Close[-1])/Close[-1]
                _Diff_CpHf = (np.amax(High[-1-35:-1])-Close[-1])/Close[-1]
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
            
            Zeros = [1]*len(Unix)
            RL3 = np.round(np.polyfit(Zeros[:-4:-1], Close[:-4:-1], 0),13)
            RL5 = np.round(np.polyfit(Zeros[:-6:-1], Close[:-6:-1], 0),13)            
            RL8 = np.round(np.polyfit(Zeros[:-9:-1], Close[:-9:-1], 0),13)
            RL13 = np.round(np.polyfit(Zeros[:-14:-1], Close[:-14:-1], 0),13)
            RL21 = np.round(np.polyfit(Zeros[:-22:-1], Close[:-22:-1], 0),13)
            RL34 = np.round(np.polyfit(Zeros[:-35:-1], Close[:-35:-1], 0),13)
            RL55 = np.round(np.polyfit(Zeros[:-56:-1], Close[:-56:-1], 0),13)           
            RL89 = np.round(np.polyfit(Zeros[:-90:-1], Close[:-90:-1], 0),13)           
            RL100 = np.round(np.polyfit(Zeros[:-101:-1], Close[:-101:-1], 0),13)      
            RL144 = np.round(np.polyfit(Zeros[:-145:-1], Close[:-145:-1], 0),13)                
            RL200 = np.round(np.polyfit(Zeros[:-201:-1], Close[:-201:-1], 0),13)
            RL233 = np.round(np.polyfit(Zeros[:-234:-1], Close[:-234:-1], 0),13)
            RL377 = np.round(np.polyfit(Zeros[:-378:-1], Close[:-378:-1], 0),13)
            
            Diff_C_RL8 = (Close[-1]-RL8)/RL8
            Diff_C_RL34 = (Close[-1]-RL34)/RL34
            Diff_C_RL89 = (Close[-1]-RL89)/RL89
            Diff_C_RL100 = (Close[-1]-RL100)/RL100            
    
            Diff_RL3_RL8 = (RL3-RL8)/RL8
            Diff_RL5_RL13 = (RL5-RL13)/RL13
            Diff_RL5_RL21 = (RL5-RL21)/RL21
            Diff_RL5_RL34 = (RL5-RL34)/RL34                
            Diff_RL8_RL21 = (RL8-RL21)/RL21 
            Diff_RL8_RL34 = (RL8-RL34)/RL34 
            Diff_RL8_RL55 = (RL8-RL55)/RL55 
            Diff_RL13_RL21 = (RL13-RL21)/RL21 
            Diff_RL21_RL34 = (RL21-RL34)/RL34 
            Diff_RL34_RL55 = (RL34-RL55)/RL55  
            Diff_RL34_RL100 = (RL34-RL100)/RL100  
            Diff_RL34_RL144 = (RL34-RL144)/RL144 
            Diff_RL34_RL200 = (RL34-RL200)/RL200 
            Diff_RL55_RL89 = (RL55-RL89)/RL89 
            Diff_RL55_RL144 = (RL55-RL144)/RL144 
            Diff_RL55_RL200 = (RL55-RL200)/RL200
            Diff_RL89_RL100 = (RL89-RL100)/RL100
            Diff_RL89_RL377 = (RL89-RL377)/RL377             
            Diff_RL100_RL144 = (RL100-RL144)/RL144
            Diff_RL100_RL377 = (RL100-RL377)/RL377             
            Diff_RL100_RL200 = (RL100-RL200)/RL200
            Diff_RL144_RL200 = (RL144-RL200)/RL200
            Diff_RL144_RL377 = (RL144-RL377)/RL377          
            Diff_RL233_RL377 = (RL233-RL377)/RL377   
            Diff_RL100_RL233 = (RL100-RL233)/RL233          
            Diff_RL200_RL233 = (RL200-RL233)/RL233
            Diff_RL200_RL377 = (RL200-RL377)/RL377
    
            _stoch100 = (Close[-1]-np.amin(Low[:-100:-1]))/(np.amax(High[:-100:-1])-np.amin(Low[:-100:-1]))*100###---------
            if _stoch100 > 80:
                _stoch100Level = 1.0  
            elif _stoch100 < 20:
                _stoch100Level = -1.0
            else:
                _stoch100Level = 0.0 
    
            _stoch55 = (Close[-1]-np.amin(Low[:-55:-1]))/(np.amax(High[:-55:-1])-np.amin(Low[:-55:-1]))*100###---------
            if _stoch55 > 80:
                _stoch55Level = 1.0  
            elif _stoch55 < 20:
                _stoch55Level = -1.0
            else:
                _stoch55Level = 0.0 
    
            _stoch5 = (Close[-1]-np.amin(Low[:-5:-1]))/(np.amax(High[:-5:-1])-np.amin(Low[:-5:-1]))*100###---------
            if _stoch5 > 80:
                _stoch5Level = 1.0  
            elif _stoch5 < 20:
                _stoch5Level = -1.0
            else:
                _stoch5Level = 0.0 
    
            _stoch89 = (Close[-1]-np.amin(Low[:-89:-1]))/(np.amax(High[:-89:-1])-np.amin(Low[:-89:-1]))*100###---------
            if _stoch89 > 80:
                _stoch89Level = 1.0  
            elif _stoch89 < 20:
                _stoch89Level = -1.0
            else:
                _stoch89Level = 0.0 
    
            _STD3_C = np.std(Close[:-4:-1])/Close[-1]
            _STD3_C1m = np.std(Close[:-5:-2])/Close[-2]        
            _STD3_C2m = np.std(Close[:-6:-3])/Close[-3]        
            _STD3_C3m = np.std(Close[:-7:-4])/Close[-4]
            _STD3_C4m = np.std(Close[:-8:-5])/Close[-5]        
            _STD3sign = (_STD3_C + _STD3_C1m + _STD3_C2m + _STD3_C3m + _STD3_C4m)/5
    
            _STD5_C = np.std(Close[:-6:-1])/Close[-1]
            _STD5_C1m = np.std(Close[:-7:-2])/Close[-2]        
            _STD5_C2m = np.std(Close[:-8:-3])/Close[-3]        
            _STD5_C3m = np.std(Close[:-9:-4])/Close[-4]
            _STD5_C4m = np.std(Close[:-10:-5])/Close[-5]       
            _STD5sign = (_STD5_C + _STD5_C1m + _STD5_C2m + _STD5_C3m + _STD5_C4m)/5
            _STD5vsSign = (_STD5_C-_STD5sign)/_STD5sign
    
            _STD13_C = np.std(Close[:-14:-1])/Close[-1]
            _STD13_C1m = np.std(Close[:-15:-2])/Close[-2]        
            _STD13_C2m = np.std(Close[:-16:-3])/Close[-3]       
            _STD13_C3m = np.std(Close[:-17:-4])/Close[-4]
            _STD13_C4m = np.std(Close[:-18:-5])/Close[-5]    
            _STD13sign = (_STD13_C + _STD13_C1m + _STD13_C2m + _STD13_C3m + _STD13_C4m)/5            
            _STD13vsSign = (_STD13_C-_STD13sign)/_STD13sign
    
            _STD21_C = np.std(Close[:-22:-1])/Close[-1]
            _STD21_C1m = np.std(Close[:-23:-2])/Close[-2]        
            _STD21_C2m = np.std(Close[:-24:-3])/Close[-3]       
            _STD21_C3m = np.std(Close[:-25:-4])/Close[-4]
            _STD21_C4m = np.std(Close[:-26:-5])/Close[-5]    
            _STD21sign = (_STD21_C + _STD21_C1m + _STD21_C2m + _STD21_C3m + _STD21_C4m)/5            
            _STD21vsSign = (_STD21_C-_STD21sign)/_STD21sign
    
            _STD34_C = np.std(Close[:-35:-1])/Close[-1]
            _STD34_C1m = np.std(Close[:-36:-2])/Close[-2]        
            _STD34_C2m = np.std(Close[:-37:-3])/Close[-3]        
            _STD34_C3m = np.std(Close[:-38:-4])/Close[-4]
            _STD34_C4m = np.std(Close[:-39:-5])/Close[-5]   
            _STD34sign = (_STD34_C + _STD34_C1m + _STD34_C2m + _STD34_C3m + _STD34_C4m)/5            
            _STD34vsSign = (_STD34_C-_STD34sign)/_STD34sign
    
            _STD55_C = np.std(Close[:-56:-1])/Close[-1]
            _STD55_C1m = np.std(Close[:-57:-2])/Close[-2]       
            _STD55_C2m = np.std(Close[:-58:-3])/Close[-3]       
            _STD55_C3m = np.std(Close[:-59:-4])/Close[-4]
            _STD55_C4m = np.std(Close[:-60:-5])/Close[-5]    
            _STD55sign = (_STD55_C + _STD55_C1m + _STD55_C2m + _STD55_C3m + _STD55_C4m)/5            
            _STD55vsSign = (_STD55_C-_STD55sign)/_STD55sign
    
            _STD89_C = np.std(Close[:-90:-1])/Close[-1]
            _STD89_C1m = np.std(Close[:-91:-2])/Close[-2]       
            _STD89_C2m = np.std(Close[:-92:-3])/Close[-3]       
            _STD89_C3m = np.std(Close[:-93:-4])/Close[-4]
            _STD89_C4m = np.std(Close[:-94:-5])/Close[-5]    
            _STD89sign = (_STD89_C + _STD89_C1m + _STD89_C2m + _STD89_C3m + _STD89_C4m)/5            
            _STD89vsSign = (_STD89_C-_STD89sign)/_STD89sign
    
            _STD100_C = np.std(Close[:-101:-1])/Close[-1]
            _STD100_C1m = np.std(Close[:-102:-2])/Close[-2]        
            _STD100_C2m = np.std(Close[:-103:-3])/Close[-3]        
            _STD100_C3m = np.std(Close[:-104:-4])/Close[-4]
            _STD100_C4m = np.std(Close[:-105:-5])/Close[-5]
            _STD100sign = (_STD100_C + _STD100_C1m + _STD100_C2m + _STD100_C3m + _STD100_C4m)/5
    
            _STD144_C = np.std(Close[:-145:-1])/Close[-1]
            _STD144_C1m = np.std(Close[:-146:-2])/Close[-2]        
            _STD144_C2m = np.std(Close[:-147:-3])/Close[-3]       
            _STD144_C3m = np.std(Close[:-148:-4])/Close[-4]
            _STD144_C4m = np.std(Close[:-149:-5])/Close[-5]    
            _STD144sign = (_STD144_C + _STD144_C1m + _STD144_C2m + _STD144_C3m + _STD144_C4m)/5            
            _STD144vsSign = (_STD144_C-_STD144sign)/_STD144sign
    
            _STD200_C = np.std(Close[:-201:-1])/Close[-1]
            _STD200_C1m = np.std(Close[:-202:-2])/Close[-2]        
            _STD200_C2m = np.std(Close[:-203:-3])/Close[-3]        
            _STD200_C3m = np.std(Close[:-204:-4])/Close[-4]
            _STD200_C4m = np.std(Close[:-205:-5])/Close[-5]
            _STD200sign = (_STD200_C + _STD200_C1m + _STD200_C2m + _STD200_C3m + _STD200_C4m)/5
            _STD200vsSign = (_STD200_C-_STD200sign)/_STD200sign
            
            _STD233_C = np.std(Close[:-234:-1])/Close[-1]
            _STD233_C1m = np.std(Close[:-235:-2])/Close[-2]        
            _STD233_C2m = np.std(Close[:-236:-3])/Close[-3]        
            _STD233_C3m = np.std(Close[:-237:-4])/Close[-4]
            _STD233_C4m = np.std(Close[:-238:-5])/Close[-5]
            _STD233sign = (_STD233_C + _STD233_C1m + _STD233_C2m + _STD233_C3m + _STD233_C4m)/5
            
            _STD300_C = np.std(Close[:-145:-1])/Close[-1]
            _STD300_C1m = np.std(Close[:-146:-2])/Close[-2]        
            _STD300_C2m = np.std(Close[:-147:-3])/Close[-3]       
            _STD300_C3m = np.std(Close[:-148:-4])/Close[-4]
            _STD300_C4m = np.std(Close[:-149:-5])/Close[-5]    
            _STD300sign = (_STD300_C + _STD300_C1m + _STD300_C2m + _STD300_C3m + _STD300_C4m)/5            
            _STD300vsSign = (_STD300_C-_STD300sign)/_STD300sign            
          
            _STD377_C = np.std(Close[:-378:-1])/Close[-1]
            _STD377_C1m = np.std(Close[:-379:-2])/Close[-2]        
            _STD377_C2m = np.std(Close[:-380:-3])/Close[-3]        
            _STD377_C3m = np.std(Close[:-381:-4])/Close[-4]
            _STD377_C4m = np.std(Close[:-382:-5])/Close[-5]
            _STD377sign = (_STD377_C + _STD377_C1m + _STD377_C2m + _STD377_C3m + _STD377_C4m)/5 
            _STD377vsSign = (_STD377_C-_STD377sign)/_STD377sign
    
    
            _stoch5 = (Close[-1]-np.amin(Low[:-6:-1]))/(np.amax(High[:-6:-1])-np.amin(Low[:-6:-1]))*100
            _stoch5m1 = (Close[-2]-np.amin(Low[:7:-2]))/(np.amax(High[:-7:-2])-np.amin(Low[:-7:-2]))*100
            _stoch5m2 = (Close[-3]-np.amin(Low[:-8:-3]))/(np.amax(High[:-8:-3])-np.amin(Low[:-8:-3]))*100
            _stoch5m3 = (Close[-4]-np.amin(Low[:-9:-4]))/(np.amax(High[:-9:-4])-np.amin(Low[:-9:-4]))*100
            _stoch5m4 = (Close[-5]-np.amin(Low[:-10:-5]))/(np.amax(High[:-10:-5])-np.amin(Low[:-10:-5]))*100            
            _sign5Stoch5 = (_stoch5 + _stoch5m1 + _stoch5m2 + _stoch5m3 + _stoch5m4)/5
            _diffStochSign5 = (_stoch5-_sign5Stoch5)/_sign5Stoch5###---------  
            
            _stoch8 = (Close[-1]-np.amin(Low[:-9:-1]))/(np.amax(High[:-9:-1])-np.amin(Low[:-9:-1]))*100
            _stoch8m1 = (Close[-2]-np.amin(Low[:10:-2]))/(np.amax(High[:-10:-2])-np.amin(Low[:-10:-2]))*100
            _stoch8m2 = (Close[-3]-np.amin(Low[:-11:-3]))/(np.amax(High[:-11:-3])-np.amin(Low[:-11:-3]))*100
            _stoch8m3 = (Close[-4]-np.amin(Low[:-12:-4]))/(np.amax(High[:-12:-4])-np.amin(Low[:-12:-4]))*100
            _stoch8m4 = (Close[-5]-np.amin(Low[:-13:-5]))/(np.amax(High[:-13:-5])-np.amin(Low[:-13:-5]))*100            
            _sign5Stoch8 = (_stoch8 + _stoch8m1 + _stoch8m2 + _stoch8m3 + _stoch8m4)/5
            _diffStochSign8 = (_stoch8-_sign5Stoch8)/_sign5Stoch8 
    
            _stoch14 = (Close[-1]-np.amin(Low[:-15:-1]))/(np.amax(High[:-15:-1])-np.amin(Low[:-15:-1]))*100
            _stoch14m1 = (Close[-2]-np.amin(Low[:-16:-2]))/(np.amax(High[:-16:-2])-np.amin(Low[:-16:-2]))*100
            _stoch14m2 = (Close[-3]-np.amin(Low[:-17:-3]))/(np.amax(High[:-17:-3])-np.amin(Low[:-17:-3]))*100
            _stoch14m3 = (Close[-4]-np.amin(Low[:-18:-4]))/(np.amax(High[:-18:-4])-np.amin(Low[:-18:-4]))*100
            _stoch14m4 = (Close[-5]-np.amin(Low[:-19:-5]))/(np.amax(High[:-19:-5])-np.amin(Low[:-19:-5]))*100
            _sign5Stoch14 = (_stoch14+_stoch14m1+_stoch14m2+_stoch14m3+_stoch14m4)/5
            _diffStochSign14 = (_stoch14-_sign5Stoch14)/_sign5Stoch14  
    
            _stoch21 = (Close[-1]-np.amin(Low[:-22:-1]))/(np.amax(High[:-22:-1])-np.amin(Low[:-22:-1]))*100
            _stoch21m1 = (Close[-2]-np.amin(Low[:-23:-2]))/(np.amax(High[:-23:-2])-np.amin(Low[:-23:-2]))*100
            _stoch21m2 = (Close[-3]-np.amin(Low[:-24:-3]))/(np.amax(High[:-24:-3])-np.amin(Low[:-24:-3]))*100
            _stoch21m3 = (Close[-4]-np.amin(Low[:-25:-4]))/(np.amax(High[:-25:-4])-np.amin(Low[:-25:-4]))*100
            _stoch21m4 = (Close[-5]-np.amin(Low[:-26:-5]))/(np.amax(High[:-26:-5])-np.amin(Low[:-26:-5]))*100
            _sign5Stoch21 = (_stoch21+_stoch21m1+_stoch21m2+_stoch21m3+_stoch21m4)/5
            _diffStochSign21 = (_stoch21-_sign5Stoch21)/_sign5Stoch21  
    
            _stoch34 = (Close[-1]-np.amin(Low[:-35:-1]))/(np.amax(High[:-35:-1])-np.amin(Low[:-35:-1]))*100
            _stoch34m1 = (Close[-2]-np.amin(Low[:-36:-2]))/(np.amax(High[:-36:-2])-np.amin(Low[:-36:-2]))*100
            _stoch34m2 = (Close[-3]-np.amin(Low[:-37:-3]))/(np.amax(High[:-37:-3])-np.amin(Low[:-37:-3]))*100
            _stoch34m3 = (Close[-4]-np.amin(Low[:-38:-4]))/(np.amax(High[:-38:-4])-np.amin(Low[:-38:-4]))*100
            _stoch34m4 = (Close[-5]-np.amin(Low[:-39:-5]))/(np.amax(High[:-39:-5])-np.amin(Low[:-39:-5]))*100
            _sign5Stoch34 = (_stoch34+_stoch34m1+_stoch34m2+_stoch34m3+_stoch34m4)/5
            _diffStochSign34 = (_stoch34-_sign5Stoch34)/_sign5Stoch34 
    
            _stoch55 = (Close[-1]-np.amin(Low[:-56:-1]))/(np.amax(High[:-56:-1])-np.amin(Low[:-56:-1]))*100
            _stoch55m1 = (Close[-2]-np.amin(Low[:-57:-2]))/(np.amax(High[:-57:-2])-np.amin(Low[:-57:-2]))*100
            _stoch55m2 = (Close[-3]-np.amin(Low[:-58:-3]))/(np.amax(High[:-58:-3])-np.amin(Low[:-58:-3]))*100
            _stoch55m3 = (Close[-4]-np.amin(Low[:-59:-4]))/(np.amax(High[:-59:-4])-np.amin(Low[:-59:-4]))*100
            _stoch55m4 = (Close[-5]-np.amin(Low[:-60:-5]))/(np.amax(High[:-60:-5])-np.amin(Low[:-60:-5]))*100
            _sign5Stoch55 = (_stoch55+_stoch55m1+_stoch55m2+_stoch55m3+_stoch55m4)/5
            _diffStochSign55 = (_stoch55-_sign5Stoch55)/_sign5Stoch55
    
            _stoch89 = (Close[-1]-np.amin(Low[:-90:-1]))/(np.amax(High[:-90:-1])-np.amin(Low[:-90:-1]))*100
            _stoch89m1 = (Close[-2]-np.amin(Low[:-91:-2]))/(np.amax(High[:-91:-2])-np.amin(Low[:-91:-2]))*100
            _stoch89m2 = (Close[-3]-np.amin(Low[:-92:-3]))/(np.amax(High[:-92:-3])-np.amin(Low[:-92:-3]))*100
            _stoch89m3 = (Close[-4]-np.amin(Low[:-93:-4]))/(np.amax(High[:-93:-4])-np.amin(Low[:-93:-4]))*100
            _stoch89m4 = (Close[-5]-np.amin(Low[:-94:-5]))/(np.amax(High[:-94:-5])-np.amin(Low[:-94:-5]))*100
            _sign5Stoch89 = (_stoch89+_stoch89m1+_stoch89m2+_stoch89m3+_stoch89m4)/5
            _diffStochSign89 = (_stoch89-_sign5Stoch89)/_sign5Stoch89  
    
            _stoch100 = (Close[-1]-np.amin(Low[:-101:-1]))/(np.amax(High[:-101:-1])-np.amin(Low[:-101:-1]))*100
            _stoch100m1 = (Close[-2]-np.amin(Low[:-102:-2]))/(np.amax(High[:-102:-2])-np.amin(Low[:-102:-2]))*100
            _stoch100m2 = (Close[-3]-np.amin(Low[:-103:-3]))/(np.amax(High[:-103:-3])-np.amin(Low[:-103:-3]))*100
            _stoch100m3 = (Close[-4]-np.amin(Low[:-104:-4]))/(np.amax(High[:-104:-4])-np.amin(Low[:-104:-4]))*100
            _stoch100m4 = (Close[-5]-np.amin(Low[:-105:-5]))/(np.amax(High[:-105:-5])-np.amin(Low[:-105:-5]))*100
            _sign5Stoch100 = (_stoch100+_stoch100m1+_stoch100m2+_stoch100m3+_stoch100m4)/5
            _diffStochSign100 = (_stoch100-_sign5Stoch100)/_sign5Stoch100   
    
            _stoch144 = (Close[-1]-np.amin(Low[:-145:-1]))/(np.amax(High[:-145:-1])-np.amin(Low[:-145:-1]))*100
            _stoch144m1 = (Close[-2]-np.amin(Low[:-146:-2]))/(np.amax(High[:-146:-2])-np.amin(Low[:-146:-2]))*100
            _stoch144m2 = (Close[-3]-np.amin(Low[:-147:-3]))/(np.amax(High[:-147:-3])-np.amin(Low[:-147:-3]))*100
            _stoch144m3 = (Close[-4]-np.amin(Low[:-148:-4]))/(np.amax(High[:-148:-4])-np.amin(Low[:-148:-4]))*100
            _stoch144m4 = (Close[-5]-np.amin(Low[:-149:-5]))/(np.amax(High[:-149:-5])-np.amin(Low[:-149:-5]))*100
            _sign5Stoch144 = (_stoch144+_stoch144m1+_stoch144m2+_stoch144m3+_stoch144m4)/5
            _diffStochSign144 = (_stoch144-_sign5Stoch144)/_sign5Stoch144  
    
            _stoch200 = (Close[-1]-np.amin(Low[:-200:-1]))/(np.amax(High[:-200:-1])-np.amin(Low[:-200:-1]))*100###---------
            _stoch200m1 = (Close[-2]-np.amin(Low[:-201:-2]))/(np.amax(High[:-201:-2])-np.amin(Low[:-201:-2]))*100###---------
            _stoch200m2 = (Close[-3]-np.amin(Low[:-202:-3]))/(np.amax(High[:-202:-3])-np.amin(Low[:-202:-3]))*100###---------
            _stoch200m3 = (Close[-4]-np.amin(Low[:-203:-4]))/(np.amax(High[:-203:-4])-np.amin(Low[:-203:-4]))*100###---------
            _stoch200m4 = (Close[-5]-np.amin(Low[:-204:-5]))/(np.amax(High[:-204:-5])-np.amin(Low[:-204:-5]))*100###---------
            _sign5Stoch200 = (_stoch200+_stoch200m1+_stoch200m2+_stoch200m3+_stoch200m4)/5###---------
    
            _stoch233 = (Close[-1]-np.amin(Low[:-233:-1]))/(np.amax(High[:-233:-1])-np.amin(Low[:-233:-1]))*100###---------
            _stoch233m1 = (Close[-2]-np.amin(Low[:-234:-2]))/(np.amax(High[:-234:-2])-np.amin(Low[:-234:-2]))*100###---------
            _stoch233m2 = (Close[-3]-np.amin(Low[:-235:-3]))/(np.amax(High[:-235:-3])-np.amin(Low[:-235:-3]))*100###---------
            _stoch233m3 = (Close[-4]-np.amin(Low[:-236:-4]))/(np.amax(High[:-236:-4])-np.amin(Low[:-236:-4]))*100###---------
            _stoch233m4 = (Close[-5]-np.amin(Low[:-237:-5]))/(np.amax(High[:-237:-5])-np.amin(Low[:-237:-5]))*100###---------
            _sign5Stoch233 = (_stoch233+_stoch233m1+_stoch233m2+_stoch233m3+_stoch233m4)/5###---------
            _diffStochSign233 = (_stoch233-_sign5Stoch233)/_sign5Stoch233###---------  
    
            _stoch377 = (Close[-1]-np.amin(Low[:-377:-1]))/(np.amax(High[:-377:-1])-np.amin(Low[:-377:-1]))*100###---------
            _stoch377m1 = (Close[-2]-np.amin(Low[:-378:-2]))/(np.amax(High[:-378:-2])-np.amin(Low[:-378:-2]))*100###---------
            _stoch377m2 = (Close[-3]-np.amin(Low[:-379:-3]))/(np.amax(High[:-379:-3])-np.amin(Low[:-379:-3]))*100###---------
            _stoch377m3 = (Close[-4]-np.amin(Low[:-380:-4]))/(np.amax(High[:-380:-4])-np.amin(Low[:-380:-4]))*100###---------
            _stoch377m4 = (Close[-5]-np.amin(Low[:-381:-5]))/(np.amax(High[:-381:-5])-np.amin(Low[:-381:-5]))*100###---------
            _sign5Stoch377 = (_stoch377+_stoch377m1+_stoch377m2+_stoch377m3+_stoch377m4)/5###---------
            _diffStochSign377 = (_stoch377-_sign5Stoch377)/_sign5Stoch377###---------  
    
            _stoch233 = (Close[-1]-np.amin(Low[:-234:-1]))/(np.amax(High[:-234:-1])-np.amin(Low[:-234:-1]))*100
            _stoch233m1 = (Close[-2]-np.amin(Low[:-235:-2]))/(np.amax(High[:-235:-2])-np.amin(Low[:-235:-2]))*100
            _stoch233m2 = (Close[-3]-np.amin(Low[:-236:-3]))/(np.amax(High[:-236:-3])-np.amin(Low[:-236:-3]))*100
            _stoch233m3 = (Close[-4]-np.amin(Low[:-237:-4]))/(np.amax(High[:-237:-4])-np.amin(Low[:-237:-4]))*100
            _stoch233m4 = (Close[-5]-np.amin(Low[:-238:-5]))/(np.amax(High[:-238:-5])-np.amin(Low[:-238:-5]))*100
            _sign5Stoch233 = (_stoch233+_stoch233m1+_stoch233m2+_stoch233m3+_stoch233m4)/5
            if _stoch233 > 80:
                _stoch233Level = 1.0  
            elif _stoch233 < 20:
                _stoch233Level = -1.0
            else:
                _stoch233Level = 0.0      
    
            _stoch300 = (Close[-1]-np.amin(Low[:-301:-1]))/(np.amax(High[:-301:-1])-np.amin(Low[:-301:-1]))*100
            _stoch300m1 = (Close[-2]-np.amin(Low[:-302:-2]))/(np.amax(High[:-302:-2])-np.amin(Low[:-302:-2]))*100
            _stoch300m2 = (Close[-3]-np.amin(Low[:-303:-3]))/(np.amax(High[:-303:-3])-np.amin(Low[:-303:-3]))*100
            _stoch300m3 = (Close[-4]-np.amin(Low[:-304:-4]))/(np.amax(High[:-304:-4])-np.amin(Low[:-304:-4]))*100
            _stoch300m4 = (Close[-5]-np.amin(Low[:-305:-5]))/(np.amax(High[:-305:-5])-np.amin(Low[:-305:-5]))*100
            _sign5Stoch300 = (_stoch300+_stoch300m1+_stoch300m2+_stoch300m3+_stoch300m4)/5
            if _stoch300 > 80:
                _stoch300Level = 1.0  
            elif _stoch300 < 20:
                _stoch300Level = -1.0
            else:
                _stoch300Level = 0.0  
    
            _stoch377 = (Close[-1]-np.amin(Low[:-377:-1]))/(np.amax(High[:-377:-1])-np.amin(Low[:-377:-1]))*100
            _stoch377m1 = (Close[-2]-np.amin(Low[:-378:-2]))/(np.amax(High[:-378:-2])-np.amin(Low[:-378:-2]))*100
            _stoch377m2 = (Close[-3]-np.amin(Low[:-379:-3]))/(np.amax(High[:-379:-3])-np.amin(Low[:-379:-3]))*100
            _stoch377m3 = (Close[-4]-np.amin(Low[:-380:-4]))/(np.amax(High[:-380:-4])-np.amin(Low[:-380:-4]))*100
            _stoch377m4 = (Close[-5]-np.amin(Low[:-381:-5]))/(np.amax(High[:-381:-5])-np.amin(Low[:-381:-5]))*100
            _sign5Stoch377 = (_stoch377+_stoch377m1+_stoch377m2+_stoch377m3+_stoch377m4)/5
            if _stoch377 > 80:
                _stoch377Level = 1.0  
            elif _stoch377 < 20:
                _stoch377Level = -1.0
            else:
                _stoch377Level = 0.0  
            
    
            _Perc3_H80 = (Close[-1]-np.percentile(High[:-3:-1],80))/np.percentile(High[:-3:-1],80)
            _Perc3_L20 = (Close[-1]-np.percentile(Low[:-3:-1],20))/np.percentile(Low[:-3:-1],20)
            _Perc3_H = (Close[-1]-np.percentile(High[:-3:-1],95))/np.percentile(High[:-3:-1],95)             
            _Perc5_H = (Close[-1]-np.percentile(High[:-5:-1],95))/np.percentile(High[:-5:-1],95)
            _Perc5_H80 = (Close[-1]-np.percentile(High[:-5:-1],80))/np.percentile(High[:-5:-1],80)
            _Perc5_M50 = (Close[-1]-np.percentile(High[:-5:-1],50))/np.percentile(High[:-5:-1],50)
            _Perc5_L20 = (Close[-1]-np.percentile(Low[:-5:-1],20))/np.percentile(Low[:-5:-1],20)
            _Perc8_L20 = (Close[-1]-np.percentile(Low[:-9:-1],20))/np.percentile(Low[:-9:-1],20)
            _Perc8_M50 = (Close[-1]-np.percentile(High[:-8:-1],50))/np.percentile(High[:-8:-1],50)
            _Perc8_H80 = (Close[-1]-np.percentile(High[:-8:-1],80))/np.percentile(High[:-8:-1],80)
            _Perc13_M50 = (Close[-1]-np.percentile(High[:-13:-1],50))/np.percentile(High[:-13:-1],50)
            _Perc13_H80 = (Close[-1]-np.percentile(High[:-13:-1],80))/np.percentile(High[:-13:-1],80)
            _Perc13_L20 = (Close[-1]-np.percentile(Low[:-13:-1],20))/np.percentile(Low[:-13:-1],20)
            _Perc21_L20 = (Close[-1]-np.percentile(Low[:-21:-1],20))/np.percentile(Low[:-21:-1],20)
            _Perc21_H80 = (Close[-1]-np.percentile(High[:-21:-1],80))/np.percentile(High[:-21:-1],80)
            _Perc21_H = (Close[-1]-np.percentile(High[:-21:-1],95))/np.percentile(High[:-21:-1],95)            
            _Perc21_L = (Close[-1]-np.percentile(Low[:-21:-1],5))/np.percentile(Low[:-21:-1],5)
            _Perc55_L = (Close[-1]-np.percentile(Low[:-55:-1],5))/np.percentile(Low[:-55:-1],5)
            _Perc55_M50 = (Close[-1]-np.percentile(High[:-55:-1],50))/np.percentile(High[:-55:-1],50)  
            _Perc55_H = (Close[-1]-np.percentile(High[:-55:-1],95))/np.percentile(High[:-55:-1],95)
            _Perc55_H80 = (Close[-1]-np.percentile(High[:-55:-1],80))/np.percentile(High[:-55:-1],80)
            _Perc89_H = (Close[-1]-np.percentile(High[:-90:-1],95))/np.percentile(High[:-90:-1],95)
            _Perc89_H80 = (Close[-1]-np.percentile(High[:-90:-1],80))/np.percentile(High[:-90:-1],80)
            _Perc100_H80 = (Close[-1]-np.percentile(High[:-101:-1],80))/np.percentile(High[:-101:-1],80)
            _Perc100_M50 = (Close[-1]-np.percentile(High[:-101:-1],50))/np.percentile(High[:-101:-1],50)            
            _Perc144_L = (Close[-1]-np.percentile(Low[:-145:-1],5))/np.percentile(Low[:-145:-1],5)
            _Perc144_L20 = (Close[-1]-np.percentile(Low[:-145:-1],20))/np.percentile(Low[:-145:-1],20)   
            _Perc144_M50 = (Close[-1]-np.percentile(High[:-145:-1],50))/np.percentile(High[:-145:-1],50)  
            _Perc200_L20 = (Close[-1]-np.percentile(Low[:-200:-1],20))/np.percentile(Low[:-200:-1],20)   
            _Perc200_H = (Close[-1]-np.percentile(High[:-200:-1],95))/np.percentile(High[:-200:-1],95)
            _Perc233_H = (Close[-1]-np.percentile(High[:-233:-1],95))/np.percentile(High[:-233:-1],95)
            _Perc233_H80 = (Close[-1]-np.percentile(High[:-233:-1],80))/np.percentile(High[:-233:-1],80)
            _Perc377_L = (Close[-1]-np.percentile(Low[:-377:-1],5))/np.percentile(Low[:-377:-1],5)            
            _Perc377_L20 = (Close[-1]-np.percentile(Low[:-377:-1],20))/np.percentile(Low[:-377:-1],20)
            _Perc377_H80 = (Close[-1]-np.percentile(High[:-377:-1],80))/np.percentile(High[:-377:-1],80)  
    
            _EvNo10 = (Close[-1]-10)/10
            _EvNo20 = (Close[-1]-20)/20            
            _EvNo30 = (Close[-1]-30)/30            
            _EvNo50 = (Close[-1]-50)/50
            _EvNo70 = (Close[-1]-70)/70
            _EvNo80 = (Close[-1]-80)/80            
            _EvNo100 = (Close[-1]-100)/100
            _EvNo200 = (Close[-1]-200)/200             
            _EvNo300 = (Close[-1]-300)/300
            _EvNo500 = (Close[-1]-500)/500            
            _EvNo800 = (Close[-1]-800)/800
            _EvNo900 = (Close[-1]-900)/900
            _EvNo1000 = (Close[-1]-1000)/1000  
            _EvNo2000 = (Close[-1]-2000)/2000            
            _EvNo3000 = (Close[-1]-3000)/3000
            _EvNo5000 = (Close[-1]-5000)/5000
            _EvNo10000 = (Close[-1]-10000)/10000
            
            _SMA3_C = (Close[-1]-(np.sum(Close[:-4:-1])/3))/(np.sum(Close[:-4:-1])/3)
            _SMA5_C = (Close[-1]-(np.sum(Close[:-6:-1])/5))/(np.sum(Close[:-6:-1])/5)
            _SMA8_C = (Close[-1]-(np.sum(Close[:-9:-1])/8))/(np.sum(Close[:-9:-1])/8)
            _SMA13_C = (Close[-1]-(np.sum(Close[:-14:-1])/13))/(np.sum(Close[:-14:-1])/13)      
            _SMA21_C = (Close[-1]-(np.sum(Close[:-22:-1])/21))/(np.sum(Close[:-22:-1])/21)                
            _SMA34_C = (Close[-1]-(np.sum(Close[:-35:-1])/34))/(np.sum(Close[:-35:-1])/34)  
            _SMA55_C = (Close[-1]-(np.sum(Close[:-56:-1])/55))/(np.sum(Close[:-56:-1])/55)  
            _SMA89_C = (Close[-1]-(np.sum(Close[:-90:-1])/89))/(np.sum(Close[:-90:-1])/89)
            _SMA144_C = (Close[-1]-(np.sum(Close[:-145:-1])/144))/(np.sum(Close[:-145:-1])/144)
            _SMA200_C = (Close[-1]-(np.sum(Close[:-201:-1])/200))/(np.sum(Close[:-201:-1])/200)
            _SMA233_C = (Close[-1]-(np.sum(Close[:-234:-1])/233))/(np.sum(Close[:-234:-1])/233)
            _SMA300_C = (Close[-1]-(np.sum(Close[:-301:-1])/300))/(np.sum(Close[:-301:-1])/300)
            _SMA377_C = (Close[-1]-(np.sum(Close[:-378:-1])/377))/(np.sum(Close[:-378:-1])/377)
    
            _SMA3vs5 = (_SMA3_C-_SMA5_C)/_SMA5_C
            _SMA3vs8 = (_SMA3_C-_SMA8_C)/_SMA8_C              
            _SMA3vs13 = (_SMA3_C-_SMA13_C)/_SMA13_C            
            _SMA3vs34 = (_SMA3_C-_SMA34_C)/_SMA34_C
            _SMA5vs8 = (_SMA5_C-_SMA8_C)/_SMA8_C            
            _SMA5vs55 = (_SMA5_C-_SMA55_C)/_SMA55_C
            _SMA8vs13 = (_SMA8_C-_SMA13_C)/_SMA13_C
            _SMA8vs34 = (_SMA8_C-_SMA34_C)/_SMA34_C
            _SMA8vs89 = (_SMA8_C-_SMA89_C)/_SMA89_C
            _SMA13vs55 = (_SMA13_C-_SMA55_C)/_SMA55_C
            _SMA21vs34 = (_SMA21_C-_SMA34_C)/_SMA34_C
            _SMA21vs55 = (_SMA21_C-_SMA55_C)/_SMA55_C
            _SMA21vs89 = (_SMA21_C-_SMA89_C)/_SMA89_C
            _SMA34vs89 = (_SMA34_C-_SMA89_C)/_SMA89_C
            _SMA34vs233 = (_SMA34_C-_SMA233_C)/_SMA233_C
            _SMA55vs233 = (_SMA55_C-_SMA233_C)/_SMA233_C
            _SMA89vs144 = (_SMA89_C-_SMA144_C)/_SMA144_C              
            _SMA89vs377 = (_SMA89_C-_SMA377_C)/_SMA377_C            
            _SMA144vs233 = (_SMA144_C-_SMA233_C)/_SMA233_C
            _SMA233vs377 = (_SMA233_C-_SMA377_C)/_SMA377_C               
    
            _Diff_CtoO = (Close[-1]-Open[-1])/Open[-1]           
            _Diff_CtoO1 = (Close[-1]-Open[-2])/Open[-2]
            _Diff_CtoO4 = (Close[-1]-Open[-5])/Open[-5]
            _Diff_CtoO5 = (Close[-1]-Open[-6])/Open[-6]
            _Diff_CtoO6 = (Close[-1]-Open[-7])/Open[-7] 
            _Diff_CtoO8 = (Close[-1]-Open[-9])/Open[-9]              
            _Diff_CtoO9 = (Close[-1]-Open[-10])/Open[-10]
            _Diff_CtoH25 = (Close[-1]-High[-26])/High[-26]
    
            _Diff_CtoC1 = (Close[-1]-Close[-2])/Close[-2]
            _Diff_CtoC2 = (Close[-1]-Close[-3])/Close[-3]
            _Diff_CtoC3 = (Close[-1]-Close[-4])/Close[-4]
            _Diff_CtoC5 = (Close[-1]-Close[-6])/Close[-6]
            _Diff_CtoC7 = (Close[-1]-Close[-8])/Close[-8]            
            _Diff_CtoC8 = (Close[-1]-Close[-9])/Close[-9]           
            
            _Diff_CtoH = (Close[-1]-High[-1])/High[-1]
            _Diff_CtoH1 = (Close[-1]-High[-2])/High[-2]
            _Diff_CtoH2 = (Close[-1]-High[-3])/High[-3]    
            _Diff_CtoH4 = (Close[-1]-High[-5])/High[-5]           
            _Diff_CtoH5 = (Close[-1]-High[-6])/High[-6]
            _Diff_CtoH6 = (Close[-1]-High[-7])/High[-7]
            _Diff_CtoH8 = (Close[-1]-High[-9])/High[-9]
            _Diff_CtoH13 = (Close[-1]-High[-14])/High[-14]
            _Diff_CtoH14 = (Close[-1]-High[-15])/High[-15]
            _Diff_CtoH17 = (Close[-1]-High[-18])/High[-18] 
            _Diff_CtoH19 = (Close[-1]-High[-20])/High[-20]            
            _Diff_CtoH20 = (Close[-1]-High[-21])/High[-21]
            _Diff_CtoH21 = (Close[-1]-High[-22])/High[-22]
            _Diff_CtoH22 = (Close[-1]-High[-23])/High[-23]
            _Diff_CtoH23 = (Close[-1]-High[-24])/High[-24]           
    
    
            _Diff_CtoL = (Close[-1]-Low[-1])/Low[-1]
            _Diff_CtoL1 = (Close[-1]-Low[-2])/Low[-2]
            _Diff_CtoL3 = (Close[-1]-Low[-4])/Low[-4]
            _Diff_CtoL4 = (Close[-1]-Low[-5])/Low[-5]
            _Diff_CtoL5 = (Close[-1]-Low[-6])/Low[-6]            
            _Diff_CtoL9 = (Close[-1]-Low[-8])/Low[-8] 
            _Diff_CtoL10 = (Close[-1]-Low[-11])/Low[-11]   
            _Diff_CtoL11 = (Close[-1]-Low[-12])/Low[-12]            
            _Diff_CtoL12 = (Close[-1]-Low[-13])/Low[-13]
            _Diff_CtoL13 = (Close[-1]-Low[-14])/Low[-14]
            _Diff_CtoL19 = (Close[-1]-Low[-20])/Low[-20]            
            _Diff_CtoL20 = (Close[-1]-Low[-21])/Low[-21]
            _Diff_CtoL21 = (Close[-1]-Low[-22])/Low[-22]
            _Diff_CtoL22 = (Close[-1]-Low[-23])/Low[-23]
            _Diff_CtoL23 = (Close[-1]-Low[-24])/Low[-24]
            _Diff_CtoL25 = (Close[-1]-Low[-26])/Low[-26]
    
    
            _SMA_H3 = float(np.sum(High[:-4:-1])/3) # short moving average based on H & L
            _SMA_L3 = float(np.sum(Low[:-4:-1])/3)  # this two are sub-indicators
    
            _BBD3 = np.sum(Close[:-4:-1])/3-np.std(Close[:-4:-1])*2
            _DiffD3_C = (Close[-1]-_BBD3)/_BBD3    
            _DiffD3_H3 = (_SMA_H3-_BBD3)/_BBD3
    
            _BBD5 = np.sum(Close[:-6:-1])/5-(np.std(Close[-6:-1])*2) # Lower BollingerBand
            _DiffD5_C = (Close[-1]-_BBD5)/_BBD5            
            _DiffD5_H3 = (_SMA_H3-_BBD5)/_BBD5
    
            _BBD8 = np.sum(Close[:-9:-1])/8-(np.std(Close[-9:-1])*2) # Lower BollingerBand
            _DiffD8_H3 = (_SMA_H3-_BBD8)/_BBD8
            
            _BBD13 = np.sum(Close[:-14:-1])/13-(np.std(Close[:14:-1])*2)
            _DiffD13_C = (Close[-1]-_BBD13)/_BBD13
            _DiffD13_H3 = (_SMA_H3-_BBD13)/_BBD13 
    
            _BBD21 = np.sum(Close[:-22:-1])/21-(np.std(Close[-22:-1])*2) # Lower BollingerBand
            _DiffD21_H3 = (_SMA_H3-_BBD21)/_BBD21    
    
            _BBD34 = np.sum(Close[:-35:-1])/34-(np.std(Close[:-35:-1])*2)   
            _DiffD34_C = (Close[-1]-_BBD34)/_BBD34  
            _DiffD34_H3 = (_SMA_H3-_BBD34)/_BBD34
       
            
            _BBD55 = np.sum(Close[:-56:-1])/55-(np.std(Close[:-56:-1])*2)   
            _DiffD55_C = (Close[-1]-_BBD55)/_BBD55  
            _DiffD55_H3 = (_SMA_H3-_BBD55)/_BBD55
    
            _BBD89 = np.sum(Close[:-90:-1])/55-(np.std(Close[:-90:-1])*2)   
            _DiffD89_C = (Close[-1]-_BBD89)/_BBD89  
            _DiffD55_H3 = (_SMA_H3-_BBD89)/_BBD89            
    
            _BBD100 = np.sum(Close[:-101:-1])/100-(np.std(Close[:-101:-1])*2)
            _DiffD100_C = (Close[-1]-_BBD100)/_BBD100  
            _DiffD100_H3 = (_SMA_H3-_BBD100)/_BBD100
            
            _BBD144 = np.sum(Close[:-145:-1])/144-(np.std(Close[:-145:-1])*2)
            _DiffD144_C = (Close[-1]-_BBD144)/_BBD144            
    
            _BBD233 = np.sum(Close[:-234:-1])/233-(np.std(Close[:-234:-1])*2)
            _DiffD233_C = (Close[-1]-_BBD233)/_BBD233         
            _DiffD233_H3 = (_SMA_H3-_BBD233)/_BBD233
    
            _BBD300 = np.sum(Close[:-301:-1])/300-(np.std(Close[-301:-1])*2) # Lower BollingerBand
            _DiffD300_C = (Close[-1]-_BBD300)/_BBD300  
            _DiffD300_H3 = (_SMA_H3-_BBD300)/_BBD300
    
    
            _BBD377 = np.sum(Close[:-378:-1])/377-(np.std(Close[-378:-1])*2) # Lower BollingerBand
            _DiffD377_H3 = (_SMA_H3-_BBD377)/_BBD377
            _DiffD377_C = (Close[-1]-_BBD377)/_BBD377            
            
            _BBU8 = np.sum(Close[:-9:-1])/8+(np.std(Close[:-9:-1])*2)
            _DiffU8_C = np.round((Close[-1]-_BBU8)/_BBU8,3)      
    
            _BBU13 = np.sum(Close[:-14:-1])/13+(np.std(Close[:-14:-1])*2)
            _DiffU13_L3 = np.round((_SMA_L3-_BBU13)/_BBU13,3)
    
            _BBU21 = np.sum(Close[:-22:-1])/21+(np.std(Close[:-22:-1])*2)
            _DiffU21_L3 = (_SMA_L3-_BBU21)/_BBU21
            _DiffU21_C = (Close[-1]-_BBU21)/_BBU21
    
            _BBU34 = np.sum(Close[:-35:-1])/34+(np.std(Close[:-35:-1])*2)
            _DiffU34_C = (Close[-1]-_BBU34)/_BBU34
            _DiffU34_L3 = (_SMA_L3-_BBU34)/_BBU34     
            
            _BBU55 = np.sum(Close[:-56:-1])/55+(np.std(Close[:-56:-1])*2)
            _DiffU55_C = (Close[-1]-_BBU55)/_BBU55
            _DiffU55_L3 = (_SMA_L3-_BBU55)/_BBU55    
    
            _BBU89 = np.sum(Close[:-90:-1])/89+(np.std(Close[:-90:-1])*2)
            _DiffU89_C = (Close[-1]-_BBU89)/_BBU89
    
            _BBU100 = np.sum(Close[:-101:-1])/100+(np.std(Close[:-101:-1])*2)
            _DiffU100_C = (Close[-1]-_BBU100)/_BBU100
    
            _BBU144 = np.sum(Close[:-145:-1])/144+(np.std(Close[:-145:-1])*2)
            _DiffU144_C = (Close[-1]-_BBU144)/_BBU144
            _DiffU144_L3 = (_SMA_L3-_BBU144)/_BBU144
    
            _BBU200 = np.sum(Close[:-201:-1])/200+(np.std(Close[:-201:-1])*2)
            _DiffU200_L3 = (_SMA_L3-_BBU200)/_BBU200
    
            _BBU233 = np.sum(Close[:234:-1])/233+(np.std(Close[:234:-1])*2)
            _DiffU233_L3 = (_SMA_L3-_BBU233)/_BBU233
            _DiffU233_C = (Close[-1]-_BBU233)/_BBU233
            
            _BBU300 = np.sum(Close[:301:-1])/300+(np.std(Close[:301:-1])*2)
            _DiffU300_L3 = (_SMA_L3-_BBU300)/_BBU300
            _DiffU300_C = (Close[-1]-_BBU300)/_BBU300
            
            _BBU377 = np.sum(Close[:377:-1])/377+(np.std(Close[:377:-1])*2)
            _DiffU377_L3 = (_SMA_L3-_BBU377)/_BBU377
            _DiffU377_C = (Close[-1]-_BBU377)/_BBU377
     
    
            _High3_H = (Close[-1]-np.amax(High[:-4:-1]))/np.amax(High[:-4:-1])
            _High5_H = (Close[-1]-np.amax(High[:-6:-1]))/np.amax(High[:-6:-1])
            _High7_H = (Close[-1]-np.amax(High[:-8:-1]))/np.amax(High[:-8:-1])               
            _High11_H = (Close[-1]-np.amax(High[:-12:-1]))/np.amax(High[:-12:-1])
            _High14_H = (Close[-1]-np.amax(High[:-15:-1]))/np.amax(High[:-15:-1])            
            _High13_H = (Close[-1]-np.amax(High[:-14:-1]))/np.amax(High[:-14:-1])            
            _High23_H = (Close[-1]-np.amax(High[:-24:-1]))/np.amax(High[:-24:-1])
            _High55_H = (Close[-1]-np.amax(High[:-56:-1]))/np.amax(High[:-56:-1])                 
            _High233_H = (Close[-1]-np.amax(High[:-234:-1]))/np.amax(High[:-234:-1])   
    
            _Low6_L = (Close[-1]-np.amin(Low[:-7:-1]))/np.amin(Low[:-7:-1])
            _Low7_L = (Close[-1]-np.amin(Low[:-8:-1]))/np.amin(Low[:-8:-1])
            _Low8_L = (Close[-1]-np.amin(Low[:-9:-1]))/np.amin(Low[:-9:-1])            
            _Low10_L = (Close[-1]-np.amin(Low[:-11:-1]))/np.amin(Low[:-11:-1])
            _Low12_L = (Close[-1]-np.amin(Low[:-13:-1]))/np.amin(Low[:-13:-1])
            _Low14_L = (Close[-1]-np.amin(Low[:-15:-1]))/np.amin(Low[:-15:-1])
            _Low15_L = (Close[-1]-np.amin(Low[:-16:-1]))/np.amin(Low[:-16:-1])  
            _Low19_L = (Close[-1]-np.amin(Low[:-20:-1]))/np.amin(Low[:-20:-1])  
            _Low23_L = (Close[-1]-np.amin(Low[:-24:-1]))/np.amin(Low[:-24:-1])            
            _Low25_L = (Close[-1]-np.amin(Low[:-26:-1]))/np.amin(Low[:-26:-1])
            _Low34_L = (Close[-1]-np.amin(Low[:-35:-1]))/np.amin(Low[:-35:-1])
            _Low55_L = (Close[-1]-np.amin(Low[:-56:-1]))/np.amin(Low[:-56:-1])
            _Low89_L = (Close[-1]-np.amin(Low[:-99:-1]))/np.amin(Low[:-99:-1])
            _Low144_L = (Close[-1]-np.amin(Low[:-145:-1]))/np.amin(Low[:-145:-1])            
            _Low233_L = (Close[-1]-np.amin(Low[:-234:-1]))/np.amin(Low[:-234:-1])
    
            df = pd.DataFrame(columns = FEATURES_IQ19)
            df = df.append({
                            '_BBD55':_BBD55,
                            '_BBU144':_BBU144,
                            '_BBU300':_BBU300,
                            '_BBU55':_BBU55,
                            '_dateDayOfMonth':_dateDayOfMonth,
                            '_dateDayOfYear':_dateDayOfYear,
                            '_dateMonthOfYear':_dateMonthOfYear,
                            '_dateWeekOfYear':_dateWeekOfYear,
                            '_Diff_CtoH19':_Diff_CtoH19,
                            '_Diff_CtoH5':_Diff_CtoH5,
                            '_Diff_CtoL19':_Diff_CtoL19,
                            '_Diff_CtoL20':_Diff_CtoL20,
                            '_Diff_CtoL9':_Diff_CtoL9,
                            '_DiffD100_H3':_DiffD100_H3,
                            '_diffStochSign100':_diffStochSign100,
                            '_diffStochSign34':_diffStochSign34,
                            '_DiffU8_C':_DiffU8_C,
                            '_EvNo20':_EvNo20,
                            '_Low55_L':_Low55_L,
                            '_Low8_L':_Low8_L,
                            '_Low89_L':_Low89_L,
                            '_PastSCH13to34':_PastSCH13to34,
                            '_PastSCH21to34':_PastSCH21to34,
                            '_Perc200_L20':_Perc200_L20,
                            '_Perc21_H':_Perc21_H,
                            '_Perc233_H80':_Perc233_H80,
                            '_Perc377_L':_Perc377_L,
                            '_Perc8_H80':_Perc8_H80,
                            '_SMA233vs377':_SMA233vs377,
                            '_SMA34vs89':_SMA34vs89,
                            '_SMA8_C':_SMA8_C,
                            '_SMA89vs144':_SMA89vs144,
                            '_STD13sign':_STD13sign,
                            '_STD144sign':_STD144sign,
                            '_STD233_C':_STD233_C,
                            '_STD300_C':_STD300_C,
                            '_STD300sign':_STD300sign,
                            '_STD34_C':_STD34_C,
                            '_STD377_C':_STD377_C,
                            '_stoch377Level':_stoch377Level,
                            'Diff_RL100_RL377':Diff_RL100_RL377,
                            'Diff_RL144_RL200':Diff_RL144_RL200,
                            'Diff_RL144_RL377':Diff_RL144_RL377,
                            'Diff_RL200_RL377':Diff_RL200_RL377,
                            'Diff_RL21_RL34':Diff_RL21_RL34,
                            'Diff_RL233_RL377':Diff_RL233_RL377,
                            'Diff_RL5_RL21':Diff_RL5_RL21,
                            'Diff_RL55_RL89':Diff_RL55_RL89,
                            'Diff_RL8_RL55':Diff_RL8_RL55,
                            'RL200':RL200
                            }, ignore_index = True)

            FileLocation4excel = importantPath+'\\for'+eachTicker+'_excel.xlsx'
            print("Priming {0}".format(FileLocation4excel))
            df.to_excel(FileLocation4excel, index=False)
            #print(df)
    except Exception as e:
        print("Exception before saving excel: " + str(e))
        pass

    c.timer.print_elapsed("\nFinished computing features and priming files")
###################################################################3    


    Ultimate_df2 = pd.DataFrame(columns = ['Name', 'Forecast'])

    from sklearn.externals import joblib
 
    print("Loading pickled files...")

    logreg_01 = joblib.load(r''+importantPath+pklFiles+'01.pkl')
    logreg_02 = joblib.load(r''+importantPath+pklFiles+'02.pkl')
    logreg_03 = joblib.load(r''+importantPath+pklFiles+'03.pkl')
    logreg_04 = joblib.load(r''+importantPath+pklFiles+'04.pkl')
    logreg_05 = joblib.load(r''+importantPath+pklFiles+'05.pkl')
    logreg_06 = joblib.load(r''+importantPath+pklFiles+'06.pkl')
    logreg_07 = joblib.load(r''+importantPath+pklFiles+'07.pkl')
    logreg_08 = joblib.load(r''+importantPath+pklFiles+'08.pkl')
    logreg_09 = joblib.load(r''+importantPath+pklFiles+'09.pkl')
    logreg_10 = joblib.load(r''+importantPath+pklFiles+'10.pkl')
    logreg_11 = joblib.load(r''+importantPath+pklFiles+'11.pkl')
    logreg_12 = joblib.load(r''+importantPath+pklFiles+'12.pkl')
    logreg_13 = joblib.load(r''+importantPath+pklFiles+'13.pkl')
    logreg_14 = joblib.load(r''+importantPath+pklFiles+'14.pkl')
    logreg_15 = joblib.load(r''+importantPath+pklFiles+'15.pkl')
    logreg_16 = joblib.load(r''+importantPath+pklFiles+'16.pkl')    
    logreg_17 = joblib.load(r''+importantPath+pklFiles+'17.pkl')
    logreg_18 = joblib.load(r''+importantPath+pklFiles+'18.pkl')       
    logreg_19 = joblib.load(r''+importantPath+pklFiles+'19.pkl') 
    logreg_20 = joblib.load(r''+importantPath+pklFiles+'20.pkl')   
    logreg_21 = joblib.load(r''+importantPath+pklFiles+'21.pkl')   
    logreg_22 = joblib.load(r''+importantPath+pklFiles+'22.pkl')   
    logreg_23 = joblib.load(r''+importantPath+pklFiles+'23.pkl')
    logreg_24 = joblib.load(r''+importantPath+pklFiles+'24.pkl')       
    logreg_25 = joblib.load(r''+importantPath+pklFiles+'25.pkl')   
    logreg_26 = joblib.load(r''+importantPath+pklFiles+'26.pkl')   
    logreg_27 = joblib.load(r''+importantPath+pklFiles+'27.pkl')       
    logreg_28 = joblib.load(r''+importantPath+pklFiles+'28.pkl')  
    logreg_29 = joblib.load(r''+importantPath+pklFiles+'29.pkl')   
    logreg_30 = joblib.load(r''+importantPath+pklFiles+'30.pkl')    



    for eachTicker, eachRealNames in zip(yahoo_ticker_list, yahoo_RealNames_list):
        print("\n== Starting calculations for {0} ===".format(eachTicker))

        try:
            Location = importantPath+'\\for'+eachTicker+'_excel.xlsx'
            print("Reading {0}".format(Location))
            data = pd.read_excel(Location)

            feat01 = np.array(data[FEATURES01].values) # making a Numpay array from the Pandas dataset
            feat02 = np.array(data[FEATURES02].values) # making a Numpay array from the Pandas dataset
            feat03 = np.array(data[FEATURES03].values) # making a Numpay array from the Pandas dataset
            feat04 = np.array(data[FEATURES04].values) # making a Numpay array from the Pandas dataset
            feat05 = np.array(data[FEATURES05].values) # making a Numpay array from the Pandas dataset
            feat06 = np.array(data[FEATURES06].values) # making a Numpay array from the Pandas dataset
            feat07 = np.array(data[FEATURES07].values) # making a Numpay array from the Pandas dataset
            feat08 = np.array(data[FEATURES08].values) # making a Numpay array from the Pandas dataset
            feat09 = np.array(data[FEATURES09].values) # making a Numpay array from the Pandas dataset
            feat10 = np.array(data[FEATURES10].values) # making a Numpay array from the Pandas dataset
            feat11 = np.array(data[FEATURES11].values) # making a Numpay array from the Pandas dataset
            feat12 = np.array(data[FEATURES12].values) # making a Numpay array from the Pandas dataset
            feat13 = np.array(data[FEATURES13].values) # making a Numpay array from the Pandas dataset
            feat14 = np.array(data[FEATURES14].values) # making a Numpay array from the Pandas dataset
            feat15 = np.array(data[FEATURES15].values) # making a Numpay array from the Pandas dataset
            feat16 = np.array(data[FEATURES16].values) # making a Numpay array from the Pandas dataset            
            feat17 = np.array(data[FEATURES17].values)
            feat18 = np.array(data[FEATURES18].values)
            feat19 = np.array(data[FEATURES19].values)
            feat20 = np.array(data[FEATURES20].values)
            feat21 = np.array(data[FEATURES21].values)
            feat22 = np.array(data[FEATURES22].values)
            feat23 = np.array(data[FEATURES23].values)
            feat24 = np.array(data[FEATURES24].values)
            feat25 = np.array(data[FEATURES25].values)
            feat26 = np.array(data[FEATURES26].values)
            feat27 = np.array(data[FEATURES27].values)
            feat28 = np.array(data[FEATURES28].values)
            feat29 = np.array(data[FEATURES29].values)
            feat30 = np.array(data[FEATURES30].values)
            
            print("Finished reading {0} and converting to arrays".format(Location))
            
        except Exception as e:
            print("Error reading xlsx: " + str(e))    

##########################################################################
        try:
            print("Predicting probabilities for features...")
            

            feats = [
                feat01, feat02, feat03, feat04, feat05, feat06, feat07, feat08, feat09, feat10, 
                feat11, feat12, feat13, feat14, feat15, feat16, feat17, feat18, feat19, feat20,
                feat21, feat22, feat23, feat24, feat25, feat26, feat27, feat28, feat29, feat30
            ]

            for currentFeat in feats:
                for index, feat in enumerate(currentFeat[0]):
                    if type(feat) is str:
                        # Fix for (probably inconsistencies of pickled data of older version, should probably be removed)
                        print("HACK: Converting: '{0}' due to old pickle format, assuming array syntax => single float".format(feat))
                        currentFeat[0, index] = float(feat[1:-1]) # float convert literal array syntax, possibly incorrect
                        #print("Converted {0}".format(currentFeat[0, index]))
                    #print(feat)
                    #print(index)
                    #print(type(feat))

            Value_01 = logreg_01.predict_proba(feat01)

            _01N5 = round(Value_01[0][0],6)
            _01N4 = round(Value_01[0][1],6)
            _01N3 = round(Value_01[0][2],6)
            _01N2 = round(Value_01[0][3],6)
            _01N1 = round(Value_01[0][4],6)            
            _01P1 = round(Value_01[0][6],6)
            _01P2 = round(Value_01[0][7],6)
            _01P3 = round(Value_01[0][8],6) 
            _01P4 = round(Value_01[0][9],6) 
            _01P5 = round(Value_01[0][10],6)
            
            Value_02 = logreg_02.predict_proba(feat02)
            _02N5 = round(Value_02[0][0],6)
            _02N4 = round(Value_02[0][1],6)
            _02N3 = round(Value_02[0][2],6)
            _02N2 = round(Value_02[0][3],6)
            _02N1 = round(Value_02[0][4],6)            
            _02P1 = round(Value_02[0][6],6)
            _02P2 = round(Value_02[0][7],6)
            _02P3 = round(Value_02[0][8],6) 
            _02P4 = round(Value_02[0][9],6) 
            _02P5 = round(Value_02[0][10],6)
    
            Value_03 = logreg_03.predict_proba(feat03)
            _03N5 = round(Value_03[0][0],6)
            _03N4 = round(Value_03[0][1],6)
            _03N3 = round(Value_03[0][2],6)
            _03N2 = round(Value_03[0][3],6)
            _03N1 = round(Value_03[0][4],6)            
            _03P1 = round(Value_03[0][6],6)
            _03P2 = round(Value_03[0][7],6)
            _03P3 = round(Value_03[0][8],6) 
            _03P4 = round(Value_03[0][9],6) 
            _03P5 = round(Value_03[0][10],6)
            
            Value_04 = logreg_04.predict_proba(feat04)
            _04N5 = round(Value_04[0][0],6)
            _04N4 = round(Value_04[0][1],6)
            _04N3 = round(Value_04[0][2],6)
            _04N2 = round(Value_04[0][3],6)
            _04N1 = round(Value_04[0][4],6)            
            _04P1 = round(Value_04[0][6],6)
            _04P2 = round(Value_04[0][7],6)
            _04P3 = round(Value_04[0][8],6) 
            _04P4 = round(Value_04[0][9],6) 
            _04P5 = round(Value_04[0][10],6)            
    
            Value_05 = logreg_05.predict_proba(feat05)
            _05N5 = round(Value_05[0][0],6)
            _05N4 = round(Value_05[0][1],6)
            _05N3 = round(Value_05[0][2],6)
            _05N2 = round(Value_05[0][3],6)
            _05N1 = round(Value_05[0][4],6)            
            _05P1 = round(Value_05[0][6],6)
            _05P2 = round(Value_05[0][7],6)
            _05P3 = round(Value_05[0][8],6) 
            _05P4 = round(Value_05[0][9],6) 
            _05P5 = round(Value_05[0][10],6)
            
            Value_06 = logreg_06.predict_proba(feat06)
            _06N5 = round(Value_06[0][0],6)
            _06N4 = round(Value_06[0][1],6)
            _06N3 = round(Value_06[0][2],6)
            _06N2 = round(Value_06[0][3],6)
            _06N1 = round(Value_06[0][4],6)            
            _06P1 = round(Value_06[0][6],6)
            _06P2 = round(Value_06[0][7],6)
            _06P3 = round(Value_06[0][8],6) 
            _06P4 = round(Value_06[0][9],6) 
            _06P5 = round(Value_06[0][10],6)
            
            Value_07 = logreg_07.predict_proba(feat07)
            _07N5 = round(Value_07[0][0],6)
            _07N4 = round(Value_07[0][1],6)
            _07N3 = round(Value_07[0][2],6)
            _07N2 = round(Value_07[0][3],6)
            _07N1 = round(Value_07[0][4],6)            
            _07P1 = round(Value_07[0][6],6)
            _07P2 = round(Value_07[0][7],6)
            _07P3 = round(Value_07[0][8],6) 
            _07P4 = round(Value_07[0][9],6) 
            _07P5 = round(Value_07[0][10],6)   
    
            Value_08 = logreg_08.predict_proba(feat08)
            _08N5 = round(Value_08[0][0],6)
            _08N4 = round(Value_08[0][1],6)
            _08N3 = round(Value_08[0][2],6)
            _08N2 = round(Value_08[0][3],6)
            _08N1 = round(Value_08[0][4],6)            
            _08P1 = round(Value_08[0][6],6)
            _08P2 = round(Value_08[0][7],6)
            _08P3 = round(Value_08[0][8],6) 
            _08P4 = round(Value_08[0][9],6) 
            _08P5 = round(Value_08[0][10],6)  
    
            Value_09 = logreg_09.predict_proba(feat09)
            _09N5 = round(Value_09[0][0],6)
            _09N4 = round(Value_09[0][1],6)
            _09N3 = round(Value_09[0][2],6)
            _09N2 = round(Value_09[0][3],6)
            _09N1 = round(Value_09[0][4],6)            
            _09P1 = round(Value_09[0][6],6)
            _09P2 = round(Value_09[0][7],6)
            _09P3 = round(Value_09[0][8],6) 
            _09P4 = round(Value_09[0][9],6) 
            _09P5 = round(Value_09[0][10],6)
            
            Value_10 = logreg_10.predict_proba(feat10)
            _10N5 = round(Value_10[0][0],6)
            _10N4 = round(Value_10[0][1],6)
            _10N3 = round(Value_10[0][2],6)
            _10N2 = round(Value_10[0][3],6)
            _10N1 = round(Value_10[0][4],6)            
            _10P1 = round(Value_10[0][6],6)
            _10P2 = round(Value_10[0][7],6)
            _10P3 = round(Value_10[0][8],6) 
            _10P4 = round(Value_10[0][9],6) 
            _10P5 = round(Value_10[0][10],6) 

            Value_11 = logreg_11.predict_proba(feat11)
            _11N5 = round(Value_11[0][0],6)
            _11N4 = round(Value_11[0][1],6)
            _11N3 = round(Value_11[0][2],6)
            _11N2 = round(Value_11[0][3],6)
            _11N1 = round(Value_11[0][4],6)            
            _11P1 = round(Value_11[0][6],6)
            _11P2 = round(Value_11[0][7],6)
            _11P3 = round(Value_11[0][8],6) 
            _11P4 = round(Value_11[0][9],6) 
            _11P5 = round(Value_11[0][10],6)

            Value_12 = logreg_12.predict_proba(feat12)
            _12N5 = round(Value_12[0][0],6)
            _12N4 = round(Value_12[0][1],6)
            _12N3 = round(Value_12[0][2],6)
            _12N2 = round(Value_12[0][3],6)
            _12N1 = round(Value_12[0][4],6)            
            _12P1 = round(Value_12[0][6],6)
            _12P2 = round(Value_12[0][7],6)
            _12P3 = round(Value_12[0][8],6) 
            _12P4 = round(Value_12[0][9],6) 
            _12P5 = round(Value_12[0][10],6)  

            Value_13 = logreg_13.predict_proba(feat13)
            _13N5 = round(Value_13[0][0],6)
            _13N4 = round(Value_13[0][1],6)
            _13N3 = round(Value_13[0][2],6)
            _13N2 = round(Value_13[0][3],6)
            _13N1 = round(Value_13[0][4],6)            
            _13P1 = round(Value_13[0][6],6)
            _13P2 = round(Value_13[0][7],6)
            _13P3 = round(Value_13[0][8],6) 
            _13P4 = round(Value_13[0][9],6) 
            _13P5 = round(Value_13[0][10],6)  

            Value_14 = logreg_14.predict_proba(feat14)
            _14N5 = round(Value_14[0][0],6)
            _14N4 = round(Value_14[0][1],6)
            _14N3 = round(Value_14[0][2],6)
            _14N2 = round(Value_14[0][3],6)
            _14N1 = round(Value_14[0][4],6)            
            _14P1 = round(Value_14[0][6],6)
            _14P2 = round(Value_14[0][7],6)
            _14P3 = round(Value_14[0][8],6) 
            _14P4 = round(Value_14[0][9],6) 
            _14P5 = round(Value_14[0][10],6)

            Value_15 = logreg_15.predict_proba(feat15)
            _15N5 = round(Value_15[0][0],6)
            _15N4 = round(Value_15[0][1],6)
            _15N3 = round(Value_15[0][2],6)
            _15N2 = round(Value_15[0][3],6)
            _15N1 = round(Value_15[0][4],6)            
            _15P1 = round(Value_15[0][6],6)
            _15P2 = round(Value_15[0][7],6)
            _15P3 = round(Value_15[0][8],6) 
            _15P4 = round(Value_15[0][9],6) 
            _15P5 = round(Value_15[0][10],6)   

            Value_16 = logreg_16.predict_proba(feat16)
            _16N5 = round(Value_16[0][0],6)
            _16N4 = round(Value_16[0][1],6)
            _16N3 = round(Value_16[0][2],6)
            _16N2 = round(Value_16[0][3],6)
            _16N1 = round(Value_16[0][4],6)            
            _16P1 = round(Value_16[0][6],6)
            _16P2 = round(Value_16[0][7],6)
            _16P3 = round(Value_16[0][8],6) 
            _16P4 = round(Value_16[0][9],6) 
            _16P5 = round(Value_16[0][10],6)  

            Value_17 = logreg_17.predict_proba(feat17)
            _17N5 = round(Value_17[0][0],6)
            _17N4 = round(Value_17[0][1],6)
            _17N3 = round(Value_17[0][2],6)
            _17N2 = round(Value_17[0][3],6)
            _17N1 = round(Value_17[0][4],6)            
            _17P1 = round(Value_17[0][6],6)
            _17P2 = round(Value_17[0][7],6)
            _17P3 = round(Value_17[0][8],6) 
            _17P4 = round(Value_17[0][9],6) 
            _17P5 = round(Value_17[0][10],6)  

            Value_18 = logreg_18.predict_proba(feat18)
            _18N5 = round(Value_18[0][0],6)
            _18N4 = round(Value_18[0][1],6)
            _18N3 = round(Value_18[0][2],6)
            _18N2 = round(Value_18[0][3],6)
            _18N1 = round(Value_18[0][4],6)            
            _18P1 = round(Value_18[0][6],6)
            _18P2 = round(Value_18[0][7],6)
            _18P3 = round(Value_18[0][8],6) 
            _18P4 = round(Value_18[0][9],6) 
            _18P5 = round(Value_18[0][10],6)

            Value_19 = logreg_19.predict_proba(feat19)
            _19N5 = round(Value_19[0][0],6)
            _19N4 = round(Value_19[0][1],6)
            _19N3 = round(Value_19[0][2],6)
            _19N2 = round(Value_19[0][3],6)
            _19N1 = round(Value_19[0][4],6)            
            _19P1 = round(Value_19[0][6],6)
            _19P2 = round(Value_19[0][7],6)
            _19P3 = round(Value_19[0][8],6) 
            _19P4 = round(Value_19[0][9],6) 
            _19P5 = round(Value_19[0][10],6)  

            Value_20 = logreg_20.predict_proba(feat20)
            _20N5 = round(Value_20[0][0],6)
            _20N4 = round(Value_20[0][1],6)
            _20N3 = round(Value_20[0][2],6)
            _20N2 = round(Value_20[0][3],6)
            _20N1 = round(Value_20[0][4],6)            
            _20P1 = round(Value_20[0][6],6)
            _20P2 = round(Value_20[0][7],6)
            _20P3 = round(Value_20[0][8],6) 
            _20P4 = round(Value_20[0][9],6) 
            _20P5 = round(Value_20[0][10],6)

            Value_21 = logreg_21.predict_proba(feat21)
            _21N5 = round(Value_21[0][0],6)
            _21N4 = round(Value_21[0][1],6)
            _21N3 = round(Value_21[0][2],6)
            _21N2 = round(Value_21[0][3],6)
            _21N1 = round(Value_21[0][4],6)            
            _21P1 = round(Value_21[0][6],6)
            _21P2 = round(Value_21[0][7],6)
            _21P3 = round(Value_21[0][8],6) 
            _21P4 = round(Value_21[0][9],6) 
            _21P5 = round(Value_21[0][10],6)              

            Value_22 = logreg_22.predict_proba(feat22)
            _22N5 = round(Value_22[0][0],6)
            _22N4 = round(Value_22[0][1],6)
            _22N3 = round(Value_22[0][2],6)
            _22N2 = round(Value_22[0][3],6)
            _22N1 = round(Value_22[0][4],6)            
            _22P1 = round(Value_22[0][6],6)
            _22P2 = round(Value_22[0][7],6)
            _22P3 = round(Value_22[0][8],6) 
            _22P4 = round(Value_22[0][9],6) 
            _22P5 = round(Value_22[0][10],6)

            Value_23 = logreg_23.predict_proba(feat23)
            _23N5 = round(Value_23[0][0],6)
            _23N4 = round(Value_23[0][1],6)
            _23N3 = round(Value_23[0][2],6)
            _23N2 = round(Value_23[0][3],6)
            _23N1 = round(Value_23[0][4],6)            
            _23P1 = round(Value_23[0][6],6)
            _23P2 = round(Value_23[0][7],6)
            _23P3 = round(Value_23[0][8],6) 
            _23P4 = round(Value_23[0][9],6) 
            _23P5 = round(Value_23[0][10],6)

            Value_24 = logreg_24.predict_proba(feat24)
            _24N5 = round(Value_24[0][0],6)
            _24N4 = round(Value_24[0][1],6)
            _24N3 = round(Value_24[0][2],6)
            _24N2 = round(Value_24[0][3],6)
            _24N1 = round(Value_24[0][4],6)            
            _24P1 = round(Value_24[0][6],6)
            _24P2 = round(Value_24[0][7],6)
            _24P3 = round(Value_24[0][8],6) 
            _24P4 = round(Value_24[0][9],6) 
            _24P5 = round(Value_24[0][10],6)  

            Value_25 = logreg_25.predict_proba(feat25)
            _25N5 = round(Value_25[0][0],6)
            _25N4 = round(Value_25[0][1],6)
            _25N3 = round(Value_25[0][2],6)
            _25N2 = round(Value_25[0][3],6)
            _25N1 = round(Value_25[0][4],6)            
            _25P1 = round(Value_25[0][6],6)
            _25P2 = round(Value_25[0][7],6)
            _25P3 = round(Value_25[0][8],6) 
            _25P4 = round(Value_25[0][9],6) 
            _25P5 = round(Value_25[0][10],6)

            Value_26 = logreg_26.predict_proba(feat26)
            _26N5 = round(Value_26[0][0],6)
            _26N4 = round(Value_26[0][1],6)
            _26N3 = round(Value_26[0][2],6)
            _26N2 = round(Value_26[0][3],6)
            _26N1 = round(Value_26[0][4],6)            
            _26P1 = round(Value_26[0][6],6)
            _26P2 = round(Value_26[0][7],6)
            _26P3 = round(Value_26[0][8],6) 
            _26P4 = round(Value_26[0][9],6) 
            _26P5 = round(Value_26[0][10],6) 
            
            Value_27 = logreg_27.predict_proba(feat27)
            _27N5 = round(Value_27[0][0],6)
            _27N4 = round(Value_27[0][1],6)
            _27N3 = round(Value_27[0][2],6)
            _27N2 = round(Value_27[0][3],6)
            _27N1 = round(Value_27[0][4],6)            
            _27P1 = round(Value_27[0][6],6)
            _27P2 = round(Value_27[0][7],6)
            _27P3 = round(Value_27[0][8],6) 
            _27P4 = round(Value_27[0][9],6) 
            _27P5 = round(Value_27[0][10],6)

            Value_28 = logreg_28.predict_proba(feat28)
            _28N5 = round(Value_28[0][0],6)
            _28N4 = round(Value_28[0][1],6)
            _28N3 = round(Value_28[0][2],6)
            _28N2 = round(Value_28[0][3],6)
            _28N1 = round(Value_28[0][4],6)            
            _28P1 = round(Value_28[0][6],6)
            _28P2 = round(Value_28[0][7],6)
            _28P3 = round(Value_28[0][8],6) 
            _28P4 = round(Value_28[0][9],6) 
            _28P5 = round(Value_28[0][10],6)

            Value_29 = logreg_29.predict_proba(feat29)
            _29N5 = round(Value_29[0][0],6)
            _29N4 = round(Value_29[0][1],6)
            _29N3 = round(Value_29[0][2],6)
            _29N2 = round(Value_29[0][3],6)
            _29N1 = round(Value_29[0][4],6)            
            _29P1 = round(Value_29[0][6],6)
            _29P2 = round(Value_29[0][7],6)
            _29P3 = round(Value_29[0][8],6) 
            _29P4 = round(Value_29[0][9],6) 
            _29P5 = round(Value_29[0][10],6)

            Value_30 = logreg_30.predict_proba(feat30)
            _30N5 = round(Value_30[0][0],6)
            _30N4 = round(Value_30[0][1],6)
            _30N3 = round(Value_30[0][2],6)
            _30N2 = round(Value_30[0][3],6)
            _30N1 = round(Value_30[0][4],6)            
            _30P1 = round(Value_30[0][6],6)
            _30P2 = round(Value_30[0][7],6)
            _30P3 = round(Value_30[0][8],6) 
            _30P4 = round(Value_30[0][9],6) 
            _30P5 = round(Value_30[0][10],6)

            print("Completed calculations...")
        except Exception as e:
            print("Error calculating" + str(e))
            pass



        print("Building indicators for final prediction values...")

        try:       
    ### END loading the saved .pkl files with trained algo information

    ### START building own indicators for final prediction values
    

        ### 1st stage, adding all StrongBuy percentage vs all StrongSell percantage
        ### continuing with comparing all Buy percantage vs all Sell percentage
            ### Doing this for the 7 algos based on future Pattern first
            
            _Prob01 = _01P1+_01P2+_01P3+_01P4+_01P5-_01N1-_01N2-_01N3-_01N4-_01N5
            _Prob02 = _02P1+_02P2+_02P3+_02P4+_02P5-_02N1-_02N2-_02N3-_02N4-_02N5
            _Prob03 = _03P1+_03P2+_03P3+_03P4+_03P5-_03N1-_03N2-_03N3-_03N4-_03N5
            _Prob04 = _04P1+_04P2+_04P3+_04P4+_04P5-_04N1-_04N2-_04N3-_04N4-_04N5
            _Prob05 = _05P1+_05P2+_05P3+_05P4+_05P5-_05N1-_05N2-_05N3-_05N4-_05N5
            _Prob06 = _06P1+_06P2+_06P3+_06P4+_06P5-_06N1-_06N2-_06N3-_06N4-_06N5
            _Prob07 = _07P1+_07P2+_07P3+_07P4+_07P5-_07N1-_07N2-_07N3-_07N4-_07N5
            _Prob08 = _08P1+_08P2+_08P3+_08P4+_08P5-_08N1-_08N2-_08N3-_08N4-_08N5
            _Prob09 = _09P1+_09P2+_09P3+_09P4+_09P5-_09N1-_09N2-_09N3-_09N4-_09N5
            _Prob10 = _10P1+_10P2+_10P3+_10P4+_10P5-_10N1-_10N2-_10N3-_10N4-_10N5
            _Prob11 = _11P1+_11P2+_11P3+_11P4+_11P5-_11N1-_11N2-_11N3-_11N4-_11N5
            _Prob12 = _12P1+_12P2+_12P3+_12P4+_12P5-_12N1-_12N2-_12N3-_12N4-_12N5
            _Prob13 = _13P1+_13P2+_13P3+_13P4+_13P5-_13N1-_13N2-_13N3-_13N4-_13N5
            _Prob14 = _14P1+_14P2+_14P3+_14P4+_14P5-_14N1-_14N2-_14N3-_14N4-_14N5
            _Prob15 = 0.343 * (_15P1+_15P2+_15P3+_15P4+_15P5-_15N1-_15N2-_15N3-_15N4-_15N5)
            _Prob16 = 0.343 * (_16P1+_16P2+_16P3+_16P4+_16P5-_16N1-_16N2-_16N3-_16N4-_16N5)
            _Prob17 = 0.343 * (_17P1+_17P2+_17P3+_17P4+_17P5-_17N1-_17N2-_17N3-_17N4-_17N5)
            _Prob18 = 0.343 * (_18P1+_18P2+_18P3+_18P4+_18P5-_18N1-_18N2-_18N3-_18N4-_18N5)
            _Prob19 = 0.343 * (_19P1+_19P2+_19P3+_19P4+_19P5-_19N1-_19N2-_19N3-_19N4-_19N5)
            _Prob20 = 0.343 * (_20P1+_20P2+_20P3+_20P4+_20P5-_20N1-_20N2-_20N3-_20N4-_20N5)
            _Prob21 = 0.343 * (_21P1+_21P2+_21P3+_21P4+_21P5-_21N1-_21N2-_21N3-_21N4-_21N5)
            _Prob22 = 0.343 * (_22P1+_22P2+_22P3+_22P4+_22P5-_22N1-_22N2-_22N3-_22N4-_22N5)
            _Prob23 = 0.343 * (_23P1+_23P2+_23P3+_23P4+_23P5-_23N1-_23N2-_23N3-_23N4-_23N5)
            _Prob24 = 0.343 * (_24P1+_24P2+_24P3+_24P4+_24P5-_24N1-_24N2-_24N3-_24N4-_24N5)
            _Prob25 = 0.343 * (_25P1+_25P2+_25P3+_25P4+_25P5-_25N1-_25N2-_25N3-_25N4-_25N5)
            _Prob26 = 0.343 * (_26P1+_26P2+_26P3+_26P4+_26P5-_26N1-_26N2-_26N3-_26N4-_26N5)
            _Prob27 = 0.343 * (_27P1+_27P2+_27P3+_27P4+_27P5-_27N1-_27N2-_27N3-_27N4-_27N5)
            _Prob28 = 0.343 * (_28P1+_28P2+_28P3+_28P4+_28P5-_28N1-_28N2-_28N3-_28N4-_28N5)
            _Prob29 = 0.343 * (_29P1+_29P2+_29P3+_29P4+_29P5-_29N1-_29N2-_29N3-_29N4-_29N5)
            _Prob30 = 0.343 * (_30P1+_30P2+_30P3+_30P4+_30P5-_30N1-_30N2-_30N3-_30N4-_30N5)
            
            _OutlookList = [_Prob01,
                            _Prob02,
                            _Prob03,
                            _Prob04,
                            _Prob05,
                            _Prob06,
                            _Prob07,
                            _Prob08,
                            _Prob09,
                            _Prob10,
                            _Prob11,
                            _Prob12,
                            _Prob13,
                            _Prob14,
                            _Prob15,
                            _Prob16,
                            _Prob17,
                            _Prob18,
                            _Prob19,
                            _Prob20,
                            _Prob21,
                            _Prob22,
                            _Prob23,
                            _Prob24,
                            _Prob25,
                            _Prob26,
                            _Prob27,
                            _Prob28,
                            _Prob29,
                            _Prob30]
                            
            _meanList = np.mean(_OutlookList)
            _stdList = np.std(_OutlookList)

            Outlook = round(_meanList/_stdList,6)
            print(str(eachTicker)+": "+str(Outlook))

            Ultimate_df2 = Ultimate_df2.append({'Name':eachRealNames,
                                                'Forecast':Outlook,
                                                }, ignore_index = True)            
                         
        except Exception as e:
            print(str(e))
            pass

    try:    
        Ultimate_df2 = Ultimate_df2.sort_values(by=['Forecast'], ascending=False)
        Count_Row=Ultimate_df2.shape[0]
    except Exception as e:
        print(str(e))


    print("\n\n=== Saving and printing results ===\n")

    if Count_Row == 30:
        try:        
            print(Ultimate_df2)
            Ultimate_df2.to_csv(MetaStockCSVfile + '\OrderDataIQ19p.csv', sep=',', header=False, index=False)
            Ultimate_df2.to_csv(MetaStockCSVfile + '\OrderDataIQ19pTEMP.csv', sep=',', header=False, index=False)

            print("\nSaving to {0}:", MetaStockCSVfile)
            print("- OrderDataIQ19p.csv")
            print("- OrderDataIQ19pTEMP.csv")
        except Exception as e:
            print(str(e))        

    else:
        pass





def main():
    #makeForecast('Forex30')

    c = Console(
"""  _____                            _            
 |  ___|__  _ __ ___  ___ __ _ ___| |_ ___ _ __ 
 | |_ / _ \| '__/ _ \/ __/ _` / __| __/ _ \ '__|
 |  _| (_) | | |  __/ (_| (_| \__ \ ||  __/ |   
 |_|  \___/|_|  \___|\___\__,_|___/\__\___|_|   

""")


    numIterations = 100

    for i in range(1, numIterations + 1):
        c.timer.print_elapsed("Starting iteration {0} / {1}".format(i, numIterations))
        unixTimestamp = int(time.time())
        timestampXX = int(str(datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%H')))
        weekDay = int(str(datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%w')))
        timestampMin = int(str(datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%M')))    

        if timestampXX > 6 and timestampXX < 22 and weekDay < 6:
            makeForecast('Forex30')
            unixTimestamp = int(time.time())
            timestamp = str(datetime.datetime.fromtimestamp(int(unixTimestamp)).strftime('%Y-%m-%d %H_%M'))
            
            print("Timestamp of run: {0}".format(timestamp))

            c.timer.print_elapsed("\nIteration {0} / {1} finished, sleeping 30 minutes".format(i, numIterations))

            time.sleep(1800)
        else:
            print("Skipping iteration {0}".format(i))
            pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))