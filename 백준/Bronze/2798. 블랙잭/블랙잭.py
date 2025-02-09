from itertools import combinations

N, M = map(int, input().split())

cards = list(map(int, input().split()))

max_sum=0

for comb in combinations(cards, 3):
    if sum(comb) <= M:
        max_sum = max(max_sum, sum(comb))

print(max_sum)