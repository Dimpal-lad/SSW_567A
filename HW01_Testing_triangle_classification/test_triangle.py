import pytest
from Testing_triangle_classification import classify_triangle

def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles_not_right_triangle():
    assert classify_triangle(3, 3, 4) == "Isosceles and Right"

def test_isosceles_non_right_triangle():
    assert classify_triangle(3, 3, 5) == "Isosceles"

def test_scalene_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene and Right"

def test_scalene_non_right_triangle():
    assert classify_triangle(5, 6, 7) == "Scalene"

def test_not_a_triangle():
    assert classify_triangle(1, 2, 3) == "Not a valid triangle"
    assert classify_triangle(1, -1, 4) == "Not a valid triangle"

def test_isosceles_right_triangle():
    assert classify_triangle(1, 1, 2**0.5) == "Isosceles and Right"