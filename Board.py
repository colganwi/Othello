#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 12:24:43 2016

@author: William
"""
import numpy as np

class Board:
    def __init__(self, color, state = None):
        if state is None:
            self.state = np.zeros((64,), dtype=np.int)
            self.state[27] = 1
            self.state[28] = -1
            self.state[36] = 1
            self.state[35] = -1
        else:
            self.state = state
        self.color = color
        self.DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
    def validPlays(self):
        plays = []
        for x in range(8):
            for y in range(8):
                if (self.state[y*8+x] == 0):
                    for direction in self.DIRECTIONS:
                        x1 = x + direction[0]
                        y1 = y + direction[1]
                        if(x1<8 and x1>=0 and y1<8 and y1>=0 and self.state[y1*8+x1] == -self.color):
                            while(x1<8 and x1>=0 and y1<8 and y1>=0 and self.state[y1*8+x1] == -self.color):
                                x1 += direction[0]
                                y1 += direction[1]
                            if(x1<8 and x1>=0 and y1<8 and y1>=0 and self.state[y1*8+x1] == self.color):
                                plays += [y*8+x]
                                break
        return plays
                        
    def makePlay(self, play):
        newState = np.copy(self.state)
        newState[play] = self.color
        x = int(play%8)
        y = int(play/8)
        for direction in self.DIRECTIONS:
            x1 = x + direction[0]
            y1 = y + direction[1]
            if(x1<8 and x1>=0 and y1<8 and y1>=0 and self.state[y1*8+x1] == -self.color):
                while(x1<8 and x1>=0 and y1<8 and y1>=0 and self.state[y1*8+x1] == -self.color):
                    x1 += direction[0]
                    y1 += direction[1]
                if(x1<8 and x1>=0 and y1<8 and y1>=0 and self.state[y1*8+x1] == self.color):
                    x1 -= direction[0]
                    y1 -= direction[1]
                    while(x1 != x or y1 != y):
                        newState[y1*8+x1] = self.color
                        x1 -= direction[0]
                        y1 -= direction[1]
        newBoard = Board(-self.color, newState)
        if len(newBoard.validPlays()) != 0:
            return newBoard   
        else:
            newBoard = Board(self.color, newState)
            return newBoard
        
    def getState(self):
        return self.state
        
    def getColor(self):
        return self.color
        
    def getWinner(self):
        if(np.sum(self.state) < 0):
            return -1
        elif(np.sum(self.state) > 0):
            return 1
        else:
            return 0


