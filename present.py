n = int(input())
p_values = list(map(int, input().split()))

f = [0] * (n + 1)

for i in range(1, n + 1):
    f[p_values[i - 1]] = i

print(" ".join(map(str, f[1:])))
