from itertools import permutations

def  check(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0 :
            return False
            
    return True

def solution(numbers):
    answer = set()
    
    
    for i in range(1,len(numbers)+1):
        for pe in permutations(numbers,i):
            if check(int(''.join(pe))):
                answer.add(int(''.join(pe)))
    
    return len(answer)