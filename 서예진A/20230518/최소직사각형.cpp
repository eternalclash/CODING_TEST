#include <string>
#include <vector>

using namespace std;

/*
첫번째 원소 원래 / reverse vs 다음원소 
원래 원소 vs 다음원소 => 결과 값1
reverse vs 다음원소 => 결과 값2
값1 vs 값 2 => 더 작은 넓이 가진 것 기준으로 다음 원소와 같은 과정 반복*/

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    
    int fit[2] ={sizes[0][0],sizes[0][1]}; //모든 명함 수납가능한 가장 작은 지갑 초기화
    
    for (int i=1; i<sizes.size(); i++)
    {
        int origin[2]={0}; //원래원소와 비교하여 큰 값 넣은 배열
        int reverse[2]={0}; //reverse원소와 비교하여 큰 값 넣은 배열
        
        origin[0] = fit[0] > sizes[i][0] ? fit[0] : sizes[i][0];
        origin[1] = fit[1] > sizes[i][1] ? fit[1] : sizes[i][1];
        
        reverse[0] = fit[1] > sizes[i][0] ? fit[1] : sizes[i][0];
        reverse[1] = fit[0] > sizes[i][1] ? fit[0] : sizes[i][1];
        
        
        // 넓이 비교, 더 작은 값을 가진 배열의 원소가 가장 작은 지갑 배열 원소 되도록 설정
        if(origin[0]*origin[1] < reverse[0]*reverse[1]) 
        {
            fit[0]=origin[0];
            fit[1]=origin[1];
        }
        else
        {
            fit[0]=reverse[0];
            fit[1]=reverse[1];
        }
    }
    
    answer=fit[0]*fit[1];
    
    return answer;
}