#include <string>
#include <vector>

using namespace std;

string solution(string cipher, int code) {
    string answer = "";
    
    for(int i=1; i<=cipher.length()/code; i++){
        answer += cipher[code*i-1];
    }
    return answer;
}