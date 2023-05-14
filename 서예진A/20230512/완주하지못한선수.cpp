#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    sort(participant.begin(),participant.end()); //알파벳 순 정렬
    sort(completion.begin(),completion.end()); //알파벳 순 정렬

    int i=0;
    for(i; i<completion.size(); i++)
    {
        if(participant[i]!=completion[i]) //정렬된 배열끼리 비교했을 때 같은 위치에 없는 경우 완주자X
            break;
    }
    
    answer=participant[i];
        
    return answer;
}