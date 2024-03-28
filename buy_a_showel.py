'''k, r = map(int, input().split())
value = 0
price_made = 0
flag = True

while flag:
    if price_made % 10 == 0 and price_made != 0 or price_made % 10 == r:
        break
    value += 1
    price_made += k

print(value)'''


def min_operations_to_increase_median(t, test_cases):
    def median_index(arr):
        n = len(arr)
        return n // 2 if n % 2 == 1 else (n // 2) - 1

    def operations_to_increase_median(n, arr):
        arr.sort()
        med_idx = median_index(arr)
        target_med = arr[med_idx] + 1
        ops = 0

        # Move towards both ends of the array from the current median index
        # Count the number of elements less than or equal to the target median
        for i in range(med_idx, -1, -1):
            if arr[i] >= target_med:
                ops += arr[i] - target_med + 1

        for i in range(med_idx + 1, n):
            if arr[i] <= target_med:
                ops += target_med - arr[i]

        return ops

    results = []
    for i in range(t):
        n, arr = test_cases[i]
        results.append(operations_to_increase_median(n, arr))

    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

# Get the minimum number of operations required for each test case
results = min_operations_to_increase_median(t, test_cases)

# Output the results
for result in results:
    print(result)
