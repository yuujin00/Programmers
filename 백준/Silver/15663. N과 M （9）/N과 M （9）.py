from itertools import permutations

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

for per in sorted(set(permutations(numbers, M))):
    print(' '.join(map(str, per)))
