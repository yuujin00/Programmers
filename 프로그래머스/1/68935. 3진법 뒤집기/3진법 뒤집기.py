def solution(n):
    answer = 0
    list=[]
    
    while n>0:
        list.append(n%3)
        n//=3
    
    for i in range(len(list)):
        answer+=list[len(list)-i-1]*(3**i)
    return answer