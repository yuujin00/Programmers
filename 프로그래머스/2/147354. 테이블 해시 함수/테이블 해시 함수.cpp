#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int index;

int compare(vector<int>a,vector<int>b){
    if(a[index]==b[index]) return a[0]>b[0];
    return a[index] < b[index];
}

int solution(vector<vector<int>> data, int col, int row_begin, int row_end) {
    int answer = 0;
    index = col-1;
    sort(data.begin(),data.end(), compare);
    
    vector<int> s;
    for(int i=row_begin-1; i<=row_end-1; i++){
        int num=0;
        for(int j=0; j<data[i].size(); j++){
            num+=data[i][j] % (i+1);
        }
        s.push_back(num);
    }
    
    answer=s[0];
    for(int i=1; i<s.size(); i++) answer = answer^s[i];
    return answer;
}