function solution(name) {
    var answer = 0;
    let move = name.length - 1
    for (let i = 0; i < name.length; i++) {
        let count = Math.min(name[i].charCodeAt() - 'A'.charCodeAt(), 'Z'.charCodeAt() - name[i].charCodeAt()+1)
       
        answer += count
        let idx = i + 1
        while (idx < name.length && name[idx]=='A') {
            idx++
        }
        move= Math.min(move, i * 2 + name.length - idx )
        move = Math.min(move, (name.length-idx)*2 + i)
        
    }
    return answer + move
}