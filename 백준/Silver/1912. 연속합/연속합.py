N=int(input())

li = list(map(int, input().split()))

dp = []
dp.append(li[0])

for i in range(1, N):
    dp.append(max(dp[i-1]+li[i], li[i]))

print(max(dp))