function solution(progresses, speeds) {
    
    progresses=progresses.map((e,idx)=>{
        return Math.ceil((100-e)/speeds[idx])
    })
    let answer= []
    let count = 1
    let max = progresses[0]
    for (let i = 1; i < progresses.length; i++) {
        if (max >= progresses[i]) {
            count++
        }
        else {
            answer.push(count)
            count = 1
            max = progresses[i]
        }
    }
    return [...answer,count]
}