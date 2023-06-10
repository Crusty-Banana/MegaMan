import retro
import random
from helper import *
from policy import *
env = retro.make(game='MegaMan2-Nes')

env.reset()

done = False

while not done:
    env.render()

    action = env.action_space.sample()

    action = default_policy()
    screen, reward, done, info = env.step(action)
    
    rgb = env.render('rgb_array')
    contour = find_contour(rgb)
    
    contour = cv2.resize(contour, rgb.shape[:-1])
    cv2.imshow('final', contour)
    cv2.waitKey(0)

    # 14x15 grid
    print("Action", action)
    print("image ", contour.shape, "reward ", reward, "Done?", done)
    print("Info", info)