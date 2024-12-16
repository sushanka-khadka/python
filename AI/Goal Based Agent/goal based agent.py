class Goal:
    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description


class Action:
    def __init__(self, task_perform, goal_description):
        self.task_perform = task_perform
        self.goal_description = goal_description

    def get_task_perform(self):
        return self.task_perform

    def get_goal_description(self):
        return self.goal_description

    def execute_task(self):
        print(f'executing task: {self.get_task_perform()}')


class Agent:
    def __init__(self):
        self.action = []
        self.goal = []

    def add_action(self, action):
        self.action.append(action)

    def add_goal(self, goal):
        self.goal.append(goal)

    def achieve_goal(self):
        for goal in self.goal:
            print(f'\nachieving goal: {goal.get_description()}')

            action_found = False
            for action in self.action:
                if action.get_goal_description() == goal.get_description():
                    action.execute_task()
                    action_found = True
                    break
            if not action_found:
                print("\t don't know what to do....")

def main():
    agent = Agent()

    goal_1 = Goal('score a header')
    goal_2 = Goal('score a banger')
    goal_3 = Goal('win the ball')
    goal_4 = Goal('win a foul')
    goal_5 = Goal('keep possession')
    goal_6 = Goal('win the match')
    action_1 = Action('dive', 'win a foul')
    action_2 = Action('shoot from outside the box', 'score a banger')
    action_3 = Action('jump', 'score a header')
    action_4 = Action('pass the ball', 'keep possession')
    action_5 = Action('tackle the opponent', 'win the ball')

    agent.add_action(action_1)
    agent.add_action(action_2)
    agent.add_action(action_3)
    agent.add_action(action_4)
    agent.add_action(action_5)

    agent.add_goal(goal_1)
    agent.add_goal(goal_2)
    agent.add_goal(goal_3)
    agent.add_goal(goal_4)
    agent.add_goal(goal_5)
    agent.add_goal(goal_6)

    agent.achieve_goal()


if __name__ == '__main__':
    main()
# function is executed only when script is called directly not when imported as module