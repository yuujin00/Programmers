N = int(input())

li=[]

li.append(0)
li.append(1)

for i in range(2,N+1):
    li.append(li[i-2]+ li[i-1])

print(li[N])