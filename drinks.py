n = int(input())
a = list(map(int, input().split()))
sum_of_elements = sum(a)
ans = sum_of_elements / n
print(f"{ans:.12f}")
