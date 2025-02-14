# 빼기 기준으로 나누기
ex = input().split('-')
answer=0

# 어짜피 무조건 더하기기 때문에 더하기 기준으로 나누기
for i in ex[0].split('+'):
    answer+=int(i)

# 빼기
for i in ex[1:]:
    #print(i)
    for j in i.split('+'):
        #print(j)
        answer-=int(j)

print(answer)
#print(ex)