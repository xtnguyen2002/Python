import math
a = 1
b = 5.86
c = 8.5408
discriminant = b**2 - 4*a*c

if discriminant > 0:
    r1 = (((-b)+math.sqrt(discriminant))/(2*a))
    r2 = (((-b)-math.sqrt(discriminant))/(2*a))
    print('The Quadratic Function has 2 roots: %f and %f' %(r1,r2))
elif discriminant == 0:
    r = (-b) / (2*a)
    print('The Quadratic Function have one root: %f' %(r))
else:
    print('The Quadratic Function have complex roots!')