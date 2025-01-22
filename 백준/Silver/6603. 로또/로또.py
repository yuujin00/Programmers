from itertools import combinations

while True:
    n,*lotto=map(int,input().split(' '))

    if n==0:
        break

    for number in combinations(lotto,6):
        print(' '.join(map(str,number))) 
    print()