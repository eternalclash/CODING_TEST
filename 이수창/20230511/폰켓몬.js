function solution(nums) {
    var answer = 0;
    let arr= []
    for(let i=0;i<nums.length;i++)
    {
        if(!arr.includes(nums[i]))
        arr.push(nums[i])
    }
    answer =arr.length>nums.length/2 ? nums.length/2 : arr.length
    return answer;
}

// 1. 폰켓몬의 종류를 샌다.
// 2. 폰켓몬을 뽑는 수가 n/2이므로 뽑아서 나올 수 있는 최대 폰켓몬 종류는 n/2이다.
// 3. 삼항연산자를 통해 폰켓몬 종류 n/2보다 클 때는 n/2리턴 적으면 폰켓몬 전체 종류를 리턴한다.