N = int(input())

answer=0
num=set()
num.add(0)

while len(num):
    if N in num:
        print(answer)
        break
    else :
        num_tmp=set()
        for i in num:
            if i+3 <= N:
                num_tmp.add(i+3)
            if i+5 <= N:
                num_tmp.add(i+5)
        num=num_tmp
        answer+=1

if len(num)==0:
    print(-1)