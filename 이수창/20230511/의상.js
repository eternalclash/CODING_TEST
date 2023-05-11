function solution(clothes) {
    var answer = 0;
    let obj = {};
    let k = 1;
    for (let i = 0 ; i < clothes.length ; i++)
        {
            if(obj[clothes[i][1]])
                {
                  obj[clothes[i][1]]++;   
                }
            else{
                obj[clothes[i][1]]=1;
            }
        }

    for (let key in obj)  //for in 문을 통해 가지고 있는 key값에 있는 항목의 개수들을 1씩더해서 구함(key값이 0일때도 생각해야 하므로)
        {
            k=k*(obj[key]+1);
        }
    answer= k-1;
    return answer;
}
//반복문을 돌려서 새로운 옷 종류이면 옷 종류를 obj라는 객체의 키값으로 등록함
//            새로운 옷 종류가 아니고  같은 옷 종류면 해당 옷종류의 key에 value를 1씩 더해줌 
//옷 종류가 존재한다고 해서 그 옷 종류의 옷을 입지 않을 수 있기 때문에 해당 옷 종류의 키값을 가진 객체 값에 각각 1을 더해줌
//아무런 옷을 안 입을 경우의 수도 있으므로 마지막으로 1을 빼주고 리턴