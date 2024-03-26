import sys

for line in sys.stdin:
    t = int(line)
    for _ in range(t):
        a, b = map(int, input().split())
        res = 1 + a // b
        for p in range(b, b + 101):
            if p == 1:
                continue
            div = 0
            cur = a
            while cur:
                cur //= p
                div += 1
            cnt = (p - b) + div
            res = min(res, cnt)
        print(res)
