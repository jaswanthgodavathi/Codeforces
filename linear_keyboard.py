import sys
input = sys.stdin.read

data = input().split()

tt = int(data[0])
index = 1
results = []

for _ in range(tt):
    k = data[index]
    index += 1
    m = len(k)
    s = data[index]
    index += 1
    n = len(s)
    
    mp = {k[i]: i + 1 for i in range(m)}

    ans = 0
    for i in range(n - 1):
        ans += abs(mp[s[i]] - mp[s[i + 1]])

    results.append(ans)

for result in results:
    print(result)
