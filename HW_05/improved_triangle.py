# -*- coding: utf-8 -*-
"""
Created on Fri Oct 04 17:48:00 2024

The primary goal of this file is to demonstrate a simple python program to classify triangles.

@author: Dimpal Lad
"""

MAX_SIDE_LENGTH = 200

def classify_triangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    Returns:
        'Equilateral' if all sides are equal.
        'Isosceles' if exactly one pair of sides are equal.
        'Scalene' if no pairs are equal.
        'NotATriangle' if the sides do not form a valid triangle.
        'InvalidInput' if any side length is not a positive integer or exceeds the valid range.
        'Right' if the triangle is a right triangle.
    """

    # Validate inputs
    if not all(isinstance(side, int) and 0 < side <= MAX_SIDE_LENGTH for side in (a, b, c)):
        return 'InvalidInput'

    # Check for triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Classify the triangle
    if a == b == c:
        return 'Equilateral' 
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 'Right'
    if a == b or b == c or a == c:
        return 'Isosceles'

    return 'Scalene'  # If none of the above, it's a scalene triangle
