import sys
input = sys.stdin.readline
from itertools import permutations

n=int(input())
k=int(input())
KARD=[]
answer=set()

for i in range(n):
    KARD.append(int(input()))

for i in permutations(KARD,k):
    tmp=''
    for j in i :
        tmp+=str(j)
    answer.add(tmp)

print(len(answer))