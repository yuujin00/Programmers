N = int(input())

li = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = li[0][0]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + li[i][0]

for i in range(1, N):
    dp[i][i] = dp[i-1][i-1] + li[i][i]

for i in range(2, N):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + li[i][j]

print(max(dp[N-1]))