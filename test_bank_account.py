import unittest
from BankAccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc = BankAccount("Faiz", 1000)

    def test_deposit(self):
        self.acc.deposit(500)
        self.assertEqual(self.acc.balance, 1500)

    def test_withdraw(self):
        self.acc.withdraw(200)
        self.assertEqual(self.acc.balance, 800)

    def test_withdraw_gagal(self):
        result = self.acc.withdraw(2000)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

