#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(string a, string b) {
    return a + b > b + a;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> temp;
    //string으로 바꾼후 벡터에 집어넣는다.
    for (auto num : numbers)
        temp.push_back(to_string(num));
    //더할때 오름차순으로 정렬한다.
    sort(temp.begin(), temp.end(), cmp);
    //처음 숫자가 0이라면 0을 반환
    if (temp.at(0) == "0")        return "0";
    //처음부터 끝까지 문자열 합치고 리턴
    for (auto num : temp)
        answer += num;
    return answer;
}