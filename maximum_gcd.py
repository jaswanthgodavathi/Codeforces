t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Input integer n
    if n % 2 == 0:
        print(n // 2)  # Output n/2 for even n
    else:
        print((n - 1) // 2)  # Output (n-1)/2 for odd n
