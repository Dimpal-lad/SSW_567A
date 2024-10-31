# -*- coding: utf-8 -*-
"""
Updated Oct 04, 2024
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Dimpal Lad
"""

import unittest

from improved_triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTriangle(self): 
        self.assertEqual(classify_triangle(5,5,8),'Isosceles','5,5,8 should be isosceles')
    
    def testScaleneTriangle(self): 
        self.assertEqual(classify_triangle(7,8,9),'Scalene','7,8,9 should be scalene')

    def testInvalidInputNegative(self): 
        self.assertEqual(classify_triangle(-1,4,5),'InvalidInput','Negative side lengths')

    def testInvalidInputZero(self): 
        self.assertEqual(classify_triangle(0,4,5),'InvalidInput','Side length of 0')

    def testNotATriangle(self): 
        self.assertEqual(classify_triangle(1,2,100),'NotATriangle','1,2,100 should not form a triangle')

    def testLargeSides(self): 
        self.assertEqual(classify_triangle(201,200,199),'InvalidInput','Sides larger than 200')

    def testInvalidInputNonInteger(self): 
        self.assertEqual(classify_triangle(3.5, 4, 5), 'InvalidInput', 'Non-integer side lengths')

    def testInvalidInputString(self): 
        self.assertEqual(classify_triangle("3", "4", "5"), 'InvalidInput', 'String inputs should return InvalidInput')

    def testDegenerateTriangle(self): 
        self.assertEqual(classify_triangle(1, 1, 2), 'NotATriangle', '1,1,2 forms a degenerate triangle and should return NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()