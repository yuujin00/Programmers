#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    
    for(int i=0; i<s.length(); i++){
        if(i==0) answer.push_back(-1);
        else{
            int j;
            for(j=i-1; j>=0; j--){
                if(s[i]==s[j]) {
                    answer.push_back(i-j);
                    break;
                }
            }
            if(j<0) answer.push_back(-1);
        }
    }
    return answer;
}