"""High level modules should not depend on low level concrete modules but should depend on intefaces/abstractions."""


from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name) -> None:
        self.name = name


class OldRelationships:  # low-level module
    def __init__(self) -> None:
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


class OldResearch:  # high level module
    def __init__(self, relationships):
        relations = relationships.relations

        for r in relations:
            # Here the high level module is dependent on internals of a low level concrete module - wrong
            # Instead research must depend on a high level interface which is inherited by Relationship
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"John has a child called {r[2].name}.")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = OldRelationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

research = OldResearch(relationships)

# Solution


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        raise NotImplementedError


class Relationships(RelationshipBrowser):  # low-level module
    def __init__(self) -> None:
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # high level module
    def __init__(
        self, browser, name
    ) -> None:  # uses browser which is an interface (high level)
        for p in browser.find_all_children_of(name):
            print(f"{name} has a child called {p}.")


relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

research = Research(relationships, parent.name)
