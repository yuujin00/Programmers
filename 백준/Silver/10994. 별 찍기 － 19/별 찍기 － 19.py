N=int(input())
shape = [[' ' for _ in range(4*N-3)]for _ in range(4*N-3)]

def star(n,x,y):
    if n==1 :
      shape[x][y]='*'
      return 
    
    tmp=4*n - 3

    for i in range(tmp):
      shape[x][y+i]='*' # 좌
      shape[x+i][y]='*' # 상
      shape[x+tmp-1][y+i]='*' # 우
      shape[x+i][y+tmp-1]='*' # 하
    
    star(n-1,x+2,y+2)


star(N,0,0)
for s in shape :
   print(''.join(s)) 