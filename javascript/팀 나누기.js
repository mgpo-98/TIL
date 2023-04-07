let groups = [
	['영준', '캡틴'], 
	['태순', '우재'],
	['재훈', '지웅'],
	['윤형', '동욱'],
	['규식', '소원'],
];

let teams = [
	[],
	[],
];

// 여기에 코드를 작성하세요
for(let i = 0; i < groups.length; i++) {
  for(let j = 0; j < groups[i].length; j++) {
    teams[j][i] = groups[i][j];
  }
}
// 테스트 코드
console.log(teams[0]);
console.log(teams[1]);







teams[0][0] = groups[0][0];
teams[1][0] = groups[0][1];
teams[0][1] = groups[1][0];
teams[1][1] = groups[1][1];
teams[0][2] = groups[2][0];
teams[1][2] = groups[2][1];
teams[0][3] = groups[3][0];
teams[1][3] = groups[3][1];
teams[0][4] = groups[4][0];
teams[1][4] = groups[4][1];