from math import factorial

N, K = map(int, input().split())

# nCr = n! / (r! * (n-r)!)
print(factorial(N) // (factorial(K) * factorial(N - K)) % 10007)