# Create a single class called Account. Upon initialization, it should receive an owner (str) and a starting amount
# (int, optional, 0 by default). It should also have an attribute called _transactions (empty list). Create the following methods:
#   • handle_transaction(transaction_amount)
#       o If the balance becomes less than zero, raise ValueError with the message "sorry cannot go in debt!" and break the transaction.
#       o Otherwise, complete it, save it, and return a message "New balance: {account_balance}"
#   • add_transaction(amount)
#       o if the amount is not an integer, raise ValueError with the message "please use int for amount".
#       o Otherwise, check what the balance will be with the new transaction
#           ▪ If the balance becomes less than zero, raise ValueError with the message "sorry cannot go in debt!" and break the transaction.
#           ▪ Otherwise, complete it and return a message "New balance: {account_balance}"
#   • balance() - a property that returns the sum between the amount and all the transactions
# Implement the correct magic methods so the code in the example below works properly:
#   • When you print an account instance, the output should be in the format "Account of {owner} with starting amount: {amount}".
#   • When you print a representational string of an account instance, the output should be in the format "Account({owner}, {amount})".
#   • When you access the length of an account instance, you should receive the total number of transactions made.
#   • You should iterate over an account instance and receive each transaction as a result.
#   • You should be able to reverse the order of transactions by reversing an account instance.
#   • You should be able to compare (>, <, >=, <=, ==, !=) two account instances by their balance amount.
#   • When you concatenate two accounts, you should return a new account with a name-string in the format
#       "{first_owner}&{second_owner}" and the starting amount - the sum between their two.
#       Both their transactions should be added to the new account.
from typing import Optional


class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        self.balance = amount

    def handle_transaction(self, transaction_amount: int) -> Optional[str]:
        if self.balance + transaction_amount >= 0:
            self.balance += transaction_amount
            self._transactions.append(transaction_amount)
            return f"New balance: {self.balance}"
        raise ValueError("sorry cannot go in debt!")

    def add_transaction(self, amount: Optional[int]) -> None:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self.handle_transaction(amount)

    def balance(self) -> int:
        return self.balance

    def __str__(self) -> str:
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.amount})"

    def __len__(self) -> int:
        return len(self._transactions)

    def __iter__(self) -> iter:
        return iter(self._transactions)

    def __gt__(self, other) -> bool:
        return self.balance > other.balance

    def __lt__(self, other) -> bool:
        return self.balance < other.balance

    def __ge__(self, other) -> bool:
        return self.balance >= other.balance

    def __le__(self, other) -> bool:
        return self.balance <= other.balance

    def __eq__(self, other) -> bool:
        return self.balance == other.balance

    def __ne__(self, other) -> bool:
        return self.balance != other.balance

    def __add__(self, other: "Account") -> "Account":
        new_acc = Account(f"{self.owner}&{other.owner}", sum([self.amount, other.amount]))
        new_acc._transactions = self._transactions + other._transactions
        return new_acc

    def __getitem__(self, item: int) -> int:
        return self._transactions[item]


# 100/100
# test
acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
# output
# Account of bob with starting amount: 10
# Account(bob, 10)
# 40
# 3
# 20
# -20
# 30
# -20
# [30, -20, 20]
# False
# False
# True
# True
# False
# True
# Account of bob&john with starting amount: 10
# [20, -20, 30, 10, 60]
