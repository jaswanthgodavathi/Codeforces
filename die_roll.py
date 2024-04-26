from fractions import Fraction
a, b = map(int,input().split())
maxi = max(a,b)
rem = 7 - maxi
n,d = rem,6
frac = Fraction(n,d)
print(frac)
