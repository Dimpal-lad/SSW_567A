def classify_triangle(a, b, c):
    # Check if the sides of triangle
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return "Not a valid triangle"
    
    # Determine the type of triangle based on the sides
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    
    # Check for a right triangle
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        return f"{triangle_type} and Right"
    else:
        return triangle_type
    
# input for the triangle
a = 2
b = 5
c = 7
    
result = classify_triangle(a, b, c)
print(f"The triangle is: {result}")