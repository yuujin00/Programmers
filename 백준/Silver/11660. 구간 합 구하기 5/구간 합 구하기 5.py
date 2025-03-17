import sys 
input = sys.stdin.readline

N,M = map(int,input().split())

li = [list(map(int,input().split()))for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        # 행 + 열 - 대각선 + 현재
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + li[i-1][j-1]


for _ in range(M):
    x1,y1,x2,y2= map(int,input().split())

    # x2,y2 합 - 행 - 열 + 대각선
    ans = dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1]
    print(ans)
