import numpy as np
class Agent:
    def __init__(self, state_size):
        self.exploring_constant = 1
        self.learning_rate = 0.5
        self.discounting_factor = 0.5
        self.action_size = 8
        self.state_size = 10000 * 24 * 26
        
class state:
    def __init__(self, progress, yPos, health):
        self.progress = progress
        self.yPos = yPos
        self.health = health

def Reward(current_state, action, next_state):
    coeff = [1, 1]
    result = (coeff[0] * (next_state.progress - current_state.progress) 
              + coeff[1] * (next_state.health - current_state.health)) 
    return result

def Q_update(current_state, action):
    pass