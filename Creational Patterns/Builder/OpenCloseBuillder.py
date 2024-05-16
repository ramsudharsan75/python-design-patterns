class Person:
    def __init__(self) -> None:
        self.name = None
        self.address = None
        self.hobby = None


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    def build(self):
        return self.person


class PersonNameBuilder(PersonBuilder):
    def named(self, name):
        self.person.name = name
        return self


class PersonAddressBuilder(PersonNameBuilder):
    def lives_at(self, address):
        self.person.address = address
        return self


class PersonHobbyBuilder(PersonAddressBuilder):
    def enjoys(self, hobby):
        self.person.hobby = hobby
        return self


pb = PersonHobbyBuilder()
person = pb.named("Ram").lives_at("Whitefield").enjoys("Coding").build()

print(person.hobby)
