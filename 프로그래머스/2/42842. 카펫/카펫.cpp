#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int w,h;
    // 넓이
    int sum = brown + yellow;
    
    for(int h=3; h <= sqrt(sum); h++){
        // 넓이는 높이 X 너비
        int w= sum/h;
        if((w-2)*(h-2)==yellow){
            answer.push_back(w);
            answer.push_back(h);
            return answer;
        }
    }
}