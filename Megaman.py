import retro
from Image_processing import *
from policy import *
from QLearning import *

Q_value = defaultdict(lambda: 0, {})
with open('Q_value.pickle', 'rb') as handle:
    Q_value = defaultdict(lambda: 0, pickle.load(handle))

env = retro.make(game='MegaMan2-Nes', state="Normal.Flashman.Level9")

agent = Agent(Q_value, strategy = 0, exploring_rate = 0.5, learning_rate= 0.5, discounting_factor = 0.999)

number_of_steps = 2000
number_of_episodes = 300

first_step = [0, 0, 0, 0, 0, 0, 0, 1, 0]

for i in range(number_of_episodes):
    env.reset()
    screen, reward, done, current_state = get_current_state(env, first_step)
    action = agent.chooseAction(current_state)

    for j in range(number_of_steps):
        if (j % 30 == 0):
            action = agent.chooseAction(current_state)
            
        if (j <= 100):
            action = 5
        button_pressed = agent.get_button_pressed(action)

        screen, reward, done, next_state = get_current_state(env, button_pressed)

        if (j % 1 == 0):
            # print("still running", i, j)
            # print("max action:", agent.actions_name[agent.get_max_action(current_state)], agent.actions_name[action])
            # print("Cur State's id", current_state.id, current_state.checkpoint)
            # print("Next State's id", next_state.id, next_state.checkpoint)
            print("max action:", agent.actions_name[agent.get_max_action(current_state)])
            print("max  Q:", agent.Q_value[agent.get_Qid(current_state, agent.get_max_action(current_state))])
            print("jump left Q:", agent.Q_value[agent.get_Qid(current_state, 5)])
            print("reward:", agent.Reward(current_state, next_state))
            env.render()

        agent.learn(current_state, action, next_state)

        current_state = next_state

        if (j % 500 == 0):
            Q_dict = dict(agent.Q_value)
            with open('Q_value.pickle', 'wb') as handle:
                pickle.dump(Q_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
        if (current_state.health == 0):
            agent.reduce_exploration(i/50)
            break
    
    if i % 50 == 0:
        agent.reduce_exploration(i/50)