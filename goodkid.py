t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    product = arr[0] + 1
    for i in range(1, n):
        product *= arr[i]
    print(product)
