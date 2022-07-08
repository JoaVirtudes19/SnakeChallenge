#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:29:55 2022

@author: jjvircas
"""


from utils import SnakeChallenge

BOARD1 = [4,3]
SNAKE1 = [[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[0,0]]
DEPTH1 = 3

BOARD2 = [2,3]
SNAKE2 = [[0,2],[0,1],[0,0],[1,0],[1,1],[1,2]]
DEPTH2 = 10

BOARD3 = [10,10]
SNAKE3 = [[5,5],[5,4],[4,4],[4,5]]
DEPTH3 = 4


def testSnake(board,snake,depth):
    print("\nTest")
    print("\t board: {}".format(board))
    print("\t snake: {}".format(snake))
    print("\t depth: {}".format(depth))
    result = numberOfAvailableDifferentPaths(board=board,snake=snake,depth=depth)
    print("Result: {}".format(result))
    return result
    

def numberOfAvailableDifferentPaths(board,snake,depth):
    challenge = SnakeChallenge(board, snake, depth)
    challenge.startSearch()
    return len(challenge.paths)

if __name__ == '__main__':
    
    # TEST 1
    print("\nTest 1")
    testSnake(BOARD1, SNAKE1, DEPTH1)

    
    # TEST 2
    print("\nTest 2")

    testSnake(BOARD2, SNAKE2, DEPTH2)

    
    # TEST 3
    print("\nTest 3")
    testSnake(BOARD3, SNAKE3, DEPTH3)
