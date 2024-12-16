class Agent:
    def __init__(self,start,goal):
        self.pos = start
        self.goal = goal
        self.next_pos = 0
    def perceive(self):
        pass

    def make_decision(self):
        if self.pos == self.goal:
            self.next_pos = self.goal
        elif self.pos > self.goal:
            self.next_pos = self.pos - 1
        else:
            self.next_pos = self.pos + 1

    def take_action(self):
        self.pos = self.next_pos

    def run(self):
        while self.pos != self.goal:    # run till it reaches the goal
            self.perceive()
            self.make_decision()    # make the decision
            self.take_action()  # rake action based on the action
            print(f'moved to {self.pos}')
        print('reached goal')

def main():
    agent = Agent(-1,4)
    print('start from',agent.pos)
    agent.run()


if __name__ =='__main__':
    main()
    # execute the function only when called directly not when imported