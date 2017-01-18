# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter
import time
from Board import Board
from Players import SearchPlayer
from Players import SimplePlayer
from Evaluations import NNEvaluation
from Evaluations import featureEvaluation
from sklearn.neural_network import MLPRegressor
from sklearn.externals import joblib

class OthelloGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self.root, height = 600, width = 600)
        self.canvas.pack()
        self.board = Board(-1)
        clf = joblib.load('NNRegressor.pkl')
        self.player = SimplePlayer(featureEvaluation())
        self.drawBoard()

    def updateGame(self,event:tkinter.Event):
        play = int(self.canvas.gettags(event.widget.find_withtag('current'))[0])
        if play in self.board.validPlays():
            self.board = self.board.makePlay(play)
            if self.player is not None:
                play = self.player.play(self.board)
                self.board = self.board.makePlay(play)
        self.drawState()
            
            
    def drawBoard(self):
        for  x in range(8):
            for y in range(8):
                x1 = x * 75
                y1 = y * 75
                x2 = x1 + 75
                y2 = y1 + 75
                item = self.canvas.create_rectangle(x1,y1,x2,y2,fill = '#1C9E18', tags = str(y*8+x))
                self.canvas.tag_bind(item,'<ButtonPress-1>',self.updateGame)
                self.canvas.create_oval(x1+5, y1+5, x2-5, y2-5 ,outline= '#1C9E18', tags = 'tile'+str(y*8+x))
                self.drawState()
        
    def drawState(self):
        for i in range(64):
            if(self.board.getState()[i] == 1):
                self.canvas.itemconfigure('tile'+str(i), fill = 'white')
            elif(self.board.getState()[i] == -1):
                self.canvas.itemconfigure('tile'+str(i), fill = 'black')

    def run(self):
        self.root.mainloop()


gui = OthelloGUI()
gui.run()
