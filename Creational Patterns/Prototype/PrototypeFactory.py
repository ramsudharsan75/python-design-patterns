import copy


class Address:
    def __init__(self, street_address, city, country) -> None:
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Employee:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} works at {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr", "London", "UK"))
    aux_office_employee = Employee("", Address("123 West Dr", "London", "UK"))

    @staticmethod
    def __new_employee(proto, name):
        new_employee = copy.deepcopy(proto)
        new_employee.name = name
        return new_employee

    @staticmethod
    def new_main_office_employee(name):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name
        )

    @staticmethod
    def new_aux_office_employee(name):
        return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee, name)


jane = EmployeeFactory.new_main_office_employee("Jane")
john = EmployeeFactory.new_aux_office_employee("John")
print(jane)
print(john)
