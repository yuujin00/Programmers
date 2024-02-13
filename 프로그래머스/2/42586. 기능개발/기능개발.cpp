#include <string>
#include <vector>
#include <queue>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue <int> current;
    
    // 큐에 작업 넣기
    for(int i=0; i<progresses.size(); i++){
        current.push(progresses[i]);
    }
    
    // 작업이 사라지기 전까지
    while(!current.empty()){
        // 1. 작업진도 추가
        for(int i=0; i<current.size(); i++){
            int p= current.front();
            current.pop();
            current.push(p+speeds[i]);
        }

        int count=0;
    
        while(true){
            // 2. 앞의 작업 진도가 100이 되었을때
            if(current.size()>0 && current.front() >= 100) {
                current.pop();
                speeds.erase(speeds.begin());
                count++;
                continue;
            }
            
            // 2-1. 앞의 작업이 100이 아니면
            break;
        }
        
        // 3. count 값이 생기면 벡터에 추가
        if(count>0) answer.push_back(count);
    }
    
    return answer;
}