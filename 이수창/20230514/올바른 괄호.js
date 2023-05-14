function solution(s){
    let p = 0;
    let l = s.length;

    for (let a=0; a<l; a++) {
        if (s[a] === "(") {
            p = p + 1;
        } else {
            if (p < 1) return false;
            p = p - 1;
        }
    }

    return p > 0 ? false : true;
}

//괄호==스택 국룰
// 연산속도를 위해 배열 대신 더하기 뺴기 연산을 이용했다