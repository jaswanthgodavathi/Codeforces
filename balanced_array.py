import random



def construct_array(n):
    if n%4 == 0:
        return "NO"
    even = list(range(2,n+1,2))
    odd = list(range(1,n+1,2))
    random.shuffle(even)
    random.shuffle(odd)

    arr = even + odd
    return "YES\n" + ''.join(map(str,arr))

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(construct_array(n))

if __name__ == '__main__':
    main()

