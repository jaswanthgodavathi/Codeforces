'''a = int(input())
b = input()
counta = 0
countd = 0
for i in range(len(b)):
    if b[i] == 'A':
        counta += 1 
    else:
        countd +=1 
if counta>countd:
    print("Anton")
elif countd>counta:
    print("Danik")
else:
    print("Friendship")'''
def min_potions_to_drink(n, m, d, death_eaters):
    min_potions = float('inf')
    min_death_eaters_removed = 0

    for i in range(m - d + 1):
        left = death_eaters[i]
        right = death_eaters[i + d - 1]

        potions = right - left - 1 - (d - 2)
        
        if potions < min_potions:
            min_potions = potions
            min_death_eaters_removed = 1
        elif potions == min_potions:
            min_death_eaters_removed += 1

    return min_potions, min_death_eaters_removed

# Read the number of test cases
t = int(input())

for _ in range(t):
    n, m, d = map(int, input().split())
    death_eaters = list(map(int, input().split()))

    min_potions, min_death_eaters_removed = min_potions_to_drink(n, m, d, death_eaters)
    print(min_potions, min_death_eaters_removed)
