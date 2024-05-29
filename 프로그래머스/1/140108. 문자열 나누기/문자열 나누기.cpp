#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    int a=0,b=0;
    string s_1="";
    
    for(int i=0; i<s.size(); i++){
        
        if(s_1==""){
            s_1=to_string(s[i]);
            a++;
            continue;
        }
        
        if(s_1==to_string(s[i])) a++;
        else b++;
        
        if(a==b){
            answer++;
            a=0;b=0;
            s_1="";
        }
    }

    if(a!=0) answer+=1;
    
    return answer;
}