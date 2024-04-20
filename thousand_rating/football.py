n = int(input())
goals = {}
for i in range(n):
    team = input()
    goals[team] = goals.get(team,0) + 1 

winning_team =  max(goals, key = goals.get)
print(winning_team)