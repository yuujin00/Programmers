# 디스크 컨트롤러

import heapq

def solution(jobs):
    answer = 0
    start,now =-1, 0
    job=0
    heap=[]
    
    while job < len(jobs):
        for clock,time in jobs:
            if start< clock <=now:
                heapq.heappush(heap,[time,clock])
        #print(heap)       
        
        if heap:
            time,clock = heapq.heappop(heap)
            #print(time,clock)
            start = now
            now += time
            answer += now-clock
            job+=1
            #print(start,now,answer,job)
        else : 
            now+=1
    
    return answer//len(jobs)