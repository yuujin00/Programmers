#include <string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<char> S;
    
    for(int i=0; i<s.size(); i++){
        if(s[i]=='(') S.push(s[i]);
        else {
            if(!S.empty()) S.pop();
            else S.push(')');
        }
    }
    
    if(!S.empty()) return false;

    return answer;
}