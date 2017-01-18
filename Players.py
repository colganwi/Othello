#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 15:20:54 2016

@author: William
"""
import random
from Evaluations import featureEvaluation



class SimplePlayer:
    def __init__(self, evaluation):
        self.evaluation = evaluation
        
    def play(self, board):
        plays = board.validPlays()
        bestPlay = None
        if(board.getColor() == 1):
            bestValue = -1000
            for play in plays:
                value = self.evaluation.evaluate(board.makePlay(play))
                if value > bestValue:
                    bestPlay = play
                    bestValue = value
        else:
            bestValue = 1000
            for play in plays:
                value = self.evaluation.evaluate(board.makePlay(play))
                if value < bestValue:
                    bestPlay = play
                    bestValue = value
        return bestPlay
        

class RandomPlayer:
    def __init__(self):
        self.evaluation = None
        
    def play(self, board):
        
        plays = board.validPlays()
        return random.choice(plays)
            
        
class SearchPlayer:
    def __init__(self,evaluation):
        self.evaluation = evaluation
        self.maxDepth = 3
        
    def play(self, board):  
        
        def max_value(board, alpha, beta, depth):
            if depth == self.maxDepth:
                return self.evaluation.evaluate(board)
            value = -1000
            plays = board.validPlays()
            if len(plays) == 0:
                return self.evaluation.evaluate(board)
            for play in plays:
                newBoard = board.makePlay(play)
                value = min(value, max_value(newBoard ,alpha, beta, depth+1))
                if value >= beta:
                    return value
                alpha = max(alpha, value)
            return value
    
        def min_value(board, alpha, beta, depth):
            if depth == self.maxDepth:
                return self.evaluation.evaluate(board)
            value = 1000
            plays = board.validPlays()
            if len(plays) == 0:
                return self.evaluation.evaluate(board)
            for play in plays:
                newBoard = board.makePlay(play)
                value = max(value, min_value(newBoard, alpha, beta, depth+1))
                if value <= alpha:
                    return value
                beta = min(beta, value)
            return value
                
        bestPlay = None
        if(board.getColor() == 1):
            bestValue = -1000
            plays = board.validPlays()
            if len(plays) == 0:
                return self.evaluation.evaluate(board)
            for play in plays:
                newBoard = board.makePlay(play)
                value = min_value(newBoard, -1000, 1000, 0)
                if value > bestValue:
                    bestPlay = play
                    bestValue = value
        else:
            bestValue = 1000
            plays = board.validPlays()
            if len(plays) == 0:
                return self.evaluation.evaluate(board)
            for play in plays:
                newBoard = board.makePlay(play)
                value = max_value(newBoard, -1000, 1000, 0)
                if value < bestValue:
                    bestPlay = play
                    bestValue = value
        return bestPlay