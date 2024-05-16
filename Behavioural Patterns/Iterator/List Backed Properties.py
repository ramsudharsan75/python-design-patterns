class Creature:
    _strength = 0
    _agility = 0
    _intelligence = 0

    def __init__(self) -> None:
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[self._strength]

    @strength.setter
    def strength(self, value):
        self.stats[self._strength] = value

    @property
    def agility(self):
        return self.stats[self._agility]

    @agility.setter
    def agility(self, value):
        self.stats[self._agility] = value

    @property
    def intelligence(self):
        return self.stats[self._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[self._intelligence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def avg_stat(self):
        return float(self.sum_of_stats) / len(self.stats)

    # @property
    # def sum_of_stats(self):
    #     return self.strength + self.agility + self.intelligence

    # @property
    # def max_stat(self):
    #     return max(self.strength, self.agility, self.intelligence)

    # @property
    # def avg_stat(self):
    #     return self.sum_of_stats / 3.0

    def __str__(self) -> str:
        return f"Str: {self.strength}, Agi: {self.agility}, Int: {self.intelligence}"
