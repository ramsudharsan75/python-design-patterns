class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, msg):
        s = f"{sender}: {msg}"
        print(f"[{self.name}'s chat session] {s}")
        self.chat_log.append(s)

    def private_message(self, destination, msg):
        self.room.message(self.name, destination, msg)

    def say(self, msg):
        self.room.broadcast(self.name, msg)


class ChatRoom:
    def __init__(self) -> None:
        self.people = []

    def join(self, person):
        join_msg = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, msg):
        for p in self.people:
            if p.name != source:
                p.receive(source, msg)

    def message(self, source, destination, msg):
        for p in self.people:
            if p.name == destination:
                p.receive(source, msg)


if __name__ == "__main__":
    room = ChatRoom()
    john = Person("John")
    jane = Person("Jane")
    room.join(john)
    room.join(jane)
    john.say("Hi room!")
    jane.say("Oh, hey John!")

    simon = Person("Simon")
    room.join(simon)
    simon.say("Hi everyone!")

    jane.private_message("Simon", "Glad you could join us!")
    john.private_message("Jane", "Hi Jane!")
    jane.private_message("John", "Hello John!")
