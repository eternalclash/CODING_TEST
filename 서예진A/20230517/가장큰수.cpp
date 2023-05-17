#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/* 
조합하면서 크기 비교하기 6+10 vs 10+6 => 610 > 106 , 610선택하도록
문자 결합해보고 사전 순서가 더 뒤인것(더 큰 것이 순서가 더 뒤) => 앞에 있도록 sort
return true => 순서를 유지한다
*/
bool compare(string &a, string &b) {
    return a+b > b+a;
}
string solution(vector<int> numbers) {
    string answer = "";
    
    //문자열로 바꾸어 return 하기 위해 vector<string>으로 만들기
    vector<string> v;
    
    for(int i=0;i<numbers.size();i++){
        v.push_back(to_string(numbers[i]));
    }
    sort(v.begin(), v.end(), compare); //compare함수에 기반하여 sort
    
    //원소가 0일 경우를 고려해야함
    
    for(int i=0; i<numbers.size();i++){
        answer+=v[i];
    }
    if(answer[0]=='0')
        answer='0'; //ex) 000일 경우 그냥 0으로 처리할 수 있도록 함
    
    return answer;
}