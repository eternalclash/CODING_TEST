#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    //수포자들의 찍는 방식 저장한 배열
    vector<vector<int>> persons = {{1,2,3,4,5},{2,1,2,3,2,4,2,5},{3,3,1,1,2,2,4,4,5,5}};
    // vector<int> count= {0}; //각 사람마다 맞은 갯수 저장하기 위한 배열
    
    //각 사람마다 맞은 갯수 저장하기 위한 변수
    int cnt0=0;
    int cnt1=0;
    int cnt2=0;
    
    for(int i=0;i<answers.size();i++)
    {
        // if(answers[i] == persons[0][i%persons[0].size()]) count[0]++;
        // if(answers[i] == persons[1][i%persons[1].size()]) count[1]++;
        // if(answers[i] == persons[2][i%persons[2].size()]) count[2]++;
        if(answers[i] == persons[0][i%persons[0].size()]) cnt0++;
        if(answers[i] == persons[1][i%persons[1].size()]) cnt1++;
        if(answers[i] == persons[2][i%persons[2].size()]) cnt2++;
    }
    
    // int maxcnt = max(count[0],count[1]);
    // maxcnt = max(maxcnt,count[2]);
    
    int maxcnt = max(cnt0,cnt1);
    maxcnt = max(maxcnt,cnt2);
    
    if(maxcnt==cnt0) answer.push_back(1);
    if(maxcnt==cnt1) answer.push_back(2);
    if(maxcnt==cnt2) answer.push_back(3);
    
    
    return answer;
}