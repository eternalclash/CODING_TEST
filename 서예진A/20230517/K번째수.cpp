#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(int a=0;a<commands.size();a++){
        int i=commands[a][0];
        int j=commands[a][1];
        int k=commands[a][2];
        
        vector<int> arr; //자른 배열 저장 vector
        
        for(int l=i-1;l<j;l++){ //i~j번째까지 배열 자르기
            arr.push_back(array[l]);
        }
        
        sort(arr.begin(),arr.end()); //arr 정렬
        
        answer.push_back(arr[k-1]); //연산 적용 시 나온 결과 배열에 넣기
        
    }
    return answer;
}