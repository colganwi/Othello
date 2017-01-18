#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 15:28:21 2016

@author: William
"""
from sklearn.neural_network import MLPRegressor
from sklearn.externals import joblib
import numpy as np
from Board import Board

class greedyEvaluation:
    def __init__(self):
        self.clf = None
    
    def evaluate(self, board):
        return np.sum(board.getState())
    
class featureEvaluation:
    def __init__(self):
        self.clf = None
    
    def evaluate(self, board):
        positionValues = np.array([10,2,4,4,4,4,2,10,2,0,0,0,0,0,0,2,4,0,2,1,1,2,0,4,4,0,1,0,0,1,0,4,4,0,1,0,0,1,0,4,4,0,2,1,1,2,0,4,2,0,0,0,0,0,0,2,10,2,4,4,4,4,2,10])
        return (.7*np.sum(board.getState()) + .3*np.dot(board.getState(),positionValues))/75
    
class NNEvaluation:
    def __init__(self, clf):
        self.clf = clf
    
    def evaluate(self, board):
        return self.clf.predict([board.getState()])[0]
    
    