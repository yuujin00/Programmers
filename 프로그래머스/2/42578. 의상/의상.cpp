#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    
    map<string, int> M;
    for(int i=0; i<clothes.size(); i++) M[clothes[i][1]]++;
    
    for(auto iter=M.begin(); iter!=M.end(); iter++) answer *= iter-> second+1;
    
    return answer-1;
}