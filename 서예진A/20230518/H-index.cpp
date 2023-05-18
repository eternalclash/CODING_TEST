#include <vector>
#include <algorithm>
using namespace std;


int solution(vector<int> citations) {
    
    int answer = 0;
    
    sort(citations.begin(), citations.end(), greater<>()); //내림차순 정렬
    

    for(int i=0; i<citations.size(); i++){
        if(citations[i] >= i+1){
            answer = i+1;
        }  
    }

    return answer;
}

// #include <string>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int solution(vector<int> citations) {
//     int answer = 0;
//     int size = citations.size();
//     int max = 0;
    
//     // 인용횟수 가장 큰 값 구하기 
//     for(int i=0;i<size;i++){
//         max = max < citations[i] ? citations[i] : max;
//     }
        
//     int cnt = 0; //h번 이상 인용된 논문의 갯수 count
    
//     //가장 많이 인용된 횟수 -1 해가면서 그 이상 인용된 논문 수보다 그 횟수가 작아지는 경우 찾아내기
//     for(int i=max; i>-1; i--)
//     {
//         for(int j=0;j<size;j++)
//         {
//             if(citations[j]>=i) cnt++;
//         }
        
//         if(cnt>=i) 
//         {
//             answer = i;
//             break;
//         }
//     }
    
//     return answer;
// }