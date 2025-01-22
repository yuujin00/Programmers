from itertools import permutations

N=int(input())
Nlist=[i for i in range(1,N+1)]


for i in list(permutations(Nlist,N)):
    print(' '.join(map(str,i)))