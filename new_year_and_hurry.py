n, k = map(int, input().split())
time_left = 240 - k
problems_solved = 0
problem_number = 1

while problem_number <= n and time_left >= problem_number * 5:
    time_left -= problem_number * 5
    problems_solved += 1
    problem_number += 1

print(problems_solved)
