from itertools import permutations

N=int(input())

Nlist=[i for i in range(1,N+1)]

cnt=0

for i in permutations(Nlist,2):
    if i[0]!=i[1]:
        cnt+=1

print(cnt)
