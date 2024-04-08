#include <string>
#include <vector>
#include <map>

using namespace std;

map<string,int> wantMap;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    
    for(int i=0;i<want.size();i++)
    {
        wantMap.insert({want[i],number[i]});
    }
    
    for(int i=0; i<=discount.size()-10; i++){
        map<string,int> mart;
        
        for(int j=i; j<i+10; j++){
            mart[discount[j]]++;
        }
        
        if(mart==wantMap) answer++;
    }
    return answer;
}