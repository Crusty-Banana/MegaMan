import retro
from Image_processing import *
from policy import *
from QLearning import *

Q_value = defaultdict(lambda: 0, {})
with open('Q_value.pickle', 'rb') as handle:
    Q_value = defaultdict(lambda: 0, pickle.load(handle))

env = retro.make(game='MegaMan2-Nes', state="Normal.Flashman.Level4")

agent = Agent(Q_value)

number_of_steps = 500
number_of_episodes = 300

first_step = [0, 0, 0, 0, 0, 0, 0, 1, 0]

for i in range(number_of_episodes):
    env.reset()
    screen, reward, done, current_state = get_current_state(env, first_step)
    action = agent.chooseAction(current_state)

    for j in range(number_of_steps):
        
        if (j % 30 == 0):
            env.render()
            action = agent.chooseAction(current_state)
            print("still running", i, j)
            print("max action:", agent.actions_name[agent.get_max_action(current_state)], agent.actions_name[action])

        button_pressed = agent.get_button_pressed(action)

        screen, reward, done, next_state = get_current_state(env, button_pressed)

        # if (j % 20 == 0):
        #     print("State's id", current_state.id)

        agent.learn(current_state, action, next_state)

        current_state = next_state

        if i % 50 == 0:
            agent.reduce_exploration(i/50)

# if (j % 500 == 0):
    Q_dict = dict(agent.Q_value)
    with open('Q_value.pickle', 'wb') as handle:
        pickle.dump(Q_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)