function solution(array, commands) {
    let answer = []
    for (command of commands) {
        const [start,last,num] = command
        answer.push(array.slice(start-1,last).sort((a,b)=>a-b)[num-1])
    }
    return answer
}