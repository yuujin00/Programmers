#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> S;
    string tmp;
    
    for(int i=0; i<s.length(); i++){
        if(s[i]!=' '){
            tmp +=s[i];
        }
        else{
            S.push_back(stoi(tmp));
            tmp.clear();
        }
    }
    S.push_back(stoi(tmp));

    sort(S.begin(),S.end());
    
    answer += to_string(S.front())+" "+ to_string(S.back());
    return answer;
}