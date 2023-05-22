function permutation (arr,n) {
    if (n==1) return arr = arr.map(e=>[e])
    let result = []
    for (let i = 0; i < arr.length; i++) {
        let originalIdx = arr[i]
        let sliceArr = arr.slice(0,i).concat(arr.slice(i+1,))
        let permutationArr =  permutation(sliceArr,n-1)
        permutationArr= permutationArr.map(e=>[...e,originalIdx])
        result=[...result,...permutationArr]
    }
    return result
}

function findDecimal(n) {
    if (n < 2) return false
    if (n == 2) return true
    for (let i = 2; i < Math.sqrt(n)+1; i++) {
        if (n % i == 0) return false
    }
    return true
}

function solution(numbers) {
        var answer = 0; 
        numbers = numbers.split("").map(e=>Number(e))
        let checkArr = [] 
        for (let i = 1 ; i <numbers.length+1; i++) {
            checkArr.push(...permutation(numbers,i))
        } 
        checkArr = [...new Set(checkArr.map(e=>Number(e.join(""))))]
    
        for (x of checkArr) {
            if (findDecimal(x)) { 
                answer++
            }
        } 
        return answer;
}