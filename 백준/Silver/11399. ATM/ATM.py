N=int(input())

P=list(map(int,input().split()))

P.sort()

answer=0

for i in range(N):
    answer+=sum(P[:i+1])

print(answer)