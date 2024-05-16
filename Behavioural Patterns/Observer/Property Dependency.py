from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class PropertyObservable:
    def __init__(self) -> None:
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age: int = 0) -> None:
        super().__init__()
        self._age = age

    @property
    def can_vote(self) -> bool:
        return self._age >= 18

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if self._age == value:
            return

        old_can_vote = self.can_vote
        self._age = value
        self.property_changed("age", value)

        if old_can_vote != self.can_vote:
            self.property_changed("can_vote", self.can_vote)


class TrafficAuthority:
    def __init__(self, person) -> None:
        self.person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name: str, value: Any) -> None:
        if name == "age":
            if value < 16:
                print("Sorry, you still cannot drive")
            else:
                print("Okay, you can drive now")
                self.person.property_changed.remove(self.person_changed)


if __name__ == "__main__":

    def person_changed(name: str, value: Any) -> None:
        if name == "can_vote":
            print(f"Voting ability changed to {value}")

    person = Person()
    person.property_changed.append(person_changed)

    for age in range(16, 21):
        print(f"Setting age to {age}")
        person.age = age
