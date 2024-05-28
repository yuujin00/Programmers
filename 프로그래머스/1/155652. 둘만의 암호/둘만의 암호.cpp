#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    string E="abcdefghijklmnopqrstuvwxyz";
    
    for(int i=0; i<skip.size(); i++){
        E.erase(find(E.begin(),E.end(),skip[i]));
    }
    
    for(int i=0; i<s.size(); i++){
        int tmp=E.find(s[i])+index;
        if(tmp >=E.size()) tmp %= E.size();
        answer+=E[tmp];
    }
    return answer;
}