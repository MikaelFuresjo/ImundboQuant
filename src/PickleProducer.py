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
import json
import numpy as np
import os
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib  ### Needed if you want to SAVE your learned dataset to .pkl

from config.IQConfig import IQConfig
from gui.console import Console

c = Console(
"""  ____  _      _    _                          _                     
 |  _ \(_) ___| | _| | ___ _ __  _ __ ___   __| |_   _  ___ ___ _ __ 
 | |_) | |/ __| |/ / |/ _ \ '_ \| '__/ _ \ / _` | | | |/ __/ _ \ '__|
 |  __/| | (__|   <| |  __/ |_) | | | (_) | (_| | |_| | (_|  __/ |   
 |_|   |_|\___|_|\_\_|\___| .__/|_|  \___/ \__,_|\__,_|\___\___|_|   
                          |_|                                        

 Will create pickled fit output from RandomForestClassifier
 based on previously extracted features and training data
""")


# Settings are kept in config/config.json
#########################################
#  Example config relevant to PickleProcucer:
#  {
#     "root": "c:\\data",
#     "pickleProducer": {
#       "folder": "pickles",
#       "features": {
#         "folder": "features",
#         "prefix": "FX30_IQ19p"
#       },
#       "training": {
#         "folder": "training",
#         "fileName": "TrainingDataset_IQ19qFX30.xlsx"
#       },
#       "slot": "10",
#       "horizon": "Tgt_SCH05to08",
#       "trainingInst": "LH40_535ft",
#       "numFeatures": 8,
#       "randomForest": {         /* http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html */
#         "n_estimators": 150,      /* The number of trees in the forest. */
#         "max_features": 8,        /* Consider max_features features at each split, null = all */
#         "max_depth": 150,         /* The maximum depth of the tree */
#         "min_samples_split": 150, /* Minimum number of samples required to split an internal node */
#         "min_samples_leaf": 50,   /* Minimum number of samples required to be at a leaf node */
#         "max_leaf_node": 10000,   /* Grow trees with max_leaf_nodes in best-first fashion. Best nodes are defined as relative reduction in impurity */
#         "n_jobs": -1,         /   /* The number of jobs to run in parallel for both fit and predict. If -1, then the number of jobs is set to the number of cores */
#         "random_state": 42        /* If int, random_state is the seed used by the random number generator. Null => new random number generator */
#       }
#    }
#  }


config = IQConfig()
picklePath = config.pickleProducer.getFolder()

featuresFilePath = config.pickleProducer.getFeaturesFilePath()
pickleFilePath = config.pickleProducer.getPickleFilePath()
trainFilePath = config.pickleProducer.getTrainingFilePath()

#########################################


# Import specific list of Features from file for each day
print("Reading features from {0}...".format(featuresFilePath))
FEATURES = []
featuresFile = open(featuresFilePath)
fleraFeatures = featuresFile.read()
FEATURES = fleraFeatures.split('\n')
featuresFile.close()

print("Reading training data from {0}...".format(trainFilePath))
trainData = pd.read_excel(trainFilePath)
c.timer.print_elapsed("Completed reading files...")

X = np.array(trainData[FEATURES].values) # making a np array from the pd dataset
y = trainData[config.pickleProducer.horizon].values # put in relevant target class

print("Initializing RandomForestClassfier...")
RFclf = RandomForestClassifier(**config.pickleProducer.randomForestConfig)
print("Fitting data...")
RFclf.fit(X,y)
print("Fitting completed")

joblib.dump(RFclf, pickleFilePath)
print("\nPickled forest of trees to {0}".format(pickleFilePath))

######################

c.timer.print_elapsed("Processing completed")
