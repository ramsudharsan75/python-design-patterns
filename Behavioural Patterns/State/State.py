from abc import ABC


class Switch:
    def __init__(self) -> None:
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def __init__(self) -> None:
        self.name = "State"

    def on(self, switch):
        print("Light is already on")

    def off(self, switch):
        print("Light is already off")


class OnState(State):
    def __init__(self) -> None:
        print("Light turned on")
        self.name = "OnState"

    def off(self, switch):
        print("Switching light off...")
        switch.state = OffState()


class OffState(State):
    def __init__(self) -> None:
        print("Light turned off")
        self.name = "OffState"

    def on(self, switch):
        print("Switching light on...")
        switch.state = OnState()


if __name__ == "__main__":
    sw = Switch()
    sw.state.on(sw)
    sw.state.off(sw)
    sw.state.off(sw)
