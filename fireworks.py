import math

def max_fireworks(t, test_cases):
    result = []
    for i in range(t):
        a, b, m = test_cases[i]
        lcm = (a * b) // math.gcd(a, b)
        intervals = m // lcm
        total_fireworks = intervals * (a + b - 1)
        last_interval = (m % lcm) // a + (m % lcm) // b
        total_fireworks += max(0, min(a, b) - (m % lcm)) + 1
        result.append(total_fireworks)
    return result

t = int(input())
test_cases = []
for _ in range(t):
    a, b, m = map(int, input().split())
    test_cases.append((a, b, m))

results = max_fireworks(t, test_cases)
for res in results:
    print(res)