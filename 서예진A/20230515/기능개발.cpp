#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    queue <int> q; // 각 progress 작업일수 저장할 queue
    
    /*100 - progresses 요소 /speeds 가 나누어 떨어지면 그대로 일수적용
     나누어 떨어지지 않는 경우 작업일 1일 늘어남(+1) => 값들 큐에 저장*/
    for(int i=0;i<progresses.size();i++){
        if(((100-progresses[i])%speeds[i])==0) 
            q.push((100-progresses[i])/speeds[i]);
        else q.push((100-progresses[i])/speeds[i] +1);
    }
    
    
    int cur_day = q.front(); //queue 첫번째 원소 기준 일로 지정
    int cnt = 1;
    q.pop();
    
    while(!q.empty()){
        int day = q.front(); //순차적으로 queue 내용물 뽑기
        q.pop();
        
        if(cur_day>=day) //이전 기능이 완성된 상태에서 다음기능 완성된 경우X
        {
            cnt++;
        }
        else{
            answer.push_back(cnt);
            cnt = 1; //초기화
            cur_day = day; // 기준 일 변경
        }
    }
    
    answer.push_back(cnt);
     
    
    return answer;
}