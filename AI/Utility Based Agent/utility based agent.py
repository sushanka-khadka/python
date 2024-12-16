import random

class Action:
    def __init__(self,name,utility=0.0):
        self.name = name
        self.utility = utility
    def __repr__(self):
        return f'Action(name: {self.name}, utility: {self.utility:.2f})'




class Agent:
    def __init__(self,action_list):
        self.actions = action_list
        self.next_action = None

    def perceive(self):
        pass
    def calculate_utility(self):
        return random.uniform(0,1)
        # returns random floating no inclusive of lower bound but exclusive of upper one
    def make_decision(self):
        for action in self.actions:
            action.utility = self.calculate_utility()
        self.actions.sort(key = lambda x: x.utility, reverse = True)    # sort the actions based on their utility in descending
        self.next_action = self.actions[0]  # selects the action with the highest utility
    def take_action(self):
        # perform the action with the highest utility
        if self.next_action:
            print(f'Performing {self.next_action.name} with utility {self.next_action.utility:.2f}')

    def run(self,cycles):
        for _ in range(cycles):
            self.perceive()
            self.make_decision()
            self.take_action()
            print(f'Remaining actions: {self.actions}')
            print('-'*50)


actions = [Action("Action 1"), Action("Action 2"), Action("Action 3")]

def main():
    agent = Agent(actions)
    agent.run(5)

if __name__ == '__main__':
    main()