n, m = map(int, input().split())

# Find the next prime number after n
next_prime = n + 1
while True:
    is_prime = True
    for i in range(2, int(next_prime ** 0.5) + 1):
        if next_prime % i == 0:
            is_prime = False
            break
    if is_prime:
        break
    next_prime += 1

# Check if m is the next prime number after n
if next_prime == m:
    print("YES")
else:
    print("NO")
