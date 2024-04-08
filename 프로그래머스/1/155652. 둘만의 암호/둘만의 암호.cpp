#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    string English= "abcdefghijklmnopqrstuvwxyz";
    for(int i=0; i<skip.length(); i++){
        English.erase(find(English.begin(), English.end(), skip[i]));
    };
    for(int i=0; i<s.length(); i++){
        int tmp = English.find(s[i])+index;
        if(tmp >= English.length()) tmp %= English.length();
        answer+=English[tmp];
    }
    return answer;
}