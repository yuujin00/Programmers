from collections import deque

def solution(n, wires):
    answer = n-2
    
    def bfs(start):
        visited = [0] * (n + 1)
        q = deque([start])
        visited[start] = 1
        cnt = 1    
        # print(start,visited) 
        
        while q:
            s = q.popleft()
            for i in graph[s]:
                if visited[i]==0 :
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        #print(start,visited,cnt)      
        return cnt

    # 연결리스트
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        answer = min(abs(bfs(a) - bfs(b)), answer)
        
        graph[a].append(b)
        graph[b].append(a)

    return answer