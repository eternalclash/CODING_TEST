function solution(n, lost, reserve) {
    let clothes = Array.from({length:n},()=>1)
    //clothes=[1,1,1,1,1]
    var answer = 0;
    for(let i=0;i<clothes.length;i++)
    {
        if(lost.filter((a)=>{return(a-1)==i}).length)
         clothes[i]--   //1번쟤 요소의 개수를 1 감소 clothes=[1,0,1,0,1]
        if(reserve.filter((a)=>{return(a-1)==i}).length)
         clothes[i]++  //clothes[2,0,2,0,2]
    }
    console.log(clothes)
    for(let j=0;j<clothes.length;j++)
    {  

        if(clothes[j]==0&&clothes[j-1]>1)
        {
            clothes[j]++
            clothes[j-1]--
            continue;
        }
        if(clothes[j]==0&&clothes[j+1]>1)
        {
            clothes[j]++
            clothes[j+1]--
            continue;
        }

    }
    answer=clothes.filter((a)=>{return(a>0)}).length

    return answer;
}