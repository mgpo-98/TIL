let m = require('./math.js'); //불러오기

console.log(m.add(1,2));

exports.add =add; //내보내다 왼쪽은 외부로 공개할 이름 오른쪽은 내부로 공개할 이름