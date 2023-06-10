import retro
from Image_processing import *
from policy import *
from QLearning import *

Q_value = defaultdict(lambda: 0, {})
with open('Q_value.pickle', 'rb') as handle:
    Q_value = defaultdict(lambda: 0, pickle.load(handle))

env = retro.make(game='MegaMan2-Nes')

agent = Agent(Q_value)

number_of_steps = 100
number_of_episodes = 2

first_step = [0, 0, 0, 0, 0, 0, 1, 0]

for i in range(number_of_episodes):
    env.reset()
    screen, reward, done, current_state = get_current_state(env, first_step)

    for j in range(number_of_steps):
        env.render()

        action = agent.chooseAction(current_state)

        button_pressed = agent.get_button_pressed(action)

        screen, reward, done, next_state = get_current_state(env, button_pressed)

        print(agent.Reward(current_state, next_state))

        agent.learn(current_state, action, next_state)

        if done:
            agent.reduce_exploration(i)
            break

print(agent.Q_value)

with open('Q_value.pickle', 'wb') as handle:
    pickle.dump(dict(agent.Q_value), handle, protocol=pickle.HIGHEST_PROTOCOL)