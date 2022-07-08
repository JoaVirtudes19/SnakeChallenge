#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:49:10 2022

@author: jjvircas
"""

import unittest

from main import *

class TestUtils(unittest.TestCase):
    def test_acceptance(self):
        self.assertEqual(testSnake(BOARD1,SNAKE1,DEPTH1), 7)
        self.assertEqual(testSnake(BOARD2,SNAKE2,DEPTH2), 1)
        self.assertEqual(testSnake(BOARD3,SNAKE3,DEPTH3), 81)
        
        
if __name__ == '__main__':
    unittest.main()