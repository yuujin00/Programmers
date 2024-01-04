#include <string>
#include <vector>

using namespace std;

vector<int> solution(int money) {
    vector<int> answer;
    int i=0;
    while(money>=5500){
        money-=5500;
        i++;
    }
    answer.push_back(i);
    answer.push_back(money);
    return answer;
}