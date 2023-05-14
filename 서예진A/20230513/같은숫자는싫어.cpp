#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    /*중복제거함수 erase사용하여 중복원소 제거함*/
    vector<int> answer;
    
    arr.erase(unique(arr.begin(),arr.end()),arr.end());
    /*unique함수 = 배열에서 중복되지 않는 원소들 앞에서부터 채워 나감*/
    
    answer = arr;

    return answer;
}