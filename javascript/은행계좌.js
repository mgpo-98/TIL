class BankAccount {
  constructor(name, money) {
    // 소유주
    this.holder = name;
    // 잔액
    this.balance = money;
  }

  // 입금하기
  deposit(money) {
    this.balance += money;
  }

  // 출금하기
  withdraw(money) {
    if (this.balance - money < 0) {
      console.log('Insufficient balance');
    } else {
      this.balance -= money;
    }
  }

  // 이체하기
  transfer(money, anotherAccount) {
    const account = anotherAccount;
    if (this.balance - money < 0) {
      console.log('Insufficient balance');
    } else {
      this.balance -= money;
      account.balance += money;
    }
  }
}