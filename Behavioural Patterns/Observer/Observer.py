from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self) -> None:
        self.falls_ill(self.name, self.address)


def call_doctor(name: str, address: str) -> None:
    print(f"{name} needs a doctor at {address}")


if __name__ == "__main__":
    person = Person("Sherlock", "221B Baker St")
    person.falls_ill.append(lambda name, addr: print(f"{name} is ill"))
    person.falls_ill.append(call_doctor)
    person.catch_a_cold()
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()
