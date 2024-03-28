a = int(input())
ans = 0
test_str = input()
res = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]
for i in range(len(res)):
    if (res[i].count('U') == res[i].count('D')) and (res[i].count('R') == res[i].count('L')):
        ans += 1 
print(ans)  