#include <iostream>
#include <string>
#include <stack>
using namespace std;

int solution(string s){ 
    int answer = 0;
    stack<char> S;
    for(int i=0; i<s.length(); i++){
        if(S.empty()|| S.top() != s[i]){
            S.push(s[i]);
        }
        else S.pop();
    }
    
    if(S.empty()) answer=1;
    return answer;
}