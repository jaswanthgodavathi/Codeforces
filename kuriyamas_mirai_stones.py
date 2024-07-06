a = int(input())
lst = list(map(int, input().split()))

prefix_sum = [0] * (a + 1)
for i in range(1, a + 1):
    prefix_sum[i] = prefix_sum[i - 1] + lst[i - 1]

sorta = sorted(lst)

for i in range(int(input())):
    types, l, r = map(int, input().split())
    if types == 1:
        suma = prefix_sum[r] - prefix_sum[l - 1]
        print(suma)
    elif types == 2:
        suma = sum(sorta[l - 1:r])
        print(suma)
