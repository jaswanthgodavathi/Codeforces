import math

def has_odd_divisor(n):
    if n % 2 == 0:
        return "NO"
    sqrt_n = int(math.sqrt(n))
    return "YES" if sqrt_n * sqrt_n == n else "NO"

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    print(has_odd_divisor(n))
