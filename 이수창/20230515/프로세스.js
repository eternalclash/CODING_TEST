function solution(priorities, location) {
    var answer = 0;
    let print = 0
    while (true) {
        var first = priorities.shift()
        if (priorities.filter((prior) => prior > first).length > 0) {
            priorities.push(first)
        } 
        else {
            print ++
            if (location == 0) {
                return answer = print
            }
        }
    
        location --
       
        if (location === -1) {
            
            location = priorities.length - 1
        }
}