function solution(answers) {
    let mathFirst = [1, 2, 3, 4, 5]
    let mathSecond = [2, 1, 2, 3, 2, 4, 2, 5]
    let mathThird = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    let obj = {mathFirst,mathSecond,mathThird}
    let answer = [0,0,0]
    for (let i = 0; i < answers.length; i++) {
        if (mathFirst[i%mathFirst.length]==answers[i]) {
            answer[0]++
        }
        if (mathSecond[i%mathSecond.length]==answers[i]) {
            answer[1]++
        }
        if (mathThird[i%mathThird.length]==answers[i]) {
            answer[2]++
        }
        
    }
    let max = 0;
    let idx = [];
    for (let i = 0; i < answer.length; i++) {
        if (answer[i]==max) {  
            idx.push(i+1)
        } 
        else if (answer[i]>max) {
            max = answer[i]
            idx = [i+1]
        }
    }
    return idx
}