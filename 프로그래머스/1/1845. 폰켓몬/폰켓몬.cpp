#include <vector>
#include <set>
using namespace std;

// 배열을 생성
// 중복 제거 후 배열에 넣기 => 배열 사이즈가 num/2 작으면 사이즈
//                       => 크면 num/2

// 중복제거에서 고민 ... set함수 
// set 함수는 중복 제거가 되서 저장.
int solution(vector<int> nums)
{   
    int answer = 0;
    int N = nums.size()/2;
    
    set<int> A;
    for(int i=0; i<nums.size(); i++){
        A.insert(nums[i]);
    }
    if(A.size() <=N){
        answer = A.size();
    }
    else{
        answer = N;
    }
    return answer;
}