# This is a program to solve mathematical formulas
# Date : 20/02/2024
# Name : Rose Mugwe


# Cylinder
import math

pi = 3.142
r = float(input("Enter the radius"))
h = float(input("Enter the height"))
r_sq = (r ** 2)

vol = (pi * r_sq * h)
sa = (2(pi * r_sq) + (pi * (2*r) * h))
print("The volume of the cylinder is :" ,vol)
print("The surface area of the cylinder is :" ,sa)


# Sphere
import math

pi = 3.142
r = float(input("Enter the radius"))

vol = (4/3 * pi * (r ** 3))
sa = (4 * pi * (r ** 2))
print("The volume of the sphere is :" ,vol)
print("The surface area of the sphere is :" ,sa)