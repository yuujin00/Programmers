#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int H=0,W=0;
    
    for(int i=0; i<sizes.size(); i++){
        if(sizes[i][0]>sizes[i][1]){
            H=max(H,sizes[i][0]);
            W=max(W,sizes[i][1]);
        }
        else{
            H=max(H,sizes[i][1]);
            W=max(W,sizes[i][0]);
        }
    }
    answer=H*W;
    return answer;
}