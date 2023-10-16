class Creature:
    def __init__(self, name, attack, defence) -> None:
        self.name = name
        self.attack = attack
        self.defence = defence

    def __str__(self) -> str:
        return f"{self.name} ({self.attack}/{self.defence})"


class CreatureModifier:
    def __init__(self, creature) -> None:
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class IncreaseDefenceModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increase {self.creature.name}'s defence")
            self.creature.defence += 1

        super().handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print("No bonuses for you!")


if __name__ == "__main__":
    goblin = Creature("Goblin", 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)

    root.add_modifier(DoubleAttackModifier(goblin))
    # root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenceModifier(goblin))
    root.add_modifier(NoBonusesModifier(goblin))
    root.add_modifier(NoBonusesModifier(goblin))
    root.handle()
    print(goblin)
