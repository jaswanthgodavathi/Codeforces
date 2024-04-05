def is_compostite(num):
    if num < 4:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i ==0 :
            return True
    return False
def find_composite_sum(n):
    for x in range(4,n-4):
        if is_compostite(x) and is_compostite(n-x):
            return x,n-x
n = int(input())
x,y = find_composite_sum(n)
print(x,y)