# to find roots of quadratic eqn
import math
from fractions import Fraction as F

a, b, c = [
    int(a)
    for a in input(
        "Enter coefficients of x² x  and the number with a space in between. For ex:- x²+5x-10 = 0 ,then type 1 5 -10  "
    ).split()
]


# a = int(input("Enter the number with x2"))
# b = int(input("Enter the number with x"))
# c = int(input("Enter the number part"))
d = (b * b) - (4 * a * c)
if d < 0:
    d = -d
    print(d)
    x1 = (
        f"{F(-b/(2*a)).limit_denominator()}+{F(math.sqrt(d)/(2*a)).limit_denominator()}i"
        if (b % (2 * a) != 0)
        else -b / (2 * a) + math.sqrt(d) / (2 * a)
    )
    x2 = (
        f"{F(-b/(2*a)).limit_denominator()}-{F(math.sqrt(d)/(2*a)).limit_denominator()}i"
        if (b % (2 * a) != 0)
        else -b / (2 * a) - math.sqrt(d) / (2 * a)
    )
else:
    x1 = (
        (F((-b + math.sqrt(d)) / (2 * a)).limit_denominator())
        if b % (2 * a) != 0
        else (-b + math.sqrt(d)) / (2 * a)
    )
    x2 = (
        (F((-b - math.sqrt(d)) / (2 * a)).limit_denominator())
        if b % (2 * a) != 0
        else (-b - math.sqrt(d)) / (2 * a)
    )

print(x1, x2)
