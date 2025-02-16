A,B=map(int,input().split())

answer=0

while B>A:
    if B%2==0:
        B//=2
        answer+=1
    elif B%10==1:
        B//=10
        answer+=1
    else:
        break

if B==A:
    print(answer+1)

else:
    print(-1)   