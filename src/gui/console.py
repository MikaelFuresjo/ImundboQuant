import os
import time

from metrics.Timer import Timer

class Console(object):
    timer = Timer()

    def __init__(self, moduleText, clearScreen=True, printBanner=True):
        if clearScreen:
            self.clear()
        if printBanner:
            self.print_banner(moduleText)

    def clear(self):
        os.system('cls||clear||echo -e \\\\033c')

    def print_banner(self, moduleText=None):
        print("""
  ___                           _ _            ___                    _    
 |_ _|_ __ ___  _   _ _ __   __| | |__   ___  / _ \ _   _  __ _ _ __ | |_  
  | || '_ ` _ \| | | | '_ \ / _` | '_ \ / _ \| | | | | | |/ _` | '_ \| __| 
  | || | | | | | |_| | | | | (_| | |_) | (_) | |_| | |_| | (_| | | | | |_  
 |___|_| |_| |_|\__,_|_| |_|\__,_|_.__/ \___/ \__\_\\__,_|\__,_|_| |_|\__| 
 OPEN-SOURCE PROJECT | https://github.com/MikaelFuresjo/ImundboQuant
 by Mikael Furesjö and friends

 Machine learning in Python and MQL4 for stock market and 
 forex market predictions and fully automated trading. 
    """);

        if (moduleText):
            print("MODULE\n" + str(moduleText))

        print('\n\n\n')

