"""Dont try to bloat an interface with unnecessary properties which are not common across all the implementations"""


from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        raise NotImplementedError(
            "Not supported!"
        )  # problem since an instance of this class can expect a fax but its not supported yet.


# Better approach
# make smaller interfaces


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class PhotoCopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass
