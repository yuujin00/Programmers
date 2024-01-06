#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    int round=0, zero=0;
    
    while(s!="1"){
        string tmp="";
        int num;
        round++;
        
        for(int i=0; i<s.size(); i++){
            if(s[i]=='0') zero++;
            else tmp+="1";
        }
        
        num=tmp.size();
        s="";
        
        while(num > 0)
        {
            s += to_string(num % 2);
            num /= 2;
        }
            
    }
    
    answer.push_back(round);
    answer.push_back(zero);
    
    return answer;
}