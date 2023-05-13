function solution(participant, completion) {
    var answer = '';
    participant.sort()
    completion.sort()
    let i=0;
    while(true)
    {
        if(participant[i]!=completion[i])
        {
           answer=participant[i]
           break;
        }
        i++
    }
    return answer;
}
// 사전순서로 completion과 participant 바꾼다음
// completion과 participant가 맞지 않으면 바로 해당 참가자 리턴