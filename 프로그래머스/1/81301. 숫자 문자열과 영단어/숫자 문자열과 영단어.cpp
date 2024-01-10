#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(string s) {
    string answer = "";

    map<string, int> m;
    m["zero"] = 0;
    m["one"] = 1;
    m["two"] = 2;
    m["three"] = 3;
    m["four"] = 4;
    m["five"] = 5;
    m["six"] = 6;
    m["seven"] = 7;
    m["eight"] = 8;
    m["nine"] = 9;
    
    string tmp = "";
    for(int i=0; i<s.length(); i++) {
        if(isdigit(s[i])) answer += s[i];
        else tmp += s[i];
        
        if(m.find(tmp) != m.end() ) {
            answer += to_string(m[tmp]);
            tmp = "";
        }
    }
    
    return stoi(answer);
}