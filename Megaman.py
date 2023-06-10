import retro
from Image_processing import *
from policy import *
from QLearning import *

env = retro.make(game='MegaMan2-Nes')

agent = Agent()

y_pos = 0

number_of_steps = 1000
number_of_episodes = 20

first_step = [0, 0, 0, 0, 0, 0, 1, 0]

for i in range(number_of_episodes):
    env.reset()
    screen, reward, done, current_state = get_current_state(env, first_step)

    for j in range(number_of_steps):
        env.render()

        action = agent.chooseAction(current_state)

        button_pressed = agent.get_button_pressed(action)

        screen, reward, done, next_state = get_current_state(env, button_pressed)

        agent.learn(current_state, action, next_state)

        if done:
            agent.reduce_exploration(i)
            break

