class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self) -> None:
        self.events = Event()

    def fire(self, args):
        self.events(args)


class GoalScoredInfo:
    def __init__(self, who_scored, goals_scored) -> None:
        self.who_scored = who_scored
        self.goals_scored = goals_scored


class Player:
    def __init__(self, name, game) -> None:
        self.name = name
        self.goals_scored = 0
        self.game = game

    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire(args)


class Coach:
    def __init__(self, game) -> None:
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f"Coach says: well done, {args.who_scored}!")


if __name__ == "__main__":
    game = Game()
    player = Player("Sam", game)
    coach = Coach(game)

    player.score()
    player.score()
    player.score()
