import retro

env = retro.make(game='MegaMan2-Nes')

env.reset()

done = False

while not done:
    env.render()

    action = env.action_space.sample()

    screen, reward, done, info = env.step(action)

    print("Action", action)
    print("image ", screen.shape, "reward ", reward, "Done?", done)
    print("Info", info)