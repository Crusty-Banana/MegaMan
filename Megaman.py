import retro
from Image_processing import *
from policy import *
from QLearning import *

env = retro.make(game='MegaMan2-Nes')
env.reset()

done = False
y_pos = 0

count = 0
while not done:
    count += 1
    if (count == 100000):
        break

    env.render()

    action = env.action_space.sample()

    action = default_policy()
    screen, reward, done, info = env.step(action)
    
    rgb = env.render('rgb_array')
    
    new_y_pos = find_yPos(rgb, info['xPos'])
    if (new_y_pos != -1):
        y_pos = new_y_pos

    print("y pos:", y_pos)
    print("Action", action)
    print("image ", rgb.shape, "reward ", reward, "Done?", done)
    print("Info", info)