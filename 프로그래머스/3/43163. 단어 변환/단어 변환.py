# 단어 변환

from collections import deque

def solution(begin, target, words):
    answer = 0
    V=[0]*len(words)
    
    q= deque()
    q.append([begin,0])
    
    while q :
        word, cnt = q.popleft()
        if word == target :
            answer = cnt
            break
        for i in range(len(words)):
            tmp_cnt=0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp_cnt+=1
                
                if tmp_cnt==1:
                    q.append([words[i],cnt+1])
                    V[i]=1
    
    return answer