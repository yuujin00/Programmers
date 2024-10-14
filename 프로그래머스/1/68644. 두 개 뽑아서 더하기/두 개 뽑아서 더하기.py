from itertools import combinations

def solution(numbers):
    answer = set()
    
    for number in combinations(numbers,2):
        answer.add(sum(number))
        
    return sorted(answer)