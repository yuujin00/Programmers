def solution(a, b, n):
    answer = 0
    
    while n>=a:
        tmp=n%a
        answer+=(n//a)*b
        n=(n//a)*b+tmp
    return answer