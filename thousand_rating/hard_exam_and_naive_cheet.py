def last_digit_of_1378_n(n):
    base = 1378
    mod = 10
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        n //= 2
    return result

# Input
n = int(input())
# Output
print(last_digit_of_1378_n(n))
