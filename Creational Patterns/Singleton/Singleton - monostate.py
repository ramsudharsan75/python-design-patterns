# clumsy approach


class CEO:
    __shared_state = {"name": "Steve", "age": 29}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"


if __name__ == "__main__":
    c1 = CEO()
    c2 = CEO()
    print(c1 == c2)

    c2.age = 55
    c2.new_var = 12345
    # since the dictionary is refering to __shared_state, changing any attribute will be reflected across
    # all the instances.
    print(c1)
    print(c2)
    print(c1.new_var)

########################################################################


class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self) -> None:
        self.name = ""
        self.money_managed = 0

    def __str__(self) -> str:
        return f"{self.name} manages ${self.money_managed}"


cfo1 = CFO()
cfo1.name = "Sheryl"
cfo1.money_managed = 1
print(cfo1)

cfo2 = CFO()
cfo2.name = "Ruth"
cfo2.money_managed = 10

print(cfo2)
print(cfo1)
