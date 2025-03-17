T = int(input())

for _ in range(T):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*N for _ in range(2)]

    # li 중 하나를 뜯으면 위 아래 옆 스티커는 못씀
    # dp[i][n] : n열에서 i 행 스티커 제거했을 때 최대 가치

    # 스티커 길이가 1일때
    dp[0][0] = li[0][0]
    dp[1][0] = li[1][0]

    # 스티커 길이가 2일때
    if N>1:
        dp[0][1] = li[1][0] + li[0][1] # 대각선
        dp[1][1] = li[0][0] + li[1][1] # 대각선

    # 스티커 길이가 3이상 일때
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + li[0][i] # 이전 값 최대와 현재
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + li[1][i] # 이전 값 최대와 현재

    print(max(dp[0][N-1], dp[1][N-1])) # 마지막 열에서 최대