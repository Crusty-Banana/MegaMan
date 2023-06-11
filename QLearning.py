import numpy as np
import pickle
from collections import defaultdict
        
class State:
    def __init__(self, progress, yPos, health):
        self.progress = progress
        self.yPos = yPos
        self.health = health
        self.id = (self.progress, self.yPos // 12, self.health)
        
class Agent:
    def __init__(self, Q_value):
        #epsilon
        self.exploring_rate = 0.1
        #alpha
        self.learning_rate = 0.5
        #gamma
        self.discounting_factor = 0.999999
        self.actions_space = [[0, 0, 0],
                            [0, 0, 1],
                            [0, 1, 0],
                            [0, 1, 1],
                            [1, 0, 0],
                            [1, 0, 1]]
        self.action_size = len(self.actions_space)
        #estimated state size
        self.state_size = 10000 * 24 * 26

        self.Q_value = Q_value

        self.shooting_clock = 0

        self.exploration_strategy = ["Epsilon Greedy", "Optimal"]
        self.exploration_policy = self.exploration_strategy[0]
        
    def chooseAction(self, state):
        if self.exploration_policy == "Epsilon Greedy":
            action = []
            if np.random.binomial(1, self.exploring_rate) == 1:
                action = np.random.choice(self.action_size)
            else:
                action = self.get_max_action(state)
            return action
        
        elif self.exploration_policy == "Optimal":
            return self.get_max_action(state)
    @staticmethod
    def Reward(current_state, next_state):
        coeff = [10, 1]
        result = (coeff[0] * (next_state.progress - current_state.progress) 
                + coeff[1] * (next_state.health - current_state.health)) 
        return result

    def get_Qid(self, state, action):
        Q_id = list(state.id) + self.actions_space[action]
        return tuple(Q_id)
    
    def get_max_Q(self, state):
        result = -999999999
        for action in range(self.action_size):
            result = max(result, self.Q_value[self.get_Qid(state, action)])
        return result
    
    def get_max_action(self, state):
        result = -999999999
        max_action = -1
        for action in range(self.action_size):
            if (result < self.Q_value[self.get_Qid(state, action)]):
                result = self.Q_value[self.get_Qid(state, action)]
                max_action = action
        return max_action
    
    def learn(self, current_state, action, next_state):
        reward = self.Reward(current_state, next_state)
        self.Q_value[self.get_Qid(current_state, action)] += self.learning_rate * ( reward 
                                                                            + self.discounting_factor * self.get_max_Q(next_state) 
                                                                            - self.Q_value[self.get_Qid(current_state, action)] )
    
    def button_pressed(self, action):
        return [0, 0, 0, 0, 0, 0, *self.actions_space[action]]
    
    def reduce_exploration(self, i):
            self.exploring_rate /= i + 1

    def get_button_pressed(self, action):
        button = self.button_pressed(action)

        self.shooting_clock += 1
        if (self.shooting_clock >= 5):
            self.shooting_clock = 0
            button[0] = 1

        return button

