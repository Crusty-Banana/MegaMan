import numpy as np
import pickle

        
class State:
    def __init__(self, progress, yPos, health):
        self.progress = progress
        self.yPos = yPos
        self.health = health
        self.id = (self.progress, self.yPos // 12, self.health)
        
class Agent:
    def __init__(self):
        #epsilon
        self.exploring_rate = 0.1
        #alpha
        self.learning_rate = 0.5
        #gamma
        self.discounting_factor = 0.99 
        self.action_size = 8
        self.actions_space = [[0, 0, 0],
                        [0, 0, 1],
                        [0, 1, 0],
                        [0, 1, 1],
                        [1, 0, 0],
                        [1, 0, 1],
                        [1, 1, 0],
                        [1, 1, 1],]
        #estimated state size
        self.state_size = 10000 * 24 * 26

        self.Q_value = {}
        # with open('saved_dictionary.pkl', 'rb') as f:
        #     self.Q_value = pickle.load(f)

        self.shooting_clock = 0
        
    
    def chooseAction(self, state):
        if np.random.binomial(1, self.exploring_constant) == 1:
            return np.random.choice(self.action_size)
        else:
            return self.get_max_action(state)
    
    @staticmethod
    def Reward(current_state, next_state):
        coeff = [1, 1]
        result = (coeff[0] * (next_state.progress - current_state.progress) 
                + coeff[1] * (next_state.health - current_state.health)) 
        return result

    def get_Qid(self, state, action):
        Q_id = list(state.id) + self.actions_space[action]
        return Q_id
    
    def get_max_Q(self, state):
        result = -999999999
        for action in range(8):
            result = max(result, self.Q[self.get_Qid(state, action)])
        return result
    
    def get_max_action(self, state):
        result = -999999999
        max_action = -1
        for action in range(8):
            if (result < self.Q[self.get_Qid(state, action)]):
                result = self.Q[self.get_Qid(state, action)]
                max_action = action
        return max_action
    
    def learn(self, current_state, action, next_state):
        reward = self.Reward(current_state, next_state)
        self.Q[self.get_Qid(current_state, action)] += self.learning_rate * ( reward 
                                                                            + self.discounting_factor * self.get_max_Q(next_state) 
                                                                            - self.Q[state, action] )
    
    def button_pressed(self, action):
        return [0, 0, 0, 0, 0, *self.actions_space[action]]
    
    def reduce_exploration(self, i):
            self.exploring_rate /= i + 1

    def get_button_pressed(self, action):
        button = self.button_pressed(action)

        self.shooting_clock += 1
        if (self.shooting_clock == 10):
            self.shooting_clock = 0
            button[0] = 1
        
        return button

