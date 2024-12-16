import random

class Agent:
    agents =[]
    def __init__(self,id,num_agents,leader_id):
        self.id = id
        self.leader_id = leader_id
        self.num_agents = num_agents
        self.position = 0

    @classmethod
    def set_agents(cls,agent_list):
        cls.agents = agent_list

    def follow(self):
        if self.leader_id == self.id:   # leader itself
            self.position += random.choice([-1,0,1])
            print(f'\nLeader moved to position {self.position}')
        else:
            delta = self.leader_position() - self.position
            if delta >0:
                self.position += 1
            elif delta<0:
                self.position -=1
        print(f'Agent {self.id} follows position {self.position}')


    def leader_position(self):
        return self.agents[self.leader_id].position

def main():
    num_agents = 3
    agent_list = [Agent(_,num_agents,1) for _ in range(num_agents)]
    Agent.set_agents(agent_list)

    max_iterations = 3
    for _ in range(max_iterations):
        for agent in agent_list:
            agent.follow()


if __name__ == '__main__':
    main()
