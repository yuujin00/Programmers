import sys
input = sys.stdin.readline

N,K=map(int,input().split())
rank=[]

for _ in range(N) :
    tmp=[]
    tmp=list(map(int,input().split()))
    rank.append(tmp)

rank=sorted(rank,key=lambda x: (-x[1],-x[2],-x[3]))

idx=0

for i in range(N):
    if rank[i][0]==K :
        idx=i

for i in range(N):
    if rank[idx][1:]==rank[i][1:]:
        print(i+1)
        break
        