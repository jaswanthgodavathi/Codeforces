t = int(input())

for i in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    
    total_weight = sum(candies)
    
    # If the total weight is odd, it's impossible to divide the candies fairly
    if total_weight % 2 != 0:
        print("NO")
    else:
        # Check if there are enough candies of each weight to divide them equally
        count_1 = candies.count(1)
        count_2 = candies.count(2)
        if count_1 % 2 == 0 or (count_1 > 0 and count_2 > 0):
            print("YES")
        else:
            print("NO")
