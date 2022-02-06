import math

xp1 = int(input("Enter first point x:"))
yp1 = int(input("Enter first point y:"))
xp2 = int(input("Enter second point x:"))
yp2 = int(input("Enter second point y:"))

distance = math.sqrt( (xp2 - xp1)**2 + (yp2 -yp1)**2 )

print(distance)