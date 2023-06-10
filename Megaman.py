import retro
import random
from helper import *
from policy import *

env = retro.make(game='MegaMan2-Nes')
env.reset()

done = False
y_pos = 0

while not done:
    env.render()

    action = env.action_space.sample()

    action = default_policy()
    screen, reward, done, info = env.step(action)
    
    rgb = env.render('rgb_array')
    
    new_y_pos = find_yPos(rgb, info['xPos'])
    if (new_y_pos != -1):
        y_pos = new_y_pos

    print("y pos:", y_pos)
    # 14x15 grid
    print("Action", action)
    print("image ", rgb.shape, "reward ", reward, "Done?", done)
    print("Info", info)