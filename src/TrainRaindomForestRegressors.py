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
from collections import defaultdict
import joblib
import os
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint
import pathlib
import time
import random
from scipy.stats import mstats
from sklearn.model_selection import cross_val_predict, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn import metrics, preprocessing
import sys
import traceback
import uuid

from config.IQConfig import IQConfig
from gui.console import Console
from metrics.Timer import Timer


def main():
    c = Console(
    """  _____          _         ____                 _                                
     |_   _| __ __ _(_)_ __   |  _ \\ __ _ _ __   __| | ___  _ __ ___                 
       | || '__/ _` | | '_ \\  | |_) / _` | '_ \\ / _` |/ _ \\| '_ ` _ \\                
       | || | | (_| | | | | | |  _ < (_| | | | | (_| | (_) | | | | | |               
       |_||_|  \\__,_|_|_| |_| |_| \\_\\__,_|_| |_|\\__,_|\\___/|_| |_| |_|               
      _____                   _     ____                                             
     |  ___|__  _ __ ___  ___| |_  |  _ \\ ___  __ _ _ __ ___  ___ ___  ___  _ __ ___ 
     | |_ / _ \\| '__/ _ \\/ __| __| | |_) / _ \\/ _` | '__/ _ \\/ __/ __|/ _ \\| '__/ __|
     |  _| (_) | | |  __/\\__ \\ |_  |  _ <  __/ (_| | | |  __/\\__ \\__ \\ (_) | |  \\__ \\
     |_|  \\___/|_|  \\___||___/\\__| |_| \\_\\___|\\__, |_|  \\___||___/___/\\___/|_|  |___/
                                              |___/                                  """)


    config = IQConfig()

    randomSearchCVResultsScore = pd.DataFrame(columns=["Score", "Hyperparams"])
    randomSearchCVResults = pd.DataFrame()
    bestPipelines = pd.DataFrame()

    featuresStrategyName = config.features.featuresStrategy
    print("\nFeatures strategy: {}".format(featuresStrategyName))

    targetsStrategyName = config.features.targetsStrategy
    print("Targets strategy: {}".format(targetsStrategyName))


    featuresOutputPath = config.features.getFeaturesOutputPath()
    targetsOutputPath = config.features.getTargetsOutputPath()

    #print(featuresOutputPath)
    #print(targetsOutputPath)

    featuresLocation = featuresOutputPath + ".msg"
    targetsLocation = targetsOutputPath + ".msg"


    trainFileSize = os.path.getsize(featuresLocation) / 1024. / 1024.
    print ('\nReading {0:.2f}MB of training data (features) from {1}...'.format(trainFileSize, featuresLocation))
    trainData = pd.read_msgpack(featuresLocation)
    c.timer.print_elapsed("Read {} rows of training data".format(len(trainData)))

    targetFileSize = os.path.getsize(targetsLocation) / 1024. / 1024.
    print ('Reading {0:.2f}MB of target data (target features) from {1}...'.format(targetFileSize, targetsLocation))
    targetData = pd.read_msgpack(targetsLocation)
    c.timer.print_elapsed("Read {} rows of target data".format(len(targetData)))


    if len(trainData) != len(targetData):
        raise AssertionError("Training and target data length mismatch. Must contain equal number of rows.")

    #Inspect data
    #print(trainData.head())
    #print(targetData.head())


    featureNames = trainData.columns.values.tolist();
    targetNames = targetData.columns.values.tolist();

    print ("List of features: {}".format(featureNames))
    print ("\nList of targets: {}".format(targetNames))



    #print ("\nData types of columns (should normally show floats, ints and one date column only):")
    #print(trainData.dtypes)


    _CV = 3 #USE 60 to slit in to seperate 3 month periods or 180 to 1 month periods for daily data


    trainingDataOutputFile = os.path.join(config.root, config.trainRandomForestRegressors.trainingDataOutputFile)
    pathlib.Path(os.path.dirname(trainingDataOutputFile + ".msg")).mkdir(parents=True, exist_ok=True) 
    print("\nOne line of output per iteration will be saved to {}".format(trainingDataOutputFile))

    numIterations = config.trainRandomForestRegressors.numIterations

    for countX in range(1, numIterations+1):
        iterationTimer = Timer()

        print("\n\nStarting iteration {0} / {1}".format(countX, numIterations))


    ####---------------------------------------------------------------------------   
    #### This part optimized 2016-10-10
        try: 

            selectedFeaturesCount = random.randrange(round(len(featureNames) / 2.), len(featureNames))
            selectedTargetIndex = random.randrange(0, len(targetNames))

            min_samples_leaf_Rand = 50 #random.randrange(20, 200, 1)# [100],
        

            _delare1 = random.randrange(618, 850, 1)
            _delare2 = round(_delare1/1000.0001,8)
            max_feat_Rand = int(round(selectedFeaturesCount * _delare2,0))
            max_leaf_nodes_Rand = 10000 #random.randrange(10000, 12000, 1)# [10000 rätt],
            min_samples_split_Rand = 150 #random.randrange(30, 300, 1)# [150 rätt],
            max_depth_Rand = 50 #random.randrange(30, 300, 1)#[150 rätt]    
            n_estimators_Rand = 50 #random.randrange(100, 250, 1)# [150 rätt]
 
    

            selectedFeatureNames = (random.sample(featureNames, selectedFeaturesCount))
            selectedTargetName = targetNames[selectedTargetIndex]
        ####---------------------------------------------------------------------------  
    
        
    
            #print(featureNames)
            #print("====")
            #print(selectedFeatureNames)
    
            X = trainData[selectedFeatureNames].values
            y = targetData[selectedTargetName].values

            forest = RandomForestRegressor(n_estimators = n_estimators_Rand,
                                            max_depth = max_depth_Rand,
                                            warm_start='False',
                                            max_features=max_feat_Rand,
                                            min_samples_leaf=min_samples_leaf_Rand,
                                            bootstrap='True',
                                            #oob_score = True,
                                            max_leaf_nodes=max_leaf_nodes_Rand,
                                            min_samples_split=min_samples_split_Rand,
                                            #random_state=42,
                                            n_jobs=-1)

            pipeline = Pipeline(steps = [
                ("scaler", preprocessing.StandardScaler()),  # Note: one-hot encoder should be used for weekdays, months, etc
                ("forest", forest)
            ])
   



            # http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
            hyperparameters = { 
                'forest__n_estimators': [int(x) for x in np.linspace(start = 10, stop = 100, num = 5)], #10E1 => 10E3
                'forest__max_features': ['auto', 'sqrt', 'log2'],
                'forest__max_depth': [None, 10, 30, 80, 110],
                'forest__min_samples_split': [x for x in np.logspace(-2, -6, 10)],
                #'forest__min_samples_leaf ': [x for x in np.logspace(-2, -6, 10)],
                'forest__bootstrap': [True, False]
            }
            #print(pipeline.get_params())

        except Exception as e:
            print("Error setting up initial Random Forest")
            traceback.print_exc()
    
        try:
            clf = RandomizedSearchCV(
                pipeline, 
                hyperparameters, 
                cv=3, 
                verbose=2, 
                #random_state = 42, 
                n_iter=2, n_jobs=1
            )

            print("\n\nSet of hyperparams investigated")
            pprint(hyperparameters)

            print("\n\nStarting RandomizedSearchCV over pipeline hyperparams...")
            clf.fit(X, y)

            print("\n\n\nBest params")
            pprint(clf.best_params_)
            print("\nBest score")
            print(clf.best_score_)

            newRow = pd.DataFrame(clf.cv_results_)
            
            randomSearchCVResults = randomSearchCVResults.append(newRow, ignore_index=True)
            randomSearchCVResultsScore = randomSearchCVResultsScore.append(pd.DataFrame([[clf.best_score_, clf.best_params_]], columns=randomSearchCVResultsScore.columns))

            #randomSearchCVResults = pd.DataFrame(clf.cv_results_)
            randomSearchCVResults.to_excel(os.path.join(config.root, "randomSearchCVResults.xlsx"))
            randomSearchCVResultsScore.to_excel(os.path.join(config.root, "randomSearchCVResultsScore.xlsx"))

            best_pipeline = clf.best_estimator_
            scores = cross_val_score(best_pipeline, X, y, cv=_CV, scoring="neg_mean_squared_error")
            pred = cross_val_predict(best_pipeline, X, y, cv=_CV)
            accuracy = metrics.r2_score(y, pred)
            print ("Cross-Predicted Accuracy: {0}".format(accuracy))

            spearman = mstats.spearmanr(y, pred)
            pearson = mstats.pearsonr(y, pred)

            #print(f'Out-of-bag R-2 score estimate: {forest.oob_score_:>5.3}')
            #print('Out-of-bag R-2 score estimate')
            #print(forest.oob_score_)
        
            print(f'Test data R-2 score: {accuracy:>5.3}')
            print(f'Test data Spearman correlation: {spearman[0]:.3}')
            print(f'Test data Pearson correlation: {pearson[0]:.3}')

            print ("R2: {}".format(metrics.r2_score(y, pred)))
            print ("MSE: {}".format(metrics.mean_squared_error(y, pred)))
 
            ##### MEAN DECREASED IMPURITY impurity reduction #####     (meaning feat1 reduces impurity that feat2 would have reduced 99% of -> feat2 gets low score and feat1 high
            
            best_pipeline.fit(X, y)
            importance = best_pipeline.named_steps["forest"].feature_importances_
            importance = pd.DataFrame(importance, index=selectedFeatureNames, columns=["Importance"])
        
            importance["Std"] = np.std([tree.feature_importances_ for tree in best_pipeline.named_steps["forest"].estimators_], axis=0)
            importance["Part"] = importance["Importance"] / importance["Importance"].sum()
            importance = importance.sort_values(by='Importance', ascending=0)
        
            #print(importance)
        
            runId = uuid.uuid4().hex
            joblib.dump(best_pipeline, os.path.join(config.root, "pipeline-{}.pkl".format(runId)))

            _minScore = round(np.amin(scores),6)
            _maxScore = round(np.amax(scores),6)
            _meanScore = round(np.mean(scores),6)
            _stdScore = round(np.std(scores),6)
            _SharpMin = round(_minScore/_stdScore,6)
            _SharpMean = round(_meanScore/_stdScore,6)

            test = importance.T
            test["RunId"] = runId
            test["BestScore"] = clf.best_score_
            test["MinScore"] = _minScore
            test["MaxScore"] = _maxScore
            test["MeanScore"] = _meanScore
            test["stdScore"] = _stdScore
            test["SharpMin"] = _SharpMin
            test["SharpMean"] = _SharpMean


            bestPipelines = bestPipelines.append(test, ignore_index = True)
            bestPipelines.to_excel(os.path.join(config.root, "best-pipelines.xlsx"))


            topFeatures = importance.head(10) #Top 10
        


            x = range(topFeatures.shape[0])
            y2 = topFeatures.ix[:, 0]
            yerr = topFeatures.ix[:, 1]
        
            plt.bar(x, y2, yerr=yerr, align="center")
            plt.title("Most important features, share of total impurity reduction")
            plt.figtext(.9,.9,"Accuracy: {}, min: {}, mean: {}, max: {}, std: {}".format(accuracy, _minScore, _meanScore, _maxScore, _stdScore),fontsize=10,ha='right')

            #plt.title()

            plt.xticks(x, topFeatures.index.values, rotation=20, ha="right")
            plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))

            plt.tight_layout()

            fig = plt.figure(1)


            plt.show(block=False)
            plt.pause(5)
            #plt.pause(3)
            plt.close(fig)





        
        
            c.timer.print_elapsed("Min score {0}".format(_minScore))


            appendFile = open(trainingDataOutputFile, 'a') # put in path and filename for results
            appendFile.write('\n' + str(_minScore)+

                            str(',Time:,')  +
                            str(iterationTimer.elapsed()) + 

                            str(',CV:,')  +
                            str(_CV) + 
                        
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
                            str(selectedFeaturesCount) +
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
                            str(selectedFeatureNames) +
                            str(',Target: ,') + 
                            str(selectedTargetName))
     
            print("Appended row to {0}".format(trainingDataOutputFile))
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
    #print("Sort:          {0}".format(_featureToCheck))
    print("Max score:     {0:.4f}".format(_meanScore))
    print("Std score:     {0:.4f}".format(_stdScore))
    print("Sharp min:     {0:.4f}".format(_SharpMin))
    print("Sharp mean:    {0:.4f}".format(_SharpMean))
    print("Num feats:     {0}".format(selectedFeaturesCount))
    print("Min leaf:      {0}".format(min_samples_leaf_Rand))
    print("Max feat:      {0}".format(max_feat_Rand))
    print("Leaf nodes:    {0}".format(max_leaf_nodes_Rand))
    print("Depth of tree: {0}".format(max_depth_Rand))
    print("Num trees:     {0}".format(n_estimators_Rand))


if __name__ == "__main__":
    sys.exit(int(main() or 0))