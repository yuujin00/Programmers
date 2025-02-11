N,M = map(int,input().split(' '))

board = [list(input()) for _ in range(N)]
c = float('inf')

for i in range(N-7):
    for j in range(M-7):
        cnt=0
        cnt2=0
        for x in range(8):
            for y in range(8):
                if (x+y)%2==0:
                    if board[i+x][j+y] != 'W':
                        cnt+=1
                    if board[i+x][j+y] != 'B':
                        cnt2+=1
                else:
                    if board[i+x][j+y] != 'B':
                        cnt+=1
                    if board[i+x][j+y] != 'W':
                        cnt2+=1
        c = min(c,cnt,cnt2)

print(c)