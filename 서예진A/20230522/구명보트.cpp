#include <string>
#include <vector>
#include <algorithm>

using namespace std;
/*
한 구명보트에 최대 2명밖에 탈 수 없다는 것이 keypoint
1. people vector sorting
2. 맨앞(최솟값) + 맨뒤(최댓값) < limit 여부 판단
2.1 limit보다 작을 경우 같이 탑승, 최솟값 index + 1 , 맨 뒤 pop()
2.2 limit보다 클 경우 같이 탑승X, 맨 뒤 pop()
*/

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    sort(people.begin(),people.end());
    int min_idx = 0;
    
    while(people.size() > min_idx)
    { //index가 people크기보다 커지는 경우 모두 보트에 탑승한 것
        int max = people.back(); //최댓값
        
        if(people[min_idx] + max <= limit) //2
        {
            answer ++; // 최소+최대 같은 구명보트 탑승
            min_idx ++; //다음 최솟값과 비교하기 위해 index ++
        }
        else answer++; // 최대 혼자만 구명보트 탑승
        
        people.pop_back(); //최댓값 pop하여 people 크기 줄임
    }
    
    return answer;
}