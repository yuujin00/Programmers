#include <vector>
#include <set>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int N=nums.size()/2;
    
    set<int> A;
    for(int i=0; i<nums.size(); i++){
        A.insert(nums[i]);
    }
    if(A.size() <= N){
        answer= A.size();
    }
    else answer= N;
    
    return answer;
}