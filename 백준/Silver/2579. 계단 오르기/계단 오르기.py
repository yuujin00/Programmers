N=int(input())

li=[]

for _ in range(N):
    li.append(int(input()))

dp=[0]*N

# 초기값 설정
dp[0]=li[0]

if N>1:
    dp[1]=li[0]+li[1]
if N>2:
    dp[2]=max(li[0]+li[2],li[1]+li[2])

# 점화식
for i in range(3,N):
    dp[i]=max(dp[i-2]+li[i],dp[i-3]+li[i-1]+li[i])

print(dp[-1])