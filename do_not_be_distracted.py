t = int(input())
for i in range(t):
    n = int(input())
    str = input()
    mp = {chr(i): 0 for i in range(65, 123)}
    found = False
    for i in range(n):
        if i != 0:
            if str[i] != str[i - 1] and mp[str[i]] > 0:
                found = True
                print("NO")
                break
        mp[str[i]] += 1
    if not found:
        print("YES")
