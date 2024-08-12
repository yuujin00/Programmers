# 연속 부분 수열 합의 개수

def solution(elements):
    answer = set()
    elements = elements * 2 #[7,9,1,1,4,7,9,1,1,4]
    
    for i in range(len(elements)//2):
        for j in range(len(elements)//2):
            answer.add(sum(elements[j:j+i]))
            
    return len(answer)