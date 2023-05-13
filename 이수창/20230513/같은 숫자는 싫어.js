function solution(arr)
{
    var answer = [];
   
    for(let i=0 ;i<arr.length;i++)
        {   if(arr[i]==arr[i-1])
               continue;
            else
                answer.push(arr[i])
        }
    
    return answer;
}

//같은 숫자면 넘기고 다른 숫자면 답에 넣는다