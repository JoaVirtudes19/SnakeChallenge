#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:29:55 2022

@author: jjvircas
"""

class SnakeChallenge():
    def __init__(self,board,snake,depth):
        self.board = board
        self.snake = snake
        self.depth = depth
        self.paths = []
        # Constraints
        self.boardConstraints()
        self.snakeConstraints()
        self.coordinateConstraints()
        self.depthConstraints()
        
    def boardConstraints(self):
        if not (len(self.board) == 2 and all([1<=x and x<=10 for x in self.board])):
            raise SnakeError("Incorrect board size")
        return True
                
    def snakeConstraints(self):
        if not (3<=len(self.snake) and len(self.snake)<=7):
            raise SnakeError('Incorrect snake length')
        if not all([len(x) == 2 for x in self.snake]):
            raise SnakeError("Incorrect coordinates' size")
        return True
                
    def coordinateConstraints(self):
        if not all((0 <= x[0] and 0 <=x[1]) and (x[0] < self.board[0] and x[1] < self.board[1]) for x in self.snake):
            raise SnakeError("Incorrect snake's coordinates")
        return True
                
    def depthConstraints(self):
        if not (1<=self.depth and self.depth<=20):
            raise SnakeError('Incorrect depth')
        return True
        
    def validActions(self):
        valid = []
        headCol = self.snake[0][0]
        headRow = self.snake[0][1]
        if headCol-1 >= 0 and [headCol-1,headRow] not in self.snake[:-1]:
            valid.append('L') #We can move to the left
        if headCol+1 < self.board[0] and [headCol+1,headRow] not in self.snake[:-1]:
            valid.append('R') #We can move to the right
        if headRow+1 < self.board[1] and [headCol,headRow+1] not in self.snake[:-1]:
            valid.append('D')
        if headRow-1 >= 0 and [headCol,headRow-1] not in self.snake[:-1]:
            valid.append('U')
        return valid
        
    def neighbours(self,actions):
        snakes = []
        headCol = self.snake[0][0]
        headRow = self.snake[0][1]
        if 'L' in actions:
            aux = [[headCol-1,headRow]]+ self.snake[:-1]
            snakes.append((aux,'L'))
        if 'R' in actions:
            aux = [[headCol+1,headRow]]+ self.snake[:-1]
            snakes.append((aux,'R'))
        if 'D' in actions:
            aux = [[headCol,headRow+1]]+ self.snake[:-1]
            snakes.append((aux,'D'))
        if 'U' in actions:
            aux = [[headCol,headRow-1]]+ self.snake[:-1]
            snakes.append((aux,'U'))
        return snakes

            
    def search(self,path,actualDepth):
        if actualDepth == self.depth:
            self.paths.append(path)
        else:
            for s,a in self.neighbours(self.validActions()):
                self.snake = s
                self.search(path+a,actualDepth+1)
            
    def startSearch(self):
        self.search("",0)

        
class SnakeError(Exception): pass

