from itertools import combinations

heights = [int(input()) for _ in range(9)]

for h in combinations(heights, 7):
    if sum(h) == 100:
        for i in sorted(h):
            print(i)
        break