N=int(input())
xy=[list(map(int,input().split(' ')))for _ in range(N)]

xy.sort()

for x,y in xy:
    print(x,y)