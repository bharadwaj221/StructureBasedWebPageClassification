# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 23:01:51 2014

@author: bharadwaj
"""

import numpy
import sys
import lxml.html
import collections
import nltk
import re
import string
import os
import itertools
import pickle

import numpy
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import StratifiedKFold,LeavePOut
from sklearn.metrics import roc_curve, auc, accuracy_score
from sklearn.feature_selection import SelectKBest,chi2

features=numpy.loadtxt('COMPLETE_ACTUAL_features.txt');
output=numpy.loadtxt('COMPLETE_output.txt')
c1=1
c2=2
x1=features[output==c1];
x2=features[output==c2];

y1=output[output==c1];
y1=y1/max(y1)
y2=output[output==c2];
y2=y2*0

X=numpy.append(x1,x2,axis=0);
y=numpy.append(y1,y2,axis=0);
print 'LINEAR SVC........................'

# classifier = svm.SVC(kernel='rbf', probability=True, random_state=0, C = 1, gamma = 10)
# classifier = svm.LinearSVC()
#classifier = RandomForestClassifier(n_estimators=1000, max_features='log2')
#classifier = RandomForestClassifier(n_estimators=1000, max_features=0.0005)
#classifier = GradientBoostingClassifier(loss='deviance', learning_rate=0.1, n_estimators=1000, subsample=1.0, min_samples_split=2, min_samples_leaf=1, max_depth=3, init=None, random_state=None, max_features='sqrt', verbose=0)
#classifier = RandomForestClassifier(n_estimators=1000, max_features=0.0005)
classifier = LogisticRegression()
cv = StratifiedKFold(y, n_folds=5)
print 'Prod Vs Listing'
j=1
for i, (train, test) in enumerate(cv):
    print i
    scaler = preprocessing.StandardScaler().fit(X[train])
    classifier.fit(scaler.transform(X[train]), y[train])
    pickle.dump( classifier, open( "LinSvc_"+str(c1)+'vs'+str(c2)+'_'+str(j), "wb" ) )    
    j=j+1
    labTrain = classifier.predict(scaler.transform(X[train]))
    trainAccuracy = accuracy_score(y[train],labTrain)
    proTrain = classifier.predict_proba(scaler.transform(X[train]))
    fprTrain, tprTrain, thresholdsTrain = roc_curve(y[train], proTrain[:, 1])
    AUCTrain = auc(fprTrain, tprTrain)
    errorsTrain = numpy.absolute(y[train] - proTrain[:, 1])
    trainErrorMean = numpy.mean(errorsTrain)
    trainErrorStd = numpy.std(errorsTrain)  

    labTest = classifier.predict(scaler.transform(X[test]))
    testAccuracy = accuracy_score(y[test],labTest)
    proTest = classifier.predict_proba(scaler.transform(X[test]))
    fprTest, tprTest, thresholdsTest = roc_curve(y[test], proTest[:, 1])
    AUCTest = auc(fprTest, tprTest)
    errorsTest = numpy.absolute(y[test] - proTest[:, 1])
    testErrorMean = numpy.mean(errorsTest)
    testErrorStd = numpy.std(errorsTest)
    print AUCTrain, trainErrorMean, trainErrorStd, trainAccuracy, AUCTest, testErrorMean, testErrorStd, testAccuracy
##    # print trainAccuracy, testAccuracy
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    
    
    
print 'Listing Vs Other'   
c1=2
c2=3
x1=features[output==c1];
x2=features[output==c2];

y1=output[output==c1];
y1=y1/max(y1)
y2=output[output==c2];
y2=y2*0

X=numpy.append(x1,x2,axis=0);
y=numpy.append(y1,y2,axis=0);

# classifier = svm.SVC(kernel='rbf', probability=True, random_state=0, C = 1, gamma = 10)
# classifier = svm.LinearSVC()
#classifier = RandomForestClassifier(n_estimators=1000, max_features='log2')
#classifier = RandomForestClassifier(n_estimators=1000, max_features=0.0005)
#classifier = GradientBoostingClassifier(loss='deviance', learning_rate=0.1, n_estimators=1000, subsample=1.0, min_samples_split=2, min_samples_leaf=1, max_depth=3, init=None, random_state=None, max_features='sqrt', verbose=0)
#classifier = RandomForestClassifier(n_estimators=1000, max_features=0.0005)
# classifier = LogisticRegression()
cv = StratifiedKFold(y, n_folds=5)

j=1
for i, (train, test) in enumerate(cv):
    print i
    scaler = preprocessing.StandardScaler().fit(X[train])
    classifier.fit(scaler.transform(X[train]), y[train])
    pickle.dump( classifier, open( "LinSvc_"+str(c1)+'vs'+str(c2)+'_'+str(j), "wb" ) )    
    j=j+1
    labTrain = classifier.predict(scaler.transform(X[train]))
    trainAccuracy = accuracy_score(y[train],labTrain)
    proTrain = classifier.predict_proba(scaler.transform(X[train]))
    fprTrain, tprTrain, thresholdsTrain = roc_curve(y[train], proTrain[:, 1])
    AUCTrain = auc(fprTrain, tprTrain)
    errorsTrain = numpy.absolute(y[train] - proTrain[:, 1])
    trainErrorMean = numpy.mean(errorsTrain)
    trainErrorStd = numpy.std(errorsTrain)  

    labTest = classifier.predict(scaler.transform(X[test]))
    testAccuracy = accuracy_score(y[test],labTest)
    proTest = classifier.predict_proba(scaler.transform(X[test]))
    fprTest, tprTest, thresholdsTest = roc_curve(y[test], proTest[:, 1])
    AUCTest = auc(fprTest, tprTest)
    errorsTest = numpy.absolute(y[test] - proTest[:, 1])
    testErrorMean = numpy.mean(errorsTest)
    testErrorStd = numpy.std(errorsTest)
    print AUCTrain, trainErrorMean, trainErrorStd, trainAccuracy, AUCTest, testErrorMean, testErrorStd, testAccuracy
    
    
    
c1=1
c2=3
print 'Prod Vs Other'
x1=features[output==c1];
x2=features[output==c2];

y1=output[output==c1];
y1=y1/max(y1)
y2=output[output==c2];
y2=y2*0

X=numpy.append(x1,x2,axis=0);
y=numpy.append(y1,y2,axis=0);

# classifier = svm.SVC(kernel='rbf', probability=True, random_state=0, C = 1, gamma = 10)
classifier = svm.LinearSVC()
#classifier = RandomForestClassifier(n_estimators=1000, max_features='log2')
#classifier = RandomForestClassifier(n_estimators=1000, max_features=0.0005)
#classifier = GradientBoostingClassifier(loss='deviance', learning_rate=0.1, n_estimators=1000, subsample=1.0, min_samples_split=2, min_samples_leaf=1, max_depth=3, init=None, random_state=None, max_features='sqrt', verbose=0)
#classifier = RandomForestClassifier(n_estimators=1000, max_features=0.0005)
# classifier = LogisticRegression()
cv = StratifiedKFold(y, n_folds=5)

j=1
for i, (train, test) in enumerate(cv):
    print i
    scaler = preprocessing.StandardScaler().fit(X[train])
    classifier.fit(scaler.transform(X[train]), y[train])
    pickle.dump( classifier, open( "LinSvc"+str(c1)+'vs'+str(c2)+'_'+str(j), "wb" ) )    
    j=j+1
    labTrain = classifier.predict(scaler.transform(X[train]))
    trainAccuracy = accuracy_score(y[train],labTrain)
    proTrain = classifier.predict_proba(scaler.transform(X[train]))
    fprTrain, tprTrain, thresholdsTrain = roc_curve(y[train], proTrain[:, 1])
    AUCTrain = auc(fprTrain, tprTrain)
    errorsTrain = numpy.absolute(y[train] - proTrain[:, 1])
    trainErrorMean = numpy.mean(errorsTrain)
    trainErrorStd = numpy.std(errorsTrain)  

    labTest = classifier.predict(scaler.transform(X[test]))
    testAccuracy = accuracy_score(y[test],labTest)
    proTest = classifier.predict_proba(scaler.transform(X[test]))
    fprTest, tprTest, thresholdsTest = roc_curve(y[test], proTest[:, 1])
    AUCTest = auc(fprTest, tprTest)
    errorsTest = numpy.absolute(y[test] - proTest[:, 1])
    testErrorMean = numpy.mean(errorsTest)
    testErrorStd = numpy.std(errorsTest)
    print AUCTrain, trainErrorMean, trainErrorStd, trainAccuracy, AUCTest, testErrorMean, testErrorStd, testAccuracy