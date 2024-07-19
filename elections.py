t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    mx = max(a, b, c)
    tie = ((a == mx) + (b == mx) + (c == mx)) > 1
    
    u = tie if a == mx else (mx + 1 - a)
    v = tie if b == mx else (mx + 1 - b)
    w = tie if c == mx else (mx + 1 - c)
    
    print(u, v, w)
