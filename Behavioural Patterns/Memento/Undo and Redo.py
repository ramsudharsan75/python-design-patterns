class Memento:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state


class BankAccount:
    def __init__(self, balance=0) -> None:
        self.balance = balance
        self.changes = [Memento(self.balance)]
        self.current = 0

    def deposit(self, amount):
        self.balance += amount
        m = Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        return m

    def restore(self, memento):
        if memento:
            self.balance = memento.get_state()
            self.changes.append(memento)
            self.current = len(self.changes) - 1

        self.balance = memento.get_state()

    def undo(self):
        if self.current > 0:
            self.current -= 1
            m = self.changes[self.current]
            self.balance = m.get_state()
            return m

        return None

    def redo(self):
        if self.current + 1 < len(self.changes):
            self.current += 1
            m = self.changes[self.current]
            self.balance = m.get_state()
            return m

        return None

    def __str__(self) -> str:
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    ba.undo()
    print(f"Undo 1: {ba}")
    ba.undo()
    print(f"Undo 2: {ba}")
    ba.redo()
    print(f"Redo 1: {ba}")
    ba.redo()
    print(f"Redo 2: {ba}")
