function calculateChange(payment, cost) {
  // 여기에 코드를 작성하세요
  let change = payment - cost; // 거스름돈 총액

  const fiftyCount = (change - (change % 50000)) / 50000;
  change = change - 50000 * fiftyCount;

  const tenCount = (change - (change % 10000)) / 10000;
  change = change - 10000 * tenCount;

  const fiveCount = (change - (change % 5000)) / 5000;
  change = change - 5000 * fiveCount;

  const oneCount = (change - (change % 1000)) / 1000;
  change = change - 1000 * oneCount;

  console.log(`50000원 지폐: ${fiftyCount}장`);
  console.log(`10000원 지폐: ${tenCount}장`);
  console.log(`5000원 지폐: ${fiveCount}장`);
  console.log(`1000원 지폐: ${oneCount}장`);
}

// 테스트 코드
calculateChange(100000, 33000);
console.log('');
calculateChange(500000, 378000);