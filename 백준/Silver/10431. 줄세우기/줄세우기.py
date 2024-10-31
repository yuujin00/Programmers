import sys
input = sys.stdin.readline

n=int(input())

for _ in range(n):
    H=list(map(int,input().split()))
    total=0
    for i in range(1,len(H)-1):
        for j in range(i+1,len(H)):
            if H[i]>H[j]:
                H[i],H[j]=H[j],H[i]
                total+=1
    print(H[0],total)    