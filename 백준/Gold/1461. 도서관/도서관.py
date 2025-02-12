N, M =  map(int,input().split(' '))

book= list(map(int, input().split()))

p,n,answer=[],[],0

for b in book:
    if b>0 :
        p.append(b)
    else :
        n.append(abs(b))

p.sort(reverse=True)
n.sort(reverse=True)

for i in range(0,len(p),M):
    answer += p[i]*2
for i in range(0,len(n),M):
    answer += n[i]*2

if p and n:
    print(min(answer-p[0],answer-n[0]))
elif p:
    print(answer-p[0])
elif n:
    print(answer-n[0])
else :
    print(answer)