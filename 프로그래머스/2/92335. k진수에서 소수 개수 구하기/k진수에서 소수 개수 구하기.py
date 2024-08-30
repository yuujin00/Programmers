import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = ''
    
    # n을 k진수로 변환
    while n > 0:
        n, r = divmod(n, k)
        num = str(r) + num
        
    # 0을 기준으로 분할
    num = num.split('0')
    
    # 소수 개수 세기
    for i in num:
        if len(i) > 0 and is_prime(int(i)):
            answer += 1
        
    return answer
