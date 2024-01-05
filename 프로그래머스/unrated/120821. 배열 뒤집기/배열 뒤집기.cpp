#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    int end = num_list.size();
        
    for(int i=0; i<end; i++){
        answer.push_back(num_list[end-1-i]);
    }
    
    return answer;
}