from ..kuhn_poker import Player, Action

class Human_Player(Player):
    def __init__(self):
        self.counter = 0


    def get_move(self, possible_actions):
        print("Possible actions: ", [f"{action.name}: {action.value}" for action in possible_actions])
        return Action(int(input("Enter your move: ")))


    def inform(self, event):
        if self.counter == 0:
            print("Your card: ", event)
            self.counter += 1
        else:
            if isinstance(event, Action):
                print("Action: ", event.name)
        return