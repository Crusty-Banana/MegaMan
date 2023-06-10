import retro
from Image_processing import *
from policy import *
from QLearning import *

Q_value = defaultdict(lambda: 0, {})
with open('Q_value.pickle', 'rb') as handle:
    Q_value = defaultdict(lambda: 0, pickle.load(handle))

env = retro.make(game='MegaMan2-Nes', state="Normal.Flashman.Level1")

agent = Agent(Q_value)

number_of_steps = 2000
number_of_episodes = 100

first_step = [0, 0, 0, 0, 0, 0, 0, 1, 0]

for i in range(number_of_episodes):
    env.reset()
    screen, reward, done, current_state = get_current_state(env, first_step)
    action = agent.chooseAction(current_state)

    for j in range(number_of_steps):
        if (j % 10 == 0):
            env.render()
            action = agent.chooseAction(current_state)

        button_pressed = agent.get_button_pressed(action)

        screen, reward, done, next_state = get_current_state(env, button_pressed)

        agent.learn(current_state, action, next_state)

        current_state = next_state

        # rgb = env.render('rgb_array')
        # rgb = repeat_upsample(rgb, 2, 2)
        # rgb = repeat_upsample(rgb, 2, 2)
        # bgr = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
        # cv2.imshow("bruh", bgr)

        if done:
            agent.reduce_exploration(i)
            break

    Q_dict = dict(agent.Q_value)
    with open('Q_value.pickle', 'wb') as handle:
        pickle.dump(Q_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)