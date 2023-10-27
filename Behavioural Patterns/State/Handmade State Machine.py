from enum import Enum


class State(Enum):
    OFF_HOOK = 0
    CONNECTING = 1
    CONNECTED = 2
    ON_HOLD = 3
    ON_HOOK = 4


class Trigger(Enum):
    CALL_DIALED = 0
    HUNG_UP = 1
    CALL_CONNECTED = 2
    PLACED_ON_HOLD = 3
    TAKEN_OFF_HOLD = 4
    LEFT_MESSAGE = 5


if __name__ == "__main__":
    rules = {
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING),
            (Trigger.HUNG_UP, State.ON_HOOK),
        ],
        State.CONNECTING: [
            (Trigger.CALL_CONNECTED, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK),
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD),
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK),
        ],
    }

    state = State.OFF_HOOK
    exit_state = State.ON_HOOK

    while state != exit_state:
        print(f"The phone is currently {state}")

        for i in range(len(rules[state])):
            t = rules[state][i][0]
            print(f"{i}: {t}")

        idx = int(input("Select a trigger:"))
        s = rules[state][idx][1]
        state = s

    print("We are done using the phone")
