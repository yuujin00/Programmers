N, M = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*M for _ in range(N)]
dp[0][0] = li[0][0]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + li[i][0]

for i in range(1, M):
    dp[0][i] = dp[0][i-1] + li[0][i]

for i in range(1, N):    
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + li[i][j]

print(dp[N-1][M-1])