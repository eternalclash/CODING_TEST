#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    /*
    번호 순대로 정렬 -> 중복 제거
    N/2마리 가져가야하므로 answer이 N/2보단 크면 안됨
    */
    
    int answer = 0;
    int nums_size = nums.size(); //원래 배열 사이즈
    
    sort(nums.begin(),nums.end()); // 정렬
    
    nums.erase(unique(nums.begin(),nums.end()),nums.end()); // 중복제거
    
    int num=nums.size(); //중복 제거한 배열 사이즈
    
    
    if(num>nums_size/2)
        answer=nums_size/2;
    else answer=num;
    //but, 중복 제거한 배열 사이즈 값이 N/2마리보다 큰 경우 N/2마리가 answer값
    
    return answer;
}