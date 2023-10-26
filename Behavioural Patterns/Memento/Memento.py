class Memento:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state


class BankAccount:
    def __init__(self, balance=0) -> None:
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento):
        self.balance = memento.get_state()

    def __str__(self) -> str:
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    # restore to m1
    ba.restore(m1)
    print(ba)

    # restore to m2
    ba.restore(m2)
    print(ba)
