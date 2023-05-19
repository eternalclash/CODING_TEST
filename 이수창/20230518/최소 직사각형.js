function solution(sizes) {
    sizes=sizes.map(e=>e.sort((a,b)=>a-b))
    let xsizes = sizes.map(e=>e[0])
    let ysizes = sizes.map(e=>e[1])
    return Math.max(...xsizes) * Math.max(...ysizes)
}

//sort()메소드 생각하자 python이랑 다르다 헷갈리지 말자