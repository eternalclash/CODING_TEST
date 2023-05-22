#include <string>
#include <vector>
#include <algorithm>

using namespace std;
/*
number의 길이-k => return 값의 길이
ex) 1924 => k=2, return 길이는 4-2 =2

<1. 첫번째 index부터 return값 길이번째까지 값 비교
=> 그 뒤에 적어도 최소한의 값들이 있어야하기 때문에, k+i만큼 비교>
192 중 가장 큰 수 찾아내기 => 9

<2. 비교한 값 중 가장 큰 값의 index 다음에서부터 다시 비교 >
9이후 에서 1개 더 선택 => 24에서 가장 큰 수 찾아내기 =>4

*/
string solution(string number, int k) {
    string answer = "";
    
    int answer_len = number.size() - k; //return 값의 길이
    int start_idx=0; //비교 시작 index
    
    for(int i=0;i<answer_len;i++){  //1
        char max = number[start_idx];
        int max_idx = start_idx;
        
        for(int j=start_idx; j<=k+i; j++){
            if(max < number[j]) //가장 큰 값 찾기
            {
                max = number[j];
                max_idx = j;
            }       
        }
        
        start_idx = max_idx + 1; // 가장 큰 값 이후의 idx부터 다시 비교
        answer += max;
    }
    
    
    return answer;
}