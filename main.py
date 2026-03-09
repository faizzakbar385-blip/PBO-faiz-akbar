from BankAccount import BankAccount

def main():
    rekening1 = BankAccount("Faiz", 1000)

    print("Saldo awal:")
    rekening1.check_balance()

    print("\nDeposit 500")
    rekening1.deposit(500)

    rekening1.check_balance()

    print("\nWithdraw 300")
    rekening1.withdraw(300)

    rekening1.check_balance()


if __name__ == "__main__":
    main()

