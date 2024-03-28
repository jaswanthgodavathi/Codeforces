t = int(input())

for _ in range(t):
    a, b, c, n = map(int, input().split())
    total = a + b + c + n
    if total % 3 != 0 or total // 3 < a or total // 3 < b or total // 3 < c:
        print("NO")
    else:
        print("YES")
