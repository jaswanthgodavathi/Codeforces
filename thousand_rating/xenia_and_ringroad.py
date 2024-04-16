n, m = map(int, input().split())

loc = 1
ans = 0
now = list(map(int,input().split()))
for i in range(m):
    #now = int(input().strip())  # Remove newline character before conversion
    if now[i] >= loc:
        ans += now[i] - loc
    else:
        ans += n - (loc - now[i])
    loc = now[i]

print(ans)
