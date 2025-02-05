from itertools import combinations

N, S = map(int, input().split())

numbers = list(map(int, input().split()))

cnt=0

for i in range(1, N + 1):
    for j in combinations(numbers, i):
        if sum(j) == S:
            cnt+=1

print(cnt)