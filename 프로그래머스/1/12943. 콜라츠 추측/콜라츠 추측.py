def solution(num):
    i=0
    while i<500:
        if num==1 :
            break
        elif num%2==0 :
            num/=2
        else:
            num=num*3+1
        i+=1
        
    
    if i==500 : return -1
    return i