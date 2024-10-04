# -*- coding: utf-8 -*-
"""
Created on Fri Oct 04 17:48:00 2024

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Dimpal Lad
"""
def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    Returns:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, return 'Right'
    """

    # Validate inputs are integers and within the valid range
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    
    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # Check for triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Check for equilateral triangle
    if a == b == c:
        return 'Equilateral'
    
    # Check for right triangle (Pythagorean theorem)
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 'Right'
    
    # Check for isosceles triangle
    if a == b or b == c or a == c:
        return 'Isosceles'
    
    # If none of the above, it's a scalene triangle
    return 'Scalene'