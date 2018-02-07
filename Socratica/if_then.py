# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides have the same lengths.
# Equilateral triangle: All sides are equal.

a = int(raw_input("The length of side a = "))
b = int(raw_input("The length of side b = "))
c = int(raw_input("The length of side c = "))

if a + b > c and a + c > b and b + c > a:
    if a != b and b != c and a != c:
        print("This is a Scalene triangle.")
    elif a == b and b == c:
        print("This is an Equilateral triangle.")
    else:
        print("This is an Isosceles triangle.")
else:
    print("The provided numbers don't form a triangle")
