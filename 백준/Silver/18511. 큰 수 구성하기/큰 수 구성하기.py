from itertools import product

N , k = map(int, input().split())

number=list(map(int, input().split()))

result=[]

length= len(str(N))
# product 중복순열, repeat= 꼭 필요!
while True:
    for num in product(number, repeat=length):
        tmp = ''.join(map(str,num))
        if N >= int(tmp):
            result.append(tmp)

    if result : 
        print(max(result))
        break
    else :
        length-=1