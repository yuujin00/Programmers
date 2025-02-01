from itertools import combinations

N,K=map(int,input().split())

Nlist=[i for i in range(1,N+1)]

cnt=0

for i in combinations(Nlist,K):
    cnt+=1

print(cnt)